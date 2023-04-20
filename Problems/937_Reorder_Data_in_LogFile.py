from util.python2Markdown import Block 

num = 937
subject = 'Reorder_Data_in_LogFile'        
leetcode_addr = 'https://leetcode.com/problems/reorder-data-in-log-files/'
info = 'reorder log files'
sub = '첫번째 문자 식별자 ex) "dig2 a","dig1 b"-> "a","b"'

block = Block()
title_block = f"""
## LeetCode-[{num}]({leetcode_addr}) 
##### {subject} : {info}
##### note: {sub}
"""
block.titleblock(title_block)

sub_context = 'Myanswer'
subtitle = f'### {sub_context}'
block.titleblock(subtitle)

    
code = """
    class Solution:
        def reorderLogFiles(self, logs: List[str]) -> List[str]:   
            let = []
            digit = []

            for i in logs:
                if i.split()[1].isdigit()==False:
                    let.append(i)
                else:
                    digit.append(i) 
            
            let.sort(key = lambda x: (x.split()[1:], x.split()[0]))
            #digit.sort(key = lambda x: x.split()[1:],reverse=True)

            return let + digit
"""
code1 = f"""
    :::python
    {code}
"""
block.codeblock(code1)

sec = 38
memory = 14
performance_title = f'#### Result : {sec}ms Memory: {memory}mb'
block.titleblock(performance_title)

print_result = ''.join(block.result)

with open(f"{num}_{subject}.md",'w') as f:
    f.write(print_result)
    

####### using slicing
