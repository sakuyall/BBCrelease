"""2/7/26
在这里记录bisect库的二分使用
"""
import bisect

arr = [1, 3, 3, 5, 7, 9]

# 1. bisect_left(a, x): 返回第一个 >= x 的元素位置
print(bisect.bisect_left(arr, 3))   # 1 (索引1)
print(bisect.bisect_left(arr, 4))   # 3 (第一个>=4的位置)

# 2. bisect_right(a, x) / bisect(a, x): 返回第一个 > x 的元素位置
print(bisect.bisect_right(arr, 3))  # 3 (第一个>3的位置)
print(bisect.bisect(arr, 3))        # 3 (同bisect_right)

# 3. insort_left(a, x): 在合适位置插入x，保持有序
bisect.insort_left(arr, 4)
print(arr)  # [1, 3, 3, 4, 5, 7, 9]

# 4. insort_right(a, x) / insort(a, x): 在合适位置插入x
arr = [1, 3, 3, 5, 7, 9]
bisect.insort_right(arr, 4)
print(arr)  # [1, 3, 3, 4, 5, 7, 9]