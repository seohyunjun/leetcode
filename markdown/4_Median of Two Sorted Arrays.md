<h2>LeetCode-<a href="https://leetcode.com/problems/median-of-two-sorted-arrays/description/">4</a></h2>
<h5>Median of Two Sorted Arrays : Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.</h5>
<h5>note : The overall run time complexity should be O(log (m+n)).</h5><h3>Answer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">findMedianSortedArrays</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">nums1</span><span class="p">:</span><span class="w"> </span><span class="n">List</span><span class="o">[</span><span class="n">int</span><span class="o">]</span><span class="p">,</span><span class="w"> </span><span class="nl">nums2</span><span class="p">:</span><span class="w"> </span><span class="n">List</span><span class="o">[</span><span class="n">int</span><span class="o">]</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="nc">float</span><span class="err">:</span><span class="w"></span>
<span class="w">        </span><span class="n">p</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">nums1</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">nums2</span><span class="w"></span>
<span class="w">        </span><span class="n">p</span><span class="p">.</span><span class="n">sort</span><span class="p">()</span><span class="w"></span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">p</span><span class="p">)</span><span class="o">%</span><span class="mi">2</span><span class="o">!=</span><span class="mi">0</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="n">median</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">p</span><span class="o">[</span><span class="n">len(p)//2</span><span class="o">]</span><span class="w">    </span>
<span class="w">        </span><span class="k">else</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="n">median</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">(</span><span class="n">p</span><span class="o">[</span><span class="n">len(p)//2</span><span class="o">]+</span><span class="n">p</span><span class="o">[</span><span class="n">len(p)//2-1</span><span class="o">]</span><span class="p">)</span><span class="o">/</span><span class="mi">2</span><span class="w"></span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="n">median</span><span class="w"></span>
</code></pre></div><h5>Result : 93ms Memory: 14mb</h5># Median of Two Sorted Arrays
- 두 개의 정렬된 배열이 주어질 때, 두 배열의 중앙값을 찾는 문제입니다.
- 예를 들어, 배열 A = [1, 3, 5], 배열 B = [2, 4, 6] 이 주어지면, 중앙값은 (3+4)/2 = 3.5 가 됩니다.
- 두 배열의 크기는 같은 경우도 있지만, 다른 경우도 있으므로 코드로 구현할 때에는 이를 고려하여 작성해야 합니다.
- 이 문제는 이진 검색을 활용하여 풀 수 있습니다. 이진 검색이란 배열을 반으로 나누어 탐색하는 방법으로, 시간복잡도는 O(log(n+m)) 입니다.
- 이진 검색을 이용해 두 배열을 나누고, 각각의 중간값을 비교하여 조건에 따라 배열의 왼쪽 또는 오른쪽 부분만 탐색합니다.
- 마지막으로 중앙값을 찾아 반환합니다.