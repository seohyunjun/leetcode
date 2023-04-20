<h2>LeetCode-<a href="leetcode">9</a></h2>
<h5>PalindromeNumber : Given an integer x, return true if x is a palindrome, and false otherwise.</h5>
<h5>note : From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.</h5><h3>Answer</h3><div class="codehilite"><pre><span></span><code>        <span class="s s-Atom">:::python</span>

<span class="s s-Atom">class</span> <span class="nv">Solution</span><span class="s s-Atom">:</span>
    <span class="s s-Atom">def</span> <span class="nf">isPalindrome</span><span class="p">(</span><span class="s s-Atom">self</span><span class="p">,</span> <span class="nn">x</span><span class="p">:</span> <span class="s s-Atom">int</span><span class="p">)</span> <span class="s s-Atom">-&gt;</span> <span class="nn">bool</span><span class="p">:</span>
        <span class="s s-Atom">return</span> <span class="nf">str</span><span class="p">(</span><span class="s s-Atom">x</span><span class="p">)</span> <span class="o">==</span> <span class="nf">str</span><span class="p">(</span><span class="s s-Atom">x</span><span class="p">)[</span><span class="s s-Atom">::-</span><span class="mi">1</span><span class="p">]</span>
</code></pre></div><h3>Result : 57ms Memory: 13.7mb</h3># PalindromeNumber

PalindromeNumber는 앞으로 읽으나 뒤로 읽으나 동일한 값을 가지는 숫자를 말합니다.

예를 들어, 121이PalindromeNumber입니다. 왜냐하면 121을 뒤에서부터 읽어도 121이기 때문입니다.

하지만, 123은PalindromeNumber가 아닙니다. 왜냐하면 123을 뒤에서부터 읽으면 321이기 때문입니다.

PalindromeNumber는 주로 알고리즘 문제에서 많이 등장합니다. 대표적인 예로는 숫자를 뒤집어서 판별하는 문제가 있습니다. 숫자를 뒤집어서 원래 숫자와 같은지 비교하면PalindromeNumber인지 아닌지 판별할 수 있습니다.

PalindromeNumber 판별 방법은 일반적으로 문자열로 변환한 뒤, 첫 번째 문자와 마지막 문자를 비교하고, 두 번째 문자와 뒤에서 두 번째 문자를 비교하는 방식으로 진행합니다. 이렇게 순차적으로 비교하다가 비교 중 하나라도 다른 문자가 나오면PalindromeNumber가 아니라고 판별하면 됩니다. 이러한 방식으로 구현된 알고리즘은 시간복잡도가 O(n)으로 매우 빠릅니다.