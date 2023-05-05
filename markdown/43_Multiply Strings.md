<h2>LeetCode-<a href="leehttps://leetcode.com/problems/multiply-strings/description/tcode">43</a></h2>
<h5>Multiply Strings : Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.</h5>
<h5>note : Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.</h5><h3></h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">:::</span><span class="n">python</span><span class="w"></span>

<span class="n">class</span><span class="w"> </span><span class="n">Solution</span><span class="o">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">multiply</span><span class="p">(</span><span class="kr">self</span><span class="p">,</span><span class="w"> </span><span class="n">num1</span><span class="o">:</span><span class="w"> </span><span class="n">str</span><span class="p">,</span><span class="w"> </span><span class="n">num2</span><span class="o">:</span><span class="w"> </span><span class="n">str</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">str</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="nf">if</span><span class="w"> </span><span class="p">(</span><span class="n">num1</span><span class="o">==</span><span class="s">&#39;0&#39;</span><span class="p">)</span><span class="w"> </span><span class="kr">or</span><span class="w"> </span><span class="p">(</span><span class="n">num2</span><span class="o">==</span><span class="s">&#39;0&#39;</span><span class="p">)</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="s">&#39;0&#39;</span><span class="w"></span>
<span class="w">        </span><span class="kr">return</span><span class="w"> </span><span class="n">str</span><span class="p">(</span><span class="n">int</span><span class="p">(</span><span class="n">num1</span><span class="p">)</span><span class="o">*</span><span class="n">int</span><span class="p">(</span><span class="n">num2</span><span class="p">))</span><span class="w"></span>
</code></pre></div><h3>Result : 19ms Memory: 13.9mb</h3><h3>using dict</h3><div class="codehilite"><pre><span></span><code>        <span class="s s-Atom">:::python</span>

<span class="s s-Atom">class</span> <span class="nv">Solution</span><span class="s s-Atom">:</span>
    <span class="s s-Atom">def</span> <span class="nf">multiply</span><span class="p">(</span><span class="s s-Atom">self</span><span class="p">,</span> <span class="s s-Atom">num1:</span> <span class="s s-Atom">str</span><span class="p">,</span> <span class="s s-Atom">num2:</span> <span class="s s-Atom">str</span><span class="p">)</span> <span class="s s-Atom">-&gt;</span> <span class="nn">str</span><span class="p">:</span>
        <span class="s s-Atom">num_dict</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s2">&quot;0&quot;</span><span class="s s-Atom">:</span><span class="mi">0</span>
            <span class="p">,</span><span class="s2">&quot;1&quot;</span><span class="s s-Atom">:</span><span class="mi">1</span>
            <span class="p">,</span><span class="s2">&quot;2&quot;</span><span class="s s-Atom">:</span><span class="mi">2</span>
            <span class="p">,</span><span class="s2">&quot;3&quot;</span><span class="s s-Atom">:</span><span class="mi">3</span>
            <span class="p">,</span><span class="s2">&quot;4&quot;</span><span class="s s-Atom">:</span><span class="mi">4</span>
            <span class="p">,</span><span class="s2">&quot;5&quot;</span><span class="s s-Atom">:</span><span class="mi">5</span>
            <span class="p">,</span><span class="s2">&quot;6&quot;</span><span class="s s-Atom">:</span><span class="mi">6</span>
            <span class="p">,</span><span class="s2">&quot;7&quot;</span><span class="s s-Atom">:</span><span class="mi">7</span>
            <span class="p">,</span><span class="s2">&quot;8&quot;</span><span class="s s-Atom">:</span><span class="mi">8</span>
            <span class="p">,</span><span class="s2">&quot;9&quot;</span><span class="s s-Atom">:</span><span class="mi">9</span>
        <span class="p">}</span>
        <span class="s s-Atom">i</span><span class="o">=</span><span class="mi">0</span>
        <span class="s s-Atom">answer</span> <span class="o">=</span> <span class="s s-Atom">&#39;&#39;</span>
        <span class="s s-Atom">s</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="s s-Atom">for</span> <span class="s s-Atom">nu</span><span class="p">,</span> <span class="s s-Atom">n1</span> <span class="s s-Atom">in</span> <span class="nf">enumerate</span><span class="p">(</span><span class="s s-Atom">num1</span><span class="p">[</span><span class="s s-Atom">::-</span><span class="mi">1</span><span class="p">])</span><span class="s s-Atom">:</span>
            <span class="s s-Atom">for</span> <span class="s s-Atom">nu2</span><span class="p">,</span> <span class="s s-Atom">n2</span> <span class="s s-Atom">in</span> <span class="nf">enumerate</span><span class="p">(</span><span class="s s-Atom">num2</span><span class="p">[</span><span class="s s-Atom">::-</span><span class="mi">1</span><span class="p">])</span><span class="s s-Atom">:</span>
                <span class="s s-Atom">s</span> <span class="s s-Atom">+=</span> <span class="s s-Atom">num_dict</span><span class="p">[</span><span class="s s-Atom">n1</span><span class="p">]</span><span class="o">*</span><span class="mi">10</span><span class="s s-Atom">**</span><span class="p">(</span><span class="s s-Atom">nu</span><span class="p">)</span><span class="o">*</span><span class="s s-Atom">num_dict</span><span class="p">[</span><span class="s s-Atom">n2</span><span class="p">]</span><span class="o">*</span><span class="mi">10</span><span class="s s-Atom">**nu2</span>
        <span class="s s-Atom">return</span> <span class="nf">str</span><span class="p">(</span><span class="s s-Atom">s</span><span class="p">)</span>
</code></pre></div><h3>Result : 230ms Memory: 14mb</h3>
 # Multiply Strings

**Multiply Strings**는 두 개의 문자열을 입력으로 받아서, 두 문자열이 나타내는 숫자를 곱한 결과를 문자열 형태로 반환하는 함수이다.

## 문제 설명

예를 들어, 주어진 문자열이 "123"과 "456"인 경우, 두 숫자를 곱한 결과는 "56088"이 된다.

## 알고리즘 설명

주어진 문제에서는 문자열로 표시된 두 숫자를 곱한 결과를 문자열 형태로 반환해야한다. 이를 계산하기 위해서는 다음과 같은 알고리즘을 사용할 수 있다.

1. 입력으로 주어진 두 문자열을 뒤집는다.
2. 입력으로 주어진 문자열 중 길이가 짧은 문자열을 기준으로 숫자를 하나씩 가져와서, 긴 문자열과 곱한다.
3. 곱셈 결과를 answer라는 변수에 더해준다. answer는 초기값으로 0을 가진다.
4. 마지막으로, answer에 저장된 값을 다시 뒤집어서 리턴한다.

이 알고리즘은 두 문자열의 길이가 최대 10^4인 경우에도 작동할 수 있으며, 시간복잡도는 O(nm)이 된다. (n은 문자열1의 길이, m은 문자열2의 길이)

## 예시 코드

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        m, n = len(num1), len(num2)
        ans = [0] * (m + n)
        for i in range(m):
            for j in range(n):
                ans[i+j] += int(num1[i]) * int(num2[j])
                
        carry = 0
        for i in range(m+n):
            temp = ans[i] + carry
            ans[i] = temp % 10
            carry = temp // 10
        
        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()
        
        return ''.join(map(str, ans[::-1]))
```

위 코드는 Python으로 작성된 Multiply Strings의 예시 코드이다. 코드의 전반적인 부분에서는 위에서 설명한 알고리즘과 유사한 방법이 사용되고 있다. 단, 디테일한 부분은 코드를 보면서 이해를 하도록 하자.