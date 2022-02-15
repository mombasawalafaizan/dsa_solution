import math
# from heapq import heapify, heapreplace

# class heapNode:
#     def __init__(self, data, mul):
#         self.data = data
#         self.mul = mul

#     def __lt__(self, other):
#         mints1 = (self.mul * (self.mul + 1)) // 2 * self.data
#         mints2 = (other.mul * (other.mul + 1)) // 2 * other.data
#         if self.data != other.data:
#             return mints1 < mints2
#         else:
#             return mints1+(self.mul + 1)*self.data < mints2+(other.mul + 1)*other.data 


# def calculateMinutes(arr, parata):
#     heap = [heapNode(i, 1) for i in arr]
#     heapify(heap)
#     cur_paratas = 0
#     max_time = -1
#     while cur_paratas < parata:
#         info = heap[0].data
#         mul = heap[0].mul
#         max_time = max(max_time, (mul*(mul+1))//2 * info)
#         heapreplace(heap, heapNode(info, mul+1))
#         cur_paratas += 1
#     return max_time

    # cur_par = 0
    # i = 0
    # while i < n:
    #     j = 1
    #     while ((j*(j+1))//2)*arr[i] <= cur_time:
    #         j += 1
    #         cur_par += 1
    #         if cur_par >= p:
    #             return True
    #     i += 1
    # return False
def isFeasible(arr, n, p, cur_time):
    cnt = 0
    for i in range(n):
        if arr[i]!=0:
            cnt = cnt+math.floor(-1+(1+(8*cur_time)//arr[i])**0.5)/2
        if cnt >= p:
            return True
    return False

def calculateMinutes(arr, n, p):
    l = 0
    h = 10**7
    while l < h:
        mid = (l+h)//2
        # print(mid)
        if isFeasible(arr, n, p, mid):
            h = mid 
        else:
            l = mid + 1
    return l

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        paratas = int(input())
        s = input()
        n = int(s[0])
        arr = list(map(int, s[1:].split()))
        print(calculateMinutes(arr, n, paratas))

# This is the working code
# #include<bits/stdc++.h>
# using namespace std;
# int test,parata,cook,rnk[10000],cnt,i;
# bool check(int t)
# {
#     cnt=0;
#     for(i=0;i<cook;i++)
#     {
#         cnt=cnt+((-1)+sqrt(1+8*t/rnk[i]))/2;
#         if(cnt>=parata)
#             return true;
#     }
#     return false;
# }
# int main()
# {
 
#     scanf("%d",&test);
#     while(test--)
#     {
#         scanf("%d%d",&parata,&cook);
#         for(i=0;i<cook;i++)
#         cin>>rnk[i];
#         int hi=10000000,lo=0,mid;
#         while(hi>lo)
#         {
#             mid=(hi+lo)/2;
#             if(check(mid))
#                 hi=mid;
#             else
#                 lo=mid+1;
#         }
#         cout<<lo<<endl;
#     }
# }