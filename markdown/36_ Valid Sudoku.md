<h2>LeetCode-<a href="https://leetcode.com/problems/valid-sudoku/description/">36</a></h2>
<h5>Valid Sudoku : A Sudoku board (partially filled) could be valid but is not necessarily solvable.</h5>
<h5>note : Only the filled cells need to be validated according to the mentioned rules.</h5><h3>Answer</h3><div class="codehilite"><pre><span></span><code><span class="w">        </span><span class="o">::</span><span class="err">:</span><span class="n">python</span><span class="w"></span>

<span class="k">class</span><span class="w"> </span><span class="nl">Solution</span><span class="p">:</span><span class="w"></span>
<span class="w">    </span><span class="n">def</span><span class="w"> </span><span class="n">isValidSudoku</span><span class="p">(</span><span class="n">self</span><span class="p">,</span><span class="w"> </span><span class="nl">board</span><span class="p">:</span><span class="w"> </span><span class="n">List</span><span class="o">[</span><span class="n">List[str</span><span class="o">]</span><span class="err">]</span><span class="p">)</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="nl">bool</span><span class="p">:</span><span class="w"></span>
<span class="w">        </span><span class="n">def</span><span class="w"> </span><span class="n">valid_row</span><span class="p">(</span><span class="n">i</span><span class="p">,</span><span class="w"> </span><span class="n">j</span><span class="p">,</span><span class="w"> </span><span class="k">row</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="k">row</span><span class="o">==</span><span class="mi">1</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="n">item</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">board</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="w"></span>
<span class="w">            </span><span class="k">else</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="n">item</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">[</span><span class="n">board[n</span><span class="o">][</span><span class="n">j</span><span class="o">]</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">n</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">9</span><span class="p">)</span><span class="err">]</span><span class="w"></span>
<span class="w">            </span><span class="n">p</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="err">[]</span><span class="w"></span>
<span class="w">            </span><span class="n">box</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">[</span><span class="n">board[i//3*2 + r</span><span class="o">][</span><span class="n">j//3*2 + c</span><span class="o">]</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">r</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="n">i</span><span class="o">//</span><span class="mi">3</span><span class="p">,</span><span class="w"> </span><span class="n">i</span><span class="o">//</span><span class="mi">3</span><span class="o">+</span><span class="mi">3</span><span class="p">)</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">c</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="n">j</span><span class="o">//</span><span class="mi">3</span><span class="p">,</span><span class="w"> </span><span class="n">j</span><span class="o">//</span><span class="mi">3</span><span class="o">+</span><span class="mi">3</span><span class="p">)</span><span class="err">]</span><span class="w">    </span>
<span class="w">            </span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="err">[]</span><span class="w"></span>
<span class="w">            </span><span class="k">for</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">9</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="k">if</span><span class="w"> </span><span class="n">item</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="w"> </span><span class="o">!=</span><span class="s1">&#39;.&#39;</span><span class="err">:</span><span class="w"></span>
<span class="w">                    </span><span class="n">p</span><span class="p">.</span><span class="n">append</span><span class="p">(</span><span class="n">item</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="p">)</span><span class="w"></span>
<span class="w">                </span><span class="k">if</span><span class="w"> </span><span class="n">box</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="w"> </span><span class="o">!=</span><span class="s1">&#39;.&#39;</span><span class="err">:</span><span class="w"></span>
<span class="w">                    </span><span class="n">b</span><span class="p">.</span><span class="n">append</span><span class="p">(</span><span class="n">box</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="p">)</span><span class="w"></span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="k">set</span><span class="p">(</span><span class="n">box</span><span class="p">))</span><span class="o">-</span><span class="mi">1</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">b</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="n">pass</span><span class="w"> </span>
<span class="w">            </span><span class="k">else</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="k">return</span><span class="w"> </span><span class="k">False</span><span class="w"></span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="k">set</span><span class="p">(</span><span class="n">item</span><span class="p">))</span><span class="o">-</span><span class="mi">1</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="nf">len</span><span class="p">(</span><span class="n">p</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="k">return</span><span class="w"> </span><span class="k">True</span><span class="w"> </span>
<span class="w">            </span><span class="k">else</span><span class="err">:</span><span class="w"> </span>
<span class="w">                </span><span class="k">return</span><span class="w"> </span><span class="k">False</span><span class="w"></span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">9</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">            </span><span class="k">for</span><span class="w"> </span><span class="n">j</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="k">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">9</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">                </span><span class="k">if</span><span class="w"> </span><span class="n">valid_row</span><span class="p">(</span><span class="n">i</span><span class="p">,</span><span class="n">j</span><span class="p">,</span><span class="mi">0</span><span class="p">)</span><span class="w"> </span><span class="ow">and</span><span class="w"> </span><span class="n">valid_row</span><span class="p">(</span><span class="n">i</span><span class="p">,</span><span class="n">j</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span><span class="err">:</span><span class="w"></span>
<span class="w">                    </span><span class="n">pass</span><span class="w"></span>
<span class="w">                </span><span class="k">else</span><span class="err">:</span><span class="w"></span>
<span class="w">                    </span><span class="k">return</span><span class="w"> </span><span class="k">False</span><span class="w"></span>
<span class="w">        </span><span class="k">return</span><span class="w"> </span><span class="k">True</span><span class="w"></span>
</code></pre></div><h3>Result : 272ms Memory: 16.5mb</h3>
 문제: 유효한 스도쿠

이 문제는 9x9 크기인 스도쿠 게임이 유효한지 확인하는 문제입니다. 각 행, 열, 그리고 작은 3x3 사각형에 1~9의 숫자가 한 번씩만 등장하면 유효한 스도쿠입니다. 입력으로 이를 나타내는 9x9 문자열 배열이 주어집니다.

해결책: 

이 문제의 핵심은 각 행, 열, 사각형에 중복된 숫자가 있는지를 확인하는 것입니다. 우리는 각 행, 열, 그리고 작은 사각형을 9개씩 총 27개의 그룹으로 나눌 수 있습니다. 이 그룹들 중 한 그룹에 중복된 숫자가 있다면 스도쿠는 유효하지 않습니다. 

따라서, 각 그룹의 중복 여부를 체크하는 helper function `valid_row` 를 만들고 이 함수를 이용해서 각 행, 열, 작은 사각형에 대해 유효성을 판단할 수 있습니다.

`valid_row` 함수에는 3개의 인자가 필요합니다. `i` 와 `j` 는 현재 검사하고 있는 원소의 위치를 나타냅니다. `row` 는 0, 1로 나눌 수 있으며, 각각 해당 원소의 행과 열을 검사하는 경우입니다. 

함수는 해당 그룹에 속한 모든 원소를 모은 `item` 리스트와 같은 작은 사각형에 속한 모든 원소를 모은 `box` 리스트를 만듭니다. `item` 과 `box` 리스트에서 `.` 를 제외한 모든 원소를 `p` 와 `b` 리스트에 저장합니다. 

그리고나서 `set` 을 이용해서 중복된 숫자가 있는지 확인합니다. 만약 중복된 숫자가 있다면, 해당 그룹이 유효하지 않습니다. 마지막으로, 해당 그룹이 유효하다면 `True` 를 반환합니다.

그리고 `isValidSudoku` 메소드는 각 행, 열, 작은 사각형에 대해서 `valid_row` 함수를 호출하기만 하면 됩니다.

이렇게 작성한 해결책의 시간복잡도는 $O(81 \times (3 \times 9)) = O(2187)$ 이므로 충분히 효율적입니다.

아래는 주어진 코드입니다. 

```
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_row(i, j, row):
            if row==1:
                item = board[i]
            else:
                item = [board[n][j] for n in range(0,9)]
            p = []
            box = [board[i//3*3 + r][j//3*3 + c] for r in range(0,3) for c in range(0,3)]    
            b = []
            for i in range(0,9):
                if item[i] !='.':
                    p.append(item[i])
                if box[i] !='.':
                    b.append(box[i])
            if len(set(box))-1 == len(b):
                pass 
            else:
                return False
            if len(set(item))-1 == len(p):
                return True 
            else: 
                return False
        for i in range(0,9):
            for j in range(0,9):
                if valid_row(i,j,0) and valid_row(i,j,1):
                    pass
                else:
                    return False
        return True
```

코드 리뷰: 

주어진 코드는 위에서 정의한 해결책과 굉장히 유사합니다. 

다만, 작은 사각형에 대한 `box` 를 만들 때 잘못된 인덱싱을 사용하는 오류가 있습니다. `box` 의 원소의 인덱스를 찾을 때에는 3을 곱해야 하는데 2로 찾게 되어서 문제가 생깁니다.

올바른 코드:

```
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_row(i, j, row):
            if row==1:
                item = board[i]
            else:
                item = [board[n][j] for n in range(0,9)]
            p = []
            box = [board[i//3*3 + r][j//3*3 + c] for r in range(0,3) for c in range(0,3)]    
            b = []
            for i in range(0,9):
                if item[i] !='.':
                    p.append(item[i])
                if box[i] !='.':
                    b.append(box[i])
            if len(set(box))-1 == len(b):
                pass 
            else:
                return False
            if len(set(item))-1 == len(p):
                return True 
            else: 
                return False
        for i in range(0,9):
            for j in range(0,9):
                if valid_row(i,j,0) and valid_row(i,j,1):
                    pass
                else:
                    return False
        return True
```