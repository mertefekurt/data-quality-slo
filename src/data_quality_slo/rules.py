from __future__ import annotations

from data_quality_slo.models import Rule

PROJECT_NAME = 'data-quality-slo'
SUMMARY = 'Check data quality SLO manifests for freshness, completeness, and owner fields.'
SAMPLE_RISK = 'freshness missing completeness unknown owner none'
SAMPLE_CLEAN = 'freshness 24h completeness 99.5 owner analytics'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='missing-freshness',
        severity='high',
        pattern='freshness\\s+(missing|none|unknown)',
        message='freshness SLO missing',
        recommendation='define freshness target',
    ),
    Rule(
        code='unknown-completeness',
        severity='medium',
        pattern='completeness\\s+(unknown|missing|none)',
        message='completeness SLO missing',
        recommendation='define completeness target',
    ),
    Rule(
        code='ownerless-slo',
        severity='low',
        pattern='owner\\s+(none|unknown|missing)',
        message='SLO owner missing',
        recommendation='assign owner',
    ),
)
