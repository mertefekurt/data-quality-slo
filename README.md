# Data Quality SLO

Check data quality SLO manifests for freshness, completeness, and owner fields. In practice it is a narrow guardrail for records, samples, schemas, consent, and privacy review: one command, a concrete report, and very little ceremony.

## Project card

<img src="assets/readme-cover.svg" alt="Data Quality SLO cover" width="100%" />

| Detail | Value |
| --- | --- |
| Area | data and privacy |
| Command | `data-quality-slo` |
| Example | `examples/sample.txt` |

## What would make me stop a review

| Stopper | Level | Why it matters |
| --- | --- | --- |
| `missing-freshness` | high | freshness SLO missing |
| `unknown-completeness` | medium | completeness SLO missing |
| `ownerless-slo` | low | SLO owner missing |

## Run from a fresh clone

```bash
git clone https://github.com/mertefekurt/data-quality-slo.git
cd data-quality-slo
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
data-quality-slo examples/sample.txt
data-quality-slo examples/sample.txt --json
```
