import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())

for _ in range(n):
    p = int(input())
    if is_prime(p):
        print("Prime")
    else:
        print("Not Prime")
