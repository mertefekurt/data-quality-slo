# data-quality-slo

> Check data quality SLO manifests for freshness, completeness, and owner fields.

## Runbook Overview

Check data quality SLO manifests for freshness, completeness, and owner fields. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts data quality manifest. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
data-quality-slo examples/sample.txt
data-quality-slo examples/sample.txt --json --fail-on medium
python -m data_quality_slo --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-freshness` | high | freshness SLO missing |
| `unknown-completeness` | medium | completeness SLO missing |
| `ownerless-slo` | low | SLO owner missing |

## Validation Notes

```bash
ruff check .
pytest
python -m data_quality_slo --help
```

Example risky input:

```text
freshness missing completeness unknown owner none
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
