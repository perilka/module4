def insertion_sort(arr):
    for i in range(len(arr)):
        x = arr[i]
        j = i
        while j > 0 and arr[j-1] > x:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = x


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print("Отсортированный список:", my_list)