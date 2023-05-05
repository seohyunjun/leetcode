from util.python2Markdown import Block 

num = 225
subject = 'Implement Queue using Stacks'        
leetcode_addr = 'https://leetcode.com/problems/implement-stack-using-queues/submissions/928445125/'
info = 'Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack'
sub = 'last-in-first-out (LIFO) '
sub_context = 'Answer'
code = """
    class MyStack:
    
        def __init__(self):
            self.temp = []
            

        def push(self, x: int) -> None:
            self.temp.append(x)

        def pop(self) -> int:
            return self.temp.pop()

        def top(self) -> int:
            return self.temp[-1]
            

        def empty(self) -> bool:
            if self.temp==[]:
                return True
            else:
                return False

    # Your MyStack object will be instantiated and called as such:
    # obj = MyStack()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.empty()
"""
sec = 15
memory = 14

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
