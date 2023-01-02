def reverse_array(arr):
    start_index = 0
    end_index = len(arr) - 1
    temp = 0

    while start_index <= end_index:
        temp = arr[start_index]
        arr[start_index] = arr[end_index]
        arr[end_index] = temp
        start_index = start_index + 1
        end_index = end_index - 1


# Driver to call function
arr = [6, 9, 7, 1, 4]
reverse_array(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")
