def findTwoElement(arr, n): 
        repeating = -1
        for i in range(n):
            cur_el = arr[i]
            while cur_el != (i+1):
                if arr[cur_el-1] == cur_el:
                    repeating = cur_el
                    break
                arr[i], arr[cur_el-1] = arr[cur_el-1], arr[i]
                cur_el = arr[i]
        for i in range(n):
            if arr[i] != i+1:
                return [repeating, i+1] # This is the missing element
        return [0, 0]