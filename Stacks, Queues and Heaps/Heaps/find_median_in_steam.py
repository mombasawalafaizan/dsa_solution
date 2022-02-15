from heapq import heappush, heapreplace
import random

# THESE METHODS ARE THE IMPLEMENTATION OF ABOVE METHODS
# def reverseHeapify(heap, i):
#     if i==0:
#         return
#     parent = (i-1)//2
#     if heap[i] < heap[parent]:
#         heap[i], heap[parent] = heap[parent], heap[i]
#         reverseHeapify(heap, parent)

# def heapify(arr, i, n):
#     smallest = i
#     l = 2*i + 1
#     r = 2*i + 2
#     if l < n and arr[smallest] > arr[l]:
#         smallest = l
#     if r < n and arr[smallest] > arr[r]:
#         smallest = r
#     if smallest!=i:
#         arr[smallest], arr[i] = arr[i], arr[smallest]
#         heapify(arr, smallest, n)


# def heappush(heap, el):
#     heap.append(el)
#     i = len(heap)-1
#     reverseHeapify(heap, i)
    
# def heapreplace(heap, el):
#     heap[0] = el
#     heapify(heap, 0, len(heap))
    
if __name__ == '__main__':
    n = int(input())
    i = 0
    left=[]
    right = []
    arr = [random.randint(1, 100) for i in range(n)]
    while i != n:
        el = arr[i]
        print('LEft', left)
        print('RIght', right)
        print('arr: ', sorted(arr[:i+1]))
        if i%2==0:
            if right and el > right[0]:
                heappush(left, right[0]*-1)
                heapreplace(right, el)
            else:
                heappush(left, -1*el)
            print(left[0]*-1)
        else:
            if el < left[0]*-1:
                heappush(right, left[0]*-1)
                heapreplace(left, -1*el)
            else:
                heappush(right, el)
            print((right[0] + left[0]*-1)//2)
        i += 1