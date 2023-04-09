from util.python2Markdown import Block 
from util.func import getInfo
 
num = 641
subject = 'Design Circular Deque'        
leetcode_addr = 'https://leetcode.com/problems/design-circular-deque/'
info = 'Design your implementation of the circular double-ended queue (deque).'
sub = 'Returns -1 if the deque is empty.'
sub_context = 'MyAnswer'

content = getInfo(subject)

code = """
    class MyCircularDeque:
        
        def __init__(self, k: int):
            self.maxsize = k
            self.deq = collections.deque(maxlen=k)
            self.deq_size = 0
            

        def insertFront(self, value: int) -> bool:
            if self.deq_size < self.maxsize:
                self.deq.insert(0,value)
                self.deq_size += 1
                return True
            else:
                return False
            

        def insertLast(self, value: int) -> bool:
            if self.deq_size < self.maxsize:
                self.deq.append(value)
                self.deq_size += 1
                return True
            else:
                return False

        def deleteFront(self) -> bool:
            if self.deq_size > 0:
                self.deq.popleft()
                self.deq_size -= 1
                return True
            else:
                return False
            

        def deleteLast(self) -> bool:
            if self.deq_size > 0:
                self.deq.pop()
                self.deq_size -= 1
                return True
            else:
                return False
            

        def getFront(self) -> int:
            if self.deq_size > 0:
                return self.deq[0]
            else:
                return -1

        def getRear(self) -> int:
            if self.deq_size > 0:
                return self.deq[-1]
            else:
                return -1


        def isEmpty(self) -> bool:
            if self.deq_size==0:
                return True
            else:
                return False


        def isFull(self) -> bool:
            if self.deq_size==self.maxsize:
                return True
            else:
                return False



    # Your MyCircularDeque object will be instantiated and called as such:
    # obj = MyCircularDeque(k)
    # param_1 = obj.insertFront(value)
    # param_2 = obj.insertLast(value)
    # param_3 = obj.deleteFront()
    # param_4 = obj.deleteLast()
    # param_5 = obj.getFront()
    # param_6 = obj.getRear()
    # param_7 = obj.isEmpty()
    # param_8 = obj.isFull()


"""
sec = 61
memory = 14.7

block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)
block.result.append(content)

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
    