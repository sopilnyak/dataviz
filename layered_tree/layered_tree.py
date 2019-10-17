import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.data = value
        self.x_coord = None
        self.y_coord = None


def draw_graph():
    graph = nx.Graph()
    for node in tree:
        if node:
            graph.add_node(node.data, pos=(node.x_coord, -node.y_coord))

    for i in range(len(tree) // 2):
        if tree[i] and tree[2 * i + 1]:
            graph.add_edge(tree[i].data, tree[2 * i + 1].data)
        if tree[i] and tree[2 * i + 2]:
            graph.add_edge(tree[i].data, tree[2 * i + 2].data)

    pos = nx.get_node_attributes(graph, 'pos')
    nx.draw_networkx(graph, pos=pos)
    plt.savefig("output.png")


def y_assign(tree):
    for i in range(len(tree)):
        if tree[i]:
            tree[i].y_coord = int(math.floor(math.log(i + 1, 2)))


def inorder_assign(tree, node):
    if node >= len(tree) or tree[node] is None:
        return
    inorder_assign(tree, 2 * node + 1)
    global index
    index += 1
    tree[node].x_coord = index
    inorder_assign(tree, 2 * node + 2)


def min_x(tree, node):
    if node >= len(tree) or not tree[node]:
        return 10000
    return min(tree[node].x_coord, min_x(tree, 2 * node + 1), min_x(tree, 2 * node + 2))


def max_x(tree, node):
    if node >= len(tree) or not tree[node]:
        return 0
    return max(tree[node].x_coord, max_x(tree, 2 * node + 1), max_x(tree, 2 * node + 2))


def move_subtree(tree, node, dist):
    if node >= len(tree) or not tree[node]:
        return
    tree[node].x_coord += dist
    move_subtree(tree, 2 * node + 1, dist)
    move_subtree(tree, 2 * node + 2, dist)


def draw_subtree(tree, root):
    root_left = 2 * root + 1
    root_right = 2 * root + 2

    if (root_left >= len(tree) or not tree[root_left]) and (root_right >= len(tree) or not tree[root_right]):
        return

    if tree[root_left] and tree[root_right]:
        x_dist = (min_x(tree, root_right) - max_x(tree, root_left))
        if x_dist > 2:
            move_subtree(tree, root_left, (x_dist - 2) / 2)
            move_subtree(tree, root_right, -(x_dist - 2) / 2)
        tree[root].x_coord = (tree[root_right].x_coord + tree[root_left].x_coord) / 2

    elif root_left < len(tree) and tree[root_left]:
        tree[root].x_coord = tree[root_left].x_coord + 1
    elif root_right < len(tree) and tree[root_right]:
        tree[root].x_coord = tree[root_right].x_coord - 1

    draw_subtree(tree, 2 * root + 1)
    draw_subtree(tree, 2 * root + 2)


def generate_tree():
    tree = []
    n = 31
    data = {0: '0', 1: '1', 2: '2', 3: '3', 5: '5', 6: '6', 8: '8', 11: '11', 12: '12', 17: '17', 18: '18'}
    for i in range(n):
        if i in data:
            tree.append(Node(data[i]))
        else:
            tree.append(None)
    return tree


tree = generate_tree()
y_assign(tree)
index = 0
inorder_assign(tree, 0)
draw_subtree(tree, 0)
draw_subtree(tree, 0)
draw_graph()
