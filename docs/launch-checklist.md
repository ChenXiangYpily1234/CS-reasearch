# Launch checklist — grow a new repository by making it useful

This is an owner-facing publishing checklist, not a promise of stars.

## Before sharing

- [ ] Merge the README refresh once the links, rendered SVG, Mermaid diagram and Actions status have been checked on GitHub.
- [ ] Add a concise repository **About** description, topics, and a social preview image via GitHub's repository settings.
- [ ] Decide on a suitable open-source license (the repository currently has none). Do not assume that public visibility grants redistribution rights.
- [ ] Verify the installation command with a clean, compatible agent environment and record any OS or Node.js requirements.
- [ ] Publish a tagged initial release **only after** the package is validated.
- [ ] Provide a real example from a consenting public project only when results and provenance can be shown. Keep synthetic examples labeled.

## Distribution — show the result, not just a link

A small repository earns trust through a clear demonstration: a **15–30 second screencast or 3–4 annotated screenshots** showing installation, the Skill being detected, its protocol checklist, and a concrete (non-sensitive) decision. Do not fake usage counts or claim that the Skill trained a model when it only drafted a plan.

Share once per relevant community, following each community's self-promotion rules. Useful channels may include a relevant GitHub Discussion, a research engineering forum, or a developer newsletter; tailor the text to the audience, participate in follow-up questions, and avoid repetitive cross-posting.

### Example Chinese announcement

> 做 AI/ML 科研时，我发现 Agent 很容易给出一个看起来完整、但缺少实验来源的计划。因此开源了 **CS Research**：一个可安装的 Agent Skill，用于文献核验、实验冻结、12 方向方法卡、seed 门槛与论文作图交接。它目前是工作流与模板，并不是自动训练系统。附带可运行的门槛脚本和测试。欢迎提真实场景的改进建议： https://github.com/ChenXiangYpily1234/CS-reasearch

### Example English announcement

> I built **CS Research**, an open Agent Skill for evidence-first AI/ML research: verify papers, freeze baselines and budgets, design distinct candidates, document strict seed-gate decisions, and hand off writing and figures. It's a workflow and testable templates—not an automated GPU training claim. Feedback on real failure cases is especially welcome: https://github.com/ChenXiangYpily1234/CS-reasearch

## What to monitor

Use GitHub's **Insights → Traffic** (where available), visitor/source breakdowns, issues, forks and stars to understand which messages attract *relevant* readers. Compare consistent 7-day windows; do not infer causality from one post. Read issue quality and repeated usage alongside stars.

A useful first feedback loop is: **publish → get one independent installation attempt → fix friction → show a credible example → share the improvement**.

## Suggested repository metadata

**About:** Evidence-first Agent Skill for AI/ML research: literature, frozen experiments, seed-gated methods, paper writing & scientific figures.

**Topics (suggestions; select the most relevant):** `agent-skills`, `research-workflow`, `machine-learning`, `reproducibility`, `ai-research`, `scientific-writing`, `experiment-tracking`, `codex`.

**Naming:** Consider correcting `CS-reasearch` to `CS-research` in repository settings. Before doing so, check existing links, automations and consumers, and update README install commands and badges. GitHub redirects do not justify leaving obsolete references indefinitely.

**Social preview:** Use a readable high-contrast image at the dimensions recommended in GitHub Settings; the README SVG is a starting visual reference, not a social-preview upload.

