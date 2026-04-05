from typing import *

# -- Stack --
def calPoints(self, operations: List[str]) -> int:
    s = []
    for ops in operations:
        if ops == '+':
            s.append(s[-1] + s[-2])
        elif ops == 'D':
            s.append(s[-1] * 2)
        elif ops == 'C':
            s.pop() 
        else:
            s.append(int(ops))   
    
    return sum(s)
    

def isValid(self, s: str) -> bool:
    bracket_mapping = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    
    st = []
    for c in s:
        if c in bracket_mapping:
            st.append(c)
        
        else:
            if not st:
                return False

            last_open_bracket = st.pop()
            if bracket_mapping[last_open_bracket] != c:
                return False
        
    return len(st) == 0



class Solution:
    def rob(self, nums: List[int]) -> int:
        
        outer_n = len(nums)
        if outer_n == 1:
            return nums[0]
        if outer_n == 2:
            return max(nums[0], nums[1])
        
        def roblinear(nums_sub: List[int]):
            inner_n = len(nums_sub)
            if inner_n == 1:
                return nums_sub[0]
            if inner_n == 2:
                return max(nums_sub[0], nums_sub[1])
            
            dp = [0] * inner_n
            dp[0] = nums_sub[0]
            dp[1] = max(nums_sub[0], nums_sub[1])

            for i in range(2, inner_n):
                rob_current = nums_sub[i] + dp[i-2]
                skip_current = 0 + dp[i-1]
                dp[i] = max(rob_current, skip_current)
            
            return dp[inner_n]
        
        rob_first_skip_last = roblinear(nums[:outer_n-1])
        rob_last_skip_first = roblinear(nums[1:outer_n])
        
        return max(rob_first_skip_last, rob_last_skip_first)


        