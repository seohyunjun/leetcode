from util.python2Markdown import Block 

num = 344
subject = 'ReverseString'        
leetcode_addr = 'https://leetcode.com/problems/reverse-string/'
info = '문자열 리스트 뒤집기'
sub = '리턴 없이 리스트 내부의 주소 값이 변하도록'

block = Block()
title_block = f"""
## LeetCode-[{num}]({leetcode_addr}) 
#### {subject} : {info}
#### {sub}
"""
block.titleblock(title_block)

sub_context = 'my answer'
subtitle = f'### {sub_context}'
block.titleblock(subtitle)
code = '''
    class Solution:
        def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)):
            s.append(s.pop(-i-1)) 
'''

code1 = f"""
    :::python
    {code}
"""
block.codeblock(code1)


sec = 394
memory = 18.4
performance_title = f'#### Result : {sec} Memory: {memory}mb'
block.titleblock(performance_title)


sub_context = '1. 투 포인트 스왑'
subtitle = f'### {sub_context}'
block.titleblock(subtitle)
code = '''
    class Solution:
        def reverseString(self, s: List[str]) -> None:
            """
            Do not return anything, modify s in-place instead.
            """
            left, right = 0, len(s) - 1
            while left < right : 
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
'''

code2 = """
    :::python
    {code}
"""
block.codeblock(code2)

sec = 205
memory = 18.5
performance_title = f'#### Result : {sec} Memory: {memory}mb'
block.titleblock(performance_title)

print_result = ''.join(block.result)

with open("{num}_{subject}.md",'w') as f:
    f.write(print_result)
    

####### using slicing
