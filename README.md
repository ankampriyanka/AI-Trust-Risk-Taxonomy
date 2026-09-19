# AI Trust & Risk Taxonomy (AITRT)

**AI Trust & Risk Taxonomy (AITRT)** is an open, machine-readable knowledge layer connecting AI risks, trust characteristics, lifecycle stages, risk scenarios, controls, metrics, evidence, and established AI governance and security frameworks.

## Why AITRT?

AI governance resources solve different parts of the problem:

- **NIST AI RMF** provides a risk-management framework.
- **MITRE ATLAS** catalogs adversarial AI/ML tactics and techniques.
- **OWASP GenAI Security Project** addresses application and security risks for generative AI.
- **ISO/IEC standards** provide management-system and risk-management requirements and guidance.
- **Regulation** establishes legal obligations in applicable jurisdictions.

AITRT is intended to sit **between these resources as a relationship and knowledge layer**. It does not replace them.

## Core relationship model

```text
Risk
 ├── affects ───────► Trust Dimension
 ├── occurs_at ─────► Lifecycle Stage
 ├── manifests_as ──► Risk Scenario
 ├── measured_by ───► Metric
 ├── mitigated_by ──► Control
 ├── evidenced_by ─► Evidence Type
 └── mapped_to ─────► External Framework
```

The objective is to make these relationships machine-readable and reusable across AI governance tooling, assessments, engineering workflows, and research.

## Initial scope

v0.1 establishes:

- 9 trust dimensions
- 7 AI lifecycle stages
- 7 risk domains
- 21 canonical risks
- 15 starter controls
- 12 starter metrics
- 6 risk scenarios
- 9 evidence types
- initial external-framework mapping structures

## Repository structure

```text
AI-Trust-Risk-Taxonomy/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── requirements.txt
├── docs/
│   ├── methodology.md
│   ├── architecture.md
│   └── framework-mapping.md
├── taxonomy/
│   ├── trust/trust-dimensions.yaml
│   ├── lifecycle/lifecycle-stages.yaml
│   ├── risks/risk-domains.yaml
│   ├── risks/risks.yaml
│   ├── controls/controls.yaml
│   ├── metrics/metrics.yaml
│   ├── scenarios/scenarios.yaml
│   └── evidence/evidence-types.yaml
├── frameworks/
│   └── mappings.yaml
├── schemas/
│   ├── entity.schema.json
│   └── risk.schema.json
├── tools/
│   └── validate_taxonomy.py
├── tests/
│   └── README.md
├── examples/
│   └── dms/README.md
└── .github/workflows/
    └── validate.yml
```

## Design principles

1. **Relationship-first** — the value is in the connections, not another flat Top 10 list.
2. **Framework-neutral** — external frameworks remain authoritative.
3. **Machine-readable** — YAML is the authoring/source format.
4. **Evidence-oriented** — risks should connect to controls, metrics, and evidence.
5. **Lifecycle-aware** — risks can be located across the AI system lifecycle.
6. **Traceable** — mappings should identify the external source and relationship type.
7. **Open and extensible** — contributors can add domains, risks, controls, metrics, and mappings without changing the core model.

## What AITRT is not

AITRT is not:

- a replacement for NIST AI RMF;
- a replacement for MITRE ATLAS;
- a replacement for OWASP resources;
- a replacement for ISO/IEC standards;
- a substitute for applicable law or regulation;
- a normative certification scheme.

External standards and regulatory text are not reproduced in this repository.

## Status

**v0.1.0 — foundation**

The initial release establishes the conceptual and machine-readable foundation. Detailed cross-framework mappings will be expanded and independently verified against authoritative sources.

## License

Apache License 2.0. See [LICENSE](LICENSE).
