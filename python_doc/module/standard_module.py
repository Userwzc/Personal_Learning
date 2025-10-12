# 变量 sys.path 是字符串列表，用于确定解释器的模块搜索路径。
# 该变量以环境变量 PYTHONPATH 提取的默认路径进行初始化，
# 如未设置 PYTHONPATH，则使用内置的默认路径。可以用标准列表操作修改该变量：
import sys
sys.path.append('/ufs/guido/lib/python')

