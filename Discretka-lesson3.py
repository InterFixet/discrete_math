import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Исправленные данные (квадратная матрица 6x6)
data = np.array([
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
])

# Создание графа
G = nx.from_numpy_array(data, create_using=nx.DiGraph)

# Визуализация
pos = nx.spring_layout(G)
labels = {i: f"node {chr(97+i)}" for i in range(6)}  # node a, node b, etc.
nx.draw(G, pos, labels=labels, with_labels=True, node_color='lightgreen',
        node_size=800, font_size=12, arrows=True, arrowsize=20)
plt.title("Диаграмма Хассе")
plt.show()