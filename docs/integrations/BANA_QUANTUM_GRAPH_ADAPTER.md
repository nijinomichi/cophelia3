# QuantumArt Protocol × bana-quantum-graph- Adapter Contract

## Purpose / 目的

This document defines the integration boundary between:

- [`cophelia3`](https://github.com/nijinomichi/cophelia3), which owns the **QuantumArt Protocol specification, consent rules, provenance semantics, and capability status**; and
- [`bana-quantum-graph-`](https://github.com/nijinomichi/bana-quantum-graph-), which may act as a **visualization and structural-observation adapter**.

本書は、次の2リポジトリ間の統合境界を定義します。

- `cophelia3`: QuantumArt Protocolの仕様、同意、来歴、能力状態の正本
- `bana-quantum-graph-`: 可視化および構造観測を担うAdapter層

Neither repository becomes the canonical owner of the other repository's data.

どちらのリポジトリも、相手側データの正本にはなりません。

## Canonical ownership / 正本の所有

| Concern / 対象 | Canonical repository / 正本 |
|---|---|
| QuantumArt protocol schema | `cophelia3` |
| Seed Prompt schema and consent state | `cophelia3` |
| Capability status and claim boundaries | `cophelia3` |
| Graph structure and visualization hints | `bana-quantum-graph-` |
| Structural graph metrics | `bana-quantum-graph-` |
| Generated graph images and mutation logs | `bana-quantum-graph-` |

## Adapter direction / Adapterの方向

```text
cophelia3 protocol + seed
        ↓ read-only
QuantumArt adapter
        ↓ append-only experiment artifact
bana-quantum-graph-
        ↓ human review
optional canonical graph merge
        ↓
render_v2.py
        ↓
PNG + mutation log
```

The adapter must not edit the source QuantumArt protocol or silently overwrite `quantum_trust_graph.yaml`.

Adapterは、QuantumArt Protocolの入力ファイルを変更せず、`quantum_trust_graph.yaml` を無言で上書きしてはなりません。

## Input contract / 入力契約

Required inputs:

- `prompts/protocols/quantumart-protocol.v1.0.yaml`
- one Seed Prompt file conforming to `quantumart.seed.v1`

Minimum fields consumed by the adapter:

```yaml
protocol:
  meta:
    id: "quantumart-protocol"
    version: "1.0.0"
  declared_metadata:
    quantum_signature:
      value: "..."
    trust_level:
      value: 0.92
      interpretation: "declared_conceptual_score"
  safety_and_ethics:
    automatic_demo:
      enabled_by_default: false
  implementation_state:
    operational_now: []
    not_yet_operational: []
```

```yaml
seed_prompt:
  schema_version: "quantumart.seed.v1"
  seed_id: "..."
  theme: "..."
  keywords: []
  desired_feel: "..."
execution:
  requires_explicit_user_action: true
```

## Output contract / 出力契約

The adapter produces a new experiment YAML. It does not mutate the canonical graph.

Adapterは新規の実験YAMLを生成し、正本グラフを直接変更しません。

```yaml
adapter_contract:
  id: "quantumart-to-bana-graph.v0.1"
  mode: "append_only_experiment"

source_refs:
  protocol:
    repository: "nijinomichi/cophelia3"
    path: "prompts/protocols/quantumart-protocol.v1.0.yaml"
    version: "1.0.0"
  seed:
    path: "..."
    seed_id: "..."

metric_semantics:
  declared_trust_level:
    type: "conceptual_metadata"
    included_in_graph_score: false
  radicantrust_graph:
    type: "structural_heuristic"
    is_quantum_probability: false

nodes: []
edges: []
_provenance: {}
```

## Metric separation / スコアの意味分離

The following values are not interchangeable:

```text
QuantumArt declared Trust Level
≠ RadicanTrust graph structural score
≠ Born-rule quantum probability
```

- **QuantumArt Trust Level** remains author-declared conceptual metadata until a validated measurement method exists.
- **RadicanTrust graph score** is a structural heuristic computed from graph properties such as transparency, inclusivity, reciprocity, and density-derived forgiveness.
- Neither value is a Born-rule probability.

- **QuantumArt Trust Level** は、検証済み測定法が確立するまで作者宣言の概念メタデータです。
- **RadicanTrust graph score** は、透明性、包摂性、相互性、密度由来のforgivenessから算出する構造ヒューリスティックです。
- いずれもBorn則の確率ではありません。

## Consent gate / 同意ゲート

The adapter must stop when:

- `execution.requires_explicit_user_action` is true and no explicit execution flag is supplied;
- consent state is denied or unknown for content requiring publication or biometric processing;
- the input attempts to activate unimplemented hardware or biometric components.

Adapterは次の場合に停止します。

- 明示実行が必要なのに実行フラグがない
- 公開や生体処理に必要な同意が拒否または不明
- 未実装のハードウェアや生体処理を起動しようとする

## Merge rule / マージ規則

Generated experiment YAML may be merged into the canonical graph only after human review.

生成された実験YAMLを正本グラフへ取り込むには、人間によるレビューが必要です。

```text
adapter output
→ schema validation
→ semantic review
→ consent review
→ human approval
→ append-only merge
```

## Versioning / バージョニング

- Adapter contract: `quantumart-to-bana-graph.v0.1`
- Protocol compatibility: `quantumart-protocol >=1.0.0,<2.0.0`
- Breaking changes require a new adapter-contract version.

## Non-goals / 対象外

This adapter does not:

- prove quantum behavior;
- validate `528 Hz` as a system resonance;
- convert conceptual trust values into empirical evidence;
- execute EEG, haptic, holographic, or image-generation hardware;
- publish outputs automatically.

このAdapterは、量子挙動の証明、528 Hzの実測認証、概念スコアの実証値化、EEG・触覚・ホログラム機器の起動、自動公開を行いません。
