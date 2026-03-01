from scipy.sparse import csr_array
from scipy.sparse.csgraph import floyd_warshall
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
# Создание графа
#G = nx.Graph() #не ориентированный
G=nx.DiGraph(directed=True) # ориентированный

# Добавление вершин, т.е. задание множества A для прямого произведения A*A
G.add_nodes_from([1, 2, 3, 4, 5,6])
# Добавление рёбер, то есть задание бинарного отношения, т.е. подмножества A*A
A=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)]

G.add_edges_from(A)

# Визуализация графа
nx.draw(G, with_labels=True, node_color='lightblue')
plt.show()

#Нахождение матрицы смежности B по бинарному отношению
n=6#задание числа вершин графа
B = np.zeros((n, n))

for t in A:
    B[t[0]-1][t[1]-1]=1
#матрица смежности графа по заданному бинарному отношению
print(B)

graph = B
graph = csr_array(graph)
print(graph)

dist_matrix, predecessors = floyd_warshall(csgraph=graph, directed=True, return_predecessors=True)
print(dist_matrix) # Матрица расстояний N x N между узлами графа. dist_matrix[i,j] задает кратчайшее расстояние от точки i до точки j на графе
print(predecessors)


def check_on_reflex(matrix):
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] != 1:
            return ('Не является рефлексивным')
    return ('Является рефлексивным')

def check_on_anti_reflex(matrix):
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] != 0:
            return ('Не является антирефлексивным')
    return ('Является антирефлексивным')

def check_on_simmetry(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return ('Не является симметричным')
    return ('Является симметричным')

def check_on_anti_simmetry(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == 1 and matrix[j][i] == 1:
                return ('Не является антисимметричным')
    return ('Является антисимметричным')



def check_on_transitive(a):
  for i in range(n):
    for j in range(n):
      for k in range(n):
        if a[i][j]==1 and a[j][k]==1 and a[i][k]==0:
          return ('Не является транзитивным')
  return ('Является транзитивным')


def check_on_linearity(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i!=j and matrix[i][j] != 1 and matrix[j][i] != 1:
                return ('Не является линейным')
    return ('Является линейным')

print(check_on_reflex(B))
print(check_on_anti_reflex(B))
print(check_on_simmetry(B))
print(check_on_anti_simmetry(B))
print(check_on_transitive(B))
print(check_on_linearity(B))
