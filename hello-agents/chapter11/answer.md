# 第11章 习题参考答案

## 1. 从 LLM 训练到 Agentic RL

### 11.1 Agentic RL vs PBRFT (基于偏好的强化微调)

#### 1. 状态空间差异分析 (11.1.3 节)

**问题：** 为什么 Agentic RL 的状态空间 $s_t = (prompt, o_1, o_2, ..., o_t)$ 包含历史观察，而 PBRFT 的状态 $s_0 = prompt$ 只包含初始提示？

**深入解释：**

*   **PBRFT (Preference-Based Reinforcement Fine-Tuning)** 通常被建模为 **Contextual Bandit (上下文赌博机)** 问题，或者是单步的 MDP。在这种设定下，模型（Agent）根据初始的 Context (Prompt) 生成一个完整的回答 (Action)，然后环境（人类或奖励模型）给予一个一次性的反馈 (Reward)。模型不需要与环境进行多轮交互，生成过程是一次性的，因此其状态仅需包含初始输入。
*   **Agentic RL** 则是在 **MDP (马尔可夫决策过程)** 框架下运行。智能体需要与环境进行多轮交互（例如：思考、调用工具、观察结果、再思考）。每一步的决策都依赖于之前的交互历史。
    *   $s_t$ 必须包含历史观察 $(o_1, ..., o_t)$，因为这些观察包含了环境对智能体之前动作的反馈（例如工具的输出、代码执行的报错信息）。
    *   如果状态只包含 $prompt$，智能体将无法感知当前任务的进度，也无法利用工具调用的结果，变成了"盲目"的生成。

**影响：**

*   **训练过程**：PBRFT 的训练更简单，类似于有权重的监督学习；Agentic RL 需要处理序列决策问题，面临信用分配（Credit Assignment）难题，即需要确定哪一步动作导致了最终的高分或低分。
*   **最终效果**：PBRFT 适合"一次性生成"任务（如写诗、翻译）；Agentic RL 赋予了模型**动态调整**和**自我纠错**的能力，能解决需要多步推理和外部信息交互的复杂任务（如代码调试、复杂数学题）。

#### 2. "智能代码调试助手"的 RL 映射

**场景**：分析代码 -> 查阅文档 -> 修改代码 -> 运行测试。

*   **状态空间 (State Space, $\mathcal{S}$)**:
    *   $s_t = (C_{orig}, B_{report}, H_t)$
    *   $C_{orig}$: 原始的有 bug 代码。
    *   $B_{report}$: Bug 报告或错误日志。
    *   $H_t$: 交互历史，包括之前的动作序列和观察结果（例如：已查阅的 API 文档内容、修改后的代码片段、测试运行的输出结果）。

*   **行动空间 (Action Space, $\mathcal{A}$)**:
    *   $a_{analyze}$: 生成自然语言分析（Thought）。
    *   $a_{doc}$: `lookup_doc(api_name)` 查阅文档。
    *   $a_{edit}$: `apply_edit(file_path, line_no, new_code)` 修改代码。
    *   $a_{test}$: `run_test(test_case_id)` 运行测试。
    *   $a_{finish}$: 提交修复并结束任务。

*   **奖励函数 (Reward Function, $R(s, a)$)**:
    *   **稀疏奖励（最终结果）**:
        *   $+10$: 所有测试用例通过。
        *   $-5$: 提交后仍有测试失败。
    *   **稠密奖励（过程引导）**:
        *   $-1$: 代码语法错误（Syntax Error）。
        *   $-0.1$: 每执行一步动作（时间步惩罚，鼓励快速解决）。
        *   $+0.5$: 成功定位到 bug 所在行（如果已知 ground truth）。
        *   $+0.2$: `run_test` 执行成功且输出信息发生变化（鼓励探索）。

*   **状态转移函数 (Transition Function, $T(s, a)$)**:
    *   环境根据动作 $a$ 更新状态。例如，执行 $a_{test}$ 后，环境返回测试结果 $o_{test}$，新的状态 $s_{t+1}$ 将包含这个测试结果。这是一个确定性或半随机的环境（取决于测试运行的稳定性）。

#### 3. 监督学习的局限 vs RL 的延迟奖励

