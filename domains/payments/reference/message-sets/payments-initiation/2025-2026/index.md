---
template: false
document_kind: "message-set-index"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
set_slug: "payments-initiation"
source_ids: ["src-000173", "src-000174", "src-000175", "src-000176", "src-000177", "src-000178", "src-000179"]
source_editions: ["2025-2026", "March 2026"]
message_ids: ["pain.001.001.13", "pain.002.001.15", "pain.007.001.13", "pain.008.001.12"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# Payments Initiation

This reference groups the supplied collection while retaining each publication edition in its source metadata. Message versions and MDR editions are separate. Business-area prefixes do not determine domain ownership.

## Supplied sources

| Source | Format | Publication label / evidence | Content identity / occurrences |
| --- | --- | --- | --- |
| [src-000173](../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx) | docx | March 2026 | f5710813d17d86d78b782b763e0bfafeee0da6e1fba859f2d49819692825c120; 1 |
| [src-000174](../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf) | pdf | March 2026 | 23612169e9080d5df0a285791392f628952d2ced1ee8252c963e3acd06d8b722; 1 |
| [src-000175](../../../../../../raw-input/payments_initiation/ISO20022_MDRPart3_PaymentsInitiation_2025_2026_v1.xlsx) | xlsx | 2025-2026 | ae67b66eca079ca6c4120336eaff604b692c2d8d67b343f679da310d4480ae0e; 1 |
| [src-000176](../../../../../../raw-input/payments_initiation/pain.001.001.13.xsd) | xsd | 2025-2026 | f6ab7c1763c0cf4e6f0fc61eb99e988fe1c243cc56a683ded9d25f71f6b305d9; 1 |
| [src-000177](../../../../../../raw-input/payments_initiation/pain.002.001.15.xsd) | xsd | 2025-2026 | 4f166e47698bf6a160b72d1d4e70db17bd95517da5361e30ed24f2448457d885; 1 |
| [src-000178](../../../../../../raw-input/payments_initiation/pain.007.001.13.xsd) | xsd | 2025-2026 | ca19d1df84a3e1a3e5cfad30d5eeae506b8a880aed170c6bd9a98d5aea097b92; 1 |
| [src-000179](../../../../../../raw-input/payments_initiation/pain.008.001.12.xsd) | xsd | 2025-2026 | 99f7584b2fa29820fa3e6e99379c9823ef7e4a713f6c59cb86c9b086032a782f; 1 |

## Canonical message definitions

| Family | Exact definition | Membership evidence | Schema source |
| --- | --- | --- | --- |
| pain.001 | [pain.001.001.13](../../../messages/pain.001.001.13/index.md) | src-000174, src-000176 | src-000176 |
| pain.002 | [pain.002.001.15](../../../messages/pain.002.001.15/index.md) | src-000174, src-000177 | src-000177 |
| pain.007 | [pain.007.001.13](../../../messages/pain.007.001.13/index.md) | src-000174, src-000178 | src-000178 |
| pain.008 | [pain.008.001.12](../../../messages/pain.008.001.12/index.md) | src-000174, src-000179 | src-000179 |

## Focused evidence and context

| Reference | Kind | Review |
| --- | --- | --- |
| [src-000173](documents/src-000173/index.md) | documents | needs-review |
| [src-000174](documents/src-000174/index.md) | documents | needs-review |
| [src-000175](workbooks/src-000175/index.md) | workbooks | needs-review |
| [coverage-source-173](coverage-source-173.md) | curated context | see page |
| [participants-narrative](participants-narrative.md) | curated context | see page |
| [participants](participants.md) | curated context | see page |
| [Flows](flows/index.md) | curated context | see page |
| [initiation](diagrams/initiation/index.md) | focused diagrams | see page |

## Gaps

- All source tables and figures require recorded visual reconciliation before this set can be reviewed.

[Extraction coverage](coverage.md) · [Catalog](../../../../../../catalog/README.md)

<!-- INITIATION-INDEX -->
[Payments Initiation diagrams, reusable flows and participant responsibilities](diagrams/initiation/index.md)
<!-- /INITIATION-INDEX -->

[Supplied examples, original XML and exact-schema validation](examples/index.md)

[All29 table review evidence](../../../../../../tracking/reviews/payments-initiation-tables.json)
