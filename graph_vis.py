# -*- coding: utf-8 -*-
"""
有向图可视化（NetworkX + Matplotlib 实现）
- 自动探测交互后端（TkAgg/QtAgg）；都没有则退回 Agg，保存 PNG 并打印路径
- 用法：
    from graph_vis import visualize_graph
    visualize_graph([[0,1],[0,2],[1,3]], save_path="out.png")
  直接运行：python graph_vis.py（默认示例 + 保存 graph_output.png）
"""
import os
import matplotlib
import matplotlib.pyplot as plt

# ---- 后端探测：优先交互后端（弹窗），否则 Agg（存文件）----
_interactive = None
for _be in ("TkAgg", "QtAgg", "Qt5Agg"):
    try:
        matplotlib.use(_be, force=True)
        _f = plt.figure()
        plt.close(_f)
        _interactive = _be
        break
    except Exception:
        continue
if _interactive is None:
    matplotlib.use("Agg", force=True)
    print("[info] 无交互后端（缺 tkinter/PyQt），将保存 PNG 并打印路径")
    _interactive = False

import networkx as nx


def visualize_graph(edges, figsize=(8, 6), save_path=None,
                    layout="circular", with_arrowheads=True,
                    title="Directed Graph"):
    """
    用 NetworkX 绘制有向图。

    edges        : 边列表，如 [[0,1],[0,2],[1,3]]
    layout       : "circular" 圆形布局 / "spring" 力导向布局
    save_path    : PNG 保存路径；None 时默认 graph_output.png
    """
    G = nx.DiGraph()
    G.add_edges_from(edges)

    # 布局
    if layout == "spring":
        pos = nx.spring_layout(G, seed=42)
    else:
        pos = nx.circular_layout(G)

    fig, ax = plt.subplots(figsize=figsize)

    # 边（带箭头）
    nx.draw_networkx_edges(
        G, pos, ax=ax,
        arrows=with_arrowheads,
        arrowstyle="-|>", arrowsize=18,
        edge_color="#333333", width=1.8,
        connectionstyle="arc3,rad=0.15",   # 轻微弧度，避免重叠
    )
    # 节点
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=800,
                           node_color="#4A90E2", edgecolors="#2E5FA3", linewidths=1)
    # 标签
    nx.draw_networkx_labels(G, pos, ax=ax, font_color="white",
                            font_size=12, font_weight="bold")

    ax.set_title(title, fontsize=14)
    ax.axis("off")
    plt.tight_layout()

    if not save_path:
        save_path = "graph_output.png"
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    print("已保存:", os.path.abspath(save_path))
    if _interactive:
        plt.show()


# 兼容旧函数名
visualize_directed_graph_pure = visualize_graph


if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
    visualize_graph(edges, layout="circular")
