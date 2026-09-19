# Contributing to AITRT

Thank you for contributing to the AI Trust & Risk Taxonomy.

## Principles

- Prefer clear, reusable concepts over framework-specific jargon.
- Keep canonical entities atomic and machine-readable.
- Provide evidence or an authoritative source for external mappings.
- Do not copy copyrighted standards text into the repository.
- Avoid duplicate concepts; explain why a new entity is needed.

## Adding a risk

A risk should have a stable ID, concise definition, domain, affected trust dimensions, lifecycle stages, scenarios, controls, metrics, and evidence where applicable.

## Validation

Run `python tools/validate_taxonomy.py` before submitting a pull request.
