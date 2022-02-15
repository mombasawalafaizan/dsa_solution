if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        arr = list(map(int, input().split()))
        ans = 0
        mysum = 0
        for i in range(n):
            mysum += arr[i]
            ans += abs(mysum)
        print(ans)

if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        a = list(map(int, input().split()))
        ret = 0
        seller, buyer = 0, 0
        while True:
            while seller < n and a[seller] >= 0:
                seller += 1
            while buyer < n and a[buyer] <= 0:
                buyer += 1
            if seller == n or buyer == n:
                break

            transaction = min(a[buyer], -a[seller])
            ret += abs(buyer - seller) * transaction
            a[buyer] -= transaction
            a[seller] += transaction

        print(ret)
