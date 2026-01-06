from Planner import Planner
from Executor import Executor
from llm import HelloAgentsLLM

class PlanAndSolveAgent:
    def __init__(self, llm_client: HelloAgentsLLM):
        self.llm_client = llm_client
        self.planner = Planner(self.llm_client)
        self.executor = Executor(self.llm_client)

    def run(self, question: str):
        """  
        运行智能体的完整流程：先规划，后执行。
        """
        print(f"\n--- 开始处理问题 ---\n问题： {question}")

        # 1.调用规划器生成计划
        plan = self.planner.plan(question)
        if not plan:
            print("错误：未能生成有效的计划，流程终止。")
            return
        
        # 2.调用执行器根据计划逐步解决问题
        final_answer = self.executor.execute(question, plan)

        print(f"\n--- 智能体已完成任务 ---\n最终答案： {final_answer}")


if __name__ == '__main__':
    # 初始化LLM客户端
    llmClient = HelloAgentsLLM()

    # 初始化PlanAndSolve智能体
    agent = PlanAndSolveAgent(llmClient)

    # 运行智能体，处理一个示例问题
    sample_question = "一个水果店周一卖出了15个苹果。周二卖出的苹果数量是周一的两倍。周三卖出的数量比周二少了5个。请问这三天总共卖出了多少个苹果？"
    agent.run(sample_question)