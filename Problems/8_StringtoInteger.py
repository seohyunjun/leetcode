from util.python2Markdown import Block 
from util.func import getInfo
num = 8
subject = 'String to Integer (atoi)'        
leetcode_addr = 'leetchttps://leetcode.com/problems/string-to-integer-atoi/description/ode'
info = 'Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++\'s atoi function).'
sub = 'integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.'
sub_context = 'Answer'
code = """
    class Solution:
        def myAtoi(self, s: str) -> int:
            left = 0 
            k = ''
            p = ''
            for l in s.split(' '):
                if l=='':
                    continue
                elif l.isalpha():
                    break
                left = 0
                while left < len(l):
                    if l[left].isdigit():
                        k += l[left]
                    elif (l[left] in ['+','-']) and (left==0):
                        p += l[left]
                    else:
                        break
                    left+=1
                if k+p != '':
                    break
            if k=='':
                return 0
            k = int(p+k)    
            if k >= 2**31-1:
                return 2**31-1    
            elif k <= -2**31:
                return -2**31
            else:
                return k
"""

sec = 42
memory = 13.9


content = getInfo(subject)

block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)
block.result.append(f"\n {content}")


print_result = ''.join(block.result)

with open(f"markdown/{num}_{subject}.md",'w') as f:
    f.write(print_result)
    

####### using slicing
