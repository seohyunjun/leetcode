from util.python2Markdown import Block 

num = 238
subject = 'Product of Array Except Self'        
leetcode_addr = 'https://leetcode.com/problems/product-of-array-except-self/'
info = 'A[i]를 제외한 나머지들의 곱'
sub = '제한 O(n), divind 불가'
sub_context = 'MyAnswer'
code = """
    class Solution:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            array1 = []
            result = []
            for i in range(len(nums)):
                array1.append(nums.pop(i))
                res = nums[0]
                if 0 in nums:
                    result.append(0)
                else:
                    
                    for i in range(1, len(nums)):
                        res*=nums[i]
                    result.append(res)
                nums = array1+nums
                array1=[]
            return result
"""
sec = "Time Over-"
memory = "OOM-"

sub_context2 = 'Answer'
code2 = """
    class Solution:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            out = []
            p = 1
            for i in range(0, len(nums)):
                out.append(p)
                p = p*nums[i]
                
            p = 1
            for i in range(len(nums)-1, 0-1, -1):
                out[i] = out[i]*p
                p = p * nums[i]
            return out
"""
sec2 = 221
memory2 = 21.2


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
