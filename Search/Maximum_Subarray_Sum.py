#!/bin/python3


import sys

q = int(input().strip())
while q > 0:
    n, m = [int(x) for x in input().strip().split()]
    arry = [int(x) % m for x in input().strip().split()]
    pre_sum = [{'index': 0, 'value':arry[0]}]
    for i in range(1, n):
        pre_sum.append({'index': i, 'value': (pre_sum[i - 1]['value'] + arry[i]) % m})
    max_value = max(arry)
    pre_sum = sorted(pre_sum, key=lambda x: x['value'])
    max_value = pre_sum[n - 1]['value'] if pre_sum[n - 1]['value'] > max_value else max_value
    for i in range(n - 1):
        if pre_sum[i]['index'] > pre_sum[i + 1]['index']:
            value =   (pre_sum[i]['value'] - pre_sum[i + 1]['value'] + m)
            max_value = value if value > max_value else max_value
    print(max_value)
    q -= 1
