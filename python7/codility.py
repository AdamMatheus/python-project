import math

def get_pronic_count(num):
    n = int(math.sqrt(num))
    if n*(n+1) < num:
        return n
    else:
        return n-1

def get_pronic_count2(num):
    n = int(math.sqrt(num))
    if n*(n+1) <= num:
        return n
    else:
        return n-1


def count(A, B):
    countA = get_pronic_count(A)
    countB = get_pronic_count2(B)
    return countB - countA


print(count(6,20))
print(count(21,29))
print(count(1, 1000000000))