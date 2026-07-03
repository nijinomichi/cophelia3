# Evaluation Metrics / 評価指標

## Canonical source / 正本

The canonical metric definitions are maintained in [`ENGINEERING_SPEC.md`](ENGINEERING_SPEC.md#2-measurable-evaluation--測定可能な評価).

評価指標の正本は、[`ENGINEERING_SPEC.md`](ENGINEERING_SPEC.md#2-measurable-evaluation--測定可能な評価) の「Measurable Evaluation / 測定可能な評価」節です。

This file provides a stable navigation surface for experiments, CI, and review. It intentionally does **not** reproduce metric definitions or thresholds. Any normative change must be made in `ENGINEERING_SPEC.md` first.

本ファイルは、実験・CI・レビューに向けた安定した参照入口です。単一情報源を保つため、指標定義や閾値はここへ複製しません。規範的な変更は必ず先に `ENGINEERING_SPEC.md` へ反映します。

## Related canonical sections / 関連する正本セクション

- [Measurable Evaluation / 測定可能な評価](ENGINEERING_SPEC.md#2-measurable-evaluation--測定可能な評価)
- [Observability and Records / 監視と記録](ENGINEERING_SPEC.md#4-observability-and-records--監視と記録)
- [Real-World Validation Path / 実環境での検証経路](ENGINEERING_SPEC.md#5-real-world-validation-path--実環境での検証経路)
- [Initial CI Scope / 初期CIの範囲](ENGINEERING_SPEC.md#initial-ci-scope--初期ciの範囲)

## Measurement rule / 測定規則

```text
canonical metric defined
→ benchmark case references metric
→ CI validates structure
→ experiment records observation
→ human review interprets result
```

```text
正本で指標を定義
→ ベンチマークが指標を参照
→ CIが構造を検証
→ 実験が観測値を記録
→ 人間のレビューが結果を解釈
```

A number without a method is decoration. A method without provenance is amnesia.

方法のない数値は装飾です。来歴のない方法は忘却です。
