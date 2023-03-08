from util.python2Markdown import Block 

num = 561
subject = 'Array Partition'        
leetcode_addr = 'https://leetcode.com/problems/array-partition/'
info = 'find maximum (minimum list)'
sub = 'len(list) = 2n'
sub_context = 'myAnswer'
code = """
    class Solution:
        def arrayPairSum(self, nums: List[int]) -> int:
            nums.sort()
            return sum(nums[::2])
"""
sec = 267
memory = 16.7

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

nums = [1,4,3,2]
nums = [6,2,6,5,1,2]
nums = [1,2,3,2]

def ArrayPartition(nums):
    result = 0
    left_min = 0 
    while len(nums)>0:
        left, right = 0, len(nums)-1    
        while left < right:
            if nums[right] < nums[left_min] and nums[right] < nums[left]:
                left_min = left
                left+=1 
            else:
                right-=1
            
        if len(nums)%2==0:
            result+=nums.pop(-left_min)
        else:
            nums.pop(-left_min)
    return result
ArrayPartition(nums)
