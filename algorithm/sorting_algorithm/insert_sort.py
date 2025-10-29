# 插入排序
# 插入排序是基于选择排序的一种优化，将nums[sortedIndex]插入到左侧的有序数组中，对于有序度较高的数组，插入排序的效率比较高
# 反向思维：在nums[0..sortedIndex-1]中寻找合适的位置插入nums[sortedIndex]

def insert_sort(arr):
    n = len(arr)
    sortedIndex = 0 # 维护nums[0..sortedIndex)为有序区间
    while(sortedIndex < n):
        # 将nums[sortedIndex]插入到nums[0..sortedIndex-1]中合适的位置
        for i in range(sortedIndex, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
            else:
                break
        sortedIndex += 1
    return arr

if __name__ == "__main__":
    l = [5, 3, 8, 6, 2]
    print(insert_sort(l))
    # 稳定排序，初始有序度越高，效率越高
    # 插入排序的综合性能应该要高于冒泡排序