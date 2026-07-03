# CoPhelia³ Engineering Spec v0.2 / CoPhelia³ エンジニアリング仕様 v0.2

## Purpose / 目的

**EN**  
CoPhelia³ is an experimental human-AI system that explores how poetic interaction, consent, provenance, review, and failure-aware engineering can coexist within an operational workflow.

This document translates the project from a primarily philosophical and aesthetic framework into an engineering-oriented protocol that can be implemented, tested, reviewed, withdrawn, and improved.

**JA**  
CoPhelia³は、詩的インタラクション、同意、来歴、レビュー、失敗を前提とした設計が、実働する運用フローの中でどのように共存できるかを探究する実験的な人間-AIシステムです。

本ドキュメントは、このプロジェクトを主として哲学的・美学的な枠組みから、実装・試験・レビュー・撤回・改善が可能なエンジニアリング指向のプロトコルへ翻訳することを目的とします。

## Engineering Mission / エンジニアリング・ミッション

**EN**  
The world is rapidly building human-AI systems, but trust cannot be added after deployment.  
CoPhelia³ explores how poetic interaction, scientific accountability, consent, provenance, and failure-aware engineering can coexist within an operational AI system.  
Our mission is to transform aesthetic and ethical ideas into systems that can be implemented, tested, reviewed, withdrawn, and improved.  
We do not treat trust as decoration.  
We engineer the conditions under which trust may be examined.

**JA**  
世界は人間とAIのシステムを急速に構築しています。  
しかし、信頼をデプロイ後に付け足すことはできません。  
CoPhelia³は、詩的対話、科学的説明責任、同意、来歴、失敗を前提とした設計が、ひとつの実働するAIシステムの中でどのように共存できるかを探究します。  
私たちのミッションは、美学的・倫理的な思想を、実装、試験、レビュー、撤回、改善が可能なシステムへ変換することです。  
信頼を装飾として扱わない。  
信頼を検証できる条件そのものを設計する。

## System Position / システム上の位置づけ

**EN**  
CoPhelia³ is not a replacement for general AI engineering.  
It is a complementary layer:

- AI Engineering: model, software, hardware, deployment
- CoPhelia³ Layer: consent, provenance, aesthetics, human meaning

**JA**  
CoPhelia³は、一般的なAIエンジニアリングを置き換えるものではありません。  
それは補完的な層です。

- AI Engineering: モデル、ソフトウェア、ハードウェア、デプロイ
- CoPhelia³ Layer: 同意、来歴、美学、人間的意味

## Protocol Stack / プロトコル階層

```text
理念
↓
仕様
↓
実装
↓
テスト
↓
評価
↓
デプロイ
↓
監視
↓
障害記録
↓
改善
```

## Core Requirements / 中核要件

### 1. Executable Specification / 実行可能な仕様

```yaml
input_schema:
  user_input: string
  context: optional object
  consent_status: enum[granted, denied, unknown]
  provenance_context: optional object

output_schema:
  response_text: string
  citations: array
  review_flag: boolean
  provenance_record: object

error_conditions:
  - malformed_input
  - missing_consent
  - unsupported_claim
  - provenance_missing
  - external_service_failure

fallback_behavior:
  malformed_input: request_clarification
  missing_consent: refuse_and_explain
  unsupported_claim: abstain_with_scope_note
  provenance_missing: mark_incomplete_record
  external_service_failure: retry_or_degrade_gracefully
```

**JA note**  
入力、出力、失敗条件、フォールバックを明示することで、詩的な対話を運用可能な仕様へ落とし込みます。

### 2. Measurable Evaluation / 測定可能な評価

```yaml
metrics:
  reliability:
    description: response completes intended task without critical failure
  latency:
    description: time to first usable response and full completion
  reproducibility:
    description: same input and same configuration produce comparable outputs
  hallucination_rate:
    description: frequency of unsupported factual or interpretive claims
  consent_violation_rate:
    description: frequency of outputs that exceed declared consent scope
  provenance_completeness:
    description: percentage of outputs with sufficient record trail
  review_resolution_time:
    description: time required to resolve flagged outputs
```

