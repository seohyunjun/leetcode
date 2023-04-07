from util.python2Markdown import Block 

num = 622
subject = 'Design Circular Queue'        
leetcode_addr = 'https://leetcode.com/problems/design-circular-queue/'
info = 'Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".'
sub = 'You must solve the problem without using the built-in queue data structure in your programming language.'
sub_context = 'MyAnswer'
code = """
    class MyCircularQueue:
        def __init__(self, k: int):
            self.deq = collections.deque(maxlen=k)
            self.maxlen = k
            self.deq_len = 0

        def enQueue(self, value: int) -> bool:
            if self.deq_len < self.maxlen:
                self.deq.append(value)
                self.deq_len+=1
                return True
            else:
                return False

        def deQueue(self) -> bool:
            if self.deq_len > 0:
                self.deq.popleft()
                self.deq_len-=1
                return True
            else:
                return False
        def Front(self) -> int:
            if self.deq_len > 0:
                return self.deq[0]
            else:
                return -1
        def Rear(self) -> int:
            if self.deq_len > 0:
                return self.deq[-1]
            else:
                return -1

        def isEmpty(self) -> bool:
            if self.deq_len == 0:
                return True
            else:
                return False

        def isFull(self) -> bool:
            if self.deq_len == self.maxlen:
                return True
            else:
                return False

    # Your MyCircularQueue object will be instantiated and called as such:
    # obj = MyCircularQueue(k)
    # param_1 = obj.enQueue(value)
    # param_2 = obj.deQueue()
    # param_3 = obj.Front()
    # param_4 = obj.Rear()
    # param_5 = obj.isEmpty()
    # param_6 = obj.isFull()
"""
sec = 57
memory = 14.4

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
