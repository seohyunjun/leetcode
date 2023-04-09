<h2>LeetCode-<a href="https://leetcode.com/problems/design-circular-deque/">641</a></h2>
<h5>Design Circular Deque : Design your implementation of the circular double-ended queue (deque).</h5>
<h5>note : Returns -1 if the deque is empty.</h5><h3>MyAnswer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">:::</span><span class="n">python</span><span class="w"></span>

<span class="n">class</span><span class="w"> </span><span class="n">MyCircularDeque</span><span class="o">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">__init__</span><span class="p">(</span><span class="kr">self</span><span class="p">,</span><span class="w"> </span><span class="n">k</span><span class="o">:</span><span class="w"> </span><span class="n">int</span><span class="p">)</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="kr">self</span><span class="p">.</span><span class="n">maxsize</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">k</span><span class="w"></span>
<span class="w">        </span><span class="kr">self</span><span class="p">.</span><span class="n">deq</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">collections</span><span class="p">.</span><span class="n">deque</span><span class="p">(</span><span class="n">maxlen</span><span class="o">=</span><span class="n">k</span><span class="p">)</span><span class="w"></span>
<span class="w">        </span><span class="kr">self</span><span class="p">.</span><span class="n">deq_size</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">insertFront</span><span class="p">(</span><span class="kr">self</span><span class="p">,</span><span class="w"> </span><span class="n">value</span><span class="o">:</span><span class="w"> </span><span class="n">int</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">bool</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="nf">if</span><span class="w"> </span><span class="kr">self</span><span class="p">.</span><span class="n">deq_size</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="kr">self</span><span class="p">.</span><span class="n">maxsize</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">self</span><span class="p">.</span><span class="n">deq</span><span class="p">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">value</span><span class="p">)</span><span class="w"></span>
<span class="w">            </span><span class="kr">self</span><span class="p">.</span><span class="n">deq_size</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="mi">1</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">True</span><span class="w"></span>
<span class="w">        </span><span class="n">else</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">False</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">insertLast</span><span class="p">(</span><span class="kr">self</span><span class="p">,</span><span class="w"> </span><span class="n">value</span><span class="o">:</span><span class="w"> </span><span class="n">int</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">bool</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="nf">if</span><span class="w"> </span><span class="kr">self</span><span class="p">.</span><span class="n">deq_size</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="kr">self</span><span class="p">.</span><span class="n">maxsize</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">self</span><span class="p">.</span><span class="n">deq</span><span class="p">.</span><span class="n">append</span><span class="p">(</span><span class="n">value</span><span class="p">)</span><span class="w"></span>
<span class="w">            </span><span class="kr">self</span><span class="p">.</span><span class="n">deq_size</span><span class="w"> </span><span class="o">+=</span><span class="w"> </span><span class="mi">1</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">True</span><span class="w"></span>
<span class="w">        </span><span class="n">else</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">False</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">deleteFront</span><span class="p">(</span><span class="kr">self</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">bool</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="nf">if</span><span class="w"> </span><span class="kr">self</span><span class="p">.</span><span class="n">deq_size</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="mi">0</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">self</span><span class="p">.</span><span class="n">deq</span><span class="p">.</span><span class="n">popleft</span><span class="p">()</span><span class="w"></span>
<span class="w">            </span><span class="kr">self</span><span class="p">.</span><span class="n">deq_size</span><span class="w"> </span><span class="o">-=</span><span class="w"> </span><span class="mi">1</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">True</span><span class="w"></span>
<span class="w">        </span><span class="n">else</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">False</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">deleteLast</span><span class="p">(</span><span class="kr">self</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">bool</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="nf">if</span><span class="w"> </span><span class="kr">self</span><span class="p">.</span><span class="n">deq_size</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="mi">0</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">self</span><span class="p">.</span><span class="n">deq</span><span class="p">.</span><span class="n">pop</span><span class="p">()</span><span class="w"></span>
<span class="w">            </span><span class="kr">self</span><span class="p">.</span><span class="n">deq_size</span><span class="w"> </span><span class="o">-=</span><span class="w"> </span><span class="mi">1</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">True</span><span class="w"></span>
<span class="w">        </span><span class="n">else</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">False</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">getFront</span><span class="p">(</span><span class="kr">self</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">int</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="nf">if</span><span class="w"> </span><span class="kr">self</span><span class="p">.</span><span class="n">deq_size</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="mi">0</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">self</span><span class="p">.</span><span class="n">deq</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"></span>
<span class="w">        </span><span class="n">else</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="o">-</span><span class="mi">1</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">getRear</span><span class="p">(</span><span class="kr">self</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">int</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="nf">if</span><span class="w"> </span><span class="kr">self</span><span class="p">.</span><span class="n">deq_size</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="mi">0</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">self</span><span class="p">.</span><span class="n">deq</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="w"></span>
<span class="w">        </span><span class="n">else</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="o">-</span><span class="mi">1</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">isEmpty</span><span class="p">(</span><span class="kr">self</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">bool</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="nf">if</span><span class="w"> </span><span class="kr">self</span><span class="p">.</span><span class="n">deq_size</span><span class="o">==</span><span class="mi">0</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">True</span><span class="w"></span>
<span class="w">        </span><span class="n">else</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">False</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">isFull</span><span class="p">(</span><span class="kr">self</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">bool</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="nf">if</span><span class="w"> </span><span class="kr">self</span><span class="p">.</span><span class="n">deq_size</span><span class="o">==</span><span class="kr">self</span><span class="p">.</span><span class="n">maxsize</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">True</span><span class="w"></span>
<span class="w">        </span><span class="n">else</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">False</span><span class="w"></span>
<span class="cp"># Your MyCircularDeque object will be instantiated and called as such:</span><span class="w"></span>
<span class="cp"># obj = MyCircularDeque(k)</span><span class="w"></span>
<span class="cp"># param_1 = obj.insertFront(value)</span><span class="w"></span>
<span class="cp"># param_2 = obj.insertLast(value)</span><span class="w"></span>
<span class="cp"># param_3 = obj.deleteFront()</span><span class="w"></span>
<span class="cp"># param_4 = obj.deleteLast()</span><span class="w"></span>
<span class="cp"># param_5 = obj.getFront()</span><span class="w"></span>
<span class="cp"># param_6 = obj.getRear()</span><span class="w"></span>
<span class="cp"># param_7 = obj.isEmpty()</span><span class="w"></span>
<span class="cp"># param_8 = obj.isFull()</span><span class="w"></span>
</code></pre></div><h5>Result : 61ms Memory: 14.7mb</h5>## Design Circular Deque

Design Circular Deque는 원형 덱 자료구조를 디자인하는 문제입니다. 이를 구현하기 위해서는 원형 큐를 구현하는 방법이 필요합니다.

`CircularDeque` 클래스는 다음과 같은 기능을 제공해야 합니다.

- `CircularDeque(k)` : 길이가 k인 원형 덱을 생성합니다.
- `insertFront()` : 덱의 맨 앞에 요소를 추가합니다. 성공하면 True를 반환합니다.
- `insertLast()` : 덱의 맨 뒤에 요소를 추가합니다. 성공하면 True를 반환합니다.
- `deleteFront()` : 덱 맨 앞의 요소를 삭제합니다. 성공하면 True를 반환합니다.
- `deleteLast()` : 덱 맨 뒤의 요소를 삭제합니다. 성공하면 True를 반환합니다.
- `getFront()` : 덱 맨 앞의 요소를 반환합니다. 비어있다면 -1을 반환합니다.
- `getRear()` : 덱 맨 뒤의 요소를 반환합니다. 비어있다면 -1을 반환합니다.
- `isEmpty()` : 덱이 비어있는지 확인합니다. 비어있다면 True를 반환합니다.
- `isFull()` : 덱이 가득 차 있는지 확인합니다. 가득 차있다면 True를 반환합니다.

이러한 기능을 위해서는 `CircularDeque` 클래스 내부에 다음과 같은 변수들이 필요합니다.

- `self.queue`: 저장소
- `self.front`: 현재 맨 앞의 인덱스
- `self.rear`: 현재 맨 뒤의 인덱스
- `self.length`: 저장소의 길이

또한 `insertFront()`와 `insertLast()`, `deleteFront()`와 `deleteLast()` 메서드는 서로 대칭적인 기능을 수행합니다. 따라서 `insert()`와 `delete()`라는 하나의 함수로 묶어서 구현할 수 있습니다.