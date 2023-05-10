from util.python2Markdown import Block 
from util.func import getInfo
num = 706
subject = 'Design HashMap'        
leetcode_addr = 'https://leetcode.com/problems/design-hashmap/'
info = 'Design a HashMap without using any built-in hash table libraries.'
sub = 'At most 104 calls will be made to put, get, and remove.'
sub_context = 'Answer'
code = """
    class ListNode:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.next = None
    class MyHashMap:
        def __init__(self):
            self.size = 10**4
            self.table = collections.defaultdict(ListNode)

        def put(self, key: int, value: int) -> None:
            index = key % self.size
            if self.table[index].value is None:
                self.table[index] = ListNode(key, value)
                return
            p = self.table[index]
            while p:
                if p.key == key :
                    p.value = value
                    return
                if p.next is None:
                    break
                p = p.next
            p.next = ListNode(key, value)
        def get(self, key: int) -> int:
            index = key % self.size
            if self.table[index].value is None:
                return -1
            p = self.table[index]
            while p:
                if p.key == key:
                    return p.value
                p = p.next
            return -1

        def remove(self, key: int) -> None:
            index = key % self.size
            if self.table[index].value is None:
                return
            p = self.table[index]
            if p.key == key:
                self.table[index] = ListNode() if p.next is None else p.next 
                return
            prev = p
            while p:
                if p.key == key:
                    prev.next = p.next
                    return
                prev, p = p, p.next



    # Your MyHashMap object will be instantiated and called as such:
    # obj = MyHashMap()
    # obj.put(key,value)
    # param_2 = obj.get(key)
    # obj.remove(key)
"""
sec = 234
memory = 20.6

# sub_context2 = ''
# code2 = """"""
# sec2 = 0
# memory2 = 0

content = getInfo(subject, code)


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
