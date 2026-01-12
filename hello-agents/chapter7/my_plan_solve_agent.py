from hello_agents import PlanAndSolveAgent, Config, Message
from hello_agents.core.llm import HelloAgentsLLM
from typing import Optional, Dict, List
import ast

# 默认规划器提示词模板
DEFAULT_PLANNER_PROMPT = """
你是一个顶级的AI规划专家。你的任务是将用户提出的复杂问题分解成一个由多个简单步骤组成的行动计划。
请确保计划中的每个步骤都是一个独立的、可执行的子任务，并且严格按照逻辑顺序排列。
你的输出必须是一个Python列表，其中每个元素都是一个描述子任务的字符串。

问题: {question}

请严格按照以下格式输出你的计划:
```python
["步骤1", "步骤2", "步骤3", ...]
```
"""

# 默认执行器提示词模板
DEFAULT_EXECUTOR_PROMPT = """
你是一位顶级的AI执行专家。你的任务是严格按照给定的计划，一步步地解决问题。
你将收到原始问题、完整的计划、以及到目前为止已经完成的步骤和结果。
请你专注于解决"当前步骤"，并仅输出该步骤的最终答案，不要输出任何额外的解释或对话。

# 原始问题:
{question}

# 完整计划:
{plan}

# 历史步骤与结果:
{history}

# 当前步骤:
{current_step}

请仅输出针对"当前步骤"的回答:
"""

class Planner:
    def __init__(self, llm_client: HelloAgentsLLM, prompt_template: Optional[str] = None):
        self.llm_client = llm_client
        self.prompt_template = prompt_template if prompt_template else DEFAULT_PLANNER_PROMPT
    def plan(self, question: str, **kwargs) -> List[str]:
        prompt = self.prompt_template.format(question=question)
        response = self.llm_client.invoke([{"role": "system", "content": prompt}], **kwargs)
        try:
            plan_str = response.split("```python")[1].split("```")[0].strip()
            plan = ast.literal_eval(plan_str)
            if isinstance(plan, list):
                return plan
            else:
                return []
        except (ValueError, SyntaxError, IndexError) as e:
            print(f"❌ 解析计划时出错: {e}")
            print(f"原始响应: {response}")
            return []
        except Exception as e:
            print(f"❌ 解析计划时发生未知错误: {e}")
            return []
        
class Executor:
    def __init__(self, llm_client: HelloAgentsLLM, prompt_template: Optional[str] = None):
        self.llm_client = llm_client
        self.prompt_template = prompt_template if prompt_template else DEFAULT_EXECUTOR_PROMPT
    
    def execute(self, question: str, plan: list, **kwargs) -> str:
        history = []
        for step in plan:
            history_str = "\n".join([f"步骤: {h[0]}\n结果: {h[1]}" for h in history])
            prompt = self.prompt_template.format(
                question=question,
                plan=plan,
                history=history_str,
                current_step=step
            )
            response = self.llm_client.invoke([{"role": "system", "content": prompt}], **kwargs)
            history.append((step, response))
            print(f"✅ 完成步骤: {step}\n结果: {response}\n")
        final_answer = history[-1][1] if history else "未能完成任何步骤。"
        return final_answer
        
class MyPlanAndSolveAgent(PlanAndSolveAgent):
    """  
    重写的计划与执行Agent
    """
    def __init__(
        self,
        name: str,
        llm: HelloAgentsLLM,
        system_prompt: Optional[str] = None,
        config: Optional[Config] = None,
        custom_prompts: Optional[Dict[str, str]] = None
    ):
        super().__init__(name, llm, system_prompt, config)
        planner_prompt = custom_prompts.get("planner") if custom_prompts and "planner" in custom_prompts else DEFAULT_PLANNER_PROMPT
        executor_prompt = custom_prompts.get("executor") if custom_prompts and "executor" in custom_prompts else DEFAULT_EXECUTOR_PROMPT
        self.planner = Planner(llm, planner_prompt)
        self.executor = Executor(llm, executor_prompt)

    def run(self, input_text: str, **kwargs) -> str:
        """  
        重写的运行方法 - 实现计划与执行逻辑
        """
        print(f"\n{self.name} 开始处理问题: {input_text}")

        # 1. 生成计划
        plan = self.planner.plan(input_text, **kwargs)
        if not plan:
            error_msg = "❌ 未能生成有效的计划。"
            print(error_msg)
            return error_msg

        print(f"✅ 计划生成成功: {plan}")

        # 2. 执行计划
        final_answer = self.executor.execute(input_text, plan, **kwargs)

        # 3. 记录对话历史
        self.add_message(Message(content=input_text, role="user"))
        self.add_message(Message(content=final_answer, role="assistant"))

        print(f"{self.name} 完成问题处理。最终答案: {final_answer}")
        return final_answer
        