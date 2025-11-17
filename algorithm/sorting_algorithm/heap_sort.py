# 堆排序
# 一句话总结:
# 堆排序是从二叉堆结构衍生出来的排序算法，复杂度为O(NlogN).
# 堆排序主要分两步，第一步是在待排序数组上原地创建二叉堆(Heapify)，然后进行原地排序(sort).

def max_heap_swim(arr, index):
    while index > 0 and arr[index] > arr[(index - 1) // 2]:
        arr[index], arr[(index - 1) // 2] = arr[(index - 1) // 2], arr[index]
        index = (index - 1) // 2

def max_heap_sink(arr, index, heap_size):
    while 2 * index + 1 < heap_size or 2 * index + 2 < heap_size:
        max_index = index
        if 2 * index + 1 < heap_size and arr[2 * index + 1] > arr[max_index]:
            max_index = 2 * index + 1
        if 2 * index + 2 < heap_size and arr[2 * index + 2] > arr[max_index]:
            max_index = 2 * index + 2
        if max_index == index:
            break
        arr[index], arr[max_index] = arr[max_index], arr[index]
        index = max_index

def sort(arr):
    n = len(arr)
    # 优化：从最后一个非叶子节点开始，依次下沉，合并二叉堆
    # 利用性质：对于一个二叉堆来说，其左右子堆也是一个二叉堆
    # 给我两个二叉堆，和一个根节点，怎么把它们合并成一个二叉堆？ 左右子树已经符合堆的性质了，只需要处理根节点
    # 利用sink操作，把根节点下沉到合适位置，就能让这个新二叉堆符合堆的性质了
    # 每个单独的叶子节点都是符合堆的性质的，所以上述代码从最后一个非叶子节点开始，
    # 依次调用 max_heap_sink 方法，合并所有的子堆，最终整个数组就是一个大顶堆了。
    for i in range(n//2 - 1, -1, -1):
        max_heap_sink(arr, i, n)

    # for i in range(n):
    #     max_heap_swim(arr, i)
    while n > 0:
        # 从堆顶删除元素，放到堆的后面
        arr[0], arr[n - 1] = arr[n - 1], arr[0]
        n -= 1
        # 恢复堆的性质
        max_heap_sink(arr, 0, n)
        # 现在 arr[0:n) 是一个大顶堆，arr[n:] 是排好序的部分

        # 堆排序是不稳定的，因为二叉堆本质上把数组结构抽象成了二叉树结构，在二叉树逻辑结构上的元素交换操作映射回数组上，
        # 无法顾及相同元素的相对位置。

if __name__ == "__main__":
    arr = [3,5,1,2,4,8,7,6]
    sort(arr)
    print(arr)
