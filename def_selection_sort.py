def selection_sort(arr):
    for i in range(len(arr)):
        try:
            min_index, min_value = min(enumerate(arr[i+1:len(arr)]), key=lambda pair: pair[1])
        except ValueError:
            break
        y = arr[i]
        if y > min_value:
            arr[min_index + i + 1] = y
            arr[i] = min_value


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Отсортированный список:", my_list)