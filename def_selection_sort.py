def selection_sort(arr):
    for i in range(len(arr)):
        try:
            x = min(arr[i+1:len(arr)])
        except ValueError:
            break
        y = arr[i]
        if y > x:
            arr[arr.index(x)] = y
            arr[i] = x



# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Отсортированный список:", my_list)