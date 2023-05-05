<h2>LeetCode-<a href="https://leetcode.com/problems/rotate-image/description/">48</a></h2>
<h5>Rotate Image : You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).</h5>
<h5>note : You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.</h5><h3>Answer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">rotate</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">matrix</span><span class="p">:</span><span class="w"> </span><span class="n">List</span><span class="o">[</span><span class="n">List[int</span><span class="o">]</span><span class="err">]</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="k">None</span><span class="err">:</span><span class="w"></span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">matrix</span><span class="o">[</span><span class="n">0</span><span class="o">]</span><span class="p">)</span><span class="o">==</span><span class="mi">1</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">return</span><span class="w"> </span><span class="k">None</span><span class="w"></span>
<span class="w">        </span><span class="n">max_length</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">matrix</span><span class="o">[</span><span class="n">0</span><span class="o">]</span><span class="p">)</span><span class="w"></span>
<span class="w">        </span><span class="n">matrix</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">collections</span><span class="p">.</span><span class="n">deque</span><span class="p">(</span><span class="n">matrix</span><span class="p">)</span><span class="w"></span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="n">max_length</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">for</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="n">max_length</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="n">matrix</span><span class="o">[</span><span class="n">j</span><span class="o">]</span><span class="p">.</span><span class="n">append</span><span class="p">(</span><span class="n">matrix</span><span class="o">[</span><span class="n">max_length-i-1</span><span class="o">]</span><span class="p">.</span><span class="n">pop</span><span class="p">(</span><span class="mi">0</span><span class="p">))</span><span class="w"></span>
</code></pre></div><h3>Result : 43ms Memory: 16.3mb</h3>
 # 문제
주어진 2D 배열을 90도 회전시키는 문제입니다.

# 예시
예시 입력 배열:
```
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
```

예시 출력 배열:
```
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

# 접근 방법
이 문제를 풀기 위해서는 이차원 배열에서 행과 열의 위치를 바꾸는 것이 필요합니다. 이를 처리하기 위해서는 다음과 같은 두 가지 방법이 있습니다.

## 행과 열 바꾸기
우선 행과 열의 위치를 바꿔보겠습니다. 예시 배열을 바꾸면 다음과 같은 모양을 가지게 됩니다.
```
[
  [1,4,7],
  [2,5,8],
  [3,6,9]
]
```
이제 각 행을 뒤집으면 회전된 배열이 완성됩니다.

## 대각선 기준 바꾸기
대각선에 대해 대칭을 만들어 보겠습니다.
예시 배열을 대각선으로 뒤집으면 다음과 같은 모양을 가지게 됩니다.
```
[
  [1,4,7],
  [2,5,8],
  [3,6,9]
]
```
이제 각 형태는 둘 다 같은 모양입니다. 이 중에서 각 행을 뒤집어주면 회전된 배열이 완성됩니다.

# 시간 복잡도
이 문제의 시간 복잡도는 O(n^2)입니다. 이는 주어진 배열의 모든 요소를 한 번씩만 방문해서 처리하게 되기 때문입니다.