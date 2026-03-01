def topological_sort(elements, relations):
    elements = list(elements) # список элементов
    relations = set(relations) # множество пар (a,b) где a < b
    result = []

    while elements: # Ищем минимальный (нет входящих стрелок)
        minimal = None
        for x in elements:
            if not any((y, x) in relations for y in elements if y != x):
                minimal = x
                break

        if minimal is None:
            return None  # есть цикл

        result.append(minimal)
        elements.remove(minimal)

    return result

# Пример
U = ['a', 'b', 'c', 'd']
R = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('a', 'd')]

print("Исходное множество:", U)
print("Отношения:", R)
print("Линейный порядок:", topological_sort(U, R))