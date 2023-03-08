<h2>LeetCode-<a href="https://leetcode.com/problems/array-partition/">561</a></h2>
<h5>Array Partition : find maximum (minimum list)</h5>
<h5>note : len(list) = 2n</h5><h3>myAnswer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">arrayPairSum</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">nums</span><span class="p">:</span><span class="w"> </span><span class="n">List</span><span class="o">[</span><span class="n">int</span><span class="o">]</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="nc">int</span><span class="err">:</span><span class="w"></span>
<span class="w">        </span><span class="n">nums</span><span class="p">.</span><span class="n">sort</span><span class="p">()</span><span class="w"></span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="nf">sum</span><span class="p">(</span><span class="n">nums</span><span class="o">[</span><span class="n">::2</span><span class="o">]</span><span class="p">)</span><span class="w"></span>
</code></pre></div><h5>Result : 267ms Memory: 16.7mb</h5>