# CS reasearch

一套从研究方向、顶会文献、方法设计，到冻结实验、筛选、论文故事、写作、审稿与可编辑作图的可复用研究工作流。

**当前交付：工作流与模板。没有执行具体课题、论文检索、模型训练或论文写作；模板中的结果均为 `NOT_RUN`。**

## 快速开始

1. 新课题先填写 [课题输入](../templates/project.md)。
2. 将 [完整执行提示词](../prompts/research-workflow.md) 交给研究 Agent，并提供研究方向、GPU/服务器与 ChatGPT 网页会话。
3. 按下方阶段依次完成；缺少输入时记录 `BLOCKED`，不得用预测值替代实测结果。
4. 本仓库负责流程。具体课题的所有方法代码，统一在选定竞争方法的仓库开发；将该仓库 URL、上游 commit、开发分支写入课题 README。

## 1. 检索 20–30 篇顶会论文

根据明确的研究方向界定顶会范围与检索日期。从官方论文集、作者论文、正式论文 PDF 和官方代码仓库核验来源。预印本与已录用顶会论文分开标记。保留检索式、纳入/排除理由和 DOI/论文链接。

使用 [文献表](../templates/literature.md)，每篇填写：**年份 / 方法 / 数学公式 / 提升效果 / 局限性 / 未来展望**，同时保留会议、公式与结果的页码或表号。提升效果须说明比较对象、数据集、指标、绝对提升或相对提升；不同设置的结果不能直接排名。区分作者明确陈述的局限与研究者推断。

从多篇论文反复出现的局限性提炼可证伪的研究问题，记录“哪些论文支持 → 为什么现有方案未解决 → 可测量的成功条件”。目标同时覆盖**节约成本与提升指标**。

## 2. 选定并冻结统一标准

在具体课题仓库的 **main 分支 README.md** 写入 [实验冻结表](../templates/experiment-freeze.md)：

| 项目 | 固定要求 |
| --- | --- |
| 通用基线 | 1 个，适合该任务的标准方法 |
| 竞争方法 | 1 个，冻结日向前 2 年内的文章；记录具体日期、会议与官方代码来源 |
| 开发仓库 | 选定竞争方法的仓库；后续 12 个方法实现均在这一仓库 |
| 数据 | 1 个训练集、2 个测试集，固定版本、划分、预处理与样本哈希 |
| 初始种子 | 41、42；最终确认阶段增加 43 |
| 指标 | 明确主指标、方向、聚合方式、成本指标和比较门槛 |
| 预算 | 统一训练步数、数据顺序策略、训练配置与 checkpoint 选择规则 |
| 训练配置 | 尽可能只用 1 套；优先 1 epoch，或采用相关论文共同使用的配置 |
| 结果 | 基线与竞争方法复现后写入 README，随后冻结，作为所有方法的统一比较标准 |

相同训练集、有效 batch 和采样规则下，固定 epoch 应对应相同优化步数。若论文配置不同，先说明取舍再冻结，不混用“同 epoch”和“同更新步数”。新方法保持同样训练配置；方法特有参数、选择依据和搜索预算须预先记录，不使用测试结果调参。

冻结包含代码、环境、配置、数据和评估器的版本/哈希。基线与竞争方法结果一经确定不得修改；若发现错误，保留原记录并新增勘误和协议版本，不能静默替换。论文原报结果与本地复现结果分栏。

两个测试集在协议冻结后用于最终报告。方法筛选与 checkpoint 选择使用训练集内预先划定的验证切分，仍属于同一个训练数据来源；不得根据测试结果反复设计方法。

## 3. 构思 12 个不同方向的方法

先提出解决共性问题的 M01，再**借助 ChatGPT 网页端**构思方向各异的 M02–M12，共 12 个。保存网页会话链接、输入提示词、日期和输出导出；未实际使用网页端不得标记该步骤完成。可直接使用 [网页构思提示词](../prompts/chatgpt-ideation.md)。

每个方法使用 [方法卡](../templates/method-card.md)：数学建模、符号定义、目标函数、公式逐步推导、假设、复杂度、成本机制、效果机制、失败条件与验证实验。理论非耦合处应寻找其他文献，给出其支撑命题、适用前提与准确出处；文献不能直接支持的连接明确标为待验证假设。

