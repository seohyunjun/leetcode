<h2>LeetCode-<a href="https://leetcode.com/problems/valid-anagram/">242</a></h2>
<h5>Valid Anagram : info</h5>
<h5>note : sub</h5><h3>the two strings contain the same letters, but the order of the letters may be different.</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">:::</span><span class="n">python</span><span class="w"></span>

<span class="n">class</span><span class="w"> </span><span class="n">Solution</span><span class="o">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">isAnagram</span><span class="p">(</span><span class="kr">self</span><span class="p">,</span><span class="w"> </span><span class="n">s</span><span class="o">:</span><span class="w"> </span><span class="n">str</span><span class="p">,</span><span class="w"> </span><span class="n">t</span><span class="o">:</span><span class="w"> </span><span class="n">str</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">bool</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="nf">if</span><span class="w"> </span><span class="n">len</span><span class="p">(</span><span class="n">s</span><span class="p">)</span><span class="o">!=</span><span class="n">len</span><span class="p">(</span><span class="n">t</span><span class="p">)</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="kr">return</span><span class="w"> </span><span class="kr">False</span><span class="w"></span>
<span class="w">        </span><span class="n">for</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="kr">in</span><span class="w"> </span><span class="n">s</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="nf">if</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="kr">not</span><span class="w"> </span><span class="kr">in</span><span class="w"> </span><span class="n">t</span><span class="o">:</span><span class="w"></span>
<span class="w">                </span><span class="kr">return</span><span class="w"> </span><span class="kr">False</span><span class="w"></span>
<span class="w">            </span><span class="n">else</span><span class="o">:</span><span class="w"></span>
<span class="w">                </span><span class="n">t</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">t</span><span class="p">.</span><span class="n">replace</span><span class="p">(</span><span class="n">i</span><span class="p">,</span><span class="s">&#39;&#39;</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span><span class="w"></span>
<span class="w">        </span><span class="kr">return</span><span class="w"> </span><span class="kr">True</span><span class="w"></span>
</code></pre></div><h3>Result : 0ms Memory: 0mb</h3>
 ## 문제 이해
주어진 문자열 s와 t가 주어졌을 때, s의 문자를 재배열하여 t를 얻을 수 있는지 여부를 반환하는 문제입니다. 즉, s와 t는 알파벳의 종류와 개수가 동일해야 합니다.

## 문제 해결 방법
주어진 문자열에서 알파벳의 개수와 종류가 동일한지 비교해야 합니다. 이를 위해 두 문자열의 길이가 같은지 확인한 뒤, for 문을 이용해 s 문자열의 모든 문자에 대해 t에 포함되어 있는지 확인합니다. t에서 뽑은 문자를 하나씩 삭제하며 문자열이 동일한지 검사합니다.

## 사용자 코드 분석
주어진 코드에서는 s의 모든 문자에 대해 t에 포함되어 있는지 하나씩 확인합니다. t에서 삭제되는 과정에서 시간 복잡도가 O(n^2)이 나오므로, 문자열 길이가 길수록 실행 시간이 길어집니다. 

## 추천 코드
다음은 Counter 라이브러리를 이용한 추천 코드입니다. Counter 함수를 이용하면 두 문자열에서 알파벳의 종류와 개수를 세어 딕셔너리 형태로 반환합니다. 이후 두 딕셔너리를 비교해 두 문자열이 동일한지 파악할 수 있습니다.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return collections.Counter(s) == collections.Counter(t)
```

이 코드를 이용하면 문자열 길이가 길어져도 실행 시간이 느려지지 않습니다. 하지만 이 코드 또한 선형 시간이 소요되므로, 문자열 길이가 굉장히 길어질 경우 해시 테이블 구조를 이용해 문자열의 알파벳을 카운트하는 방법도 고려해 볼 수 있습니다.