def bubble_sort(arr):
    changes = []
    while True:
        j = 1
        for i in range(len(arr)-j):
            if arr[i] > arr [i+1]:
                a = arr[i]
                b = arr[i+1]
                arr[i+1] = a
                arr[i] = b
                changes.append(1)
        j += 1 # в сл раз проверяем на один элемент меньше (с конца, само собой)
        changes.append(0)
        if changes[-1] == 0 and changes[-2] == 0:
            return arr

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Отсортированный список:", my_list)