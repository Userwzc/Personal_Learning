# 生成器中 try/finally 能在被垃圾回收或 close() 时清理
def gen():
    try:
        yield 1
        yield 2
    finally:
        print("cleanup")

g = gen()
print(next(g))
g.close()

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b 

from itertools import islice,chain
print(list(islice(fib(), 10)))

# 创建一个生成器表达式，生成 0~9 的平方
data = (i*i for i in range(10))
# 使用 chain 将 999 和 data 连接起来，然后用 islice 取前 4 个元素
print(list(islice(chain([999], data), 4)))  