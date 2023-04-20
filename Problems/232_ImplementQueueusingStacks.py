from util.python2Markdown import Block 

num = 232
subject = 'Implement Queue using Stacks'        
leetcode_addr = 'https://leetcode.com/problems/implement-queue-using-stacks/'
info = 'Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).'
sub = 'sub'
sub_context = '선입선출'
code = """
    class MyQueue:
    
        def __init__(self):
            self.temp = collections.deque()

        def push(self, x: int) -> None:
            self.temp.append(x)

        def pop(self) -> int:   
            return self.temp.popleft()

        def peek(self) -> int:
            return self.temp[0]

        def empty(self) -> bool:
            if len(self.temp) == 0:
                return True
            else:
                return False


    # Your MyQueue object will be instantiated and called as such:
    # obj = MyQueue()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.peek()
    # param_4 = obj.empty()
"""
sec = 34
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
