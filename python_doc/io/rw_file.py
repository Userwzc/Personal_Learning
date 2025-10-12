# -*- coding: utf-8 -*-
# open() 返回一个 file object ，最常使用的是两个位置参数和一个关键字参数：open(filename, mode, encoding=None)
# mode 的值包括 'r' ，表示文件只能读取；'w' 表示只能写入（现有同名文件会被覆盖）；'a' 表示打开文件并追加内容，任何写入的数据会自动添加到文件末尾。
# 'r+' 表示打开文件进行读写。mode 实参是可选的，省略时的默认值为 'r'

#  UTF-8 是现代事实上的标准，除非你知道你需要使用一个不同的编码，否则建议使用 encoding="utf-8" 。
# 在模式后面加上一个 'b' ，可以用 binary mode 打开文件。二进制模式的数据是以 bytes 对象的形式读写的。
# 在二进制模式下打开文件时，你不能指定 encoding 

# 在文本模式下读取文件时，默认把平台特定的行结束符（Unix 上为 \n, Windows 上为 \r\n）转换为 \n。在文本模式下写入数据时，默认把 \n 转换回平台特定结束符。
# 这种操作方式在后台修改文件数据对文本文件来说没有问题，但会破坏 JPEG 或 EXE 等二进制文件中的数据。
# 注意，在读写此类文件时，一定要使用二进制模式

# 在处理文件对象时，最好使用 with 关键字。优点是，子句体结束后，文件会正确关闭，即便触发异常也可以
# 这比使用 try-finally 语句块更简洁

with open('/home/wzc/Coding/Python/python_doc/io/workfile.txt', encoding='utf-8') as f:
  read_data = f.read()
  print(read_data)
  print(f.read())  # f.read(size),如已到达文件末尾，f.read() 返回空字符串（''）
# 我们可以检测文件是否已被自动关闭  
print(f.closed)

# f.readline() 从文件中读取单行数据；字符串末尾保留换行符（\n），只有在文件不以换行符结尾时，文件的最后一行才会省略换行符
# 这种方式让返回值清晰明确
# 只要 f.readline() 返回空字符串，就表示已经到达了文件末尾，空行使用 '\n' 表示，该字符串只包含一个换行符

f = open('/home/wzc/Coding/Python/python_doc/io/workfile.txt', encoding='utf-8')
print(f.readline())  # 读取第一行
print(f.readline())  # 读取第二行
print(f.readline())  # 读取第三行
f.close() # 关闭文件

f = open('/home/wzc/Coding/Python/python_doc/io/workfile.txt', encoding='utf-8')
for line in f:
  print(line,end='')  # end='' 防止换行符重复
print() # 解决%
f.close() 

# 如需以列表形式读取文件中的所有行，可以用 list(f) 或 f.readlines()
f = open('/home/wzc/Coding/Python/python_doc/io/workfile.txt', encoding='utf-8')
data = f.readlines()  # 返回一个列表，列表中的每个元素都是文件的一行
print(data)
f.close()
f = open('/home/wzc/Coding/Python/python_doc/io/workfile.txt', encoding='utf-8')
data =list(f)
print(data)
f.close()

# f.write(string) 把 string 的内容写入文件，并返回写入的字符数
f = open('new.txt', 'w', encoding='utf-8')
string = "Hello, World!"
num = f.write(string)
print(f"写入字符数: {num}")
f.close()

# f.tell() 返回整数，给出文件对象在文件中的当前位置，表示为二进制模式下时从文件开始的字节数，以及文本模式下的意义不明的数字
# f.seek(offset, whence) 可以改变文件对象的位置。通过向参考点添加 offset 计算位置；
# 参考点由 whence 参数指定。
# whence 值为 0 时，表示从文件开头计算，1 表示使用当前文件位置，2 表示使用文件末尾作为参考点。
# 省略 whence 时，其默认值为 0，即使用文件开头作为参考点
f = open('new.txt', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)
print(f.read(1))
f.seek(-3,2)         ## 在文本文件（模式字符串未使用 b 时打开的文件）中，只允许相对于文件开头搜索 ##
print(f.read(1))
f.close()

f = open('/home/wzc/Coding/Python/python_doc/io/workfile.txt', 'r+', encoding='utf-8')
f.write('0123456789abcdef')
f.seek(5)
print(f.read(1))
print(f.tell())
f.seek(0,2) # 使用 seek(0, 2) 搜索到文件末尾是个例外），唯一有效的 offset 值是能从 f.tell() 中返回的，或 0。其他 offset 值都会产生未定义的行为。
print(f.read(1))