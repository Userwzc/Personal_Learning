import fibo

fibo.fib(1000)
print(fibo.fib2(100))

print(fibo.__name__) # 访问模块的名称

# 如果经常使用某个函数，可以把它赋值给局部变量
fib = fibo.fib
fib(500)

