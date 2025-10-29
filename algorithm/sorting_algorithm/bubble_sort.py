# 冒泡排序
# 拥有稳定性

def bubble_sort(arr):
    n = len(arr)
    sortedIndex = 0
    while(sortedIndex < n):
        # 寻找nums[sortedIndex,n-1]中的最小值
        # 同时将这个最小值逐步移动到nums[sortedIndex]位置
        swapped = False  # 用于优化，如果一趟下来没有发生交换，说明数组已经有序，可以提前结束
        for i in range(n - 1, sortedIndex, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        if not swapped:
            break
        sortedIndex += 1
    return arr

if __name__ == "__main__":
    l = [5, 3, 8, 6, 2]
    print(bubble_sort(l))