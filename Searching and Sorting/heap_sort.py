import time
import random

def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
        # Heapify the root. 
        heapify(arr, n, largest) 
  

def heapSort(arr): 
    n = len(arr)   
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i)  #i is considered root in each case in heapify
        
    # One by one extract elements from root by rearranging the heap by deleting
    # the root i.e index 0 element and add from backwards
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 

n = int(input("Enter how number to sort: "))
arr = random.sample(range(1, 100000), n)
start_time = time.time()
heapSort(arr)
print("Time taken: ",str(time.time() - start_time))
