import numpy as np
import matplotlib.pyplot as plt

def overlap(i, j, x, y):
    dx = x[i] - x[j]
    dy = y[i] - y[j]
    return dx*dx + dy*dy <= 4   # avstånd <= 2


def build_graph(x, y):
    N = len(x)
    graph = {i: [] for i in range(N)}

    for i in range(N):
        for j in range(i + 1, N):
            if overlap(i, j, x, y):
                graph[i].append(j)
                graph[j].append(i)

    return graph


def dfs(start, graph):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)

    return visited


def percolates(x, y, L):
    graph = build_graph(x, y)

    left = []
    right = []

    for i in range(len(x)):
        if x[i] <= 1:
            left.append(i)

        if x[i] >= L - 1:
            right.append(i)

    right_set = set(right)

    for node in left:
        cluster = dfs(node, graph)

        if cluster & right_set:
            return True

    return False


def simulate_percolation(n, max_circles=5000):
    L = np.sqrt(n)

    x = []
    y = []

    for k in range(1, max_circles + 1):
        x.append(np.random.uniform(0, L))
        y.append(np.random.uniform(0, L))

        if percolates(np.array(x), np.array(y), L):
            return k

    return None


def draw_configuration(x, y, L):
    fig, ax = plt.subplots(figsize=(6, 6))

    for i in range(len(x)):
        circle = plt.Circle((x[i], y[i]), 1, fill=False)
        ax.add_patch(circle)

    graph = build_graph(x, y)

    for i in graph:
        for j in graph[i]:
            if i < j:
                ax.plot([x[i], x[j]], [y[i], y[j]])

    ax.set_xlim(0, L)
    ax.set_ylim(0, L)
    ax.set_aspect("equal")
    plt.show()


# Exempel: en simulering
n = 10000
L = np.sqrt(n)

x = []
y = []

for k in range(1, 1000):
    x.append(np.random.uniform(0, L))
    y.append(np.random.uniform(0, L))

    if percolates(np.array(x), np.array(y), L):
        print("Perkolation vid", k, "cirklar")
        draw_configuration(np.array(x), np.array(y), L)
        break