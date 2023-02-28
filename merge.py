
def mergeSort(arr):
    if len(arr) > 1:
        left, right = split(arr)

        mergeSort(left)
        mergeSort(right)

        merge(left, right,arr)

def split(arr):
    mid = int(len(arr)/2)
    left = arr[:mid]
    right = arr[mid:]
    return left, right

def merge(left, right,arr):
    l = 0;r = 0; ind = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr[ind] = left[l]
            l += 1
        else:
            arr[ind] = right[r]
            r += 1
        ind += 1

    while l < len(left):
        arr[ind] = left[l]
        l += 1
        ind += 1

    while r < len(right):
        arr[ind] = right[r]
        r += 1
        ind += 1













