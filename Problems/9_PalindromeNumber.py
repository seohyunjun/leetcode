from util.python2Markdown import Block 
from util.func import getInfo
num = 9
subject = 'PalindromeNumber'        
leetcode_addr = 'leetcode'
info = 'Given an integer x, return true if x is a palindrome, and false otherwise.'
sub = 'From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.'
sub_context = 'Answer'
code = """
    class Solution:
        def isPalindrome(self, x: int) -> bool:
            return str(x) == str(x)[::-1]
"""
sec = 57
memory = 13.7


content = getInfo(subject)


block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)
block.result.append(f"\n content")

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
