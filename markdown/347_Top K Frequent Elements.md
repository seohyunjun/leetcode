<h2>LeetCode-<a href="https://leetcode.com/problems/top-k-frequent-elements/description/">347</a></h2>
<h5>Top K Frequent Elements : Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.</h5>
<h5>note : time complexity must be better than O(n log n), where n is the array s size.</h5><h3>Over *</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">topKFrequent</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">nums</span><span class="p">:</span><span class="w"> </span><span class="n">List</span><span class="o">[</span><span class="n">int</span><span class="o">]</span><span class="p">,</span><span class="w"> </span><span class="nl">k</span><span class="p">:</span><span class="w"> </span><span class="nc">int</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">List</span><span class="o">[</span><span class="n">int</span><span class="o">]</span><span class="err">:</span><span class="w"></span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="k">set</span><span class="p">(</span><span class="n">nums</span><span class="p">))</span><span class="o">==</span><span class="mi">1</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">return</span><span class="w"> </span><span class="o">[</span><span class="n">nums[0</span><span class="o">]</span><span class="err">]</span><span class="w"></span>
<span class="w">        </span><span class="n">answer</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="err">[]</span><span class="w"></span>
<span class="w">        </span><span class="nf">count</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">collections</span><span class="p">.</span><span class="n">Counter</span><span class="p">(</span><span class="n">nums</span><span class="p">).</span><span class="n">most_common</span><span class="p">(</span><span class="n">n</span><span class="o">=</span><span class="n">k</span><span class="p">)</span><span class="w"></span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="o">[</span><span class="n">i[0</span><span class="o">]</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="nf">count</span><span class="err">]</span><span class="w"></span>
</code></pre></div><h3>Result : 111ms Memory: 21mb</h3>
 # Top K Frequent Elements

Top K Frequent Elements는 정수 배열에서 가장 빈번하게 등장하는 상위 K개의 원소를 찾는 알고리즘입니다.

예를 들어, [1,1,1,2,2,3]에서 상위 2개의 원소를 찾는다면, 1과 2가 선택됩니다. 1은 3번, 2는 2번 등장하였기 때문입니다.

이 알고리즘은 hash table과 heap을 이용하여 구현할 수 있습니다.

1. hash table
- 정수 배열을 순회하며 원소의 등장 횟수를 저장하는 hash table을 생성합니다.
- 접근 횟수가 많은 상위 K개의 원소를 저장할 결과 배열을 생성합니다.
- hash table에서 가장 등장한 횟수가 큰 원소부터 K개 까지만 결과 배열에 저장합니다.

2. heap
- 정수 배열을 순회하며 원소의 등장 횟수를 저장하는 hash table을 생성합니다.
- hash table을 바탕으로 heap을 생성합니다. heap에는 원소의 등장 횟수를 저장합니다.
- heap에서 상위 K개의 원소를 pop하여 결과 배열에 저장합니다.

이 알고리즘의 시간복잡도는 정수 배열을 순회하는 O(n)과 hash table 또는 heap을 사용하여 원소를 추출하는 O(K log K)입니다. 따라서 전체 시간복잡도는 O(n + K log K)입니다.

위 알고리즘은 빅데이터 분석에서 비즈니스적인 인사이트를 도출하는 등 매우 중요한 역할을 합니다.

``` python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hash table to store the frequency of each element
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Sort the hash table by frequency in descending order
        freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
        
        # Select the k elements with the highest frequency
        result = []
        i = 0
        for num, count in freq.items():
            result.append(num)
            i += 1
            if i == k:
                break
        
        return result

```