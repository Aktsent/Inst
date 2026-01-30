def sum_negatives_between_min_max(A):
    if not A:
        return 0

    # найти индексы минимального и максимального элементов
    min_index = A.index(min(A))
    max_index = A.index(max(A))

    # определить границы диапазона
    start = min(min_index, max_index) + 1
    end = max(min_index, max_index)

    # суммирование отрицательного числа в диапазоне [start, end)
    total = sum(x for x in A[start:end] if x < 0)

    return total

