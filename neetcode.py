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