from bisect import bisect_right

def possibleKills(soldiers, soldiers_sum, cur_power):
    number_of_kills = bisect_right(soldiers, cur_power)
    if number_of_kills==0:
        return [0, 0]
    return [number_of_kills, soldiers_sum[number_of_kills-1]]

if __name__ == "__main__":
    n = int(input())
    soldiers = list(map(int, input().split()))
    soldiers.sort()
    power_sum = [0] * n
    power_sum[0] = soldiers[0]
    for i in range(1, n):
        power_sum[i] = power_sum[i-1] + soldiers[i]
    Q = int(input())
    for i in range(Q):
        cur_power = int(input())
        kills, sum_of_powers = possibleKills(soldiers, power_sum,\
                    cur_power)
        print(kills, sum_of_powers)
    