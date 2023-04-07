<h2>LeetCode-<a href="https://leetcode.com/problems/implement-queue-using-stacks/">232</a></h2>
<h5>Implement Queue using Stacks : Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).</h5>
<h5>note : sub</h5><h3>선입선출</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">:::</span><span class="n">python</span><span class="w"></span>

<span class="n">class</span><span class="w"> </span><span class="n">MyQueue</span><span class="o">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">__init__</span><span class="p">(</span><span class="kr">self</span><span class="p">)</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="kr">self</span><span class="p">.</span><span class="n">temp</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">collections</span><span class="p">.</span><span class="n">deque</span><span class="p">()</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">push</span><span class="p">(</span><span class="kr">self</span><span class="p">,</span><span class="w"> </span><span class="n">x</span><span class="o">:</span><span class="w"> </span><span class="n">int</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">None</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="kr">self</span><span class="p">.</span><span class="n">temp</span><span class="p">.</span><span class="n">append</span><span class="p">(</span><span class="n">x</span><span class="p">)</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">pop</span><span class="p">(</span><span class="kr">self</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">int</span><span class="o">:</span><span class="w">   </span>
<span class="w">        </span><span class="kr">return</span><span class="w"> </span><span class="kr">self</span><span class="p">.</span><span class="n">temp</span><span class="p">.</span><span class="n">popleft</span><span class="p">()</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">peek</span><span class="p">(</span><span class="kr">self</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">int</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="kr">return</span><span class="w"> </span><span class="kr">self</span><span class="p">.</span><span class="n">temp</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">empty</span><span class="p">(</span><span class="kr">self</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">bool</span><span class="o">:</span><span class="w"></span>
<span class="w">        </span><span class="nf">if</span><span class="w"> </span><span class="n">len</span><span class="p">(</span><span class="kr">self</span><span class="p">.</span><span class="n">temp</span><span class="p">)</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">True</span><span class="w"></span>
<span class="w">        </span><span class="n">else</span><span class="o">:</span><span class="w"></span>
<span class="w">            </span><span class="kr">return</span><span class="w"> </span><span class="kr">False</span><span class="w"></span>
<span class="cp"># Your MyQueue object will be instantiated and called as such:</span><span class="w"></span>
<span class="cp"># obj = MyQueue()</span><span class="w"></span>
<span class="cp"># obj.push(x)</span><span class="w"></span>
<span class="cp"># param_2 = obj.pop()</span><span class="w"></span>
<span class="cp"># param_3 = obj.peek()</span><span class="w"></span>
<span class="cp"># param_4 = obj.empty()</span><span class="w"></span>
</code></pre></div><h5>Result : 34ms Memory: 13.9mb</h5>