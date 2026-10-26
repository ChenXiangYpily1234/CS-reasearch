# CS reasearch

可安装的 **CS Research skill**：从20–30篇顶会论文、冻结实验和12方法筛选，到Paper StoryCraft定故事、Nature Writing写作、独立审稿与顶会风格作图。

本仓库交付skill与测试；没有执行具体研究或GPU训练，默认状态为 `NOT_RUN`。

## 安装与调用

```bash
npx skills add https://github.com/ChenXiangYpily1234/CS-reasearch --skill cs-research
```

也可克隆后将 `skills/cs-research` **完整目录**复制到支持Agent Skills的工具的技能目录（例如 `~/.codex/skills/cs-research`），保留references、config、scripts和templates。避免覆盖已有同名目录。

调用：

```text
请使用 $cs-research，研究方向为【方向】，GPU资源为【资源】。
先核对输入并按照冻结协议推进，报告每阶段证据、状态与下一步。
```

入口：[SKILL.md](skills/cs-research/SKILL.md)。详解：[完整流程](skills/cs-research/references/workflow.md)。默认配置：[workflow.yaml](skills/cs-research/config/workflow.yaml)。UI元数据：[openai.yaml](skills/cs-research/agents/openai.yaml)。

YAML是供Agent读取、复制并填写的协议模板，不是自动训练调度器。数据、batch、模型等待选项保留null；先按课题冻结后执行。外部skills入口和职责见[Skills表](skills/cs-research/references/workflow.md#skills-与来源)，不会随本仓库自动安装。

## 测试

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
```

测试覆盖skill发现、YAML固定协议、可移植引用，以及seed门槛的胜/负/平、最小化指标、阈值边界和非法数值。GitHub Actions在push/PR执行同一测试。测试通过不等于实验、模型监督或作图已完成。

单独检查seed资格（不启动训练）：

```bash
python3 skills/cs-research/scripts/check_seed_gate.py --candidate 0.8001 --competitor 0.8000 --direction maximize
```

返回 `eligible_seed_42`。输入必须来自同配置、同seed的未四舍五入验证结果；脚本只计算门槛，不核验日志来源。命令成功返回0，非法参数返回2；不满足门槛通过JSON中的false表达。

## 文件结构

```text
skills/cs-research/
  SKILL.md
  agents/openai.yaml
  config/workflow.yaml
  references/workflow.md
  templates/
  prompts/
  scripts/check_seed_gate.py
tests/
  test_skill_package.py
  test_seed_gate.py
  scenarios.yaml
.github/workflows/tests.yaml
```

行为场景见[scenarios.yaml](tests/scenarios.yaml)；它们供独立Agent评估，不作为真实实验结果。当前本地验证与行为评估记录见[验证记录](tests/VALIDATION.md)。
