---
template: false
document_kind: "message-set-index"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
set_slug: "t2s-collateral-reporting"
source_ids: ["src-000259", "src-000260", "src-000356", "src-000357", "src-000358"]
source_editions: ["march-2024"]
message_ids: ["colr.001.001.02", "colr.002.001.02"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S CollateralReporting

This reference groups the supplied collection while retaining each publication edition in its source metadata. Message versions and MDR editions are separate. Business-area prefixes do not determine domain ownership.

## Supplied sources

| Source | Format | Publication label / evidence | Content identity / occurrences |
| --- | --- | --- | --- |
| [src-000259](../../../../../../raw-input/target2securities_t2s/colr.001.001.02.xsd) | xsd | march-2024 | be7162da92e4d2c1124a3b28c0480d1325dce05ae9baf68967eae7ff9c9b388c; 2 |
| [src-000260](../../../../../../raw-input/target2securities_t2s/colr.002.001.02.xsd) | xsd | march-2024 | cefc2ede6f99d14f0745921e1654ca711140e4496ede9b5a479204fe605001bf; 2 |
| [src-000356](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralReporting_2023_2024_v2.docx` | docx | march-2024 | 467ab2787e1efbfd6bdf4df301aa52c854057c299bf6fe3574f6ed00357444b5; 1 |
| [src-000357](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf` | pdf | march-2024 | bba13c1299fa1a9db3c2476ee7a5f5b178abbaeb6fb01f85dcafc956dae80b57; 1 |
| [src-000358](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | xlsx | march-2024 | 8c8d21cb14733babfbd3e75ff24bd51b58f579cc6d99a60a8151ad5487457e5f; 1 |

## Canonical message definitions

| Family | Exact definition | Membership evidence | Schema source |
| --- | --- | --- | --- |
| colr.001 | [colr.001.001.02](../../../messages/colr.001.001.02/index.md) | src-000259, src-000357 | src-000259 |
| colr.002 | [colr.002.001.02](../../../messages/colr.002.001.02/index.md) | src-000260, src-000357 | src-000260 |

## Focused evidence and context

| Reference | Kind | Review |
| --- | --- | --- |
| [src-000356](documents/src-000356/index.md) | documents | needs-review |
| [src-000357](documents/src-000357/index.md) | documents | needs-review |
| [src-000358](workbooks/src-000358/index.md) | workbooks | needs-review |
| [participants-narrative](participants-narrative.md) | curated context | see page |
| [participants](participants.md) | curated context | see page |
| [Flows](flows/index.md) | curated context | see page |

## Gaps

- All source tables and figures require recorded visual reconciliation before this set can be reviewed.

[Extraction coverage](coverage.md) · [Catalog](../../../../../../catalog/README.md)
