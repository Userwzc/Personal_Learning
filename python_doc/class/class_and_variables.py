class Dog:

    kind = 'canine' # 类变量被所有实例共享
    # tricks = []    # 类变量的错误用法

    def __init__(self, name):
        self.name = name  # 实例变量为每个实例所独有
        self.tricks = []  # 正确的用法：每个实例有自己的列表
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)

# 共享数据可能在涉及 mutable 对象例如列表和字典的时候导致令人惊讶的结果

d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)
