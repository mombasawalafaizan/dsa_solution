def dieHard(h, a):
    elmts = [[-5 , -10], [-20, 5]]
    cur_place = -1
    time = 0
    while h>0 and a>0:
        if cur_place != 2:
            h += 3
            a += 2
            cur_place = 2
        else:
            prev_place = cur_place
            for i in range(2):
                if (elmts[i][0]+h)>0 and (elmts[i][1]+a)>0:
                    h += elmts[i][0]
                    a += elmts[i][1]
                    cur_place = i
                    break
            if prev_place == cur_place:
                break
            
        time += 1
    return time

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        h, a = map(int, input().split())
        print(dieHard(h, a))