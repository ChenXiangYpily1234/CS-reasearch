# First run: try CS Research without a GPU

[中文主页](../README.md) · [English guide](../README.en.md) · [Project template](../skills/cs-research/templates/project.md)

This is an **illustrative interaction guide**, not a log of an actual agent run. No literature search, model training, supervisor session or scientific evaluation was performed to create this example.

## 1. Install and ask a scoped question

```bash
npx skills add ChenXiangYpily1234/CS-reasearch --skill cs-research
```

In your compatible agent, try this example request (or use your own research area):

```text
请使用 $cs-research。
研究方向：高效文本分类。
目标：在保证主指标可比的前提下，探索推理成本降低。
GPU：暂时没有。
先只做课题输入核对、研究问题澄清、实验冻结草案和缺失证据检查。
输出下一步清单，不启动训练，不编造论文、结果和模型监督。
```

## 2. What a reasonable *draft* might contain

The following is a **sketch of expected categories**, not measured output:

| Field | Illustrative entry | Evidence state |
| --- | --- | --- |
| Research area | Efficient text classification | User-provided topic |
| Specific task/dataset | Not selected | `NOT_RUN` |
| Baseline and recent competitor | Need literature and code verification | `BLOCKED_EVIDENCE` |
| Primary metric/direction | To be agreed and frozen | `NOT_RUN` |
| GPU and environment | Not supplied | `BLOCKED` |
| Seeds | 41/42 screen, 43 confirmation | Protocol default; not executed |
| Actual performance / paper quality | Unknown | No results |

An agent should ask for the exact task definition, data availability, compute limits, target venue and metrics, and draft a protocol without filling unknown fields with convenient numbers.

## 3. Inspect the templates

- [Project input](../skills/cs-research/templates/project.md): collect task and constraints.
- [Literature matrix](../skills/cs-research/templates/literature.md): record evidence and comparisons.
- [Experiment freeze](../skills/cs-research/templates/experiment-freeze.md): define reproducible baselines and budgets.
- [Method card](../skills/cs-research/templates/method-card.md): record mechanism, assumptions and counterexamples.

The defaults in [`workflow.yaml`](../skills/cs-research/config/workflow.yaml) intentionally contain `null` and `NOT_RUN` values. Copy it to **your project workspace** before filling those values.

## 4. Try the actual small helper

This is the part you can run even without an agent or GPU:

```bash
python3 skills/cs-research/scripts/check_seed_gate.py --candidate 0.8001 --competitor 0.8000 --direction maximize
```

The helper will return:

```json
{"eligible_seed_42": true, "decision": "ELIGIBLE"}
```

These values are synthetic inputs for demonstrating the CLI. The helper checks a strict comparison only; it cannot establish whether the values came from a fair experiment.

## 5. Continue safely

Once real evidence and compute are available, continue with the [full protocol](../skills/cs-research/references/workflow.md). Record the real data/code versions, results and failure states. A working protocol is useful even if the first method shows no improvement.

