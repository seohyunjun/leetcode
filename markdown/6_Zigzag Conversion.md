<h2>LeetCode-<a href="https://leetcode.com/problems/zigzag-conversion/description/">6</a></h2>
<h5>Zigzag Conversion : The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows</h5>
<h5>note : like this: (you may want to display this pattern in a fixed font for better legibility)</h5><h3>Answer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="nf">convert</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">s</span><span class="p">:</span><span class="w"> </span><span class="nf">str</span><span class="p">,</span><span class="w"> </span><span class="nl">numRows</span><span class="p">:</span><span class="w"> </span><span class="nc">int</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="nf">str</span><span class="err">:</span><span class="w"></span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="n">numRows</span><span class="o">==</span><span class="mi">1</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">return</span><span class="w"> </span><span class="n">s</span><span class="w"></span>
<span class="w">        </span><span class="n">answer</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s1">&#39;&#39;</span><span class="w"></span>
<span class="w">        </span><span class="k">interval</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">numRows</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="p">(</span><span class="n">numRows</span><span class="o">-</span><span class="mi">2</span><span class="p">)</span><span class="w"></span>
<span class="w">        </span><span class="n">ls</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">[</span><span class="n">[&#39;&#39;</span><span class="o">]</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">_</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="n">numRows</span><span class="p">)</span><span class="err">]</span><span class="w"> </span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="n">i</span><span class="p">,</span><span class="w"> </span><span class="n">l</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">enumerate</span><span class="p">(</span><span class="n">s</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="n">inter</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">i</span><span class="o">%</span><span class="k">interval</span><span class="w"></span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="n">inter</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="nl">numRows</span><span class="p">:</span><span class="w"></span>
<span class="w">                </span><span class="n">ls</span><span class="o">[</span><span class="n">inter</span><span class="o">]+=</span><span class="n">l</span><span class="w"></span>
<span class="w">            </span><span class="k">else</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="n">ls</span><span class="o">[</span><span class="n">interval-(inter)</span><span class="o">]+=</span><span class="n">l</span><span class="w"></span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="s1">&#39;&#39;</span><span class="p">.</span><span class="k">join</span><span class="p">(</span><span class="nf">sum</span><span class="p">(</span><span class="n">ls</span><span class="p">,</span><span class="err">[]</span><span class="p">))</span><span class="w"></span>
</code></pre></div><h3>Result : 97ms Memory: 14.2mb</h3>
 # Zigzag Conversion

Zigzag Conversion은 문자열을 지그재그 형태로 변환하는 알고리즘입니다.

## 문제 설명

주어진 문자열 `s`와 정수 `numRows`가 주어지면, `s`를 지그재그 형태로 변환합니다.

예를 들어, 다음과 같은 문자열과 `numRows`가 주어졌다고 가정해봅시다.

```
s = "PAYPALISHIRING"
numRows = 3
```

그러면 문자열 `s`는 다음과 같이 변환됩니다.

```
P   A   H   N
A P L S I I G
Y   I   R
```

즉, `numRows`개의 행으로 구성된 표에 문자열 `s`를 적절하게 배치하여 위와 같은 모양을 만듭니다.

## 해결 방법

Zigzag Conversion 문제를 해결하기 위해서는 다음과 같은 알고리즘을 사용할 수 있습니다.

1. `numRows`개의 빈 문자열 생성

2. 문자열 `s`를 처음부터 끝까지 순회하면서 다음과 같은 과정을 반복합니다.

    1. 현재 문자를 `row`번째 행에 추가합니다.
    
    2. `row`값이 0이거나 `numRows - 1`이면 방향을 전환합니다.
    
    3. 현재 방향에 따라 `row`값을 증가하거나 감소합니다.

3. 생성된 `numRows`개의 문자열을 순서대로 이어붙인 결과를 반환합니다.

예를 들어, 앞서 나온 예제를 위의 알고리즘으로 해결해보면 다음과 같습니다.

```
s = "PAYPALISHIRING"
numRows = 3

초기 상태:
["", "", ""]

s[0] = "P" 추가:
["P", "", ""]

s[1] = "A" 추가:
["P", "A", ""]

s[2] = "Y" 추가:
["P", "A", "Y"]

방향 전환:
["P", "A", "Y"]
["", "L", ""]

s[3] = "P" 추가:
["P", "A", "Y"]
["", "L", "P"]

s[4] = "A" 추가:
["P", "A", "Y"]
["", "L", "PA"]

s[5] = "L" 추가:
["P", "A", "Y"]
["", "L", "PAL"]

s[6] = "I" 추가:
["P", "A", "Y"]
["I", "L", "PAL"]

s[7] = "S" 추가:
["P", "A", "Y"]
["I", "LS", "PAL"]

s[8] = "H" 추가:
["P", "A", "Y"]
["I", "LSH", "PAL"]

s[9] = "I" 추가:
["P", "A", "Y"]
["IH", "LSH", "PAL"]

s[10] = "R" 추가:
["P", "A", "Y"]
["IH", "LSHR", "PAL"]

최종 결과: "PAHNAPLSIIGYIR"
```