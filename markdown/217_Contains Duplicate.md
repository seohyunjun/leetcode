<h2>LeetCode-<a href="https://leetcode.com/problems/contains-duplicate/">217</a></h2>
<h5>Contains Duplicate : Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.</h5>
<h5>note : 1 &lt;= nums.length &lt;= 105</h5><h3>Answer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">containsDuplicate</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">nums</span><span class="p">:</span><span class="w"> </span><span class="n">List</span><span class="o">[</span><span class="n">int</span><span class="o">]</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="nl">bool</span><span class="p">:</span><span class="w"></span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">nums</span><span class="p">)</span><span class="o">==</span><span class="mi">1</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">return</span><span class="w"> </span><span class="k">False</span><span class="w"></span>
<span class="w">        </span><span class="n">nums</span><span class="p">.</span><span class="n">sort</span><span class="p">()</span><span class="w"></span>
<span class="w">        </span><span class="nf">left</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="w"></span>
<span class="w">        </span><span class="k">while</span><span class="w"> </span><span class="nf">left</span><span class="o">+</span><span class="mi">1</span><span class="w"> </span><span class="o">&lt;=</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">nums</span><span class="p">)</span><span class="o">-</span><span class="mi">1</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="n">nums</span><span class="o">[</span><span class="n">left</span><span class="o">]==</span><span class="n">nums</span><span class="o">[</span><span class="n">left+1</span><span class="o">]</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="k">return</span><span class="w"> </span><span class="k">True</span><span class="w"></span>
<span class="w">            </span><span class="nf">left</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="mi">1</span><span class="w"></span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="k">False</span><span class="w"></span>
</code></pre></div><h3>Result : 634ms Memory: 27.9mb</h3>
 ### 문제 설명

"Contains Duplicate" 문제는 정수 배열이 주어졌을 때, 중복된 값이 있는지 여부를 확인하는 문제입니다.

### 해결 방법

해당 문제를 해결하기 위해서는 우선 배열을 정렬해야 합니다. 그 이유는 중복된 값은 배열 내에서 인접한 위치에 있기 때문입니다. 그리고 정렬된 배열에서 인접한 두 값이 같은지 비교하면 중복된 값이 있는지를 쉽게 판별할 수 있습니다.

따라서, 정렬된 배열을 왼쪽부터 오른쪽으로 탐색하며 인접한 두 값이 같은 경우에는 중복된 값이 있는 것으로 판단하여 `True`를 반환하고, 배열 내에 중복된 값이 없을 경우에는 `False`를 반환합니다. 또한, 배열의 길이가 1인 경우에는 중복된 값이 없으므로 `False`를 반환합니다.

### 사용자 코드 분석

사용자 코드는 주어진 문제를 정확하게 해결하는 코드입니다. 먼저, 주어진 배열의 길이가 1인 경우에는 중복된 값이 없으므로 `False`를 반환합니다. 그리고 배열을 정렬한 후, 배열의 가장 왼쪽 위치에서부터 인접한 두 값이 같은지를 확인하여 중복된 값이 있을 경우 `True`를 반환하고, 중복된 값이 없는 경우에는 `False`를 반환합니다.

이 코드의 시간 복잡도는 `O(nlogn)`으로, 배열을 정렬하는 시간이 가장 큰 영향을 미치며, 배열을 한 번 탐색하는 시간은 `O(n)`입니다.

### 평가

이 코드는 주어진 문제를 효율적으로 해결하는 코드입니다. 정렬된 배열에서 인접한 두 값이 같은지를 확인하여 중복된 값을 판별하기 때문에, 중복된 값이 인접한 위치에 있어도 놓치지 않습니다. 따라서, 이 코드는 문제에 대한 정확한 이해와 효율적인 알고리즘을 적용한 결과물이라고 평가할 수 있습니다.