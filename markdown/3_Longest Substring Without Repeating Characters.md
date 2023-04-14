<h2>LeetCode-<a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/">3</a></h2>
<h5>Longest Substring Without Repeating Characters : Given a string s, find the length of the longest substring without repeating characters.</h5>
<h5>note : s consists of English letters, digits, symbols and spaces.</h5><h3>Answer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">lengthOfLongestSubstring</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">s</span><span class="p">:</span><span class="w"> </span><span class="nf">str</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="nc">int</span><span class="err">:</span><span class="w"></span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">s</span><span class="p">)</span><span class="o">==</span><span class="mi">1</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">return</span><span class="w"> </span><span class="mi">1</span><span class="w"></span>
<span class="w">        </span><span class="nf">left</span><span class="p">,</span><span class="w"> </span><span class="nf">right</span><span class="p">,</span><span class="w"> </span><span class="n">answer_max</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="w"></span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="n">_</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="nf">len</span><span class="p">(</span><span class="n">s</span><span class="p">))</span><span class="err">:</span><span class="w">    </span>
<span class="w">            </span><span class="k">while</span><span class="w"> </span><span class="p">(</span><span class="nf">left</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="nf">right</span><span class="p">)</span><span class="w"> </span><span class="ow">and</span><span class="w"> </span><span class="p">(</span><span class="nf">right</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">s</span><span class="p">))</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="k">if</span><span class="w"> </span><span class="n">s</span><span class="o">[</span><span class="n">right</span><span class="o">]</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">s</span><span class="o">[</span><span class="n">left:right</span><span class="o">]</span><span class="err">:</span><span class="w"></span>
<span class="w">                    </span><span class="n">answer</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nf">right</span><span class="w"> </span><span class="o">-</span><span class="w"> </span><span class="nf">left</span><span class="w"> </span>
<span class="w">                    </span><span class="nf">left</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="mi">1</span><span class="w"> </span>
<span class="w">                    </span><span class="nf">right</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nf">left</span><span class="o">+</span><span class="mi">1</span><span class="w"></span>
<span class="w">                    </span><span class="k">break</span><span class="w"></span>
<span class="w">                </span><span class="k">else</span><span class="err">:</span><span class="w"></span>
<span class="w">                    </span><span class="nf">right</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="mi">1</span><span class="w"></span>
<span class="w">                </span><span class="k">if</span><span class="w"> </span><span class="nf">right</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">s</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">                    </span><span class="n">answer</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nf">right</span><span class="o">-</span><span class="nf">left</span><span class="w"></span>
<span class="w">                    </span><span class="k">break</span><span class="w"> </span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="n">answer_max</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="nl">answer</span><span class="p">:</span><span class="w"></span>
<span class="w">                </span><span class="n">answer_max</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">answer</span><span class="w"></span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="n">answer_max</span><span class="w"></span>
</code></pre></div><h5>Result : 878ms Memory: 14mb</h5>## Longest Substring Without Repeating Characters

Longest Substring Without Repeating Characters는 중복되지 않는 문자열의 최대 길이를 찾는 알고리즘이다.

### 알고리즘 설명

이 알고리즘은 sliding window 알고리즘을 사용하여 구현할 수 있다. 첫번째 인덱스와 마지막 인덱스를 가리키는 두 개의 포인터(또는 인덱스)를 사용하여 중복이 없는 부분 문자열을 찾을 수 있다.

두 개의 포인터를 사용하여 문자열을 탐색하면서 새로운 문자를 발견했을 때는 해당 문자의 인덱스를 기억하고, 중복되는 문자를 발견했을 때는 첫 번째 포인터를 중복된 문자 다음 인덱스로 옮긴다. 이제 두 번째 포인터와 첫 번째 포인터 사이의 문자열이 중복되지 않는 가장 긴 부분 문자열이다.

### 시간 복잡도

이 알고리즘의 시간 복잡도는 O(n)이다. 포인터를 이동시키면서 문자열을 한 번만 탐색하기 때문에 탐색 시간은 문자열의 길이와 비례한다.

### 예시

```
입력: "abcabcbb"
출력: 3 (abc)

입력: "bbbbb"
출력: 1 (b)

입력: "pwwkew"
출력: 3 (wke)
```