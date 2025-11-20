# 基数排序
# 一句话总结：
# 基数排序是计数排序算法的扩展，它的主要思路是对待排序元素的每一位依次进行计数排序。
# 由于计数排序是稳定的，所以对每一位完成计数排序后，所有元素就完成了排序。

# 基数(Radix)其实就是进制的意思，比如十进制的基数就是10，二进制的基数就是2.
# 看这个名字就知道这个排序算法肯定和数字的进制有关，进而可以推断，这个算法不是通用排序算法
# 待排序数据必须是整数，或者能够通过某种规则转化成整数，才能使用基数排序。

# 为什么对每一位必须使用稳定排序？
# 比如56，57已经按个位数排序完毕，56在57前面，使用不稳定排序可能会把57放在56前面

# 使用什么稳定排序比较好？
# 对于基数排序的场景，十进制的数字只有0-9共10个不同的取值，所以使用计数排序是最合适的。O(n+10)=O(n)

# 位数不同怎么办？、
# 位数不同的数字，可以在高位补0，比如9可以看成09，001等

# 有负数怎么办？
# 使用偏移量 ,完成排序后再减去偏移量即可

# 必须从低位到高位吗?
# 低到高(Least Significant Digit, LSD)和高到低(Most Significant Digit, MSD)
# MSD的主要应用场景是字典序排序，其排序算法需要用到递归，和LSD有较大差异。

def radix_sort(nums):
    if len(nums) < 2:
        return 
    min_val = min(nums)
    max_val = max(nums)
    if min_val == max_val:
        return
    offset = -min_val
    for num in nums:
        num += offset
    
    max_len = 0
    while max_val > 0:
        max_val //= 10
        max_len += 1
    
    for k in range(max_len):
        counting_sort(nums, k)
        
    for num in nums:
        num -= offset
    
    
def counting_sort(nums, k):
    count = [0] * 10
    for num in nums:
        digit = (num // (10 ** k)) % 10
        count[digit] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    sorted_nums = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        digit = (nums[i] // (10 ** k)) % 10
        sorted_nums[count[digit] - 1] = nums[i]
        count[digit] -= 1
    
    for i in range(len(nums)):
        nums[i] = sorted_nums[i]
        
# 时间复杂度: O(d*(n+b))，d是数字的最大位数，b是基数，这里是10
# 空间复杂度: O(n+b)        


if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(arr)
    print(arr)  # [2, 24, 45, 66, 75, 90, 170, 802]