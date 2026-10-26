# 可复用执行指令

请读取本仓库 README.md 与 templates/project.md，按阶段完成研究。先核对研究方向、GPU、网页端访问、监督模型和技能依赖；缺少必要信息时记录阻塞，同时继续独立可完成的工作。

1. 核验 20–30 篇顶会论文，填写文献表，提炼有证据的共性问题。
2. 选定通用基线和两年内竞争方法；使用竞争方法仓库开发。预先冻结 1 训练集、2 测试集、指标、训练 seed 41/42（确认阶段增加 43）、对应同号的推理/评估 seed、统一训练配置/步数及评估设置。
3. 设计M01，在ChatGPT网页端构思M02–M12，完成数学卡、理论文献和差异矩阵。
4. 先复现基线与竞争方法，通过profile调batch争取0.95利用率，冻结统一batch与实测结果到main README。由实际Codex Luna high监督运行，保存模型ID、命令与日志。
5. 所有方法配置一致；41超过竞争方法才运行42；不同卡和batch执行归入同一实验并保留执行记录。
6. 12方法达到终态后统一审查，用[Paper StoryCraft](https://github.com/ChenXiangYpily1234/paper-storycraft-skills)定故事；有论文潜力再增加43，并冻结消融和自选模型泛化。
7. [Nature Writing](https://github.com/SyntaxSmith/nature-writing-skill/blob/main/SKILL.md)写作，[Anti-Defensive Writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/blob/main/skills/anti-defensive-writing-en/SKILL.md)修订，独立[Peer Review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/peer-review/SKILL.md)审核。
8. GPT网页端构思图，用[image-to-editable-ppt](https://github.com/ningzimu/image-to-editable-ppt-skill/blob/main/skills/image-to-editable-ppt/SKILL.md)重建白底可编辑PPT，再用[presentation-skill](https://github.com/siril9/presentation-skill/blob/main/SKILL.md)优化布局、排版与美观并渲染检查；[Scientific Visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md)统一数据图风格，依真实顶会参考减少AI味道。

推理/评估须与训练运行配对：同一个 seed（41/42/43）下，基线、竞争方法及所有候选使用相同推理随机 seed，并固定评估样本与顺序、评估器版本、checkpoint 选择规则和通用解码/采样设置；方法创新所需差异必须事先声明。随机采样按样本设 seed 时固定样本到 seed 的映射，不得换 seed 挑选结果。确定性推理记录 N/A；接口不支持设置 seed 则记录 UNCONTROLLED、受影响范围及复现风险，不得虚称已对齐。ChatGPT 网页端构思的内部 seed 不属于可控制的实验推理 seed。

每个阶段报告证据、产物、状态与下一步。NOT_RUN、STOPPED_AFTER_41、FAILED、BLOCKED和COMPLETE须据实际情况填写。最终逐项核对README完成标准。
