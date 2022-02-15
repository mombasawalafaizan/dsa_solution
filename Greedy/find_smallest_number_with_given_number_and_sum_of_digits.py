def smallestNumber (S,D):
        if (S>9*D):
            return -1
        res = ''
        remaining_sum = S-1
        for i in range(D):
            if i==(D-1):
                remaining_sum += 1
            if remaining_sum > 9:
                res = '9' + res
                remaining_sum -= 9
            else:
                res = str(remaining_sum) + res
                remaining_sum = 0
        return res