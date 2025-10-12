import os 
print(os.getcwd())  # 获取当前工作目录
os.chdir('/home/wzc/Workspace/Python/python_doc') # 修改当前工作目录
os.system('ls')  # 执行系统命令

# 内置的dir()和help()函数可用于交互式辅助工具
# print(dir(os))  # 列出 os 模块的所有属性和方法
# print(help(os)) # 查看 os 模块的帮助文档

# 对于日常文件和目录管理任务，shutil 模块提供了更高级的接口
import shutil
shutil.copyfile('new.txt','new_copy.txt')
shutil.move('new_copy.txt','a.txt')