from hello_agents import ReflectionAgent, Config, Message,HelloAgentsLLM
from typing import Optional

DEFAULT_PROMPTS = {
    "initial": """
请根据以下要求完成任务:

任务: {task}

请提供一个完整、准确的回答。
""",
    "reflect": """
请仔细审查以下回答，并找出可能的问题或改进空间:

# 原始任务:
{task}

# 当前回答:
{content}

请分析这个回答的质量，指出不足之处，并提出具体的改进建议。
如果回答已经很好，请回答"无需改进"。
""",
    "refine": """
请根据反馈意见改进你的回答:

# 原始任务:
{task}

# 上一轮回答:
{last_attempt}

# 反馈意见:
{feedback}

请提供一个改进后的回答。
"""
}

class memory:
    """
    简单的短期记忆模块，用于存储智能体的行动与反思轨迹。
    """
    def __init__(self):
        self.records = []

    def add_record(self, record_type: str, content: str):
        """向记忆中添加一条新记录"""
        self.records.append({"type": record_type, "content": content})
        print(f"📝 记忆已更新，新增一条 '{record_type}' 记录。")

    def get_trajectory(self) -> str:
        """将所有记忆记录格式化为一个连贯的字符串文本"""
        trajectory = ""
        for record in self.records:
            trajectory += f"{record['type'].upper()}:\n{record['content']}\n\n"
        return trajectory.strip()
    
    def get_last_execution(self) -> Optional[str]:
        """获取最近一次的执行结果"""
        for record in reversed(self.records):
            if record["type"] == 'execution':
                return record["content"]
        return None


class MyReflectionAgent(ReflectionAgent):
    """重写的反思Agent - 具备自我评估和改进能力的智能体"""
    def __init__(self,
        name: str,
        llm: HelloAgentsLLM,
        system_prompt: Optional[str] = None,
        config: Optional[Config] = None,
        max_iterations: int = 3,
        custom_prompts: Optional[dict] = None
    ):
        super().__init__(name, llm, system_prompt, config)
        self.max_iterations = max_iterations
        self.prompt_template = custom_prompts if custom_prompts else DEFAULT_PROMPTS

    def run(self, input_text: str, **kwargs) -> str:
        """运行反思Agent"""
        print(f"\n🤖 {self.name} 开始处理任务: {input_text}")

        self.memory = memory()

        # 1.构建初始提示词
        initial_prompt = self.prompt_template["initial"].format(task=input_text)
        initial_message = {"role": "user", "content": initial_prompt}
        response_text = self.llm.invoke([initial_message], **kwargs)
        self.memory.add_record("execution", response_text)
        for i in range(self.max_iterations):
            print(f"\n--- 第 {i+1}/{self.max_iterations} 轮反思与改进 ---")

            # a. 反思
            last_execution = self.memory.get_last_execution()
            reflect_prompt = self.prompt_template["reflect"].format(
                task=input_text,
                content=last_execution
            )
            reflect_message = {"role": "user", "content": reflect_prompt}
            feedback = self.llm.invoke([reflect_message], **kwargs)
            self.memory.add_record("reflection", feedback)

            # b.检查是否需要停止
            if "无需改进" in feedback:
                print("\n✅ 回答已达到最优，无需进一步改进。")
                break

            # c. 优化
            refine_prompt = self.prompt_template["refine"].format(
                task=input_text,
                last_attempt=last_execution,
                feedback=feedback
            )
            refine_message = {"role": "user", "content": refine_prompt}
            refined_response = self.llm.invoke([refine_message], **kwargs)
            self.memory.add_record("execution", refined_response)
        
        final_response = self.memory.get_last_execution()
        print(f"\n🎉 任务完成！最终回答:\n{final_response}")

        self.add_message(Message(content=input_text, role="user"))
        self.add_message(Message(content=final_response, role="assistant"))
        return final_response


