from util.python2Markdown import Block 

num = 234
subject = 'Palindrome Linked List'        
leetcode_addr = 'https://leetcode.com/problems/palindrome-linked-list/'
info = '주어진 head가 palindrome인지 아닌지'
sub = 'range : 1~10^5'
sub_context = 'MyAnswer'
code = """
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def isPalindrome(self, head: Optional[ListNode]) -> bool:        
            temp: List = []
            if not head:
                return True
            node = head
            while node is not None:
                temp.append(node.val)
                node = node.next
            if len(temp)%2==0:
                return temp[:len(temp)//2] == temp[(len(temp)//2):][::-1]
            else:
                return temp[:len(temp)//2] == temp[(len(temp)//2)+1:][::-1]
"""
sec = 855
memory = 46.6

block = Block()


sub_context2 = 'Answer'
code2 = """
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def isPalindrome(self, head: Optional[ListNode]) -> bool:        
            q: Deque = collections.deque()

            if not head:
                return True
            
            node = head
            while node is not None:
                q.append(node.val)
                node = node.next
            
            while len(q) > 1:
                if q.popleft()!=q.pop():
                    return False
            return True
        
"""
sec2 = 775
memory2 = 47.5


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
    
