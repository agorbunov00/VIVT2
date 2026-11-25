# Алгоритм 3: Быстрая сортировка (Quick Sort)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", data)
    print("Отсортированный массив (быстрая):", quick_sort(data.copy()))
