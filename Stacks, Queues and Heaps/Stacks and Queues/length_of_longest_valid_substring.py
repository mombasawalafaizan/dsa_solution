def findMaxLen(S):
        # code here
        left = 0
        right = 0
        n = len(S)
        maxlength = 0
        for ch in S:
            if ch == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2*right)
            elif right>left:
                left = right = 0
        
        left = right = 0
        
        for i in range(n-1, -1, -1):
            if S[i]=='(':
                left += 1
            else:
                right += 1
            if left==right:
                maxlength = max(maxlength, 2*left)
            elif left>right:
                left = right = 0
        return maxlength