# Contributing to CS Research

Thanks for improving the documentation, protocol, tooling and reproducibility of this Agent Skill.

[中文 README](README.md) · [English README](README.en.md) · [Full protocol](skills/cs-research/references/workflow.md)

## Good first contributions

- Fix unclear installation instructions, broken references or confusing examples.
- Report reproducible problems in the seed gate, default YAML or Skill discovery.
- Improve templates with a clear use case and evidence-backed rationale.
- Add tests for a **specific** failure condition rather than changing protocol defaults silently.
- Suggest ways to make the first-run experience easier for researchers new to Agent Skills.

## How to propose a change

1. Open an issue explaining the observed problem, steps to reproduce (if applicable), expected behavior and environment.
2. Create a focused branch and make one logically related change at a time.
3. For behavior or code changes, add or update tests, then run:

   ```bash
   python3 -m venv .venv
   .venv/bin/python -m pip install -r requirements-dev.txt
   .venv/bin/python -m unittest discover -s tests -v
   ```

4. Open a pull request with a summary, tests performed, and any relevant limitations.

## Research integrity requirements

- Do **not** add invented papers, benchmark numbers, testimonials, star counts, model supervision sessions or screenshots disguised as real results.
- Label synthetic examples clearly; keep default project status `NOT_RUN` unless real work was performed.
- Preserve existing frozen protocols and results when correcting an error; document a versioned erratum instead of silently rewriting evidence.
- Keep the [Skill directory](skills/cs-research) portable. Its relative references must resolve within that directory.
- External Skills are linked dependencies, not bundled code. Check upstream licensing and actual availability before proposing integration.

## Issue reporting format

**Problem:** What did you try, and what did you expect?

**Reproduction:** Commands, inputs, versions and relevant files (please remove secrets).

**Observed output:** Error messages or incorrect decisions.

**Proposed improvement:** The smallest concrete fix, if known.

Small, well-documented PRs are preferred over broad changes that make the workflow harder to audit.

