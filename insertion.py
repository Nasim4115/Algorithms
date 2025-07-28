import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr

arr = [21, 11, 1, 25, 46, 34, 21, 6, 2, 98, 21, 11, 1, 25, 46, 17, 25, 46, 34, 21, 6]

start_time = time.time()
sorted_arr = insertion_sort(arr.copy())
end_time = time.time()

total_time = end_time - start_time

print("Execution Time:", total_time)
print("Sorted Array:", sorted_arr)