# 希尔排序：突破O(n^2)

# 希尔排序是基于插入排序的简单改进，通过预处理增加数组的局部有序性，突破了插入排序的O(n^2)的时间复杂度。
# 首先要明确一个h有序数组的概念
# 一个数组是h有序的，是指当这个数组中的任意间隔为h(或者说间隔元素的个数为h-1)的元素都是有序的。
# 按照这个定义，当一个数组完成排序时，其实就是1有序数组。

def shell_sort(arr):
    n = len(arr)
    h = 1
    while h < n / 3:
        h = 3 * h + 1  # 生成初始的h值，使用Knuth增量序列

    # 改动一：把插入排序的主要逻辑套在h的while循环中
    while h >= 1:
        # 改动二：sortedIndex初始为h,而不是0
        sortedIndex = h
        # 下面让数组变成h有序数组
        while sortedIndex < n:
            i = sortedIndex
            # 改动三：把比较和交换元素的步长设置为h
            while i >= h:
                if arr[i] < arr[i - h]:
                    arr[i], arr[i - h] = arr[i - h], arr[i]
                else:
                    break
                i -= h
            sortedIndex += 1
        h = h // 3 # 更新h值
    return arr

if __name__ == "__main__":
    l = [5, 3, 8, 6, 2, 7, 4, 1]
    print(shell_sort(l))
    # 希尔排序是不稳定的排序算法
    # 希尔排序的空间复杂度是O(1)，是原地排序算法
    # 希尔排序的性能和递增函数的选择有很大关系,主要修改h的初始化和更新逻辑