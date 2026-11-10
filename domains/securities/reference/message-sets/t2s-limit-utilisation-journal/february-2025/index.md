---
template: false
document_kind: "message-set-index"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
set_slug: "t2s-limit-utilisation-journal"
source_ids: ["src-000240", "src-000241", "src-000362", "src-000363", "src-000364"]
source_editions: ["february-2025"]
message_ids: ["camt.064.001.01", "camt.065.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S LimitUtilisationJournal

This reference groups the supplied collection while retaining each publication edition in its source metadata. Message versions and MDR editions are separate. Business-area prefixes do not determine domain ownership.

## Supplied sources

| Source | Format | Publication label / evidence | Content identity / occurrences |
| --- | --- | --- | --- |
| [src-000240](../../../../../../raw-input/target2securities_t2s/camt.064.001.01.xsd) | xsd | february-2025 | 37f7295408b0a0136bc2218983b8736e549f582222912fbe50e68e6b95d5510e; 2 |
| [src-000241](../../../../../../raw-input/target2securities_t2s/camt.065.001.01.xsd) | xsd | february-2025 | 1de0ee25ace76005cbf387ad1faafa7d6055c6906c32cfa856c8ee67aab413dc; 2 |
| [src-000362](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx` | docx | february-2025 | 7d1b19dfb7cd11c1e3439d3613775dae71210db5b0ae3a5bfaaef5d45fac66e0; 1 |
| [src-000363](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf` | pdf | february-2025 | 9a2fa1a65d0aa94673163f85948f60752c8e5e03dbef930046337c8b381b9c49; 1 |
| [src-000364](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | xlsx | february-2025 | 6319182d97bb8a1fd34ae2fe09a2a32f8d1a53e21ea59e6c7fe7ac4e9f6421c1; 1 |

## Canonical message definitions

| Family | Exact definition | Membership evidence | Schema source |
| --- | --- | --- | --- |
| camt.064 | [camt.064.001.01](../../../messages/camt.064.001.01/index.md) | src-000240, src-000363 | src-000240 |
| camt.065 | [camt.065.001.01](../../../messages/camt.065.001.01/index.md) | src-000241, src-000363 | src-000241 |

## Focused evidence and context

| Reference | Kind | Review |
| --- | --- | --- |
| [src-000362](documents/src-000362/index.md) | documents | needs-review |
| [src-000363](documents/src-000363/index.md) | documents | needs-review |
| [src-000364](workbooks/src-000364/index.md) | workbooks | needs-review |
| [participants-narrative](participants-narrative.md) | curated context | see page |
| [participants](participants.md) | curated context | see page |
| [Flows](flows/index.md) | curated context | see page |

## Gaps

- All source tables and figures require recorded visual reconciliation before this set can be reviewed.

[Extraction coverage](coverage.md) · [Catalog](../../../../../../catalog/README.md)
