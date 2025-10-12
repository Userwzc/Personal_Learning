# 内置函数 dir() 用于查找模块定义的名称。
# 返回结果是经过排序的字符串列表：
import fibo, sys
print(dir(fibo))
print(dir(sys))

# 没有参数时，dir() 列出当前已定义的名称：
fib = fibo.fib
print(dir())
# 注意它列出所有类型的名称：变量，模块，函数，……。

# dir() 不会列出内置函数和变量的名称。这些内容的定义在标准模块 builtins 中：
import builtins
print(dir(builtins))
