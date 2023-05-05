<h2>LeetCode-<a href="https://leetcode.com/problems/longest-common-prefix/description/">14</a></h2>
<h5>Longest Common Prefix : Write a function to find the longest common prefix string amongst an array of strings.</h5>
<h5>note : If there is no common prefix, return an empty string "".</h5><h3>Answer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">longestCommonPrefix</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">strs</span><span class="p">:</span><span class="w"> </span><span class="n">List</span><span class="o">[</span><span class="n">str</span><span class="o">]</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="nf">str</span><span class="err">:</span><span class="w"></span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">strs</span><span class="p">)</span><span class="o">==</span><span class="mi">1</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">return</span><span class="w"> </span><span class="n">strs</span><span class="o">[</span><span class="n">0</span><span class="o">]</span><span class="w"></span>
<span class="w">        </span><span class="n">answer</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s1">&#39;&#39;</span><span class="w"></span>
<span class="w">        </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="w"></span>
<span class="w">        </span><span class="n">min_p</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nf">min</span><span class="p">(</span><span class="o">[</span><span class="n">len(s) for s in strs</span><span class="o">]</span><span class="p">)</span><span class="w"></span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="n">min_p</span><span class="o">==</span><span class="mi">0</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">return</span><span class="w"> </span><span class="ss">&quot;&quot;</span><span class="w"></span>
<span class="w">        </span><span class="k">while</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="nl">min_p</span><span class="p">:</span><span class="w"></span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="k">set</span><span class="p">(</span><span class="o">[</span><span class="n">s[i</span><span class="o">]</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">s</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">strs</span><span class="err">]</span><span class="p">))</span><span class="o">==</span><span class="mi">1</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="n">answer</span><span class="o">+=</span><span class="n">strs</span><span class="o">[</span><span class="n">0</span><span class="o">][</span><span class="n">i</span><span class="o">]</span><span class="w"></span>
<span class="w">            </span><span class="k">else</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="k">break</span><span class="w"></span>
<span class="w">            </span><span class="n">i</span><span class="o">+=</span><span class="mi">1</span><span class="w"></span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="n">answer</span><span class="w"></span>
</code></pre></div><h3>Result : 24ms Memory: 14mb</h3><h3>Answer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">longestCommonPrefix</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">strs</span><span class="p">:</span><span class="w"> </span><span class="n">List</span><span class="o">[</span><span class="n">str</span><span class="o">]</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="nf">str</span><span class="err">:</span><span class="w"></span>
<span class="w">        </span><span class="n">minimum</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">strs</span><span class="o">[</span><span class="n">0</span><span class="o">]</span><span class="p">)</span><span class="w"></span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="nf">len</span><span class="p">(</span><span class="n">strs</span><span class="p">))</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="nf">len</span><span class="p">(</span><span class="n">strs</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="n">minimum</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="n">minimum</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">strs</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="p">)</span><span class="w"></span>
<span class="w">        </span><span class="k">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s1">&#39;&#39;</span><span class="w"></span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="n">minimum</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">current</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">strs</span><span class="o">[</span><span class="n">0</span><span class="o">][</span><span class="n">i</span><span class="o">]</span><span class="w"></span>
<span class="w">            </span><span class="k">for</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="nf">len</span><span class="p">(</span><span class="n">strs</span><span class="p">))</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">strs</span><span class="o">[</span><span class="n">j</span><span class="o">][</span><span class="n">i</span><span class="o">]</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="k">current</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">                    </span><span class="k">return</span><span class="w"> </span><span class="k">result</span><span class="w"></span>
<span class="w">            </span><span class="k">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">result</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="k">current</span><span class="w"></span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="k">result</span><span class="w"></span>
</code></pre></div><h3>Result : 24ms Memory: 14mb</h3>
 # Longest Common Prefix 

`Longest Common Prefix`는 문자열 배열에서 모든 문자열에 공통으로 있는 가장 긴 접두사를 찾는 알고리즘입니다.

예를 들어, 다음과 같은 문자열 배열이 있다고 가정해봅시다.
```
["flower", "flow", "flight"]
```
위 배열에서 모든 문자열에 공통으로 있는 가장 긴 접두사는 "fl" 입니다. 따라서, Longest Common Prefix는 "fl"입니다.

이 알고리즘의 구현 방법으로는 `순차 비교`나 `정렬 후 비교`가 있습니다.

## 순차 비교

`순차 비교`방식은 가장 단순한 방법 중 하나입니다. 문자열 배열의 첫번째 문자열을 기준으로 하나의 문자씩 다른 문자열들과 비교하면서 공통된 접두사를 찾아 나갑니다.

- 순차 비교 알고리즘 예시

```
function longestCommonPrefix(strs) {
    if (!strs || !strs.length) {
        return "";
    }
    let prefix = strs[0];
    for (let i = 1; i < strs.length; i++) {
        while (strs[i].indexOf(prefix) !== 0) {
            prefix = prefix.substring(0, prefix.length - 1);
        }
        if (!prefix) {
            return "";
        }
    }
    return prefix;
}
```

## 정렬 후 비교

`정렬 후 비교`방식은 문자열 배열을 정렬한 후 가장 첫번째 문자열과 마지막 문자열을 비교하는 방식입니다.

- 정렬 후 비교 알고리즘 예시

```
function longestCommonPrefix(strs) {
    if (!strs || !strs.length) {
        return "";
    }
    strs.sort();
    let prefix = strs[0];
    let last = strs[strs.length - 1];
    for (let i = 0; i < prefix.length; i++) {
        if (prefix[i] !== last[i]) {
            prefix = prefix.substring(0, i);
        }
    }
    return prefix;
}
```

이 알고리즘의 시간 복잡도는 `O(n*m)`으로, `n`은 문자열 배열의 길이, `m`은 가장 짧은 문자열의 길이입니다.