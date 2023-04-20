from util.python2Markdown import Block 

num = 819
subject = 'Most Common Word'        
leetcode_addr = 'https://leetcode.com/problems/most-common-word'
info = '금지된 단어를 제외한 가장 많은 빈도의 단어 추출'
sub = 'Info : 대소 문자, 구두점 무시'

code = """
    class Solution:
        def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return Counter([word for word in re.sub("[^a-z]", ' ',paragraph.lower()).split() if word not in banned]).most_common(1)[0][0]
"""

sec = 28
memory = 13.9


block = Block()
title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### {sub}
"""
block.titleblock(title_block)

sub_context = ''
subtitle = f'### {sub_context}'
block.titleblock(subtitle)

code1 = f"""
    :::python
    {code}
"""
block.codeblock(code1)

performance_title = f'##### Result : {sec} Memory: {memory}mb'
block.titleblock(performance_title)

print_result = ''.join(block.result)

with open(f"{num}_{subject}.md",'w') as f:
    f.write(print_result)
    

####### using slicing
