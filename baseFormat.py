from util.python2Markdown import Block 

num = 0
subject = 'subject'        
leetcode_addr = 'leetcode'
info = 'info'
sub = 'sub'
code = """"""

sec = 0
memory = 0

block = Block()
title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)

sub_context = ''
subtitle = f'### {sub_context}'
block.titleblock(subtitle)

code1 = f"""
    :::python
    {code}
"""
block.codeblock(code1)

performance_title = f'##### Result : {sec}ms Memory: {memory}mb'
block.titleblock(performance_title)

print_result = ''.join(block.result)

with open(f"{num}_{subject}.md",'w') as f:
    f.write(print_result)
    

####### using slicing
