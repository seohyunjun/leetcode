from util.python2Markdown import Block 

num = 121
subject = 'Best Time to Buy and Sell Stock'        
leetcode_addr = 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock/'
info = '싸게 사서 비싸게 팔아라!'
sub = 'max(profit)'

sub_context = 'myAnswer'
code = """
    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            len_prices = len(prices)
            if len_prices < 2:
                return 0

            buy = prices[0]
            profit = prices[1] - prices[0]
            for i in range(1,len_prices):
                sell = max(prices[i:])
                
                if profit < sell-buy:
                    profit = sell - buy
                buy = prices[i]
            if profit < 0:
                profit = 0
            return profit
"""

sec = "Time Over-"
memory = "Over-"


sub_context2 = 'Answer'
code2 = """
    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            profit = 0
            min_price = sys.maxsize
            for price in prices:
                min_price = min(min_price, price)
                profit = max(profit, price - min_price)
            return profit
"""

sec2 = 1102
memory2 = 25.1

block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)
block.addcode_block(sub_context2, code2, sec2, memory2)

# subtitle = f'### {sub_context}'
# block.titleblock(subtitle)

# code1 = f"""
#     :::python
#     {code}
# """
# block.codeblock(code1)

# performance_title = f'##### Result : {sec}ms Memory: {memory}mb'
# block.titleblock(performance_title)

print_result = ''.join(block.result)

with open(f"markdown/{num}_{subject}.md",'w') as f:
    f.write(print_result)
    

####### using slicing