**任务：** 证明数学不等式 "证明对于所有 $n \ge 3$， $2^n > 2n + 1$"。

**监督学习的局限：**
*   监督学习通常使用 "Teacher Forcing"，即在每一步都要求模型输出与训练数据完全一致的 "标准答案"。
*   **中间步骤僵化**：证明过程可能有多种路径（例如可以使用数学归纳法，也可以用求导分析函数单调性）。如果模型想尝试一种新颖但正确的证明路径，监督学习会认为它是"错误"的，因为它与数据集中的路径不符。
*   **误差累积**：一旦模型在中间某一步实际上是对的但与标签微小偏离，监督学习的 loss 会强行纠正，通过微调破坏模型的推理逻辑。

**RL 的优势（延迟奖励）：**
*   **延迟奖励**：RL 不关心中间步骤是否与某个人类写的步骤一模一样。
*   只要最终证明逻辑严密、结论正确，整个路径都会得到正向奖励（Reward）。
*   **Credit Assignment**：RL 算法（如 PPO/GRPO）会将最终的奖励回传给中间的关键步骤。模型可以探索出训练数据中未出现的、更简洁或更巧妙的证明步骤。

---

## 2. SFT 与 GRPO 核心方法

### 11.2 SFT 与 LoRA (11.2.4 节)

#### 1. LoRA (Low-Rank Adaptation) 分析

*   **核心思想**：冻结预训练模型的大部分权重 $W$，只在每一层旁边增加一个旁路分支，该分支由两个低秩矩阵 $A$ 和 $B$ 相乘组成（$\Delta W = B \cdot A$）。
    *   假设 $W$ 的维度是 $d \times d$，LoRA 的秩 $r \ll d$。
    *   前向传播时：$h = Wx + \Delta Wx = Wx + B(Ax)$。
*   **为什么高效**：
    *   参数量极少：$r$ 通常取 8, 16, 32 等，相比于 $d$ (如 4096)，需要训练的参数量只有全量的 0.1% 甚至更少。
    *   内存占用低：不需要存储全量参数的优化器状态（Optimizer States）。
*   **选择 LoRA 的时机**：
    *   显存资源受限（如在消费级显卡上训练）。
    *   需要为多个下游任务微调同一个大模型（可以快速切换 Adapter）。
    *   数据集较小，全参数微调容易过拟合（Catastrophic Forgetting）。
*   **选择全参数微调的时机**：
    *   拥有海量数据（如继续预训练）。
    *   希望彻底改变模型的基础能力或知识结构。

### 11.3 GRPO 算法 (11.3 节)

#### 2. GRPO vs PPO

*   **优势**：
    *   **去 Critic (Value Network)**：PPO 需要训练一个 Critic 网络来估计价值函数 $V(s)$，不仅增加显存开销，而且 Critic 的训练往往很难收敛。GRPO 不需要 Critic。
    *   **群组相对奖励 (Group Relative Reward)**：GRPO 对同一个 Prompt 采样一组输出 $\{o_1, o_2, ..., o_G\}$，计算这组输出的平均奖励作为 Baseline。$Advantage_i = \frac{R_i - Mean(R)}{Std(R)}$。
    *   **稳定性**：通过组内对比，自动适应了不同 Prompt 的难度差异，减少了方差。
*   **应用调整**：
    *   **代码生成**：Group Size 可以设置得较小（如 4-8），因为代码生成的验证（执行测试）成本较高。
    *   **对话优化**：需要结合 Reward Model。可以使用 LLM 作为裁判来进行打分，作为组内排序的依据。

#### 3. 扩展 SFT 训练代码 (基于 11.2.5)

要扩展 `SFT` 训练流程，可以在数据处理和 Trainer 配置阶段进行修改：

**(1) 多轮对话数据支持**
标准 SFT 数据通常是 `(instruction, output)` 对。多轮对话数据通常格式为 `[{"role": "user", "content": ...}, {"role": "assistant", "content": ...}, ...]`。
*   **扩展方法**：编写自定义的 `DataCollator`，将多轮对话拼接成模型通过的 Prompt 格式（如 ChatML 格式），并只对他/assistant 的回复部分计算 Loss (Mask user tokens)。

