from collections import deque

class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        length = len(s)
        p_length = len(p)
        
        p_idx = 0
        possible = ""
        
        s_idx = 0
        while p_idx < p_length:
            if p[p_idx] == ".":
                possible = 'all'
                s_idx += 1
            
            elif p[p_idx] == "*":
                # while True:
                    # 없는 취급을 하거나 하나 이상 앞에거랑 똑같아야 함
                    # if possible == 'all' or possible == s[s_idx]:
                        
                while s_idx < length - 1 and (possible == 'all' or possible == s[s_idx]):
                    s_idx += 1
                
                    
            else:
                possible = s[s_idx]
                if s[s_idx] != p[p_idx]:
                    return False
                
                s_idx += 1
            
            p_idx += 1
            
        
        print(p_idx, s_idx)
        
        if s_idx <= length-1:
            return False
        
        
        return True
            
            
                