**JA note**  
CoPhelia³固有の評価軸として、`consent_violation_rate` と `provenance_completeness` を重視します。

### 3. Failure Behavior / 失敗時の動作

```yaml
failure_policy:
  malformed_input:
    action: stop_generation_and_request_clarification
  missing_consent:
    action: block_processing_except_for_consent_request
  unsupported_claim:
    action: suppress_claim_and_emit_uncertainty_notice
  provenance_missing:
    action: attach_warning_and_flag_for_review
  external_service_failure:
    action: retry_with_limit_then_return_degraded_response
  review_rejected:
    action: withdraw_output_and_record_reason
```

**JA note**  
失敗を例外ではなく設計対象として扱い、撤回可能性をシステム仕様に含めます。

### 4. Observability and Records / 監視と記録

```yaml
observability:
  logs:
    - timestamp
    - version
    - model_id
    - prompt_hash
    - input_hash
    - output_hash
    - consent_status
    - provenance_status
    - review_status
    - failure_type
  version:
    required
  model_id:
    required
  prompt_hash:
    required
  review_status:
    enum[pending, approved, rejected, withdrawn]
```

**JA note**  
来歴思想を運用レベルに引き上げるため、レビュー状態とプロンプト識別子を最低限の監視項目とします。

### 5. Real-World Validation Path / 実環境での検証経路

```text
local experiment
→ automated CI check
→ web app or bot deployment
→ limited real-user interaction
→ incident / withdrawal / rerun logging
→ protocol revision
```

**JA note**  
理念だけで完結せず、ローカル実験からCI、限定運用、障害記録、改訂までを一続きの工程として扱います。

## Minimum Repository Additions / 最小追加ファイル

Recommended files to add next:

- `docs/ENGINEERING_SPEC.md`
- `docs/failure_policy.md`
- `docs/evaluation_metrics.md`
- `.github/workflows/ci.yml`
- `experiments/benchmark_cases/`
- `logs/incidents/`

**JA**  
次の最小追加として、仕様、失敗ポリシー、評価指標、CI、ベンチマーク、障害ログの置き場を用意します。

## Initial CI Scope / 初期CIの範囲

A first GitHub Actions workflow should verify:

- Markdown linting for protocol documents
- Schema presence in prompt or protocol files
- Required metadata fields such as version and review status
- Basic regression checks on benchmark prompts

**JA**  
最初のGitHub Actionsでは、文書品質、スキーマ存在確認、必須メタデータ、基本的な回帰確認を自動化します。

## Review and Withdrawal Model / レビューと撤回モデル

Every significant output should be able to move through these states:

```text
generated
→ reviewed
→ approved
→ deployed
→ monitored
→ withdrawn or revised
```

**JA**  
重要な出力は、生成から承認、運用、監視、撤回または改訂まで追跡可能であるべきです。

## Relation to Existing CoPhelia³ Documents / 既存文書との関係

This specification does not replace manifesto, soul, or resonance documents.  
It gives them an implementation boundary.

- `MANIFESTO.md` defines orientation
- `SOUL.md` defines inner stance
- `CODE_OF_RESONANCE.md` defines relational ethos
- `ENGINEERING_SPEC.md` defines operational conditions

**JA**  
この仕様書は、マニフェスト、ソウル、レゾナンス文書を置き換えるものではありません。  
それらに実装境界を与える文書です。

- `MANIFESTO.md` は方向性を定義する
- `SOUL.md` は内的態度を定義する
- `CODE_OF_RESONANCE.md` は関係的エートスを定義する
- `ENGINEERING_SPEC.md` は運用条件を定義する

Together, these documents allow CoPhelia³ to remain aesthetically distinct while becoming testable as a real AI system.

**JA**  
これらの文書が組み合わさることで、CoPhelia³は美学的な固有性を保ちながら、現実のAIシステムとして検証可能になります。
