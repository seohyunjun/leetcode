<h2>LeetCode-<a href="https://leetcode.com/problems/integer-to-roman/description/">12</a></h2>
<h5>Integer to Roman : Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.</h5>
<h5>note : Given an integer, convert it to a roman numeral.</h5><h3>Answer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">intToRoman</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">num</span><span class="p">:</span><span class="w"> </span><span class="nc">int</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="nf">str</span><span class="err">:</span><span class="w"></span>
<span class="w">        </span><span class="n">roman_dict</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="err">{</span><span class="w"></span>
<span class="w">            </span><span class="mi">0</span><span class="w"> </span><span class="err">:</span><span class="w"> </span><span class="ss">&quot;V&quot;</span><span class="w"> </span>
<span class="w">            </span><span class="p">,</span><span class="mi">1</span><span class="w"> </span><span class="err">:</span><span class="w"> </span><span class="ss">&quot;L&quot;</span><span class="w"> </span>
<span class="w">            </span><span class="p">,</span><span class="mi">2</span><span class="w"> </span><span class="err">:</span><span class="w"> </span><span class="ss">&quot;D&quot;</span><span class="w"> </span>
<span class="w">            </span><span class="err">}</span><span class="w"></span>
<span class="w">        </span><span class="n">d_dict</span><span class="o">=</span><span class="w"> </span><span class="err">{</span><span class="w"></span>
<span class="w">            </span><span class="mi">0</span><span class="w"> </span><span class="err">:</span><span class="w"> </span><span class="ss">&quot;I&quot;</span><span class="w"> </span>
<span class="w">            </span><span class="p">,</span><span class="mi">1</span><span class="w"> </span><span class="err">:</span><span class="w"> </span><span class="ss">&quot;X&quot;</span><span class="w"></span>
<span class="w">            </span><span class="p">,</span><span class="mi">2</span><span class="w"> </span><span class="err">:</span><span class="w"> </span><span class="ss">&quot;C&quot;</span><span class="w"></span>
<span class="w">            </span><span class="p">,</span><span class="mi">3</span><span class="w"> </span><span class="err">:</span><span class="w"> </span><span class="ss">&quot;M&quot;</span><span class="w"></span>
<span class="w">        </span><span class="err">}</span><span class="w"></span>
<span class="w">        </span><span class="n">answer</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s1">&#39;&#39;</span><span class="w"></span>
<span class="w">        </span><span class="n">set_num</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">3</span><span class="w"></span>
<span class="w">        </span><span class="k">while</span><span class="w"> </span><span class="n">set_num</span><span class="w"> </span><span class="o">&gt;=</span><span class="w"> </span><span class="mi">0</span><span class="err">:</span><span class="w">    </span>
<span class="w">            </span><span class="n">remain</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">num</span><span class="w"> </span><span class="o">//</span><span class="w"> </span><span class="mi">10</span><span class="o">**</span><span class="n">set_num</span><span class="w"></span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="n">remain</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mi">4</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="n">answer</span><span class="o">+=</span><span class="w"> </span><span class="n">d_dict</span><span class="o">[</span><span class="n">set_num</span><span class="o">]</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">remain</span><span class="w"></span>
<span class="w">            </span><span class="n">elif</span><span class="w"> </span><span class="n">remain</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">4</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="n">answer</span><span class="o">+=</span><span class="w"> </span><span class="n">d_dict</span><span class="o">[</span><span class="n">set_num</span><span class="o">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">roman_dict</span><span class="o">[</span><span class="n">set_num</span><span class="o">]</span><span class="w"></span>
<span class="w">            </span><span class="n">elif</span><span class="w"> </span><span class="n">remain</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">9</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="n">answer</span><span class="o">+=</span><span class="w"> </span><span class="n">d_dict</span><span class="o">[</span><span class="n">set_num</span><span class="o">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">d_dict</span><span class="o">[</span><span class="n">set_num+1</span><span class="o">]</span><span class="w"> </span>
<span class="w">            </span><span class="n">elif</span><span class="w"> </span><span class="n">remain</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="n">pass</span><span class="w"></span>
<span class="w">            </span><span class="k">else</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="n">answer</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="n">roman_dict</span><span class="o">[</span><span class="n">set_num</span><span class="o">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">d_dict</span><span class="o">[</span><span class="n">set_num</span><span class="o">]*</span><span class="p">(</span><span class="n">remain</span><span class="o">-</span><span class="mi">5</span><span class="p">)</span><span class="w"></span>
<span class="w">            </span><span class="n">num</span><span class="w"> </span><span class="o">%=</span><span class="w"> </span><span class="mi">10</span><span class="o">**</span><span class="n">set_num</span><span class="w"></span>
<span class="w">            </span><span class="n">set_num</span><span class="w"> </span><span class="o">-=</span><span class="w"> </span><span class="mi">1</span><span class="w"></span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="n">answer</span><span class="w"></span>
</code></pre></div><h3>Result : 48ms Memory: 13.9mb</h3>
 ## Integer to Roman이란?
Integer to Roman이란, 정수를 로마 숫자로 변환하는 알고리즘입니다. 로마 숫자는 기원전 1세기에 로마 제국에서 사용되었던 기호 체계이며, I, V, X, L, C, D, M의 숫자를 사용합니다.

## 알고리즘 설명
Integer to Roman 알고리즘은 일반적으로 다음과 같이 진행됩니다.

1. 로마 숫자와 정수 간의 대응 관계를 나타내는 딕셔너리를 선언합니다.
2. 입력된 정수를 가장 큰 로마 숫자부터 나누어 몫을 구하고, 로마 숫자에 해당하는 기호를 문자열에 추가합니다.
3. 나머지로 남은 정수로 다시 1~2번 과정을 반복합니다.
4. 최종적으로 만들어진 로마 숫자 문자열을 반환합니다.

예를 들어, 입력된 정수가 1994일 경우 다음과 같은 과정을 거칩니다.

1. 로마 숫자 딕셔너리: {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
2. 1994를 1000으로 나눈 몫은 1, 로마 숫자는 "M"가 됩니다. 문자열에 "M"을 추가합니다.
3. 나머지는 994입니다. 994를 900으로 나눈 몫은 1, 로마 숫자는 "CM"이 됩니다. 문자열에 "CM"을 추가합니다.
4. 나머지는 94입니다. 94를 50으로 나눈 몫은 1, 로마 숫자는 "L"이 됩니다. 문자열에 "L"을 추가합니다.
5. 나머지는 44입니다. 44를 40으로 나눈 몫은 1, 로마 숫자는 "XL"이 됩니다. 문자열에 "XL"을 추가합니다.
6. 나머지는 4입니다. 4를 4로 나눈 몫은 1, 로마 숫자는 "IV"가 됩니다. 문자열에 "IV"를 추가합니다.
7. 최종 로마 숫자 문자열은 "MCMXLIV"입니다.

## 예제 코드(파이썬)
```python
def int_to_roman(num):
    roman_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    roman = ''
    for key in roman_dict:
        roman += key * (num // roman_dict[key])
        num %= roman_dict[key]
    return roman
```
이 코드는 입력된 정수를 로마 숫자로 변환하여 반환합니다. 딕셔너리를 활용하여 로마 숫자와 정수 간의 대응 관계를 설정하고, 반복문을 통해 각 로마 숫자를 순차적으로 처리합니다. 최종 로마 숫자 문자열을 반환합니다.