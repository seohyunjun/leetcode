<h2>LeetCode-<a href="https://leetcode.com/problems/merge-two-sorted-lists/">21</a></h2>
<h5>Merge Two Sorted Lists : Merge Two lists</h5>
<h5>note : recursive</h5><h3></h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="err">#</span><span class="w"> </span><span class="n">Definition</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">singly</span><span class="o">-</span><span class="n">linked</span><span class="w"> </span><span class="n">list</span><span class="p">.</span><span class="w"></span>
<span class="err">#</span><span class="w"> </span><span class="k">class</span><span class="w"> </span><span class="nl">ListNode</span><span class="p">:</span><span class="w"></span>
<span class="err">#</span><span class="w">     </span><span class="n">def</span><span class="w"> </span><span class="n">__init__</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="n">val</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="k">next</span><span class="o">=</span><span class="k">None</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="err">#</span><span class="w">         </span><span class="n">self</span><span class="p">.</span><span class="n">val</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">val</span><span class="w"></span>
<span class="err">#</span><span class="w">         </span><span class="n">self</span><span class="p">.</span><span class="k">next</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">next</span><span class="w"></span>
<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">mergeTwoLists</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">list1</span><span class="p">:</span><span class="w"> </span><span class="n">Optional</span><span class="o">[</span><span class="n">ListNode</span><span class="o">]</span><span class="p">,</span><span class="w"> </span><span class="nl">list2</span><span class="p">:</span><span class="w"> </span><span class="n">Optional</span><span class="o">[</span><span class="n">ListNode</span><span class="o">]</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="n">Optional</span><span class="o">[</span><span class="n">ListNode</span><span class="o">]</span><span class="err">:</span><span class="w"></span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="ow">not</span><span class="w"> </span><span class="n">list1</span><span class="p">)</span><span class="w"> </span><span class="ow">or</span><span class="w"> </span><span class="p">(</span><span class="n">list2</span><span class="w"> </span><span class="ow">and</span><span class="w"> </span><span class="n">list1</span><span class="p">.</span><span class="n">val</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="n">list2</span><span class="p">.</span><span class="n">val</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="n">list1</span><span class="p">,</span><span class="w"> </span><span class="n">list2</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">list2</span><span class="p">,</span><span class="w"> </span><span class="n">list1</span><span class="w"></span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="nl">list1</span><span class="p">:</span><span class="w"></span>
<span class="w">            </span><span class="n">list1</span><span class="p">.</span><span class="k">next</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">self</span><span class="p">.</span><span class="n">mergeTwoLists</span><span class="p">(</span><span class="n">list1</span><span class="p">.</span><span class="k">next</span><span class="p">,</span><span class="w"> </span><span class="n">list2</span><span class="p">)</span><span class="w"></span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="n">list1</span><span class="w"></span>
</code></pre></div><h5>Result : 42ms Memory: 13.8mb</h5>