'''Taking last element as pivot
int partition (int arr[], int l, int h) 
{ 
    int x = arr[h]; 
    int i = (l - 1); 
  
  
    for (int j = l; j <= h- 1; j++) 
    { 
        if (arr[j] <= x) 
        { 
            i++; 
            swap (&arr[i], &arr[j]); 
        } 
    } 
    swap (&arr[i + 1], &arr[h]); 
    return (i + 1); 
} 
  
/* A[] --> Array to be sorted, l  --> Starting index, h  --> Ending index */
void quickSort(int A[], int l, int h) 
{ 
    if (l < h) 
    {         
        int p = partition(A, l, h); /* Partitioning index */
        quickSort(A, l, p - 1);   
        quickSort(A, p + 1, h); 
    } 
} '''

# Quick sort on double linked list is like the above approach only:
# see at LINK: https://www.geeksforgeeks.org/quicksort-for-linked-list/

# Quick sort on singly linked list(a little hard):
# see at LINK: https://www.geeksforgeeks.org/quicksort-on-singly-linked-list/