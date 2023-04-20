from util.python2Markdown import Block 

num = 20
subject = 'Valid Parentheses'        
leetcode_addr = 'https://leetcode.com/problems/valid-parentheses/description/'
info = 'Given a string s containing just the characters \(, \), \{, \}, \[ and \], determine if the input string is valid.'
sub = 's consists of parentheses only \(\)\[\]\{\}'
sub_context = 'Answer'
code = """
    class Solution:
        def isValid(self, s: str) -> bool:
            valid = []
            dict_valid = {
                "}":"{",
                "]":"[",
                ")":"("
            }

            for l in s:
                if l not in dict_valid:
                    valid.append(l)

                elif not valid or dict_valid[l] != valid.pop():
                    return False
            return len(valid)==0
"""
sec = 31
memory = 13.9

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
