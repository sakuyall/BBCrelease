"""1/3/25
"""
def get_unique_count(li, n):
    aset = set(li)
    return len(aset)
n = input()
a = list(map(int, input().split()))
print(get_unique_count(a, n))