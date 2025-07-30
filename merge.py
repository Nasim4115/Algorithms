def mergeSort(arr, left, right):
    if left >= right:
        return  # Base case: single element is already sorted

    mid = (left + right) // 2  # Find the middle index

    # Recursively sort both halves
    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)

    # Merge sorted halves
    merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    temp = []  # Temporary list for merging
    i, j = left, mid + 1

    # Merge elements in sorted order
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    # Add remaining elements
    temp.extend(arr[i:mid + 1])
    temp.extend(arr[j:right + 1])

    # Copy back to original array
    arr[left:right + 1] = temp

# Example
arr = [38, 27, 43, 3, 9, 82, 10]
print("Before Sorting:", arr)
mergeSort(arr, 0, len(arr) - 1)
print("After Sorting:", arr)
#Best Case	O(n log n)