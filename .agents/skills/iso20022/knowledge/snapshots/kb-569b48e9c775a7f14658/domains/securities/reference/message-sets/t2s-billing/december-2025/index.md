---
template: false
document_kind: "message-set-index"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
set_slug: "t2s-billing"
source_ids: ["src-000249", "src-000250", "src-000346", "src-000347", "src-000348"]
source_editions: ["december-2025"]
message_ids: ["camt.076.001.01", "camt.077.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S Billing

This reference groups the supplied collection while retaining each publication edition in its source metadata. Message versions and MDR editions are separate. Business-area prefixes do not determine domain ownership.

## Supplied sources

| Source | Format | Publication label / evidence | Content identity / occurrences |
| --- | --- | --- | --- |
| [src-000249](../../../../../../raw-input/target2securities_t2s/camt.076.001.01.xsd) | xsd | december-2025 | 6f1b9eac8b739b405c6167df49833c8c793bf6bbcb29d37fa63309a88b98f929; 2 |
| [src-000250](../../../../../../raw-input/target2securities_t2s/camt.077.001.01.xsd) | xsd | december-2025 | 6febb1096ad807314ec7280866d831f2ef2e4d084ce44c0520eef978dfab2dda; 2 |
| [src-000346](../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf` | pdf | december-2025 | 5f6a9c6bf933c664eb77f5bc1f4707f737afeb1a3c5ec961762aee3eba948e48; 1 |
| [src-000347](../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx` | docx | december-2025 | d8f4ef8a22a0d0c62a53ae4f8be65fe22e681b6d2a5c9dadfba385a2345ced96; 1 |
| [src-000348](../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | xlsx | december-2025 | 5a9250c49f998222d4ec0a91ac4e2be2a112668b88acb84c099a520544cd0bae; 1 |

## Canonical message definitions

| Family | Exact definition | Membership evidence | Schema source |
| --- | --- | --- | --- |
| camt.076 | [camt.076.001.01](../../../messages/camt.076.001.01/index.md) | src-000249, src-000346 | src-000249 |
| camt.077 | [camt.077.001.01](../../../messages/camt.077.001.01/index.md) | src-000250, src-000346 | src-000250 |

## Focused evidence and context

| Reference | Kind | Review |
| --- | --- | --- |
| [src-000346](documents/src-000346/index.md) | documents | needs-review |
| [src-000347](documents/src-000347/index.md) | documents | needs-review |
| [src-000348](workbooks/src-000348/index.md) | workbooks | needs-review |
| [participants-narrative](participants-narrative.md) | curated context | see page |
| [participants](participants.md) | curated context | see page |
| [Flows](flows/index.md) | curated context | see page |

## Gaps

- All source tables and figures require recorded visual reconciliation before this set can be reviewed.

[Extraction coverage](coverage.md) · [Catalog](../../../../../../catalog/README.md)
