from util.python2Markdown import Block 
        
block = Block()

input_text = """
## LeetCode 125 [Valid Palindrome](https://leetcode.com/problems/Valid-Palindrome/) 
### Palindrome : 대소문자 구분 없이 좌우가 대칭인 문자열
"""
block.titleblock(input_text)

subtitle = '### 1. isalnum : 문자 판별 후 소문자 변환'
block.titleblock(subtitle)

code1 = """
    :::python
    test = 'is a car ; rac a si'

    c_string = []
    for s in test:
        if s.isalnum(): # 문자인지 판별
            c_string.append(s.lower()) # 소문자로 변환
            # c_string # ['i', 's', 'a', 'c', 'a', 'r', 'r', 'a', 'c', 'a', 's', 'i']
"""
block.codeblock(code1)


subtitle2 = '### 2. loop로 첫번째 마지막 문자열 비교 후 pop'
block.titleblock(subtitle2)

code2 = '''
    :::python
    while len(c_string) > 1:
        if c_string.pop(0) != c_string.pop():
        break
    #c_string  # = [] True
'''
block.codeblock(code2)

result_title = '### Result : 221ms  Memory: 19.5MB'
block.titleblock(result_title)
# my answer runtime 63 ms

subtitle3 = '### 3. 처음 도출한 답안'

block.titleblock(subtitle3)


mycode = """
    :::python
    class Solution:
        def isPalindrome(self, s: str) -> bool:
        p = []
        for i in range(len(s)):
            if s[i].isalnum():
                p.append(s[i].lower())
        p = ''.join(p)        
        k = len(p) // 2
        if p[:k] == ''.join([p[len(p)-i-1] for i in range(k)]):
            return True
        else: 
            return False
"""

block.codeblock(mycode)

result2_title = '### Result : 63ms Memory: 19.3'

block.titleblock(result2_title)


subtitle4 = '### 4. 개선 답안 (데코 자료형을 이용한 최적화)'
block.titleblock(subtitle4)
subtitle4_2 = '* pop(0)은 복잡도가 O(n), popleft()는 O(1)로 리스트 접근보다 5배 빠르다.'
block.titleblock(subtitle4_2)




up_code = """
    :::python
    class Solution:
        def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        
        for i in s:
            if i.isalnum():
                strs.append(i.lower())
        

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True
"""

block.codeblock(up_code)

result3_title = '### Result : 31ms Memory: 19.3'

block.titleblock(result3_title)

print_result = ''.join(block.result)

print(print_result.replace('\n <br>',''))

with open("125_valid_panlindrome.md",'w') as f:
    f.write(print_result)
    

####### using slicing

block = Block()
slicing_title = """
### using Slicing 
#### [leetcode-125](https://leetcode.com/problems/valid-palindrome)
#### + 정규식 사용
"""

block.titleblock(slicing_title)

            
mycode = """
    :::python
    import re
    import collections

    class Solution:
        def isPalindrome(self, s: str) -> bool:
            s = s.lower()
            s = re.sub('[^a-z0-9]','',s)
            
            return s == s[::-1]  # reverse
"""

block.codeblock(mycode)


performance_title = '### Result : 46ms Memory: 15.7mb'

block.titleblock(performance_title)


print(''.join(block.result))


