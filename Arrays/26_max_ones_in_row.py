import sys

'''#A very good solution from comments 
int findRow(int m, int n, int a[m][n]){
    int row = 0;
    int i = 0, j = n - 1;
    while(i < m && j >= 0){
        if(a[i][j] == 1){
            row = i;
            j--;
        }
        else i++;
    }
    return row;
}'''

def rowwithMaxOnes(arr: list, r: int, c: int):
    max_row = -1
    max_ones = 0
    for i in range(r):
        for j in range(c-max_ones):
            if arr[i*c+j] == 1: # Can be done using Binary Search
                max_ones = max_ones + (c-max_ones-j)
                max_row = i
                break
    return max_row
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        print(rowwithMaxOnes(arr, n, m))