**(2) 数据增强**
*   **同义改写**：在 `Dataset` 的 `__getitem__` 或预处理阶段，使用另一个轻量级 LLM 对 Instruction 进行重写。
*   **难度调整**：对于推理任务，可以通过随机 mask 掉部分中间推理步骤，强迫模型学会跳跃推理或是更健壮的生成。

**(3) 训练可视化**
*   **集成 WandB / TensorBoard**：在 `TrainingArguments` 中设置 `report_to="wandb"`。
*   **自定义 Callback**：编写一个 HuggingFace `TrainerCallback`，在每个 `log_steps` 周期，使用当前模型生成几个固定 Prompt 的回复，记录到日志中，人工观察模型在训练过程中的变化。

```python
# 概念代码：自定义 Callback 进行生成质量监控
from transformers import TrainerCallback

class GenerationEvalCallback(TrainerCallback):
    def on_log(self, args, state, control, model, tokenizer, **kwargs):
        if state.global_step % args.eval_steps == 0:
            prompt = "Please solve: 3x + 5 = 20"
            inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
            outputs = model.generate(**inputs, max_new_tokens=50)
            generated_text = tokenizer.decode(outputs[0])
            print(f"\n[Step {state.global_step}] Generate Check: {generated_text}")
```

---

## 3. 奖励函数设计

### 11.3.3 奖励函数扩展实践

#### 1. GSM8K 精细化奖励函数

```python
def refined_math_reward(prediction: str, ground_truth: str, solution_steps: list) -> float:
    reward = 0.0
    
    # 1. 最终答案正确性 (权重最大)
    if extract_answer(prediction) == ground_truth:
        reward += 1.0
    else:
        # 部分奖励：如果答案格式是对的（是数字），但数值不对，给微小鼓励
        if extract_answer(prediction) is not None:
            reward += 0.1
            
    # 2. 推理过程合理性 (使用规则或轻量级模型判定)
    # 例如：检查是否包含关键公式或步骤关键词
    if "let" in prediction.lower() or "=" in prediction:
        reward += 0.1
    
    # 3. 效率/长度惩罚
    # 假设标准长度为 L，生成长度为 len_pred
    # 如果过于冗长，扣分
    length_penalty = 0.001 * len(prediction)
    reward -= length_penalty
    
    return max(0, reward) # 保持非负
```

#### 2. 不同领域的奖励函数

*   **(1) 代码生成助手**
    *   $R = w_1 \cdot I(Passed) + w_2 \cdot I(Style) + w_3 \cdot \frac{1}{Latency}$
    *   $I(Passed)$: 是否通过单元测试 (0/1)。
    *   $I(Style)$: 静态代码分析 (Lint) 得分，无警告得 1，否则扣分。
    *   $Latency$: 代码运行时间，越快奖励越高。

*   **(2) 客服对话智能体**
    *   $R = w_1 \cdot I(Solved) + w_2 \cdot Sentiment + w_3 \cdot I(Quick)$
    *   $I(Solved)$: 用户是否标记"问题已解决"或未进行追问。
    *   $Sentiment$: 使用 NLP 模型分析用户回复的情感极性（正向/负向）。
    *   $I(Quick)$: 轮数惩罚，解决问题所用的对话轮数越少越好。

*   **(3) 游戏 AI (如 MOBA)**
    *   $R = w_1 \cdot I(Win) + w_2 \cdot KDA + w_3 \cdot Gold$
    *   $I(Win)$: 胜负奖励 (稀疏，权重最大)。
    *   $KDA$: 击杀/死亡/助攻比 (稠密奖励，引导战斗技巧)。
    *   $Gold$: 经济获取效率 (引导发育策略)。

#### 3. 奖励黑客 (Reward Hacking)

*   **现象举例**：
    *   **扫地机器人**：奖励设为"吸入灰尘的数量"。机器人学会了先把灰尘倒出来，再吸进去，反复刷分。
    *   **赛船游戏**：奖励设为"获得分数"（通过吃道具）。AI 发现转圈吃道具比跑完全程得分更高，于是它在原地无限转圈，不通过终点。
*   **防御机制**：
    *   **Reward Cap (奖励上限)**：限制单位时间内或单步能获得的最大奖励。
    *   **多目标优化**：引入相互制衡的奖励项。例如，不仅奖励"吸入灰尘"，还大幅奖励"完成整个区域的清洁并归位"。
    *   **人工反馈循环 (RLHF)**：定期让人类评估 Agent 的行为视频，如果发现怪异行为，通过负反馈通过 PPO 修正。

