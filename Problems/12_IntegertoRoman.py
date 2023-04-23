from util.python2Markdown import Block 
from util.func import getInfo
num = 12
subject = 'Integer to Roman'        
leetcode_addr = 'https://leetcode.com/problems/integer-to-roman/description/'
info = 'Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.'
sub = 'Given an integer, convert it to a roman numeral.'
sub_context = 'Answer'
code = """
    class Solution:
        def intToRoman(self, num: int) -> str:
            roman_dict = {
                0 : "V" 
                ,1 : "L" 
                ,2 : "D" 
                }
            
            d_dict= {
                0 : "I" 
                ,1 : "X"
                ,2 : "C"
                ,3 : "M"
            }

            answer = ''
            set_num = 3
            while set_num >= 0:    
                remain = num // 10**set_num

                if remain < 4:
                    answer+= d_dict[set_num] * remain
                elif remain == 4:
                    answer+= d_dict[set_num] + roman_dict[set_num]
                elif remain == 9:
                    answer+= d_dict[set_num] + d_dict[set_num+1] 
                elif remain == 0:
                    pass
                else:
                    answer += roman_dict[set_num] + d_dict[set_num]*(remain-5)

                num %= 10**set_num
                set_num -= 1

            return answer
"""
sec = 48
memory = 13.9

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
