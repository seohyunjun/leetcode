from util.python2Markdown import Block 

num = 739
subject = 'Daily Temperature'        
leetcode_addr = 'https://leetcode.com/problems/daily-temperatures/'
info = '몇 일 후 기온이 오를까?'
sub = 'Answer'
sub_context = ''
code = """
    class Solution:
        def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            out = []
            left, right = 0, 0
            while left != len(temperatures)-1:
                day = 0
                check = 0
                while right < len(temperatures): 
                    if (temperatures[left] < temperatures[right]):
                        out.append(day)
                        check = 1
                        right = left + 1
                        break  
                    right+=1
                    day+=1
                if check==0:
                    out.append(0)
                    right = left + 1
                left+=1
            
            out.append(0)
            return out
"""
sec = "Timeout"
memory = "Timeout"


sub_context2 = 'Answer'
code2 = """
    class Solution:
        def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
            answer = [0] * len(temperatures)
            stack = []

            for i, cur in enumerate(temperatures):
                
                while stack and cur > temperatures[stack[-1]] :
                    last = stack.pop()
                    answer[last] = i - last
                stack.append(i)
            return answer
"""
sec2 = "1352"
memory2 = "28.6"


block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)


block.addcode_block(sub_context2, code2, sec2, memory2)


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
