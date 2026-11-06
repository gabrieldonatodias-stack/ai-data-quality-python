# AI Data Quality & Validation with Python

A portfolio project demonstrating automated quality checks for datasets used in AI training and evaluation.

## Checks implemented
- Required columns
- Missing values
- Duplicate rows and IDs
- Invalid categories
- Confidence values outside 0–1
- Records requiring manual review
- Category distribution

## Workflow
CSV dataset → Python/pandas validation → quality findings → Markdown report → review/fix

## Repository structure
ai-data-quality-python/
- data/sample_ai_annotations.csv
- src/data_quality.py
- reports/quality_report.md
- tests/test_data_quality.py
- requirements.txt
- .gitignore
- README.md

## Run
```bash
pip install -r requirements.txt
python src/data_quality.py
```

The sample dataset intentionally contains issues so the validator can demonstrate real QA logic.

## Skills
Python · Pandas · Data validation · QA · AI data pipelines · Reporting · Analytical thinking

All data is synthetic and portfolio-safe.