用差异矩阵比较 12 个方法的核心假设、干预对象、优化目标、信息来源与成本机制。只是改权重、换名字或堆叠相同模块，不算不同方向。可以从数据选择、目标设计、估计器、优化、表示、结构稀疏、检索/记忆、计算分配、蒸馏、推理策略、鲁棒性和缓存等轴探索，但须依课题判断适用性，不能强行套入。

## 4. 先复现，再固定 batch

先跑通通用基线与竞争方法。仅在正式结果冻结前，通过短时 profile 调整 batch，使稳态 GPU 利用率尽可能接近 **0.95**，同时记录采样窗口、吞吐、显存和利用率。利用率不是模型质量指标；数据瓶颈或硬件限制导致无法达到时，记录实际值与原因。

根据两种参考方法都能运行的配置，确定统一 batch 并写入 main README。后续所有方法固定一致。记录每卡 micro-batch、GPU 数量和梯度累积：

`effective_batch = micro_batch_per_gpu × GPU_count × gradient_accumulation_steps`

按用户约定，**不同卡运行和 batch 配置视为同一实验**，使用同一实验 ID 下的 execution ID 保存执行记录，不重复计为独立 seed。后续仍遵循冻结 batch；如故障恢复需要改变物理执行方式，记录差异。硬件、有效 batch 和数值精度仍须保留，便于解释可复现性与成本差异。

代码运行由 **Codex Luna high** 监督：记录平台实际模型 ID、reasoning effort、代码检查、启动命令、进程状态、日志、失败恢复和结果核验。模型不可用时标记 `BLOCKED_MODEL` 并报告，不得声称已由它监督或静默换模型。监督不等于训练已完成。

## 5. 逐方法 seed 门槛

预先固定 12 个方法及运行顺序。每个方法先跑 **seed 41**，与竞争方法同 seed 比较。仅当主指标收益超过竞争方法时启动 **seed 42**；否则记录 `STOPPED_AFTER_41`。严格大于的判断基于未四舍五入原值，指标方向和最小改善阈值在冻结表预先定义。

以最大化指标为例，令 `Δ_s = score(M,s) − score(C,s)`，默认门槛为 `Δ_41 > 0`；最小化指标相应反向。成本也按冻结口径报告，不能仅凭指标提升就宣布同时省成本。

“12 个方法全部跑完”指每个方法均达到完整终态：完成 41/42，或按门槛停在 41；基础设施失败与算法失败分开标记。所有尝试保留，不把只完成 41 的方法伪装为双 seed 结果。

## 6. 审查、确定故事、第三 seed

所有方法达到终态后统一审查，按预先冻结的验证主指标选择最优方法，缺失第二 seed 的候选不能直接与完整双 seed 均值混排。记录选择规则、同分规则、全部 12 方法结果及成本。

