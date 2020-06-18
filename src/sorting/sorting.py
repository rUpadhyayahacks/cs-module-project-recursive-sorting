# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)

    merged_arr = []
    left_pointer=right_pointer = 0

    while left_pointer < len(arrA) and right_pointer < len(arrB):
        if arrA[left_pointer] < arrB[right_pointer]:
            merged_arr.append(arrA[left_pointer])
            left_pointer += 1
        else:
            merged_arr.append(arrB[right_pointer])
            right_pointer += 1
    merged_arr += arrA[left_pointer:]
    merged_arr += arrB[right_pointer:]
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # select whole array
    # split it as evenly as possible
    # print(arr)
    # basecase is if once the array has been halved into single elements
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

print(merge_sort([10, 14, 22, 5, 8, 5, 7, 7, 4, 3, 2, 1]))