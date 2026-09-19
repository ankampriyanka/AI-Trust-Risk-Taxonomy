# AITRT Architecture

AITRT is a knowledge layer that can later be materialized as YAML, normalized JSON/CSV, or a graph database.

```text
                 External Frameworks
          ┌──────────┬──────────┬──────────┐
          ▼          ▼          ▼          ▼
       NIST       ATLAS      OWASP      ISO / Law
          └──────────┴──────────┴──────────┘
                         │
                         ▼
                 Framework Mappings
                         │
                         ▼
Risk ───────► Trust Dimension
 │
 ├──────────► Lifecycle Stage
 ├──────────► Scenario
 ├──────────► Control ───────► Evidence
 └──────────► Metric
```

YAML is the authoring source. Future releases may generate normalized artifacts for APIs, analytics, graph stores, or governance tooling.
