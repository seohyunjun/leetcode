from util.python2Markdown import Block 
from util.func import getInfo
num = 14
subject = 'Longest Common Prefix'        
leetcode_addr = 'https://leetcode.com/problems/longest-common-prefix/description/'
info = 'Write a function to find the longest common prefix string amongst an array of strings.'
sub = 'If there is no common prefix, return an empty string "".'
sub_context = 'Answer'
code = """
    class Solution:
        def longestCommonPrefix(self, strs: List[str]) -> str:
        
            if len(strs)==1:
                return strs[0]

            answer = ''
            i = 0
            min_p = min([len(s) for s in strs])
            if min_p==0:
                return ""

            while i < min_p:
                
                if len(set([s[i] for s in strs]))==1:
                    answer+=strs[0][i]
                else:
                    break

                i+=1
            return answer
"""
sec = 24
memory = 14

sub_context2 = 'Answer'
code2 = """
    class Solution:
        def longestCommonPrefix(self, strs: List[str]) -> str:
            minimum = len(strs[0])
            for i in range(1,len(strs)):
                if (len(strs[i]) < minimum):
                    minimum = len(strs[i])

            result = ''
            for i in range(minimum):
                current = strs[0][i]

                for j in range(1,len(strs)):
                    if (strs[j][i] != current):
                        return result

                result = result + current
            return result
"""
sec2 = 24
memory2 = 14

content = getInfo(subject)


block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)
block.addcode_block(sub_context2, code2, sec2, memory2)

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
