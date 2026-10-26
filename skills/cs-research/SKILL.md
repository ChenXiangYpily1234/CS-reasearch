---
name: cs-research
description: Use when a user requests a complete AI/ML research workflow, frozen baseline experiments, multi-method seed screening, evidence-based paper storytelling, or continuation of such a research project.
---

# CS Research

执行从顶会证据到实验、论文和可编辑科研图的完整研究流程。用户只要求工作流模板时，交付模板而不启动课题训练。

## 开始与继续

读取 [完整流程](references/workflow.md) 对应阶段及 [默认配置](config/workflow.yaml)。新课题填写 [课题输入](templates/project.md)；继续课题先读取课题 main README 的冻结协议、结果账本和当前状态。复制配置到课题工作区后填写待选项，不回写此 skill 的默认值。固定项不得因某个方法的结果而改变。

缺少方向、GPU、网页会话或模型时，报告实际阻塞，继续不依赖它的工作。公开工作流不等于授权公开未发表稿件或数据；是否发布课题产物按该课题用户指令执行。

## 阶段路由

| 阶段 | 执行与证据 |
| --- | --- |
| 1 文献 | 检索核验20–30篇顶会论文；填写[文献表](templates/literature.md)，从共同局限提炼问题。 |
| 2 冻结 | 选1通用基线、1两年内竞争方法；在竞争方法仓库开发，按[冻结表](templates/experiment-freeze.md)写入main README。固定1训练集、2测试集、41/42、主指标、训练预算。 |
| 3 方法 | M01加ChatGPT网页端11个方向，共12个；用[网页提示词](prompts/chatgpt-ideation.md)和[方法卡](templates/method-card.md)记录公式推导、理论支撑与方向差异。 |
| 4 复现 | 先复现基线/竞争方法，profile争取0.95利用率，固定统一batch，冻结实测结果；实际Codex Luna high监督，保存模型ID及日志。 |
| 5 筛选 | 每法先跑41，严格超过竞争方法才跑42；未改善记STOPPED_AFTER_41，缺少原始证据记BLOCKED_EVIDENCE。 |
| 6 确认 | 全部候选达到终态后审查；[Paper StoryCraft](https://github.com/ChenXiangYpily1234/paper-storycraft-skills)定故事，有论文潜力再加43，并敲定消融与自选模型泛化。 |
| 7 论文 | [Nature Writing](https://github.com/SyntaxSmith/nature-writing-skill/blob/main/SKILL.md)写作、[Anti-Defensive Writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/blob/main/skills/anti-defensive-writing-en/SKILL.md)修订、独立[Peer Review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/peer-review/SKILL.md)审稿；根据证据修订。 |
| 8 图形 | GPT网页端构思框图，[image-to-editable-ppt](https://github.com/ningzimu/image-to-editable-ppt-skill/blob/main/skills/image-to-editable-ppt/SKILL.md)重建白底可编辑PPT；[Scientific Visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md)控制数据图风格，按[图形brief](templates/figure-brief.md)验收。 |

## 关键执行决策

- 基线与竞争方法结果一旦冻结，不得覆盖；勘误保留旧值并新增版本。新方法严格使用同一训练配置。
- 按约定不同卡和batch执行归入同一实验ID，保留execution ID、硬件与有效batch，不把重复执行计为独立seed。
- seed门槛用未四舍五入的原始数值、固定方向和阈值。可运行 `python3 scripts/check_seed_gate.py --candidate 0.8001 --competitor 0.8000 --direction maximize`。此命令仅计算资格，不证明来源、监督或训练完成，也不启动任务。
- 监督模型不可用记BLOCKED_MODEL；不冒充指定模型监督。网页构思和绘图必须有实际会话证据。
- 12方法“跑完”包括按门槛停止；缺失证据或基础设施故障不等于算法无效。保留每个候选的终态。
- 探索性筛选与最终确认分开报告；不从一轮筛选直接推出可发表或统计显著。

## 外部 skills

运行相关阶段前读取对应skill及必要依赖并记录来源版本。链接不等于已安装；缺少必要依赖应记录阻塞。

| 职责 | 原始 skill 链接 |
| --- | --- |
| 论文故事与论证 | [paper-storycraft](https://github.com/ChenXiangYpily1234/paper-storycraft-skills) |
| 论文写作 | [nature-writing](https://github.com/SyntaxSmith/nature-writing-skill/blob/main/SKILL.md) |
| 独立科学审核 | [peer-review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/peer-review/SKILL.md) |
| 防御性写作修订 | [anti-defensive-writing-en](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/blob/main/skills/anti-defensive-writing-en/SKILL.md) |
| 顶会风格数据图 | [scientific-visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md) |
| 框图语义与PPT设计 | [pptx-paper-figure-story](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/blob/main/12-pptx-visual/SKILL.md) |
| 图像重建为可编辑PPT | [image-to-editable-ppt](https://github.com/ningzimu/image-to-editable-ppt-skill/blob/main/skills/image-to-editable-ppt/SKILL.md) |

## 交付与验证

每阶段更新课题的配置、证据路径、状态与下一步。结束前逐项检查[完整流程的完成标准](references/workflow.md#完成标准)。模板默认NOT_RUN；仅按真实产物推进状态。包结构与门槛测试不替代GPU实验、网页操作或图形渲染验收。
