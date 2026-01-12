# test_reflection_agent.py
from dotenv import load_dotenv
from hello_agents import HelloAgentsLLM
from my_reflection_agent import MyReflectionAgent

load_dotenv()

llm = HelloAgentsLLM()

# 使用默认通用提示词
general_agent = MyReflectionAgent(name="我的反思助手", llm=llm)

# 使用自定义代码生成提示词（类似第四章）
code_prompts = {
    "initial": "你是写作专家，请根据任务进行写作:{task}",
    "reflect": "请审查写作的内容是否需要优化:\n任务:{task}\n内容:{content}",
    "refine": "请根据反馈优化写作内容:\n任务:{task}\n上一轮回答:{last_attempt}\n反馈:{feedback}"
}
code_agent = MyReflectionAgent(
    name="我的代码生成助手",
    llm=llm,
    custom_prompts=code_prompts
)

# 测试使用
result = general_agent.run("写一篇关于人工智能发展历程的简短文章")
print(f"最终结果: {result}")
