from util.python2Markdown import Block 
from util.func import getInfo
num = 36
subject = ' Valid Sudoku'        
leetcode_addr = 'https://leetcode.com/problems/valid-sudoku/description/'
info = 'A Sudoku board (partially filled) could be valid but is not necessarily solvable.'
sub = 'Only the filled cells need to be validated according to the mentioned rules.'
sub_context = 'Answer'
code = """
    class Solution:
        def isValidSudoku(self, board: List[List[str]]) -> bool:
            def valid_row(i, j, row):
                if row==1:
                    item = board[i]
                else:
                    item = [board[n][j] for n in range(0,9)]
                p = []
                
                box = [board[i//3*2 + r][j//3*2 + c] for r in range(i//3, i//3+3) for c in range(j//3, j//3+3)]    
                b = []
                for i in range(0,9):
                    if item[i] !='.':
                        p.append(item[i])
                    if box[i] !='.':
                        b.append(box[i])
                    
                if len(set(box))-1 == len(b):
                    pass 
                else:
                    return False
                        
                if len(set(item))-1 == len(p):
                    return True 
                else: 
                    return False
                
            for i in range(0,9):

                for j in range(0,9):
                    if valid_row(i,j,0) and valid_row(i,j,1):
                        pass
                    else:
                        return False
            return True
"""
sec = 272
memory = 16.5

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
