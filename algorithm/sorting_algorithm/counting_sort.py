# 计数排序
# 原理：统计每种元素出现的次数，进而推算出每个元素在排序后数组中的索引位置，最终完整排序。
# 计数排序的时间和空间复杂度都是O(n + max - min), 其中n是待排序数组的长度，max-min是待排序数组的元素范围。

# 疑问：
# 包含负数时如何排序？对自定义的类型如何排序？
# 我们仅关心某一个元素出现了多少次，而并不关心相同元素的相对位置，那么看起来计数排序是一个不稳定排序，对吗？
# 如果数组中的最大元素的值很大时，会不会导致count数组太大，空间复杂度过高？

# 解决：
# 处理负数和自定义类型：通过简单映射技巧来处理负数和自定义类型；计数排序的映射函数的关键指标是不能丧失原数据的大小关系。
# 稳定性：通过在构建输出数组时，倒序遍历输入数组来保证稳定性。

# 在计数排序的代码中，没有类似其他排序中的交换元素操作，而是通过依靠数组索引的有序性，所以不用对元素进行比较。
# 将数据映射到count数组的索引上，这个映射关系保留了原数据的大小关系，又因为count数组索引是单调递增的，所以最后可以count数组推导出排序后的数组。

# 非比较排序
# 本质在于将原数据映射到一个自带有序性的参考系中(比如数组索引),然后借助这个参考系推导出排序后的结果。
# 反之，如果待排序的数据不能找到这样一个映射和参考系，则无法使用非比较排序算法.


def counting_sort(nums):
    # 找到最大元素和最小元素
    # 计算索引偏移量和count数组大小
    min_val = min(nums)
    max_val = max(nums)
    offset = -min_val
    count_size = max_val - min_val + 1
    count = [0] * count_size
    # 统计每个元素出现的次数
    for num in nums:
        count[num + offset] += 1
    # 累加count数组，得到的是nums[i]在排序后的数组中的结束位置
    for i in range(1, count_size):
        count[i] += count[i - 1]
    
    # 根据每个元素排序后的索引位置，完成排序
    # 倒序遍历保证稳定性
    sorted_nums = [0] * len(nums)
    for i in range(len(nums) -1 , -1 , -1):
        sorted_nums[count[nums[i]+offset] - 1] = nums[i]
        count[nums[i]+offset] -= 1
    
    # 把排序后的结果拷贝回原数组
    for i in range(len(nums)):
        nums[i] = sorted_nums[i]

# 测试
if __name__ == "__main__":
    arr = [4, 2, -3, 6, 1, 0, -2, 4, 3, 2]
    counting_sort(arr)
    print(arr)  # 输出: [-3, -2, 0, 1, 2, 2, 3, 4, 4, 6]