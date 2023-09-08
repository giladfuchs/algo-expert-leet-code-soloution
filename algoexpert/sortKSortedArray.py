def mergeSort(arr, k):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L, k)
        mergeSort(R, k)
        if mid<=k*2:

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        else:
            arr = L.copy() + R.copy()
            return arr


def sortKSortedArray(array, k):
    arr = mergeSort(array, k)
    # array = mergeSort(array, k)
    return array if arr is None else arr

from heapq import heapify, heappush, heappop

def sortKSortedArray2(array, k):
    heap = []
    heapify(heap)
    i = 0
    n = len(array)
    ans = []
    for _ in array[:k]:
        heappush(heap, _)
    for _ in array[k:]:
        heappush(heap, _)
        ans.append(heappop(heap))

    while heap:
        ans.append(heappop(heap))
    return ans
    #
    # while i<k:
    #     heappush(heap, array[i])


    
    #     i+=1
    #
    # while i < n:
    #     array[i-k] = heappop(heap)
    #     heappush(heap, array[i])
    #     i+=1
    # while i < + n + k:
    #     array[i-k] = heappop(heap)
    #     i+=1
    # return array

print(sortKSortedArray2([3, 2, 1, 5, 4, 7, 6, 5], 3))