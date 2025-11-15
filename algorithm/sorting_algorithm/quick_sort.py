# 快速排序
# 一句话总结：在二叉树遍历的前序位置将一个元素排好位置，然后递归地将剩下的元素排好位置
# 思路是：选择一个pivot元素，将pivot元素排好序，然后递归地对pivot左边和右边的子数组进行排序

# 代码框架:根据上述思路描述，可以写出快速排序的代码框架，代码中的nums[p]就是上面所说的pivot元素
# def sort(nums: List[int], lo: int, hi: int):
#     if lo >= hi:
#         return
#     # *******前序位置*******
#     # 对 nums[lo..hi]进行切分，将 nums[p]排好序
#     # 使得 nums[lo..p-1] <= nums[p] < nums[p+1..hi]
#     p = partition(nums, lo, hi)

#     # 去左右子数组进行切分
#     sort(nums, lo, p - 1)
#     sort(nums, p + 1, hi)

# 其中partition函数的实现是快速排序的核心，即遍历nums[lo..hi]，将切分点元素pivot放到正确的位置，并返回该位置的索引p.

# 时间复杂度: 平均时间复杂度O(nlogn)，最坏时间复杂度O(n^2)
# 空间复杂度: O(logn)~O(n)，取决于递归
# 稳定性：一般认为是不稳定的排序算法