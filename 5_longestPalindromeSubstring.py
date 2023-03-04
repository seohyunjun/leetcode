from util.python2Markdown import Block 

num = 5
subject = 'Longest Palindrome Substring'        
leetcode_addr = 'https://leetcode.com/problems/longest-palindromic-substring/'
info = '가장 긴 Palindrome'
sub = ''


sub_context = 'Myanswer'
code = """
    class Solution:
        def longestPalindrome(self, s: str) -> str:
            if len(s)==1:
                return s[0]
            for i in range(0,len(s)-1):
                for j in range(0,i+1):
                    org = s[j:len(s)-(-j+i)]            
                    if org[::-1]==org:
                        return org
            return org[0]
"""

sec = 6515
memory = 13.9

sub_context2 = 'Solution'
code2 = """
    class Solution:
        def longestPalindrome(self, s: str) -> str:
            def expend(left: int, right: int) -> str:
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    
                    left -= 1
                    right += 1
                return s[left+1:right]
            
            if len(s) < 2 or s == s[::-1]:
                return s

            result = ''

            for i in range(len(s)-1):
                # 'babaddasdasd'
                
                print(result)
                result = max(
                    result,
                    expend(i, i+1),
                    expend(i, i+2),
                    key=len
                )
                
            return result
"""
sec2 = 103
memory2 = 13.9
            
            
block = Block()
title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)

subtitle = f'### {sub_context}'
block.titleblock(subtitle)

code1 = f"""
    :::python
    {code}
"""
block.codeblock(code1)
performance_title = f'##### Result : {sec}ms Memory: {memory}mb'
block.titleblock(performance_title)


subtitle2 = f'### {sub_context2}'
block.titleblock(subtitle2)

code2_ = f"""
    :::python
    {code2}
"""
block.codeblock(code2_)
performance_title2 = f'##### Result : {sec2}ms Memory: {memory2}mb'
block.titleblock(performance_title2)

print_result = ''.join(block.result)

with open(f"{num}_{subject}.md",'w') as f:
    f.write(print_result)
    

####### using slicing
