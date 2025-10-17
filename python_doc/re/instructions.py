# re模块
import re
# 1.常用匹配方式
## 直接搜索：re.search(pattern, text) 返回第一个匹配
## 查找全部：re.findall(pattern, text) 返回所有匹配列表
## 替换： re.sub(pattern, repl, text)
## 预编译: p = re.compile(pattern) 然后用p.search(...) 在多次重复匹配时更高效

# 2，核心元字符
## . : 匹配任意单个字符（默认不含换行）
## ^/$ : 匹配字符串开头/结尾
## * / + / ? : 分别表示前一个字符出现0次或多次/1次或多次/0次或1次
## {m, n} : 前一个字符出现m到n次, {m}表示出现m次, {m,}表示至少出现m次
## [] :字符集, 如[abc],[0-9],[A-Za-z_]
## | : 或操作符, 如cat|dog匹配cat或dog
## () :分组; (?:...) 非捕获分组; (?P<name>...) 命名捕获分组
## \d \w \s : 数字/单词字符/空白; 相对的\D \W \S表示非数字/非单词字符/非空白
## \b :单词边界; \B ：非单词边界
## 转义: 需要匹配字面量. ？等，用\转义; python里的r''字符串表示原始字符串，不需要转义 例如r'\n'表示两个字符\和n，而不是换行符

# 3.常见用例
## 提取邮箱地址
def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(?:\.[a-zA-Z0-9-]+)+'
    return re.findall(pattern, text)