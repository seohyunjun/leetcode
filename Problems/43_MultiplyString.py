from util.python2Markdown import Block 
from util.func import getInfo
num = 43
subject = 'Multiply Strings'        
leetcode_addr = 'leehttps://leetcode.com/problems/multiply-strings/description/tcode'
info = 'Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.'
sub = 'Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.'
sub_context = ''
code = """
    class Solution:
        def multiply(self, num1: str, num2: str) -> str:
            if (num1=='0') or (num2=='0'):
                return '0'
                
            return str(int(num1)*int(num2))
"""
sec = 19
memory = 13.9

sub_context2 = 'using dict'
code2 = """
    class Solution:
        def multiply(self, num1: str, num2: str) -> str:
            num_dict = {
                "0":0
                ,"1":1
                ,"2":2
                ,"3":3
                ,"4":4
                ,"5":5
                ,"6":6
                ,"7":7
                ,"8":8
                ,"9":9
            }
            i=0
            answer = ''
            s = 0
            for nu, n1 in enumerate(num1[::-1]):
                for nu2, n2 in enumerate(num2[::-1]):
                    s += num_dict[n1]*10**(nu)*num_dict[n2]*10**nu2
                    
            return str(s)
"""
sec2 = 230
memory2 = 14

content = getInfo(subject)


block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)
block.addcode_block(sub_context2, code2, sec2, memory2)
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