使用 **[Paper StoryCraft](https://github.com/ChenXiangYpily1234/paper-storycraft-skills) 确定论文故事**：研究问题 → 共性缺口 → 核心洞察 → 方法机制 → 关键证据 → 结论范围。理解最优方法为何有效，检验替代解释；不按试验发生顺序写实验日记。

判断是否具备论文潜力：新颖性是否经文献核验、效果与成本是否有实测证据、机制能否被消融检验、结果是否可复现。此判断不是接收保证。具备潜力时，为最终方法以及缺少对应结果的基线、竞争方法补跑 **seed 43**，保证配对比较。

seed 41 门槛和 12 选 1 是探索性筛选，报告选择过程。seed 43 是预先保留的确认运行，不将三 seed 自动解释为统计显著。报告逐 seed、均值、离散程度及合适的不确定性；未经实际检验不得写“显著提升”。

随后冻结消融和泛化协议：每项消融对应一个机制假设；泛化模型自行选择，写清依据与适用范围。泛化可因模型架构要求采用单独预冻结配置，但同一泛化设置内各方法公平一致，并与主实验分开报告。

## 7. 写作与独立审稿

执行顺序：**[Paper StoryCraft](https://github.com/ChenXiangYpily1234/paper-storycraft-skills) 定故事 → [Nature Writing](https://github.com/SyntaxSmith/nature-writing-skill/blob/main/SKILL.md) 写作 → [Anti-Defensive Writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/blob/main/skills/anti-defensive-writing-en/SKILL.md) 修订表达 → [Peer Review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/peer-review/SKILL.md) 独立审核 → 根据证据修订**。

- 故事阶段输出研究问题、核心贡献、claim–evidence 映射和逐图叙事。
- [Nature Writing](https://github.com/SyntaxSmith/nature-writing-skill/blob/main/SKILL.md) 根据目标会议篇幅与格式写作，不因使用该 skill 就改投 Nature。
- [Anti-Defensive Writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/blob/main/skills/anti-defensive-writing-en/SKILL.md) 直接使用其原始说明组织有说服力的论文表达。
- 独立审核使用独立审稿会话，提供稿件、冻结协议、方法公式、代码版本、原始结果与文献。审核正确性、创新性、统计、成本、公平性、引用和论文—代码一致性。
- 审稿输出位置、问题、证据、影响、具体修改及复查状态；没有证据的批评标记不确定性，不编造审稿结论。

## 8. GPT 网页绘图与顶会风格

用 ChatGPT/GPT 网页端构思方法图，保存提示词、会话、原始图片与版本。随后使用 **[image-to-editable-ppt](https://github.com/ningzimu/image-to-editable-ppt-skill/blob/main/skills/image-to-editable-ppt/SKILL.md)**，重建白底、对象级可编辑 PPT 框图；配合 [Paper StoryCraft](https://github.com/ChenXiangYpily1234/paper-storycraft-skills) `12-pptx-visual` 检查语义。

**[Scientific Visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md)** 负责数据图与出版风格。方法框图与统计图分开处理；数据图直接由真实结果和可复现绘图脚本生成，导出 PDF/SVG/PNG，不从生成式图片读取或重画数值。

减少 AI 味道的具体验收：

- 从目标方向选择 3–5 篇真实顶会论文，记录图号和视觉参考，只借鉴布局、编码与排版。
- 白底，优先黑/灰文字，控制在 2–4 个语义色；同模块同颜色，贡献模块使用有限强调色。
- 去掉渐变、阴影、发光、立体装饰、无语义图标与营销卡片；避免彩色圆角框堆砌。
- 箭头必须对应真实数据流、计算或依赖；训练与推理、冻结与可训练模块有清楚图例。
- 字体、线宽、框距、箭头和公式统一；按最终单栏/双栏尺寸检查标签可读性。
- 数值图标明单位、样本与误差含义；可区分线型/点型，检查灰度可读性和坐标表达。
- PPT 的文字、主要模块和连接线须可单独编辑；整图贴进 PPT 不算完成。逐项检查公式、文字、遮挡、越界和连接线位置。
- 交付原始图片、原生 PPTX、绘图源代码/数据、PDF/SVG 和预览；实际查看渲染后才声明视觉验收通过。

参见 [图形 brief](../templates/figure-brief.md)。

## Skills 与来源

以下是技能职责与可访问的原始入口；链接不代表已安装运行时，也不代表已经执行某项研究。运行前读取完整 skill 及依赖，记录来源 commit。核验日期：2026-10-26。

| 职责 | Skill 与入口 |
| --- | --- |
| 论文故事与论证主线 | [Paper StoryCraft](https://github.com/ChenXiangYpily1234/paper-storycraft-skills) · [WORKFLOW](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/blob/main/WORKFLOW.md) |
| Nature 风格写作 | [Nature Writing](https://github.com/SyntaxSmith/nature-writing-skill/blob/main/SKILL.md) |
| 独立科学审核 | [K-Dense Peer Review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/peer-review/SKILL.md) |
| 防止防御性写作 | [Anti-Defensive Writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/blob/main/skills/anti-defensive-writing-en/SKILL.md) |
| 顶会风格数据绘图 | [Scientific Visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md) |
| 科研框图语义与 PPT 设计 | [Paper StoryCraft PPTX Visual](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/blob/main/12-pptx-visual/SKILL.md) |
| 图像重建为可编辑 PPT | [Image to Editable PPT](https://github.com/ningzimu/image-to-editable-ppt-skill/blob/main/skills/image-to-editable-ppt/SKILL.md) |

本仓库仅链接第三方 skills，不复制分发其代码或附件。ChatGPT 网页端、GPU 服务器、模型监督与 PPT 转换运行时须在具体课题中实际准备和验证。

## 完成标准

文献 20–30 篇有证据；标准在 main README 冻结；基线与竞争方法有原始复现日志；12 方法有数学卡和差异检查；全部候选有终态；最优方法有故事与确认实验；消融/泛化有冻结协议；论文经过写作与独立审核；图像/PPTX 有渲染和可编辑验收。任何缺项保留实际状态，不以模板文件存在代替完成。
