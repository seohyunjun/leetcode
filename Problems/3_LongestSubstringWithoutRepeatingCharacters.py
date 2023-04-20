from util.python2Markdown import Block 
from util.func import getInfo
num = 3
subject = 'Longest Substring Without Repeating Characters'        
leetcode_addr = 'https://leetcode.com/problems/longest-substring-without-repeating-characters/'
info = 'Given a string s, find the length of the longest substring without repeating characters.'
sub = 's consists of English letters, digits, symbols and spaces.'
sub_context = 'Answer'
code = """
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            if len(s)==1:
                return 1

            left, right, answer_max = 0, 1, 0
            for _ in range(len(s)):    
                while (left < right) and (right < len(s)):
                    if s[right] in s[left:right]:
                        answer = right - left 
                        left += 1 
                        right = left+1
                        break
                    else:
                        right += 1
                    if right == len(s):
                        answer = right-left
                        break 
                    
                if answer_max < answer:
                    answer_max = answer
            return answer_max
"""
sec = 878
memory = 14


content = getInfo(subject)


block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)
block.result.append(content)

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
