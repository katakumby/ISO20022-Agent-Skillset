---
template: false
document_kind: "message-set-index"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
set_slug: "t2s-link-reference-data"
source_ids: ["src-000300", "src-000301", "src-000302", "src-000303", "src-000304", "src-000305", "src-000365", "src-000366", "src-000367"]
source_editions: ["december-2024"]
message_ids: ["reda.045.001.01", "reda.046.001.01", "reda.047.001.01", "reda.049.001.01", "reda.050.001.01", "reda.051.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S LinkReferenceData

This reference groups the supplied collection while retaining each publication edition in its source metadata. Message versions and MDR editions are separate. Business-area prefixes do not determine domain ownership.

## Supplied sources

| Source | Format | Publication label / evidence | Content identity / occurrences |
| --- | --- | --- | --- |
| [src-000300](../../../../../../raw-input/target2securities_t2s/reda.045.001.01.xsd) | xsd | december-2024 | c070e4610f7cdd09da8c670f6b7a04450c1f9e8ceda34c7183b8d9eaed94a3b2; 2 |
| [src-000301](../../../../../../raw-input/target2securities_t2s/reda.046.001.01.xsd) | xsd | december-2024 | 45c43b4fd1759092c8d2ead39c9de16f115077a78d64fd09323b3578b36d133d; 2 |
| [src-000302](../../../../../../raw-input/target2securities_t2s/reda.047.001.01.xsd) | xsd | december-2024 | c17cb39c0259ed9722f9b97927ed8c0c9071becb8d35e41d64cb01d19c7351b2; 2 |
| [src-000303](../../../../../../raw-input/target2securities_t2s/reda.049.001.01.xsd) | xsd | december-2024 | 008f13beedad424d0544333d04fc449ece8edf2efefb27a3c874096bdbf44632; 2 |
| [src-000304](../../../../../../raw-input/target2securities_t2s/reda.050.001.01.xsd) | xsd | december-2024 | 914fc158b63575eea0623a5dddc6d955be803a4962ead5613ed7333cd7651d0c; 2 |
| [src-000305](../../../../../../raw-input/target2securities_t2s/reda.051.001.01.xsd) | xsd | december-2024 | ceeb81c0d0def2caf426c21d0b4625d01cc1a51943fc5cf87669044944b249fe; 2 |
| [src-000365](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx` | docx | december-2024 | de694c470c5968121b8e460620d4f2beb7d2709f6cb03578e0befb3af5832767; 1 |
| [src-000366](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf` | pdf | december-2024 | c5f45276b8600d9d0f6a998fea6bc74d220f50e3300aa57bae4e7e1e33e8a4d0; 1 |
| [src-000367](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | xlsx | december-2024 | fa861625f56e5feb05925aabb4e981f17058853d84fdf41c97b5ca278ea7a703; 1 |

## Canonical message definitions

| Family | Exact definition | Membership evidence | Schema source |
| --- | --- | --- | --- |
| reda.045 | [reda.045.001.01](../../../messages/reda.045.001.01/index.md) | src-000300, src-000366 | src-000300 |
| reda.046 | [reda.046.001.01](../../../messages/reda.046.001.01/index.md) | src-000301, src-000366 | src-000301 |
| reda.047 | [reda.047.001.01](../../../messages/reda.047.001.01/index.md) | src-000302, src-000366 | src-000302 |
| reda.049 | [reda.049.001.01](../../../messages/reda.049.001.01/index.md) | src-000303, src-000366 | src-000303 |
| reda.050 | [reda.050.001.01](../../../messages/reda.050.001.01/index.md) | src-000304, src-000366 | src-000304 |
| reda.051 | [reda.051.001.01](../../../messages/reda.051.001.01/index.md) | src-000305, src-000366 | src-000305 |

## Focused evidence and context

| Reference | Kind | Review |
| --- | --- | --- |
| [src-000365](documents/src-000365/index.md) | documents | needs-review |
| [src-000366](documents/src-000366/index.md) | documents | needs-review |
| [src-000367](workbooks/src-000367/index.md) | workbooks | needs-review |
| [example-consistency](example-consistency.md) | curated context | see page |
| [link-business-rules](link-business-rules.md) | curated context | see page |
| [participants-narrative](participants-narrative.md) | curated context | see page |
| [participants](participants.md) | curated context | see page |
| [Flows](flows/index.md) | curated context | see page |

## Gaps

- All source tables and figures require recorded visual reconciliation before this set can be reviewed.

[Extraction coverage](coverage.md) · [Catalog](../../../../../../catalog/README.md)
