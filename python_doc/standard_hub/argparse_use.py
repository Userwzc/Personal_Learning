# 核心概念
# 参数解析器: parse = argparse.ArgumentParser() 创建解析器对象
# 声明参数： parse.add_argument()  定义位置参数和可选参数
# 解析参数: args = parse.parse_args() 获取解析后的命名空间
# 自动帮助：内置的 -h/--help 选项显示帮助信息

# 最小示例
import argparse
parser = argparse.ArgumentParser(description="示例参数解析器")
parser.add_argument("path", help="文件路径")  # 位置参数
parser.add_argument("-o", "--output", help="输出文件路径" )  # 可选参数
parser.add_argument("-v", "--verbose", action="count", default=0, help="增加日志级别，可叠加使用如-vv")
args = parser.parse_args()
print(f"path={args.path}, output={args.output}, verbose={args.verbose}")

# 常用参数选项
# help:帮助文本
# type:转换类型，如int,float,Path（需from pathlib import Path）
# choices:限制可选值，如choices=['red','green','blue']
# default:默认值,与required=True互斥(对可选参数)
# required:是否必须提供(对可选参数)
# nargs:参数个数，如nargs='*'任意个，nargs='+'至少一个，nargs=3固定三个，nargs='?'可选一个
# action:行为控制:
#  store_true/false:存储布尔值
#  append: 重复出现累加到列表(如 -t val1 -t val2 变成 ['val1','val2'])
#  count: 计算出现次数(如 -vvv 变成 3)
# metavar: 用于帮助信息中显示的占位符名, 如metavar='FILE'
# dest: 指定存入args的属性名, 如dest='filename'

# 多功能CLI示例
# import argparse

# parser = argparse.ArgumentParser(prog="tool")
# subparsers = parser.add_subparsers(dest="cmd", required=True)  # 子命令解析器

# p_run = subparsers.add_parser("run", help="运行任务")
# p_run.add_argument("--steps", type=int, default=1)

# p_init = subparsers.add_parser("init", help="初始化项目")
# p_init.add_argument("--template", choices=["basic", "pro"], default="basic")

# args = parser.parse_args()
# if args.cmd == "run":
#     print(f"run steps={args.steps}")
# elif args.cmd == "init":
#     print(f"init template={args.template}")
