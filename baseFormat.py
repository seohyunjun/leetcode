from util.python2Markdown import Block 

num = 0
subject = ''        
leetcode_addr = ''
info = ''
sub = ''

block = Block()
title_block = f"""
## LeetCode-[{num}]({leetcode_addr}) 
#### {subject} : {info}
#### {sub}
"""
block.titleblock(title_block)

sub_context = ''
subtitle = f'### {sub_context}'
block.titleblock(subtitle)

code = ''
code1 = """
    :::python
    {code}
"""
block.codeblock(code1)

sec = 0
memory = 0
performance_title = f'#### Result : {sec} Memory: {memory}mb'
block.titleblock(performance_title)

print_result = ''.join(block.result)

with open(f"{num}_{subject}.md",'w') as f:
    f.write(print_result)
    

####### using slicing
