# 博采众长: 桶排序
# 一句话总结:
# 算法核心思想分三步:
# 1.将待排序数组中的元素使用映射函数分配到若干个[桶]中
# 2.对每个桶中的元素进行排序
# 3.最后将这些排好序的桶进行合并，得到排序结果

# 核心步骤：
# 1.如何将待排序元素分配到桶中？你需要决定桶的数量，并提供一个映射函数
# 2.如何对每个桶中的元素进行排序？
# 3.如何将排好序的桶合并起来？

# 数学基础：分开排序的时间复杂度总和是小于整体排序的
# 如果桶排序将待排序元素分配到尽可能多的桶中(k尽可能大),即每个桶至多只有一个元素时，桶排序就转化为了计数排序，复杂度也降到O(n)

# 使用插入排序的桶排序

def bucket_sort(nums: list[int], bucket_count: int = None) -> list[int]:
    if len(nums) < 2:
        return nums

    min_val = min(nums)
    max_val = max(nums)
    if min_val == max_val:
        return nums

    if bucket_count is None:
        bucket_count = len(nums)//2 + 1  # 默认桶数为数组长度的一半或相等

    # 初始化桶
    buckets = [[] for _ in range(bucket_count)]
    #  将元素放入对应的桶中
    for num in nums:
        index = int((num - min_val) / (max_val - min_val) * bucket_count)
        if index == bucket_count:
            index -= 1
        buckets[index].append(num)

    # 对每个桶进行排序（这里使用插入排序）
    # 同时合并回原数组
    index = 0
    for i in range(bucket_count):
        insert_sort(buckets[i])
        for num in buckets[i]:
            nums[index] = num
            index += 1
    
    return nums

def insert_sort(arr: list[int]) -> list[int]:
    sorted_index = 1
    while sorted_index < len(arr):
        for i in range(sorted_index, 0 , -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
            else:
                break
        sorted_index += 1
    return arr

def bucket_sort_recursive(nums: list[int], bucket_count: int):
    # 1. 基准条件：元素少于2个，自然有序，无需排序
    if len(nums) < 2:
        return
    
    min_val = min(nums)
    max_val = max(nums)
    
    # 2. 如果所有元素都相同，直接返回（避免除以0错误，也避免死循环）
    if min_val == max_val:
        return

    # 初始化桶
    buckets = [[] for _ in range(bucket_count)]
    
    # 3. 修正桶索引计算公式
    # 使用 (num - min) * k // (max - min) 可以将数据均匀映射到 0 到 k-1
    # 这是一个更稳健的映射方式，避免了人为 +1 造成的分布扭曲
    range_val = max_val - min_val
    for num in nums:
        # 注意：这里使用 (bucket_count) 作为乘数
        index = int((num - min_val) * bucket_count / range_val)
        
        # 边界处理：max_val 会计算出 index == bucket_count，需要放到最后一个桶
        if index == bucket_count:
            index -= 1
            
        buckets[index].append(num)

    # 4. 递归排序每个桶
    # 5. 合并回原数组
    index = 0 
    for bucket in buckets:
        # 优化：如果某个桶里的元素数量就是原数组的长度，说明分布失败（所有元素都在一个桶）
        # 此时必须换策略（如减少 bucket_count 或改用其他排序），否则会死循环。
        # 但上面的公式保证了只要 min != max，元素至少会分到两个不同的逻辑区间（除非 bucket_count=1）。
        if len(bucket) == len(nums):
             # 这种情况通常只发生在 bucket_count=1 时。
             # 此时无法使用递归桶排序解决，必须直接排序。
             bucket.sort() 
        else:
            bucket_sort_recursive(bucket, bucket_count)
            for num in bucket:
                nums[index] = num
                index += 1


# 稳定性
# 桶排序的稳定性主要取决于对每个桶的排序算法
# 首先，分配元素到k个桶的过程中，我们是按顺序遍历nums数组的，所有相同元素必然会被分到同一个桶中，且在桶中的相对顺序不会改变。
# 最后一步合并多个桶的过程中，我们是按顺序遍历桶中的元素，所以排序稳定性主要取决于对每个桶的排序算法。
# 如果对每个桶的元素使用插入排序，因为插入排序是稳定排序，所以排序过程中相同元素的相对顺序也不会改变。因此整个桶排序算法是稳定的。

# 如果对当前桶递归地使用桶排序，那么当前桶的元素分配到新的桶中时，相同元素的相对顺序也不会改变，以此类推，最终的排序结果也没有改变相同元素的相对位置，所以排序结果也是稳定的。

# 时空复杂度分析
# 空间复杂度： O(n + k)
# 时间复杂度: 均摊时间复杂度为O(n + k),最坏时间复杂度为O(n^2)（当所有元素都被分配到同一个桶中时）


if __name__ == "__main__":
    arr = [3, 6, 2, 8, 4, 5, 7, 1]
    sorted_arr = bucket_sort(arr, 8)
    print(sorted_arr)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8]
    arr2 = [3, 6, 2, 8, 4, 5, 7, 1]
    bucket_sort_recursive(arr2, 4)
    print(arr2)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8]