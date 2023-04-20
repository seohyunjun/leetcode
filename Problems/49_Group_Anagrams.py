from util.python2Markdown import Block 

num = 49
subject = 'Group Anagrams'        
leetcode_addr = 'https://leetcode.com/problems/group-anagrams/'
info = '언어유희 ex) cat -> act cat'
sub = """hint: [collections.defaultdict(list)](https://docs.python.org/3/library/collections.html) """

code = """
    class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())
"""
info2 = '##### default_factory: index[x] 에서 x를 찾을 수 없을 때 ValueError때 발생한다. 모든 구현이 추가 인수 i, j 전달을 지원하는 것은 아닙니다. 이러한 인수를 사용하면 시퀀스의 하위 섹션을 효율적으로 검색할 수 있습니다. 추가 인수를 전달하는 것은 데이터를 복사하지 않고 반환된 인덱스가 슬라이스의 시작이 아닌 시퀀스의 시작에 상대적이라는 점만 제외하면 사용하는 것과 거의 동일하다. __s[i:j].index(x)__'


block = Block()
title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
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

sec = 98
memory = 17.2
performance_title = f'##### Result : {sec}ms Memory: {memory}mb'
block.titleblock(performance_title)

block.titleblock(info2)

print_result = ''.join(block.result)

with open(f"{num}_{subject}.md",'w') as f:
    f.write(print_result)
    

####### using slicing
