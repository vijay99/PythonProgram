def bubble_sort(arr):
    temp = 0
    is_sorted = False

    for i in range(len(arr) - 1):
        is_sorted = True
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                is_sorted = False
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
        if is_sorted:
            break


# Driver class
arr = [7, 9, 1, 0, 6]
bubble_sort(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")
