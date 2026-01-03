"""1/3/25
"""
def reverse(li, size):
    li[:size] = reversed(li[:size])

n, size = map(int, input().split())
li = list(map(int, input().split()))
reverse(li, size)
print(*li)