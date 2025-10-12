import math
print(f'the value of pi is {math.pi:.3f}')

table = {'Sjoerd':4127, 'Jack':4098, 'Dcab':7678}
for name, phone in table.items():
  print(f'{name:10} ==> {phone:10d}')
  
# 修饰符可以在格式化前转换值 '!a' 应用 ascii() ，'!s' 应用 str()，'!r' 应用 repr()：
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')

# = 说明符可被用于将一个表达式扩展为表达式文本、等号再加表达式求值结果的形式
bugs = 'roaches'
count = 13
area = 'living room'
print(f"Debugging {bugs=}, {count=}, {area=}")

# 字符串format()方法
print('We are the {} who say "{}!"'.format('Knights', 'Ni'))
print('{0} and {1}'.format('Spam', 'eggs'))
print('{1} and {0}'.format('Spam', 'eggs'))
# 使用关键字参数名引用值
print('This {food} is {adjective}.'.format(food='spam', adjective = 'absolutely horrible'))
# 位置参数和关键字参数可以任意组合
print('The story of {0} and {1}, and {other}.'.format('Bill', 'Ted', other = 'Genghis Khan'))

# 如果不想分拆较长的格式字符串，最好按名称引用变量进行格式化，不要按位置。这项操作可以通过传递字典，并用方括号 '[]' 访问键来完成
table = {'Sjoerd':4127, 'Jack':4098, 'Dcab':7678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

# 这也可以通过将 table 字典作为采用 ** 标记的关键字参数传入来实现
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# 与内置函数 vars() 一同使用时这种方式非常实用，它将返回一个包含所有局部变量的字典
table = {k : str(v) for k, v in vars().items()}
print(table)
message = " ".join([f'{k}:' + '{' + k + '};' for k in table.keys()])
print(message.format(**table))

for x in range(1,11):
  print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
  
for x in range(1,11):
  print(repr(x).rjust(2), repr(x*x).rjust(3),end= ' ')
  print(repr(x*x*x).rjust(4))
  
#  str.zfill() ，该方法在数字字符串左边填充零，且能识别正负号
print('42'.zfill(5))
print('-3.14'.zfill(7))