from util.python2Markdown import Block 
from util.func import getInfo
num = 10
subject = 'Regular Expression Matching'        
leetcode_addr = 'https://leetcode.com/problems/regular-expression-matching/description/'
info = 'Given an input string s and a pattern p, implement regular expression matching '
sub = 'The matching should cover the entire input string (not partial).'
sub_context = 'Answer'
code = """
    class Solution:
        def isMatch(self, s: str, p: str) -> bool:
            
            if len(re.findall(p,s))>0:
                return s == re.findall(p,s)[0]
            else:
                return False
"""
sec = 201
memory = 13.9

sub_context2 = 'Solve'
code2 = """
    class Solution:
        def isMatch(self, s: str, p: str) -> bool:
            i, j = len(s) - 1, len(p) - 1
            return self.backtrack({}, s, p, i, j)

        def backtrack(self, cache, s, p, i, j):
            key = (i, j)
            if key in cache:
                return cache[key]

            if i == -1 and j == -1:
                cache[key] = True
                return True

            if i != -1 and j == -1:
                cache[key] = False
                return cache[key]

            if i == -1 and p[j] == '*':
                k = j
                while k != -1 and p[k] == '*':
                    k -= 2
                
                if k == -1:
                    cache[key] = True
                    return cache[key]
                
                cache[key] = False
                return cache[key]
            
            if i == -1 and p[j] != '*':
                cache[key] = False
                return cache[key]

            if p[j] == '*':
                if self.backtrack(cache, s, p, i, j - 2):
                    cache[key] = True
                    return cache[key]
                
                if p[j - 1] == s[i] or p[j - 1] == '.':
                    if self.backtrack(cache, s, p, i - 1, j):
                        cache[key] = True
                        return cache[key]
            
            if p[j] == '.' or s[i] == p[j]:
                if self.backtrack(cache, s, p, i - 1, j - 1):
                    cache[key] = True
                    return cache[key]

            cache[key] = False
            return cache[key]
"""
sec2 = 198
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
