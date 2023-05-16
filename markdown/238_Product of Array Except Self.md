<h2>LeetCode-<a href="leetcode">238</a></h2>
<h5>Product of Array Except Self : Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].</h5>
<h5>note : Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)</h5><h3>Answer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">productExceptSelf</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">nums</span><span class="p">:</span><span class="w"> </span><span class="n">List</span><span class="o">[</span><span class="n">int</span><span class="o">]</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">List</span><span class="o">[</span><span class="n">int</span><span class="o">]</span><span class="err">:</span><span class="w"></span>
<span class="w">        </span><span class="k">out</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="err">[]</span><span class="w"></span>
<span class="w">        </span><span class="n">p</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="w"></span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">nums</span><span class="p">))</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">out</span><span class="p">.</span><span class="n">append</span><span class="p">(</span><span class="n">p</span><span class="p">)</span><span class="w"></span>
<span class="w">            </span><span class="n">p</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">p</span><span class="o">*</span><span class="n">nums</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="w"></span>
<span class="w">        </span><span class="n">p</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="w"></span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="nf">len</span><span class="p">(</span><span class="n">nums</span><span class="p">)</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="o">-</span><span class="mi">1</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">out</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">out</span><span class="o">[</span><span class="n">i</span><span class="o">]*</span><span class="n">p</span><span class="w"></span>
<span class="w">            </span><span class="n">p</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">p</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="n">nums</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="w"></span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="k">out</span><span class="w"></span>
</code></pre></div><h3>Result : 221ms Memory: 21.2mb</h3>
 # Leetcode Problem "Product of Array Except Self" Solution

이 문제는 주어진 배열에서 자신을 제외한 모든 요소들의 곱을 계산하는 문제입니다. 추가적인 배열을 사용하지 않고 O(n) 시간복잡도 내에 풀어야 합니다.

우선, 모든 요소들의 곱을 구하기 위해서는 배열 전체의 곱을 계산한 뒤, 각 요소마다 전체 곱에서 자신의 값을 나눠줘야 합니다. 하지만 이 방법은 0이 하나라도 있는 경우 오류가 발생합니다.

따라서, 각 요소를 제외한 왼쪽 요소들의 곱과 오른쪽 요소들의 곱을 구해야 합니다. 이를 위해서는 두 개의 배열을 사용합니다. 첫 번째 배열은 각 요소의 왼쪽 요소들의 곱을, 두 번째 배열은 각 요소의 오른쪽 요소들의 곱을 저장합니다.

그리고 나서 각 요소의 왼쪽 요소들의 곱과 오른쪽 요소들의 곱을 곱하면, 자신을 제외한 모든 요소들의 곱이 됩니다.

이렇게 해서 추가적인 배열 없이 O(n) 시간복잡도 내에 문제를 풀 수 있습니다.

# User Python Code Evaluation

위 코드는 올바르게 구현되어 있습니다. 각 요소의 왼쪽 요소들의 곱을 구하는 반복문과 오른쪽 요소들의 곱을 구하는 반복문으로 구성되어 있고, 추가적인 배열을 사용하지 않고 O(n) 시간복잡도 내에 문제를 풀었습니다. 따라서, 이 코드는 정확성과 효율성 모두를 충족시키는 좋은 코드입니다.