## LeetCode 125 [Valid Palindrome](https://leetcode.com/problems/Valid-Palindrome/)

### Palindrome : 대소문자 구분 없이 좌우가 대칭인 문자열

### 1\. isalnum : 문자 판별 후 소문자 변환

```
    test = 'is a car ; rac a si'
    c_string = []
    for s in test:
        if s.isalnum(): # 문자인지 판별
            c_string.append(s.lower()) # 소문자로 변환
            # c_string # ['i', 's', 'a', 'c', 'a', 'r', 'r', 'a', 'c', 'a', 's', 'i']
```

### 2\. loop로 첫번째 마지막 문자열 비교 후 pop

```
while len(c_string) > 1:
    if c_string.pop(0) != c_string.pop():
    break
#c_string  # = [] True
```

### Result : 221ms Memory: 19.5MB

### 3\. 처음 도출한 답안

```
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
```

### Result : 63ms Memory: 19.3

### 4\. 개선 답안 (데코 자료형을 이용한 최적화)

-   pop(0)은 복잡도가 O(n), popleft()는 O(1)로 리스트 접근보다 5배 빠르다.

```
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
```

### Result : 31ms Memory: 19.3

#### \* python-markdown을 이용한 자동 code review markdown 생성기