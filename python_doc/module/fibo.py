def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
    
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
  
# 可以用以下方式运行 Python 模块：
# python fibo.py <arguments>
# 这项操作将执行模块里的代码，和导入模块一样，但会把 __name__ 赋值为 "__main__"。 也就是把下列代码添加到模块末尾：
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
# 这个文件既能被用作脚本，又能被用作一个可供导入的模块，因为解析命令行参数的那两行代码只有在模块作为“main”文件执行时才会运行：
# python fibo.py 50
# sys.argv[0] 是脚本的名称，sys.argv[1] 是第一个参数（在这里是 50）。如果没有提供参数，程序会报错。



