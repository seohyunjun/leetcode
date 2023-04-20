<h2>LeetCode-<a href="https://leetcode.com/problems/reverse-integer/description/">7</a></h2>
<h5>Reverse Integer : Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.</h5>
<h5>note : Assume the environment does not allow you to store 64-bit integers (signed or unsigned).</h5><h3>Answer</h3><div class="codehilite"><pre><span></span><code>        <span class="s s-Atom">:::python</span>

<span class="s s-Atom">class</span> <span class="nv">Solution</span><span class="s s-Atom">:</span>
    <span class="s s-Atom">def</span> <span class="nf">reverse</span><span class="p">(</span><span class="s s-Atom">self</span><span class="p">,</span> <span class="nn">x</span><span class="p">:</span> <span class="s s-Atom">int</span><span class="p">)</span> <span class="s s-Atom">-&gt;</span> <span class="nn">int</span><span class="p">:</span>
        <span class="s s-Atom">if</span> <span class="s s-Atom">x</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="s s-Atom">:</span>
            <span class="s s-Atom">x</span> <span class="o">=</span> <span class="nf">int</span><span class="p">(</span><span class="nf">str</span><span class="p">(</span><span class="s s-Atom">x</span><span class="p">)[</span><span class="s s-Atom">::-</span><span class="mi">1</span><span class="p">])</span>
        <span class="nn">else</span><span class="p">:</span>
            <span class="s s-Atom">x</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span><span class="o">*</span><span class="nf">int</span><span class="p">(</span><span class="nf">str</span><span class="p">(</span><span class="s s-Atom">x*-</span><span class="mi">1</span><span class="p">)[</span><span class="s s-Atom">::-</span><span class="mi">1</span><span class="p">])</span>
        <span class="nf">if</span> <span class="p">(</span><span class="o">-</span><span class="mi">2</span><span class="s s-Atom">**</span><span class="mi">31</span> <span class="o">&gt;</span> <span class="s s-Atom">x</span><span class="p">)</span> <span class="nf">or</span> <span class="p">(</span><span class="s s-Atom">x</span> <span class="o">&gt;</span> <span class="mi">2</span><span class="s s-Atom">**</span><span class="mi">31</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span><span class="s s-Atom">:</span>
            <span class="s s-Atom">return</span> <span class="mi">0</span>
        <span class="nn">else</span><span class="p">:</span>
            <span class="s s-Atom">return</span> <span class="s s-Atom">x</span>
</code></pre></div><h3>Result : 34ms Memory: 13.8mb</h3>
 # Reverse Integer
Reverse Integer는 숫자를 뒤집어서 반환하는 알고리즘이다.

## 예시
### 입력(Input)
```
123
```

### 출력(Output)
```
321
```

### 입력(Input)
```
-123
```

### 출력(Output)
```
-321
```

### 입력(Input)
```
120
```

### 출력(Output)
```
21
```

## 알고리즘
1. 입력된 숫자의 부호를 체크한다.
2. 만약 부호가 음수이면 양수로 바꾼다.
3. 숫자를 뒤집은 값을 저장할 변수를 선언한다.
4. 입력된 숫자를 10으로 나눈 나머지를 변수에 더하고 입력된 숫자를 10으로 나눈 몫으로 갱신한다. 이를 반복하여 입력된 숫자를 모두 뒤집은 값을 구한다.
5. 구한 뒤집은 값을 부호에 맞게 반환한다.

## 시간 복잡도
입력된 숫자의 자리수에 비례하는 O(n)이 소요된다. (n은 숫자의 자리수)