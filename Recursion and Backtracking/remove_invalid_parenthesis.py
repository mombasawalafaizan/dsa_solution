from typing import List
class Solution:
    def __init__(self):
        self.valid_expressions = None
        self.min_removed = None
    
    def reset(self):
        self.valid_expressions = set()
        self.min_removed = float('inf')
    
    def remaining(self, s, idx, left, right, expr, rem_count):
        if idx==len(s):
            if left==right and rem_count <= self.min_removed:
                possible_ans = ''.join(expr)
                if rem_count < self.min_removed:
                    self.valid_expressions = set()
                    self.min_removed = rem_count
                self.valid_expressions.add(possible_ans)
        else:
            cur_char = s[idx]
            if cur_char not in ['(', ')']:
                expr.append(cur_char)
                self.remaining(s, idx+1, left, right, expr, rem_count)
                expr.pop()
            else:
                #Ignore
                self.remaining(s, idx+1, left, right, expr, rem_count + 1)
                expr.append(cur_char)
                
                if s[idx] == '(':
                    self.remaining(s, idx+1, left+1, right, expr, rem_count)
                elif right < left:
                    self.remaining(s, idx+1, left, right + 1, expr, rem_count)
                expr.pop()
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
#         self.reset()
#         self.remaining(s, 0, 0, 0, [], 0)
#         return list(self.valid_expressions)
        left = 0
        right = 0

        # First, we find out the number of misplaced left and right parentheses.
        for char in s:

            # Simply record the left one.
            if char == '(':
                left += 1
            elif char == ')':
                # If we don't have a matching left, then this is a misplaced right, record it.
                right = right + 1 if left == 0 else right

                # Decrement count of left parentheses because we have found a right
                # which CAN be a matching one for a left.
                left = left - 1 if left > 0 else left

        result = {}
        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            # If we reached the end of the string, just check if the resulting expression is
            # valid or not and also if we have removed the total number of left and right
            # parentheses that we should have removed.
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)
                    result[ans] = 1
            else:

                # The discard case. Note that here we have our pruning condition.
                # We don't recurse if the remaining count for that parenthesis is == 0.
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem - (s[index] == '('),
                            right_rem - (s[index] == ')'), expr)

                expr.append(s[index])    

                # Simply recurse one step further if the current character is not a parenthesis.
                if s[index] != '(' and s[index] != ')':
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == '(':
                    # Consider an opening bracket.
                    recurse(s, index + 1,
                            left_count + 1,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == ')' and left_count > right_count:
                    # Consider a closing bracket.
                    recurse(s, index + 1,
                            left_count,
                            right_count + 1,
                            left_rem,
                            right_rem, expr)

                # Pop for backtracking.
                expr.pop()                 

        # Now, the left and right variables tell us the number of misplaced left and
        # right parentheses and that greatly helps pruning the recursion.
        recurse(s, 0, 0, 0, left, right, [])     
        return list(result.keys())