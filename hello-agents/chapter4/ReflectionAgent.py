from llm import HelloAgentsLLM
from memory import Memory
from prompt import REFINE_PROMPT_TEMPLATE, REFLECT_PROMPT_TEMPLATE, INITIAL_PROMPT_TEMPLATE


class ReflectionAgent:
    def __init__(self, llm_client: HelloAgentsLLM, max_iterations: int = 3):
        self.llm_client = llm_client
        self.memory = Memory()
        self.max_iterations = max_iterations

    def run(self,task: str):
        print(f"\n--- 开始处理任务 ---\n任务: {task}")

        # 1.初始执行
        print("\n--- 正在进行初始尝试 ---")
        initial_prompt = INITIAL_PROMPT_TEMPLATE.format(task=task)
        initial_code = self.llm_client.think(messages=[{"role": "user", "content": initial_prompt}]) or ""
        self.memory.add_record("execution", initial_code)

        # 2.迭代循环：反思与优化
        for i in range(self.max_iterations):
            print(f"\n--- 第 {i+1}/{self.max_iterations} 轮迭代 ---")

            # a. 反思
            print("\n--- 正在进行代码反思 ---")
            last_code = self.memory.get_last_execution()
            reflect_prompt = REFLECT_PROMPT_TEMPLATE.format(task=task, code=last_code)
            feedback = self.llm_client.think(messages=[{"role": "user", "content": reflect_prompt}]) or ""
            self.memory.add_record("reflection", feedback)

            # b.检查是否需要停止
            if "无需改进" in feedback:
                print("\n--- 代码已达到最优，无需进一步改进 ---")
                break

            # c. 优化
            print("\n--- 正在进行代码优化 ---")
            refine_prompt = REFINE_PROMPT_TEMPLATE.format(task=task, last_code_attempt = last_code, feedback=feedback)
            refined_code = self.llm_client.think(messages=[{"role": "user", "content": refine_prompt}]) or ""
            self.memory.add_record("execution", refined_code)

        final_code = self.memory.get_last_execution()
        print(f"\n --- 任务完成 ---\n最终生成的代码:\n{final_code}")
        return final_code 
    
if __name__ == "__main__":
    llm_client = HelloAgentsLLM()
    agent = ReflectionAgent(llm_client=llm_client)

    # 示例任务：编写一个高效的函数来计算前N个素数
    task = "编写一个Python函数，找出1到n之间所有的素数 (prime numbers)。"
    agent.run(task=task)