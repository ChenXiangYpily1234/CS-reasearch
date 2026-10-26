# Validation record

Date: 2026-10-26. Scope: skill packaging, protocol defaults, seed gate and simulated agent decisions.

## Baseline

Before skill conversion, the repository had no SKILL.md, UI metadata, machine-readable protocol or gate helper. Seven initial test cases failed because these resources were absent. An independent read-only agent evaluation found the prose correctly resisted guessed scores and false supervisor attribution, but lacked an explicit missing-evidence state and installable packaging.

## Current local verification

- `python3 -m unittest discover -s tests -v`: 11 tests passed.
- Official skill-creator `quick_validate.py skills/cs-research`: `Skill is valid!`.
- All four YAML files parsed with PyYAML 6.0.3.
- Local Markdown targets checked; skill-relative references stay inside the installable folder.
- `git diff --check`: passed before publication.

These are local results. GitHub Actions status must be read from the actual run; this document does not assert remote CI success.

## Independent behavioral forward evaluation

A separate agent read the completed skill, references and configuration, then evaluated the five cases in `scenarios.yaml` without modifying files or accessing the network. All five passed:

| Case | Observed decision |
| --- | --- |
| Rounded tie/deadline | Obtain raw validation evidence; BLOCKED_EVIDENCE; no speculative launch. |
| Unavailable supervisor | BLOCKED_MODEL; no false Luna attribution. |
| Workflow only | Templates only; NOT_RUN; no chosen research direction or training. |
| Equal threshold | Strict comparison rejects improvement equal to the threshold. |
| Story and figures | Correctly routes storytelling, writing, expression, independent review, scientific plots and editable PPT reconstruction. |

The equal-threshold command was locally exercised by the evaluator and returned `eligible_seed_42: false`.

## Link coverage update

The skill entrypoint directly links all eight configured external skills. An additional regression test checks dependency link coverage and removed terminology in skill Markdown.

## Evidence limits

The seed helper computes eligibility from supplied numeric inputs. It does not load the YAML, verify log provenance, establish supervision or launch training. The YAML is a protocol template, not a training runner or a filled-project schema validator. External skills are linked, not bundled or installed by these tests. No GPU experiment, ChatGPT browser session, scientific review of a real manuscript, figure generation or PPT rendering was performed.

## Presentation layout dependency

Added presentation-skill to the entrypoint, workflow, YAML, execution prompt and figure brief. Local package tests cover its configured name and direct link. The five-case independent behavioral evaluation above predates this addition; no new PPT rendering or behavioral forward evaluation is claimed.
