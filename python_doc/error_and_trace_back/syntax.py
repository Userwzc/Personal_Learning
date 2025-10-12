# while True:
#     try:
#         x = int(input("请输入一个整数: "))
#         break
#     except (ValueError,RuntimeError,NameError):
#         print("Ops! 你输入的不是一个整数，请重新输入。")
        
# 注意，用户中断程序会触发 KeyboardInterrupt 异常
# try 语句的工作原理如下：

# 首先，执行 try 子句 （try 和 except 关键字之间的（多行）语句）。
# 如果没有触发异常，则跳过 except 子句，try 语句执行完毕。
# 如果在执行 try 子句时发生了异常，则跳过该子句中剩下的部分。 
# 如果异常的类型与 except 关键字后指定的异常相匹配，则会执行 except 子句，然后跳到 try/except 代码块之后继续执行。
# 如果发生的异常与 except 子句 中指定的异常不匹配，则它会被传递到外层的 try 语句中；
# 如果没有找到处理器，则它是一个未处理异常 且执行将停止并输出一条错误消息。

# 可以有多个 except 子句 来为不同的异常指定处理程序。 但最多只有一个处理程序会被执行
#  处理程序只处理对应的 try 子句 中发生的异常，而不处理同一 try 语句内其他处理程序中的异常。 
#  except 子句 可以用带圆括号的元组来指定多个异常
# 例如：
# except (RuntimeError, TypeError, NameError): pass

class B(Exception):
    pass

class C(B):
    pass

class D(C):
	pass

for cls in [B, C, D]:
	try:
		raise cls()
	except D:
		print("D")
	except C:
		print("C")
	except B:
		print("B")
  
# 输出  D C B
# 一个 except 子句中的类匹配的异常将是该类本身的实例或其所派生的类的实例
# 注意如果颠倒 except 子句 的顺序（把 except B 放在最前），则会输出 B, B, B --- 即触发了第一个匹配的 except 子句

try:
    raise Exception('spam','eggs')
except Exception as inst:
    print(type(inst))    # inst 是一个异常实例
    print(inst.args)    # 实例的参数
    print(inst)        # __str__ 允许args被直接打印 但可能在异常子类中被覆盖
    x, y = inst.args    #解包args
    print(f'{x=}, {y=}')