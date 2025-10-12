# tuple 
# immutable
# 可包含异质数据类型
# 定义方式：小括号() 或者逗号,
empty_tuple = ()
single_element_tuple = 32,
multi_element_tuple = (1, 2, 3, 4, 5)
print(empty_tuple)
print(single_element_tuple)
print(multi_element_tuple)

# set
# 空集合
empty_set = set()
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket) # membership test
# 运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)

print(a - b)     # letters in a but not in b
print(a | b)     # letters in a or b or both
print(a & b)     # letters in both a and b
print(a ^ b)     # letters in a or b but not both
# 集合推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# dict
# 字典的键是唯一的
# 定义方式：花括号{} 或者 dict()
empty_dict = {}
print(empty_dict)
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
print(tel)
tel['irv'] = 4127
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)

# 构造函数               可以直接使用键值对序列创建字典
d1= dict([('sape',4139), ('guido',4127), ('jack',4098)])

# 字典推导式
d2 = {x: x**2 for x in (2, 4, 6)}
print(d2)

# 关键字是比较简单的字符串时，直接用关键字指定键值对更方便
d3 = dict(sape=4139, guido=4127, jack=4098)
print(d3)


# tricks for loop
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# enumerate()可以同时获得索引和值
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 对逆向序列进行循环
for i in reversed(range(1, 10, 2)):
    print(i)

# 按指定顺序计算可以使用sorted()
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(basket, key = lambda x: x[-1]):
    print(f)

for f in sorted(set(basket)):
    print(f)

# 一般来说，在循环中修改列表的内容时，创建新列表比较简单，且安全：
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

filtered_data = [value for value in raw_data if not math.isnan(value)]
print(filtered_data)