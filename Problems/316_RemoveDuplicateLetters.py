from util.python2Markdown import Block 

num = 316
subject = 'Remove Duplicate Letters'        
leetcode_addr = 'https://leetcode.com/problems/remove-duplicate-letters/description/'
info = 'Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.'
sub = ''
sub_context = 'Answer'
code = """
    class Solution:
        def removeDuplicateLetters(self, s: str) -> str:
            for char in sorted(set(s)):
                suffix = s[s.index(char):]

                if set(s)==set(suffix):
                    return char + self.removeDuplicateLetters(suffix.replace(char,''))
            return ''
"""
sec = 55
memory = 14.1

block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)

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
