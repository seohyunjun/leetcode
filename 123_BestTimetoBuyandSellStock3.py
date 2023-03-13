from util.python2Markdown import Block 

num = 123
subject = 'Best Time to Buy and Sell Stock3'        
leetcode_addr = 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/'
info = '2번의 매수 매도 max(profit)'
sub = '주식을 다시 사기 전에 매도를 해야함'
sub_context = ''
code = """"""
sec = 0
memory = 0

prices = [3,3,5,0,0,3,1,4]

profit = 0
min_price = sys.maxsize

for price in prices:
    min_price = min(price, min_price)
    profit = max(profit,price-min_price)
    prices.pop(0)
    if profit > price-min_price:
        
        for price in prices:
            profit1 = 0
            min_price = sys.maxsize
            min_price = min(price, min_price)
            profit1 = max(profit1,price-min_price)
    
    return



block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)

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
