class Solution(object):
    def reOrderArray(self, array):
        """
        :type array: List[int]
        :rtype: void
        左指针右移直到找到偶数停下
        右指针左移直到找到奇数停下
        当左指针小于右指针, 交换这两个数
        """
        length = len(array)
        i, j = 0, length - 1
        
        while i < j:
            if array[i] % 2 != 0:
                i += 1
            if array[j] % 2 == 0:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]
        
        return array