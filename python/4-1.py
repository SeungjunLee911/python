'''
import numpy as np

a, b = input("").split()

a = int(a)
b = int(b)

if 2<= b <= 36:
    print(np.base_repr(a, base =b))
else:
    print("B 조건오류")
'''

a, b = map(int, input().split())

if 2 <= b <= 36:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while a > 0:
        a, r = divmod(a, b)
        result = digits[r] + result
    if result:
        print(result)
    else:
        print("0")
else:
    print("B 조건오류")
