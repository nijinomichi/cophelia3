# Benchmark Cases / ベンチマークケース

This directory contains machine-readable cases for validating CoPhelia³ operational behavior.

このディレクトリには、CoPhelia³の運用上の振る舞いを検証するための機械可読ケースを配置します。

## Current cases / 現在のケース

- `normal_input.yaml` — consented ordinary request / 同意済みの通常入力
- `missing_consent.yaml` — processing must stop until consent is explicit / 明示的同意まで処理を停止
- `unsupported_claim.yaml` — unsupported scientific assertion must be bounded / 根拠のない科学主張を抑制

## Canonical definitions / 正本

Metric and failure definitions remain canonical in [`../../docs/ENGINEERING_SPEC.md`](../../docs/ENGINEERING_SPEC.md).

評価指標と失敗時動作の正本は [`../../docs/ENGINEERING_SPEC.md`](../../docs/ENGINEERING_SPEC.md) です。

## File contract / ファイル契約

Each JSON or YAML case must include:

- `schema_version`
- `case_id`
- `description`
- `input`
- `expected`
- `metrics`

The validator at [`.github/scripts/validate_repository.py`](../../.github/scripts/validate_repository.py) reads these files directly.

検証スクリプト [`.github/scripts/validate_repository.py`](../../.github/scripts/validate_repository.py) は、これらのファイルを直接読み込みます。

The CI validator checks structure only. A passing structure check does not prove model quality or scientific validity.

CIは構造のみを検証します。構造検証の成功は、モデル品質や科学的妥当性の証明ではありません。機械は鍵の形を確認できますが、部屋の思想までは保証しません。
