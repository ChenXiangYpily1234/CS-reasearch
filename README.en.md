# CS Research — evidence-driven AI/ML research workflow

**[简体中文 / Chinese](README.md)** · [Install](#quick-start) · [Workflow](#workflow) · [What is included](#whats-included) · [Contribute](CONTRIBUTING.md)

<p align="center">
  <img src="assets/cover.svg" width="100%" alt="CS Research — Evidence first. Reproducibility by design." />
</p>

[![Skill tests](https://github.com/ChenXiangYpily1234/CS-reasearch/actions/workflows/tests.yaml/badge.svg)](https://github.com/ChenXiangYpily1234/CS-reasearch/actions/workflows/tests.yaml)

**A reusable Agent Skill that helps researchers move from literature review to a frozen experimental protocol, method screening, paper storytelling, and editable scientific figures.**

Unlike a generic research prompt, CS Research requires explicit artifacts, evidence, stage status, and honest handling of missing data. It is **not** an automated training system, and installing it does not mean a research project has been executed.

## Quick start

### Install

Run the following in an environment with Node.js and a compatible coding agent:

```bash
npx skills add ChenXiangYpily1234/CS-reasearch --skill cs-research
```

Select your agent when prompted. See the [official CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) for options. Alternatively copy the **entire** [`skills/cs-research`](skills/cs-research) directory to your agent's Skill directory.

### Try the workflow without a GPU

Send this request to your agent:

```text
Use $cs-research.
Research area: efficient text classification (replace with your own).
Compute available: none yet.
Start by identifying missing inputs and drafting a protocol-freeze checklist.
Show evidence, stage status and next actions. Do not invent research results.
```

See the [first-run example](examples/first-run.md) for an **illustrative** response. You can use the planning and review steps before setting up training infrastructure.

## Workflow

| Stage | Expected work / evidence |
| --- | --- |
| **01 · Read** | Verify 20–30 relevant papers; track venues, formulas, claims, comparisons and limitations. |
| **02 · Freeze** | Select a standard baseline and a recent competitor; freeze datasets, metrics, seeds and training budgets. |
| **03 · Design** | Develop 12 distinct, testable method directions with equations, assumptions and method cards. |
| **04 · Reproduce** | Reproduce reference methods, profile resource use and record executable evidence. |
| **05 · Screen** | Compare seed 41 to the competitor; run seed 42 only when the pre-declared strict threshold is exceeded. |
| **06 · Confirm** | Review candidates, build a paper story, and plan seed 43, ablations and generalization where justified. |
| **07 · Write** | Organize writing, expression review and independent scientific critique through linked external Skills. |
| **08 · Visualize** | Specify reproducible data plots and editable paper diagrams with explicit visual acceptance criteria. |

The sequence is a **protocol**, not a report of completed experiments. Read the [detailed workflow](skills/cs-research/references/workflow.md) for full conditions and decision rules.

## What's included

| File | Purpose |
| --- | --- |
| [`SKILL.md`](skills/cs-research/SKILL.md) | Agent Skill entrypoint and stage routing |
| [`config/workflow.yaml`](skills/cs-research/config/workflow.yaml) | Copyable, intentionally incomplete protocol template |
| [Project template](skills/cs-research/templates/project.md) | Research direction and project prerequisites |
| [Literature template](skills/cs-research/templates/literature.md) | Evidence-driven paper tracking |
| [Experiment freeze](skills/cs-research/templates/experiment-freeze.md) | Fair comparison and reproducibility checklist |
| [Method card](skills/cs-research/templates/method-card.md) | Mechanistic hypotheses, assumptions and falsification |
| [Seed-gate script](skills/cs-research/scripts/check_seed_gate.py) | Strict comparison from user-supplied metric values |
| [Figure brief](skills/cs-research/templates/figure-brief.md) | Diagrams, scientific plots and editability checks |
| [Validation notes](tests/VALIDATION.md) | What the existing tests do—and do not—prove |

Run the seed-gate helper without training a model:

```bash
python3 skills/cs-research/scripts/check_seed_gate.py \
  --candidate 0.8001 --competitor 0.8000 --direction maximize
```

Expected result for these *illustrative input values*:

```json
{"eligible_seed_42": true, "decision": "ELIGIBLE"}
```

The helper does **not** establish metric provenance, experimental fairness, or whether training occurred.

## Verification and limitations

The repository includes local unit tests and a GitHub Actions workflow. To run those tests:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
```

These tests check the Skill package, protocol defaults and threshold logic. They do **not** validate the scientific merit of an unexecuted project. The included project defaults are `NOT_RUN`; linked writing, reviewing and plotting Skills are not automatically installed.

## Contribute

Issues and pull requests about incorrect assumptions, documentation, broken dependencies, tests, accessibility and reproducibility are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

If you find this protocol useful, consider giving the repository a **Star** and sharing concrete feedback. The most valuable contributions are real-world failure cases and evidence-backed improvements.

[Back to Chinese](README.md) · [First-run example](examples/first-run.md) · [Detailed workflow](skills/cs-research/references/workflow.md)

