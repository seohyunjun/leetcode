<h2>LeetCode-<a href="https://leetcode.com/problems/reorder-data-in-log-files/">937</a></h2>
<h5>Reorder_Data_in_LogFile : reorder log files</h5>
<h5>첫번째 문자 식별자 ex) "dig2 a","dig1 b"-&gt; "a","b"</h5><h3>Myanswer</h3><div class="codehilite"><pre><span></span><code><span class="k">class</span> <span class="nc">Solution</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">reorderLogFiles</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">logs</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>   
        <span class="n">let</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">digit</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">logs</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">i</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">isdigit</span><span class="p">()</span><span class="o">==</span><span class="kc">False</span><span class="p">:</span>
                <span class="n">let</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">digit</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> 
        <span class="n">let</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="p">(</span><span class="n">x</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">x</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">0</span><span class="p">]))</span>
        <span class="c1">#digit.sort(key = lambda x: x.split()[1:],reverse=True)</span>
        <span class="k">return</span> <span class="n">let</span> <span class="o">+</span> <span class="n">digit</span>
</code></pre></div><h4>Result : 38ms Memory: 14mb</h4>