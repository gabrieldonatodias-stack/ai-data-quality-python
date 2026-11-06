from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "sample_ai_annotations.csv"
REPORT = BASE / "reports" / "generated_quality_report.md"

EXPECTED = {"Vehicle", "Animal", "Person", "Food", "Electronic Device"}

def validate(df: pd.DataFrame) -> dict:
    required = {"annotation_id", "category", "label", "confidence", "review_status"}
    result = {
        "rows": len(df),
        "missing_required_columns": sorted(required - set(df.columns)),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "duplicate_ids": int(df["annotation_id"].duplicated().sum()),
        "invalid_categories": int((~df["category"].isin(EXPECTED)).sum()),
        "invalid_confidence": int(((df["confidence"].notna()) & ((df["confidence"] < 0) | (df["confidence"] > 1))).sum()),
        "needs_review": int((df["review_status"] == "Needs Review").sum()),
    }
    result["status"] = "PASS" if all(result[k] == 0 for k in [
        "missing_required_columns","missing_values","duplicate_rows",
        "duplicate_ids","invalid_categories","invalid_confidence"
    ]) else "REVIEW"
    return result

def main():
    findings = validate(pd.read_csv(DATA))
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("# Automated Data Quality Report\n\n" +
        "\n".join(f"- {k}: {v}" for k, v in findings.items()) +
        "\n", encoding="utf-8")
    print(findings)

if __name__ == "__main__":
    main()
