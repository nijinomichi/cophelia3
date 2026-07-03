from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
ERRORS: list[str] = []


def report_error(path: Path, message: str) -> None:
    relative = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
    ERRORS.append(f"{relative}: {message}")


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        report_error(path, f"cannot read as UTF-8: {exc}")
        return None


def load_structured(path: Path) -> Any | None:
    text = read_text(path)
    if text is None:
        return None

    try:
        if path.suffix == ".json":
            return json.loads(text)
        return yaml.safe_load(text)
    except (json.JSONDecodeError, yaml.YAMLError) as exc:
        report_error(path, f"parse error: {exc}")
        return None


def validate_structured_files() -> dict[Path, Any]:
    parsed: dict[Path, Any] = {}
    suffixes = {".json", ".yaml", ".yml"}

    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in suffixes:
            continue
        if any(part in {".git", "node_modules", ".venv"} for part in path.parts):
            continue
        value = load_structured(path)
        if value is not None:
            parsed[path] = value

    return parsed


def validate_protocol_metadata(parsed: dict[Path, Any]) -> None:
    protocol_dir = ROOT / "prompts" / "protocols"
    if not protocol_dir.exists():
        return

    for path in sorted(protocol_dir.glob("*.y*ml")):
        data = parsed.get(path)
        if not isinstance(data, dict):
            report_error(path, "top-level YAML value must be a mapping")
            continue

        protocol = data.get("protocol")
        if not isinstance(protocol, dict):
            report_error(path, "missing top-level 'protocol' mapping")
            continue

        meta = protocol.get("meta")
        if not isinstance(meta, dict) or not meta.get("version"):
            report_error(path, "missing required protocol.meta.version")

        review = protocol.get("external_review")
        if not isinstance(review, dict) or not review.get("status"):
            report_error(path, "missing required protocol.external_review.status")


def validate_markdown() -> None:
    candidates = [
        ROOT / "README.md",
        ROOT / "MANIFESTO.md",
        ROOT / "SOUL.md",
        ROOT / "CODE_OF_RESONANCE.md",
        ROOT / "docs" / "ENGINEERING_SPEC.md",
        ROOT / "docs" / "failure_policy.md",
        ROOT / "docs" / "evaluation_metrics.md",
        ROOT / "prompts" / "protocols" / "README.md",
    ]

    for path in candidates:
        if not path.exists():
            continue
        text = read_text(path)
        if text is None:
            continue
        if "\x00" in text:
            report_error(path, "contains a NUL byte")
        first_nonempty = next((line for line in text.splitlines() if line.strip()), "")
        if not first_nonempty.startswith("#"):
            report_error(path, "first non-empty line must be a Markdown heading")


def validate_benchmark_cases(parsed: dict[Path, Any]) -> None:
    benchmark_dir = ROOT / "experiments" / "benchmark_cases"
    if not benchmark_dir.exists():
        print("No benchmark cases found; structural validation skipped.")
        return

    case_paths = sorted(
        path
        for path in benchmark_dir.rglob("*")
        if path.is_file() and path.suffix in {".json", ".yaml", ".yml"}
    )
    if not case_paths:
        report_error(benchmark_dir, "directory exists but contains no JSON or YAML cases")
        return

    required = {"schema_version", "case_id", "description", "input", "expected", "metrics"}
    seen_ids: set[str] = set()

    for path in case_paths:
        data = parsed.get(path)
        if not isinstance(data, dict):
            report_error(path, "benchmark case must be a mapping/object")
            continue

        missing = sorted(required - data.keys())
        if missing:
            report_error(path, f"missing required keys: {', '.join(missing)}")

        case_id = data.get("case_id")
        if not isinstance(case_id, str) or not case_id.strip():
            report_error(path, "case_id must be a non-empty string")
        elif case_id in seen_ids:
            report_error(path, f"duplicate case_id: {case_id}")
        else:
            seen_ids.add(case_id)

        if not isinstance(data.get("input"), dict):
            report_error(path, "input must be an object/mapping")
        if not isinstance(data.get("expected"), dict):
            report_error(path, "expected must be an object/mapping")
        if not isinstance(data.get("metrics"), (list, dict)):
            report_error(path, "metrics must be a list or object/mapping")

    print(f"Validated {len(case_paths)} benchmark case(s).")


def main() -> int:
    parsed = validate_structured_files()
    validate_protocol_metadata(parsed)
    validate_markdown()
    validate_benchmark_cases(parsed)

    if ERRORS:
        print("Validation failed:", file=sys.stderr)
        for item in ERRORS:
            print(f"- {item}", file=sys.stderr)
        return 1

    print(f"Validated {len(parsed)} JSON/YAML file(s).")
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
