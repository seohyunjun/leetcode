from util.python2Markdown import Block 
from util.func import getInfo
num = 242
subject = 'Valid Anagram'        
leetcode_addr = 'https://leetcode.com/problems/valid-anagram/'
info = 'info'
sub = 'sub'
sub_context = 'the two strings contain the same letters, but the order of the letters may be different.'
code = """
    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            if len(s)!=len(t):
            return False
            for i in s:
                if i not in t:
                    return False
                else:
                    t = t.replace(i,'',1)
            return True
"""
sec = 0
memory = 0

# sub_context2 = ''
# code2 = """"""
# sec2 = 0
# memory2 = 0

content = getInfo(subject,code)

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
