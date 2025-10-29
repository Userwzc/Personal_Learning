# 选择排序
# 算法没有使用额外的数组空间进行辅助，只是用了几个变量，空间复杂度是O(1)
# 算法的时间复杂度是O(n^2)
# 算法是不稳定的排序算法
# 即使数组已经有序，算法的时间复杂度依然是O(n^2),原始数据的有序度对算法的时间复杂度没有任何影响

def selection_sort(arr):
    # sortedIndex 是一个分割线
    # 索引 < sortedIndex 的元素都是已排序的
    # 索引 >= sortedIndex 的元素都是未排序的
    # 初始化为 0，表示整个数组都是未排序的
    sortedIndex = 0
    while(sortedIndex < len(arr)):
        min_index = sortedIndex
        for i in range(sortedIndex + 1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i
        arr[sortedIndex], arr[min_index] = arr[min_index], arr[sortedIndex]
        sortedIndex += 1
    return arr


if __name__ == "__main__":
    l = [5, 3, 8, 6, 2]
    print(selection_sort(l))


