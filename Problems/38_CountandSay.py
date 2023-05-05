from util.python2Markdown import Block 
from util.func import getInfo
num = 38
subject = 'Count and Say'        
leetcode_addr = 'https://leetcode.com/problems/count-and-say/description/'
info = 'The count-and-say sequence is a sequence of digit strings defined by the recursive formula:'
sub = 'To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.'
sub_context = 'Answer'
code = """
    class Solution:
        def countAndSay(self, n: int) -> str:
            # countAndSay(1) = "1"
            # countAndSay(2) = say "1" = one 1 = "11"
            # countAndSay(3) = say "11" = two 1's = "21"
            # countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
            if n==1:
                return '1'
            curr = 1
            num='1'
            result = ''
            while curr<n:
                left, right = 0, 1
                
                answer = ''
                while left < len(num):
                    
                    s = num[left]
                    count=1
                    while right < len(num):
                        if s == num[right]:
                            count+=1
                            right+=1
                        else:
                            break
                    answer += f'{count}{s}'
                    left = right
                    right+=1 
                num = answer
                curr+=1
            return answer
"""
sec = 64
memory = 16.4

# sub_context2 = ''
# code2 = """"""
# sec2 = 0
# memory2 = 0

content = getInfo(subject, code)


block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)
#block.addcode_block(sub_context2, code2, sec2, memory2)
block.result.append(f"\n {content}")

# subtitle = f'### {sub_context}'
# block.titleblock(subtitle)

# code1 = f"""
#     :::python
#     {code}
# """
# block.codeblock(code1)

# performance_title = f'##### Result : {sec}ms Memory: {memory}mb'
# block.titleblock(performance_title)

print_result = ''.join(block.result)

with open(f"markdown/{num}_{subject}.md",'w') as f:
    f.write(print_result)
    

####### using slicing
