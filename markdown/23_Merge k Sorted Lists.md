<h2>LeetCode-<a href="https://leetcode.com/problems/merge-k-sorted-lists/description/">23</a></h2>
<h5>Merge k Sorted Lists : You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.</h5>
<h5>note : Merge all the linked-lists into one sorted linked-list and return it.</h5><h3>MyAnswer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="err">#</span><span class="w"> </span><span class="n">Definition</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">singly</span><span class="o">-</span><span class="n">linked</span><span class="w"> </span><span class="n">list</span><span class="p">.</span><span class="w"></span>
<span class="err">#</span><span class="w"> </span><span class="k">class</span><span class="w"> </span><span class="nl">ListNode</span><span class="p">:</span><span class="w"></span>
<span class="err">#</span><span class="w">     </span><span class="n">def</span><span class="w"> </span><span class="n">__init__</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="n">val</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="k">next</span><span class="o">=</span><span class="k">None</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="err">#</span><span class="w">         </span><span class="n">self</span><span class="p">.</span><span class="n">val</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">val</span><span class="w"></span>
<span class="err">#</span><span class="w">         </span><span class="n">self</span><span class="p">.</span><span class="k">next</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">next</span><span class="w"></span>
<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">mergeKLists</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">lists</span><span class="p">:</span><span class="w"> </span><span class="n">List</span><span class="o">[</span><span class="n">Optional[ListNode</span><span class="o">]</span><span class="err">]</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">Optional</span><span class="o">[</span><span class="n">ListNode</span><span class="o">]</span><span class="err">:</span><span class="w"></span>
<span class="w">        </span><span class="n">root</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">ListNode</span><span class="p">(</span><span class="k">None</span><span class="p">)</span><span class="w"></span>
<span class="w">        </span><span class="n">heap</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="err">[]</span><span class="w"></span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="nf">len</span><span class="p">(</span><span class="n">lists</span><span class="p">))</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="n">lists</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="n">heapq</span><span class="p">.</span><span class="n">heappush</span><span class="p">(</span><span class="n">heap</span><span class="p">,</span><span class="w"> </span><span class="p">(</span><span class="n">lists</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="p">.</span><span class="n">val</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="p">,</span><span class="w"> </span><span class="n">lists</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="p">))</span><span class="w"></span>
<span class="w">        </span><span class="k">while</span><span class="w"> </span><span class="nl">heap</span><span class="p">:</span><span class="w"></span>
<span class="w">            </span><span class="n">node</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">heapq</span><span class="p">.</span><span class="n">heappop</span><span class="p">(</span><span class="n">heap</span><span class="p">)</span><span class="w"></span>
<span class="w">            </span><span class="n">idx</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">node</span><span class="o">[</span><span class="n">1</span><span class="o">]</span><span class="w"></span>
<span class="w">            </span><span class="k">result</span><span class="p">.</span><span class="k">next</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">node</span><span class="o">[</span><span class="n">2</span><span class="o">]</span><span class="w"></span>
<span class="w">            </span><span class="k">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">result</span><span class="p">.</span><span class="k">next</span><span class="w"></span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="k">result</span><span class="p">.</span><span class="k">next</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="n">heapq</span><span class="p">.</span><span class="n">heappush</span><span class="p">(</span><span class="n">heap</span><span class="p">,</span><span class="w"> </span><span class="p">(</span><span class="k">result</span><span class="p">.</span><span class="k">next</span><span class="p">.</span><span class="n">val</span><span class="p">,</span><span class="w"> </span><span class="n">idx</span><span class="p">,</span><span class="w"> </span><span class="k">result</span><span class="p">.</span><span class="k">next</span><span class="p">))</span><span class="w"></span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="n">root</span><span class="p">.</span><span class="k">next</span><span class="w"></span>
</code></pre></div><h5>Result : 97ms Memory: 17.9mb</h5>## Merge k Sorted Lists란?

Merge k Sorted Lists는 k개의 정렬된 linked list를 하나로 병합하는 알고리즘입니다. 이 알고리즘을 사용하면 효율적으로 정렬된 데이터를 하나의 리스트로 통합할 수 있습니다.

## Merge k Sorted Lists 알고리즘의 작동 방식

1. k개의 정렬된 linked list 생성
2. list의 각 element를 알맞게 비교하여 적합한 위치에 삽입
3. 합쳐진 리스트를 반환

이 알고리즘의 시간 복잡도는 O(nlogk)입니다. 이는 우선순위 큐를 사용해 각 리스트에서 기대되는 가장 최소값을 탐색하고, 그 중 최소값을 찾아 출력 리스트에 추가하는 과정을 반복하면서 삽입하는 방식입니다.


## Merge k Sorted Lists 알고리즘의 장단점

### 장점
- 정렬된 데이터를 빠르게 합칠 수 있습니다.
- 추가적인 메모리를 사용하지 않습니다.
- 유연한 사용 가능 

### 단점 
- 정렬된 데이터가 아닐 경우 알고리즘의 성능이 하락합니다.
- 입력값 k가 크면 메모리 사용량이 증가합니다. 

## Merge k Sorted Lists의 활용 방안

Merge k Sorted Lists는 정렬된 데이터를 병합해야 하는 다양한 문제에 대해 효과적인 해결책입니다. 사용예로는 매우 다양한 문제가 있습니다. 예를 들어, 최적화 문제, 빅데이터 분석, 자연어 처리 등의 분야에서 활용 가능합니다. 

## 요약

Merge k Sorted Lists는 k개의 정렬된 리스트를 하나로 병합하는 알고리즘으로, 효율적으로 정렬된 데이터를 하나의 리스트로 통합할 수 있습니다. 시간복잡도는 O(nlogk)로, 우선순위 큐를 사용해 각 리스트에서 기대값을 찾아 출력 리스트에 빠르게 추가합니다. 이를 통해 정렬되지 않은 데이터를 정리하는데 유용하게 사용될 수 있습니다.