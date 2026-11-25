# Алгоритм 1: Сортировка пузырьком (Bubble Sort)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", data)
    print("Отсортированный массив (пузырьком):", bubble_sort(data.copy()))
