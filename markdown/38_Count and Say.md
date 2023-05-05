<h2>LeetCode-<a href="https://leetcode.com/problems/count-and-say/description/">38</a></h2>
<h5>Count and Say : The count-and-say sequence is a sequence of digit strings defined by the recursive formula:</h5>
<h5>note : To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.</h5><h3>Answer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">countAndSay</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">n</span><span class="p">:</span><span class="w"> </span><span class="nc">int</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="nf">str</span><span class="err">:</span><span class="w"></span>
<span class="w">        </span><span class="err">#</span><span class="w"> </span><span class="n">countAndSay</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="ss">&quot;1&quot;</span><span class="w"></span>
<span class="w">        </span><span class="err">#</span><span class="w"> </span><span class="n">countAndSay</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">say</span><span class="w"> </span><span class="ss">&quot;1&quot;</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">one</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="ss">&quot;11&quot;</span><span class="w"></span>
<span class="w">        </span><span class="err">#</span><span class="w"> </span><span class="n">countAndSay</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">say</span><span class="w"> </span><span class="ss">&quot;11&quot;</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">two</span><span class="w"> </span><span class="mi">1</span><span class="s1">&#39;s = &quot;21&quot;</span>
<span class="s1">        # countAndSay(4) = say &quot;21&quot; = one 2 + one 1 = &quot;12&quot; + &quot;11&quot; = &quot;1211&quot;</span>
<span class="s1">        if n==1:</span>
<span class="s1">            return &#39;</span><span class="mi">1</span><span class="s1">&#39;</span>
<span class="s1">        curr = 1</span>
<span class="s1">        num=&#39;</span><span class="mi">1</span><span class="s1">&#39;</span>
<span class="s1">        result = &#39;&#39;</span>
<span class="s1">        while curr&lt;n:</span>
<span class="s1">            left, right = 0, 1</span>
<span class="s1">                                        whi                                        s = num[left]</span>
<span class="s1">                count=1</span>
<span class="s1">                while right &lt; len(num):</span>
<span class="s1">                    if s == num[right]:</span>
<span class="s1">                        count+=1</span>
<span class="s1">                        right+=1</span>
<span class="s1">                    else:</span>
<span class="s1">                        break</span>
<span class="s1">                answer += f&#39;</span><span class="err">{</span><span class="nf">count</span><span class="err">}{</span><span class="n">s</span><span class="err">}&#39;</span><span class="w"></span>
<span class="w">                </span><span class="nf">left</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nf">right</span><span class="w"></span>
<span class="w">                </span><span class="nf">right</span><span class="o">+=</span><span class="mi">1</span><span class="w"> </span>
<span class="w">            </span><span class="n">num</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">answer</span><span class="w"></span>
<span class="w">            </span><span class="n">curr</span><span class="o">+=</span><span class="mi">1</span><span class="w"></span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="n">answer</span><span class="w"></span>
</code></pre></div><h3>Result : 64ms Memory: 16.4mb</h3>
 ## 문제 설명

Count and Say 문제는 주어진 숫자 n에 대하여 n번째 문맥을 리턴하는 문제입니다. 이 때, 숫자 n은 1부터 시작합니다. 문맥의 구성은 앞자리에 숫자의 갯수, 그 뒤에 해당 숫자를 이어붙인 문자열입니다.

예를 들어, n=1일 때 문맥은 "1"입니다. n=2일 때, countAndSay(1)에서 리턴된 "1"의 문맥이므로 "11"이 리턴됩니다. n=3일 때, countAndSay(2)에서 리턴된 "11"의 문맥이므로 "21"이 리턴됩니다. 이런 식으로 문맥을 구하는 것입니다.

## 해결 방법

해당 문제에서는 현재까지 진행한 문맥과 n에 해당하는 수를 비교하여 문맥을 구하면 됩니다. 우선 n=1일 경우에는 "1"을 리턴합니다. 그 다음부터는 현재까지 구한 문맥과 n값을 비교하여 새로운 문맥을 구합니다.

예를 들어, n=2일 경우에는 countAndSay(1)에서 리턴된 "1"에 대해서 문맥을 구합니다. 여기서는 1이 한 번 나오므로 "11"이 리턴됩니다. 마찬가지로 n=3일 경우에는 countAndSay(2)에서 리턴된 "11"에 대해서 문맥을 구합니다. 이 경우에는 1이 두 번 연속으로 나오므로 "21"이 리턴됩니다.

이처럼, 현재까지 구한 문맥에서 연속해서 나오는 숫자들을 그 수의 갯수와 같이 이어붙인 문자열을 구하면 됩니다.

## 코드 평가

해당 코드는 제대로 작성되어 있습니다. n값이 1일 경우에는 "1"을, 그렇지 않은 경우에는 현재까지 구한 문맥에서 연속해서 나오는 숫자들의 갯수와 해당 숫자를 이어붙인 문자열을 구하고, n값에 도달할 때까지 반복합니다.

하지만, 코드의 가독성을 높이기 위해 변수 이름을 좀 더 명확하게 지정하는 것이 좋습니다. 예를 들어, 변수명 num에 해당하는 변수는 현재까지 구한 문맥을 의미하므로, context나 current_context와 같은 이름으로 바꿔주면 더 명확해집니다.

또한, while문의 조건식에서 쓰인 left, right와 같은 변수들은 while문 안에서만 쓰이는 지역 변수이므로, 반복문을 시작하기 전에 미리 선언해주는 것이 좋습니다. 이러한 습관을 들이는 것이 좋습니다.

따라서, 코드의 수정된 버전은 다음과 같습니다.

``` python
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        curr = 1
        current_context = '1'
        result = ''
        
        while curr < n:
            left = right = 0
            answer = ''
            
            while right < len(current_context):
                s = current_context[left]
                count = 0
                
                while right < len(current_context) and current_context[right] == s:
                    count += 1
                    right += 1
                    
                answer += f'{count}{s}'
                left = right
            
            current_context = answer
            curr += 1
        
        return answer
```

이렇게 코드를 수정하면 가독성이 좋아져 더욱 보기 쉬워집니다.