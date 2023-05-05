
    
    
from util.python2Markdown import Block 
from util.func import getInfo
num = 347
subject = 'Top K Frequent Elements'        
leetcode_addr = 'https://leetcode.com/problems/top-k-frequent-elements/description/'
info = 'Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.'
sub = 'time complexity must be better than O(n log n), where n is the array s size.'
sub_context = 'Over *'
code = """
    class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:

            if len(set(nums))==1:
                return [nums[0]]

            answer = []
            count = collections.Counter(nums).most_common(n=k)
            return [i[0] for i in count]    
"""
sec = 111
memory = 21

# sub_context2 = ''
# code2 = """"""
# sec2 = 0
# memory2 = 0

content = getInfo(subject)


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
