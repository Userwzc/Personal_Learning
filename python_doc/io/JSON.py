import json
# 标准库模块 json 可以接受带有层级结构的 Python 数据，并将其转换为字符串表示形式；这个过程称为 serializing
# 根据字符串表示形式重建数据则称为 deserializing
x = [1,'simple', 'list']
json_x = json.dumps(x)
print(json_x)
print(type(json_x))

# dumps() 函数还有一个变体， dump() ，它只将对象序列化为 text file 。因此，如果 f 是 text file 对象，可以这样做
# JSON文件必须以UTF-8编码。当打开JSON文件作为一个 text file 用于读写时，使用 encoding="utf-8"
f = open('data.json', 'r+', encoding="utf-8")
json.dump(x,f)      # 将数据写入文件，此时文件指针移动到了文件末尾
f.seek(0)
x = json.load(f)
print(x)
print(type(x))