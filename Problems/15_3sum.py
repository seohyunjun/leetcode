from util.python2Markdown import Block 

num = 15
subject = 'Match Three sum '        
leetcode_addr = 'https://leetcode.com/problems/3sum/'
info = 'Notice that the solution set must not contain duplicate triplets.'
sub = 'myAnswer'
sub_context = 'MyAnswer(Time Limit Exceeded) O(n^2)'
code = """
    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            a = []
            nums.sort()
            for i, n in enumerate(nums):
                d = {}
                for j in range(i+1,len(nums)):
                    complete = - (n + nums[j])
                    
                    if complete in d:
                        if sorted([n, nums[j], complete]) not in a:
                            a.append(sorted([n, nums[j], complete]))
                    else:
                        d[nums[j]] = j

            return a
"""
sec = "9669"
memory = "19.4"

sub_context2 = 'Answer(Two Point Sum) base|left|right'
code2 = """
    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            results = []
            nums.sort()
                
            for i in range(len(nums)-2):
                # skip duplicate number 
                if i > 0 and nums[i]==nums[i-1]:
                    continue
                
                left, right = i+1, len(nums)-1
                
                while left < right:
                    sum = nums[i] + nums[left] + nums[right]
                    if sum < 0:
                        left+=1
                    elif sum > 0:
                        right-=1
                    else:
                        results.append([nums[i],nums[left],nums[right]])
                        
                        while left < right and nums[left]==nums[left+1]:
                            left+=1
                        while left < right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
            return results
"""


sec2 = "1389"
memory2 = "18.3"

#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets.

 
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
