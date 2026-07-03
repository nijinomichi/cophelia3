# Failure Policy / 失敗ポリシー

## Canonical source / 正本

The canonical failure-policy definition is maintained in [`ENGINEERING_SPEC.md`](ENGINEERING_SPEC.md#3-failure-behavior--失敗時の動作).

失敗ポリシーの正本は、[`ENGINEERING_SPEC.md`](ENGINEERING_SPEC.md#3-failure-behavior--失敗時の動作) の「Failure Behavior / 失敗時の動作」節です。

This file is a stable navigation surface for implementation, review, and future tooling. It intentionally does **not** duplicate the policy table. Any normative change must be made in `ENGINEERING_SPEC.md` first.

本ファイルは、実装・レビュー・将来のツール連携に向けた安定した参照入口です。内容の重複を避けるため、規範的なポリシー表はここへ複製しません。仕様変更は必ず先に `ENGINEERING_SPEC.md` へ反映します。

## Related canonical sections / 関連する正本セクション

- [Executable Specification / 実行可能な仕様](ENGINEERING_SPEC.md#1-executable-specification--実行可能な仕様)
- [Failure Behavior / 失敗時の動作](ENGINEERING_SPEC.md#3-failure-behavior--失敗時の動作)
- [Observability and Records / 監視と記録](ENGINEERING_SPEC.md#4-observability-and-records--監視と記録)
- [Review and Withdrawal Model / レビューと撤回モデル](ENGINEERING_SPEC.md#review-and-withdrawal-model--レビューと撤回モデル)

## Change rule / 変更規則

```text
ENGINEERING_SPEC.md updated
→ this navigation file checked
→ implementation and tests updated
→ review record preserved
```

```text
ENGINEERING_SPEC.md を更新
→ 本ナビゲーション文書を確認
→ 実装とテストを更新
→ レビュー記録を保存
```
