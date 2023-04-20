from util.python2Markdown import Block 
from util.func import getInfo
num = 6
subject = 'Zigzag Conversion'        
leetcode_addr = 'https://leetcode.com/problems/zigzag-conversion/description/'
info = 'The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows '
sub = 'like this: (you may want to display this pattern in a fixed font for better legibility)'
sub_context = 'Answer'
code = """
    class Solution:
        def convert(self, s: str, numRows: int) -> str:

            if numRows==1:
                return s

            answer = ''
            interval = numRows + (numRows-2)
            ls = [[''] for _ in range(numRows)] 
            for i, l in enumerate(s):
                inter = i%interval
                
                if inter < numRows:
                    ls[inter]+=l
                else:
                    ls[interval-(inter)]+=l

            return ''.join(sum(ls,[]))
"""
sec = 97
memory = 14.2


content = getInfo(subject)


block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)
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
