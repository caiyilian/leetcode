# bt_visual.py
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(lst):
    """从 LeetCode 风格的列表构建二叉树"""
    if not lst or lst[0] is None:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root


def _get_positions(root):
    """用中序遍历给每个节点分配 x 坐标，y 坐标按深度"""
    positions = {}
    counter = [0]

    def inorder(node, depth):
        if not node:
            return
        inorder(node.left, depth + 1)
        positions[id(node)] = (counter[0], -depth)
        counter[0] += 1
        inorder(node.right, depth + 1)

    inorder(root, 0)
    return positions


def visualize_tree(root, title="Binary Tree", save_path=None):
    """
    可视化二叉树为图片。

    参数:
        root: 可以是 LeetCode 风格的列表，也可以是 TreeNode 根节点
        title: 图片标题
        save_path: 若提供路径，则保存图片；否则只显示
    """
    if isinstance(root, list):
        root = build_tree(root)

    if root is None:
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.text(0.5, 0.5, "Empty Tree", ha="center", va="center", fontsize=16)
        ax.axis("off")
        if save_path:
            plt.savefig(save_path, bbox_inches="tight", dpi=120)
        plt.show()
        return

    positions = _get_positions(root)

    fig, ax = plt.subplots(figsize=(max(6, len(positions) * 0.8), 5))

    # 画边
    def draw_edges(node):
        if not node:
            return
        x, y = positions[id(node)]
        for child in (node.left, node.right):
            if child:
                cx, cy = positions[id(child)]
                ax.plot([x, cx], [y, cy], color="gray", linewidth=1.2, zorder=1)
                draw_edges(child)

    draw_edges(root)

    # 画节点
    radius = 0.35
    for node_id, (x, y) in positions.items():
        # 找到对应的节点值
        pass

    def draw_nodes(node):
        if not node:
            return
        x, y = positions[id(node)]
        circle = Circle((x, y), radius, facecolor="#AED6F1",
                        edgecolor="#2C3E50", linewidth=1.5, zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, str(node.val), ha="center", va="center",
                fontsize=11, fontweight="bold", zorder=3)
        draw_nodes(node.left)
        draw_nodes(node.right)

    draw_nodes(root)

    # 计算边界
    xs = [p[0] for p in positions.values()]
    ys = [p[1] for p in positions.values()]
    ax.set_xlim(min(xs) - 1, max(xs) + 1)
    ax.set_ylim(min(ys) - 1, max(ys) + 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=13, pad=10)

    if save_path:
        plt.savefig(save_path, bbox_inches="tight", dpi=120)
    plt.show()


if __name__ == "__main__":
    visualize_tree([1, None, 2, 3], title="Demo")