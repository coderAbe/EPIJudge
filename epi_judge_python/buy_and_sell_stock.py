from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # O(n)
    maxDiff = 0
    current_p = prices[0]
       
    for price in prices:
        current_p = min(current_p, price)
        currentDiff =  price - current_p
        maxDiff = max(currentDiff, maxDiff)

    return maxDiff 


def max_continous_subarray (numbers: List{float]) -> float:
    max_len = 0
    current_len = 1
    current_num = numbers[0]

    for num in numbers[1:]:
        if current_num != num:
            current_num = num
            current_len = 1
        else:
            current_len += 1

        max_len = max(current_len, max_len)

    return max_len

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
