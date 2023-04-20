<h2>LeetCode-<a href="leetchttps://leetcode.com/problems/string-to-integer-atoi/description/ode">8</a></h2>
<h5>String to Integer (atoi) : Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).</h5>
<h5>note : integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.</h5><h3>Answer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">myAtoi</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">s</span><span class="p">:</span><span class="w"> </span><span class="nf">str</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="nc">int</span><span class="err">:</span><span class="w"></span>
<span class="w">        </span><span class="nf">left</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="w"> </span>
<span class="w">        </span><span class="n">k</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s1">&#39;&#39;</span><span class="w"></span>
<span class="w">        </span><span class="n">p</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s1">&#39;&#39;</span><span class="w"></span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="n">l</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">s</span><span class="p">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39; &#39;</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="n">l</span><span class="o">==</span><span class="s1">&#39;&#39;</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="k">continue</span><span class="w"></span>
<span class="w">            </span><span class="n">elif</span><span class="w"> </span><span class="n">l</span><span class="p">.</span><span class="n">isalpha</span><span class="p">()</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="k">break</span><span class="w"></span>
<span class="w">            </span><span class="nf">left</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="w"></span>
<span class="w">            </span><span class="k">while</span><span class="w"> </span><span class="nf">left</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">l</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="k">if</span><span class="w"> </span><span class="n">l</span><span class="o">[</span><span class="n">left</span><span class="o">]</span><span class="p">.</span><span class="n">isdigit</span><span class="p">()</span><span class="err">:</span><span class="w"></span>
<span class="w">                    </span><span class="n">k</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">l</span><span class="o">[</span><span class="n">left</span><span class="o">]</span><span class="w"></span>
<span class="w">                </span><span class="n">elif</span><span class="w"> </span><span class="p">(</span><span class="n">l</span><span class="o">[</span><span class="n">left</span><span class="o">]</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="o">[</span><span class="n">&#39;+&#39;,&#39;-&#39;</span><span class="o">]</span><span class="p">)</span><span class="w"> </span><span class="ow">and</span><span class="w"> </span><span class="p">(</span><span class="nf">left</span><span class="o">==</span><span class="mi">0</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">                    </span><span class="n">p</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">l</span><span class="o">[</span><span class="n">left</span><span class="o">]</span><span class="w"></span>
<span class="w">                </span><span class="k">else</span><span class="err">:</span><span class="w"></span>
<span class="w">                    </span><span class="k">break</span><span class="w"></span>
<span class="w">                </span><span class="nf">left</span><span class="o">+=</span><span class="mi">1</span><span class="w"></span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="n">k</span><span class="o">+</span><span class="n">p</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="s1">&#39;&#39;</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="k">break</span><span class="w"></span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="n">k</span><span class="o">==</span><span class="s1">&#39;&#39;</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="w"></span>
<span class="w">        </span><span class="n">k</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nc">int</span><span class="p">(</span><span class="n">p</span><span class="o">+</span><span class="n">k</span><span class="p">)</span><span class="w">    </span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="n">k</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="mi">2</span><span class="o">**</span><span class="mi">31</span><span class="o">-</span><span class="mi">1</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">return</span><span class="w"> </span><span class="mi">2</span><span class="o">**</span><span class="mi">31</span><span class="o">-</span><span class="mi">1</span><span class="w">    </span>
<span class="w">        </span><span class="n">elif</span><span class="w"> </span><span class="n">k</span><span class="w"> </span><span class="o">&lt;=</span><span class="w"> </span><span class="o">-</span><span class="mi">2</span><span class="o">**</span><span class="mi">31</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">return</span><span class="w"> </span><span class="o">-</span><span class="mi">2</span><span class="o">**</span><span class="mi">31</span><span class="w"></span>
<span class="w">        </span><span class="k">else</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">return</span><span class="w"> </span><span class="n">k</span><span class="w"></span>
</code></pre></div><h3>Result : 42ms Memory: 13.9mb</h3>
 # String to Integer (atoi)

"String to Integer (atoi)"는 문자열을 정수로 변환하는 함수입니다. 이때 함수는 매개변수로 받은 문자열의 맨 앞에 있는 공백을 무시하고, 그 다음부터 숫자가 나올 때까지만 변환합니다. 이후에는 숫자 이외의 값이 나오면 변환을 멈추고 그전까지 변환한 값을 반환합니다.

## 예시

다음은 "42"라는 문자열을 정수로 변환하는 예시입니다.

입력: "42"

출력: 42


## 구현

"String to Integer (atoi)" 함수를 구현할 때에는 다음과 같은 절차를 따릅니다.

1. 입력값으로 받은 문자열 s의 맨 앞에 있는 공백을 제거합니다.
2. 입력값으로 받은 문자열 s가 양수, 음수인지 확인합니다. 이후에 변환할 숫자가 나오기 전까지 문자열 s의 맨 앞에 있는 부호를 체크합니다.
3. 변환이 가능한 숫자까지 문자열 s를 탐색합니다. 이때 변환할 숫자가 맨앞에서나오는 경우에는 부호가 존재하지 않기 때문에 2번에서 체크한 부호를 사용합니다.
4. 변환된 숫자에 부호를 곱하여 최종값을 반환합니다. 

## 주의점

"String to Integer (atoi)" 함수를 구현할 때 다음과 같은 주의점이 있습니다.

1. 입력값으로 받은 문자열 s가 빈 문자열인 경우나 숫자가 아닌 다른 문자열을 입력한 경우에는 0을 반환합니다.
2. 변환된 숫자가 int의 범위를 벗어나는 경우에도 예외를 처리해야 합니다. 

```java
class Solution {
    public int myAtoi(String s) {
        if(s == null || s.length() == 0) return 0;
        
        int idx = 0;
        int sign = 1;
        int result = 0;
        // 공백 제거
        while(idx < s.length() && s.charAt(idx) == ' ') idx++;
       
        // 부호 체크
        if(idx < s.length() && (s.charAt(idx) == '+' || s.charAt(idx) == '-')){
            sign = s.charAt(idx) == '+' ? 1 : -1;
            idx++;
        }
        
        // 변환 가능한 숫자까지 탐색
        while(idx < s.length() && Character.isDigit(s.charAt(idx))){
            int digit = s.charAt(idx) - '0';
            // int 범위 넘어가는지 체크
            if(result > Integer.MAX_VALUE/10 || (result == Integer.MAX_VALUE/10 && digit > 7) ){
                return sign == -1 ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            }
            result = result * 10 + digit;
            idx++;
        }
        
        return sign * result;
    }
}
```