---

## 4. 数学推理智能体训练案例分析 (11.4 节)

#### 1. GSM8K 数据集特点与扩展

*   **特点**：高质量的小学应用题，解答包含详细的推理步骤（Chain-of-Thought）。适合训练 LLM 的基础逻辑推理、算术能力。
*   **扩展建议**：
    *   **数据集扩展**：引入 MATH 数据集（包含高中/竞赛难度）、SVAMP（侧重鲁棒性）。
    *   **合成数据**：使用更强的模型（如 GPT-4）生成新的题目和证明过程（如同伦法生成类似题目）。
    *   **形式化验证**：结合 Lean/Isabelle 等形式化数学语言，让 Agent 写出的证明可以被计算机自动验证，从而获得绝对正确的奖励信号。

#### 2. 泛化能力评估

*   **过拟合风险**：模型可能背下了题库中的数字。
*   **评估方案**：
    *   **数值扰动**：将测试集题目中的数字随机替换（如 "5个苹果" 换成 "7个苹果"），看逻辑是否依然正确。
    *   **OOD (Out-of-Distribution) 测试**：使用不同来源、不同题型的数学题库进行评估。
*   **提升泛化**：
    *   **正则化**：在 Loss 中加入 KL 散度约束，防止模型策略偏离基座模型太远。
    *   **数据增强**：Question Permutation（改变问题表述但保持逻辑不变）。

#### 3. 在线学习 (Online Learning) 方案

*   **流程**：
    1.  部署模型服务用户。
    2.  收集用户交互数据（Prompt, Response, User Feedback/Correction）。
    3.  存入 **Replay Buffer (经验回放池)**。
    4.  定期从 Buffer 采样并在当前模型上进行微步数更新。
*   **挑战与对策**：
    *   **数据质量**：用户反馈有噪声。对策：使用 Reward Model 预过滤数据，或仅利用高置信度的反馈。
    *   **灾难性遗忘**：学习新知识忘了旧知识。对策：在 Buffer 中混合一定比例的原始预训练数据（Replay）。
    *   **安全性**：防止恶意用户通过 Prompt Injection 污染模型。对策：严格的安全过滤器和红队测试。

---

## 5. 工具学习

#### 1. 工具学习训练方案

*   **Action Space 扩展**：
    *   除了生成文本 token，增加特殊的 token（如 `<tool_call>`）或特定的 JSON 格式输出来触发工具。
*   **奖励设计**：
    *   $R_{tool} = R_{format} + R_{success} + R_{efficiency}$
    *   Formatting: 正确生成符合 API 规范的 JSON (+0.2)。
    *   Success: API 成功返回非空结果 (+0.5)。
    *   Outcome: 最终利用工具得出的答案解决了用户问题 (+2.0)。
    *   Penalty: 调用不存在的工具或参数错误 (-0.5)。

#### 2. 分层强化学习 (HRL)

*   **Manager Agent (高层)**：
    *   输入：用户任务。
    *   动作：生成由子目标组成的 Plan（例如："1. 搜索天气", "2. 计算穿衣指数"）。
    *   奖励：任务最终完成度。
*   **Worker Agent (低层)**：
    *   输入：当前子目标 + 环境状态。
    *   动作：具体的 API 调用或代码执行。
    *   奖励：子目标是否达成（Intrinsic Reward）。
*   **协调**：高层每设定一个子目标，低层执行一段时间直到终止，高层根据低层执行结果更新状态并决定下一个子目标。

#### 3. 课程学习 (Curriculum Learning)

*   **课程 1 (入门)**：仅提供 1-2 个基础工具（如计算器）。Prompt 明确提示"请使用计算器"。
*   **课程 2 (进阶)**：提供 5-10 个工具。题目不再提示具体工具，需要模型自己检索 (RAG) 或选择。
*   **课程 3 (专家)**：提供 50+ 工具，且包含干扰项（功能相似但适用的场景不同的工具）。任务涉及多步依赖。
*   **晋级标准**：在当前课程难度的验证集上成功率达到 90% 以上。
