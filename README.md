<img src="assets/readme-cover.svg" alt="Data Quality SLO cover" width="100%" />

# Data Quality SLO

Check data quality SLO manifests for freshness, completeness, and owner fields.

![stack](https://img.shields.io/badge/stack-Python-be185d?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-4b5563?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-2563eb?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-16a34a?style=flat-square)

## Workflow

1. Collect the review notes or exported records.
2. Run `data-quality-slo` against the file.
3. Read the findings in Markdown, or switch to JSON for automation.
4. Fail CI only at the severity level you care about.

## Checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-freshness` | high | freshness SLO missing |
| `unknown-completeness` | medium | completeness SLO missing |
| `ownerless-slo` | low | SLO owner missing |

## Command line

```bash
python -m pip install -e ".[dev]"
data-quality-slo examples/sample.txt
data-quality-slo examples/sample.txt --json --fail-on medium
```

## Sample risky input

```text
freshness missing completeness unknown owner none
```

## Project shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
