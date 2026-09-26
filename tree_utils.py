# tree_utils.py
from typing import List, Optional, Any
from collections import deque

# matplotlib 懒加载：只有调用 visualize_tree / show_tree 时才需要
# （build_tree / TreeNode 可在无 matplotlib 的环境使用）
null = None
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def build_tree(data: List[Any]) -> Optional["TreeNode"]:
    """
    根据力扣风格的列表构建二叉树。
    例如 [1, None, 2, 3] -> 二叉树
    """
    if not data or data[0] is None:
        return None

    root = TreeNode(data[0])
    queue = deque([root])          # deque 的 popleft 是 O(1)
    i = 1
    while queue and i < len(data):
        node = queue.popleft()

        if i < len(data) and data[i] is not None:
            node.left = TreeNode(data[i])
            queue.append(node.left)
        i += 1

        if i < len(data) and data[i] is not None:
            node.right = TreeNode(data[i])
            queue.append(node.right)
        i += 1

    return root


def _setup_plt(plt):
    """matplotlib 中文字体支持（Windows 常见字体回退），并修复负号显示"""
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False


def visualize_tree(root: Optional["TreeNode"], filename: str = "tree.png",
                   title: str = "", figsize=(8, 6), node_radius: float = 0.5):
    """
    可视化二叉树并保存为图片（matplotlib 绘制）。
    :param root: 二叉树根节点
    :param filename: 保存的文件名（含扩展名，如 tree.png / tree.pdf / tree.svg）
    :param title: 图片标题（支持中文）
    :param figsize: 图片大小
    :param node_radius: 节点圆半径
    """
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    _setup_plt(plt)

    if root is None:
        fig, ax = plt.subplots(figsize=figsize)
        ax.text(0.5, 0.5, "Empty Tree", ha="center", va="center", fontsize=20)
        ax.axis("off")
        fig.savefig(filename, bbox_inches="tight")
        plt.close(fig)
        return

    # 1. 计算每个节点的位置（中序遍历 x 坐标，深度 y 坐标）
    positions = {}
    x_counter = [0]

    def assign_x(node, depth):
        if node is None:
            return
        assign_x(node.left, depth + 1)
        positions[node] = (x_counter[0], -depth)
        x_counter[0] += 1
        assign_x(node.right, depth + 1)

    assign_x(root, 0)

    # 2. 画图
    fig, ax = plt.subplots(figsize=figsize)
    ax.axis("off")

    # 画边
    def draw_edges(node):
        if node is None:
            return
        x, y = positions[node]
        for child in (node.left, node.right):
            if child is not None:
                cx, cy = positions[child]
                ax.plot([x, cx], [y, cy], color="gray", linewidth=1.2, zorder=1)
                draw_edges(child)

    draw_edges(root)

    # 画节点
    for node, (x, y) in positions.items():
        circle = patches.Circle((x, y), node_radius * 0.9,
                                facecolor="#AED6F1", edgecolor="#1F618D",
                                linewidth=1.5, zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, str(node.val), ha="center", va="center",
                fontsize=11, color="#1B2631", zorder=3)

    # 自适应范围
    xs = [p[0] for p in positions.values()]
    ys = [p[1] for p in positions.values()]
    margin = 1.0
    ax.set_xlim(min(xs) - margin, max(xs) + margin)
    ax.set_ylim(min(ys) - margin, max(ys) + margin)
    ax.set_aspect("equal")

    if title:
        ax.set_title(title, fontsize=13)

    fig.savefig(filename, bbox_inches="tight", dpi=150)
    plt.close(fig)
    print(f"Tree image saved to: {filename}")


def show_tree(root: Optional["TreeNode"], title: str = "", figsize=(8, 6)):
    """
    直接在窗口显示二叉树（不保存文件）。
    注意：需要图形界面的环境才能弹窗。
    """
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    _setup_plt(plt)

    if root is None:
        print("Empty tree")
        return

    positions = {}
    x_counter = [0]

    def assign_x(node, depth):
        if node is None:
            return
        assign_x(node.left, depth + 1)
        positions[node] = (x_counter[0], -depth)
        x_counter[0] += 1
        assign_x(node.right, depth + 1)

    assign_x(root, 0)

    fig, ax = plt.subplots(figsize=figsize)
    ax.axis("off")

    def draw_edges(node):
        if node is None:
            return
        x, y = positions[node]
        for child in (node.left, node.right):
            if child is not None:
                cx, cy = positions[child]
                ax.plot([x, cx], [y, cy], color="gray", linewidth=1.2, zorder=1)
                draw_edges(child)

    draw_edges(root)

    for node, (x, y) in positions.items():
        circle = patches.Circle((x, y), 0.45,
                                facecolor="#AED6F1", edgecolor="#1F618D",
                                linewidth=1.5, zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, str(node.val), ha="center", va="center",
                fontsize=11, color="#1B2631", zorder=3)

    xs = [p[0] for p in positions.values()]
    ys = [p[1] for p in positions.values()]
    ax.set_xlim(min(xs) - 1, max(xs) + 1)
    ax.set_ylim(min(ys) - 1, max(ys) + 1)
    ax.set_aspect("equal")

    if title:
        ax.set_title(title, fontsize=13)

    plt.show()