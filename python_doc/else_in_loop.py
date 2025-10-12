# 在这两类循环中，当在循环被 break 终结时 else 子句 不会 被执行。 当然，其他提前结束循环的方式，如 return 或是引发异常，也会跳过 else 子句的执行
# 其中 else 子句属于 for 循环，而 不属于 if 语句
for n in range(2,10):
  for x in range(2,n):
    if n % x == 0:
      print(n, 'equals', x, '*', n//x)
      break
    
  else:
    # 循环到底未找到一个因数
    print(n, 'is a prime number')
    