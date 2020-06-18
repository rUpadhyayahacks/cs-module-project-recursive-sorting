# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    # find mid point of start and end
    # check if min is target, if yes
    # return mid
    # if arr length is 1
    # return -1
    # check if midpoint is higher or lower than the target
    # if lower feed in array,target, old start and mid
    # if higher feed in array,target, mid and old end
    #
    if start <= end:
        mid = start + (end-start) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            return binary_search(arr, target, start, mid-1)
        else:
            return binary_search(arr, target, mid+1, end)
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_helper(arr, target, descending):
    mid = len(arr)//2
    if len(arr) == 1:
        return mid if arr[mid] == target else -1
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        index = agnostic_helper(arr[mid:], target, descending) if not descending else agnostic_helper(
            arr[:mid+1], target, descending)
        return mid+index if index != -1 else -1
    else:
        return agnostic_helper(arr[:mid], target, descending) if not descending else agnostic_helper(arr[mid:], target, descending)


def agnostic_binary_search(arr, target):
    descending = arr[0] >= arr[-1]
    return agnostic_helper(arr, target, descending)


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]

# print(binary_search(arr1, -8, 0, len(arr1)-1))
# print(agnostic_binary_search(arr1, 5))
# print(agnostic_binary_search(arr1, 13))
# print(agnostic_binary_search(arr1, 9))
# print(agnostic_binary_search(arr1, -9))
# print(agnostic_binary_search(arr1, 0))
print(agnostic_binary_search(descending, 49))