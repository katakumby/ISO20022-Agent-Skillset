---
template: false
document_kind: "message-set-index"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
set_slug: "post-trade-matching"
source_ids: ["src-000180", "src-000181", "src-000182", "src-000183", "src-000184", "src-000185", "src-000186", "src-000187"]
source_editions: ["2024-2025", "February 2025"]
message_ids: ["semt.023.001.02", "setr.027.001.05", "setr.029.001.02", "setr.030.001.03", "setr.044.001.04"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# Post-Trade Matching

This reference groups the supplied collection while retaining each publication edition in its source metadata. Message versions and MDR editions are separate. Business-area prefixes do not determine domain ownership.

## Supplied sources

| Source | Format | Publication label / evidence | Content identity / occurrences |
| --- | --- | --- | --- |
| [src-000180](../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx) | docx | February 2025 | afb1b22c2051a880f52bd19b1d44fe91a1b2da53488529e7002334b952a72419; 1 |
| [src-000181](../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf) | pdf | February 2025 | 9acd70dd84af618b3c7aeb1c9501f4b43168f2200b2b425420b0f015572ebb4d; 1 |
| [src-000182](../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart3_PostTradeMatching_2024_2025_v1.xlsx) | xlsx | 2024-2025 | b6e9e174e5b55685aa90bdf7e3908d1274a643c4e7a6d0fd5dea2265c3954be3; 1 |
| [src-000183](../../../../../../raw-input/post_trade_matching/semt.023.001.02.xsd) | xsd | 2024-2025 | 0a1a5ad48cf5c4abc0b1d170c9fd6813852fa1c019d9e76852573fd31418db19; 1 |
| [src-000184](../../../../../../raw-input/post_trade_matching/setr.027.001.05.xsd) | xsd | 2024-2025 | 091510de035729e2fde3c6028a1ae940b0fb06f26533a7e8ecc4aca982516486; 1 |
| [src-000185](../../../../../../raw-input/post_trade_matching/setr.029.001.02.xsd) | xsd | 2024-2025 | 5782c0a8e20f90640ae2ef50f2ab0c4169334d854b7277c9edc4eda1161c25bf; 1 |
| [src-000186](../../../../../../raw-input/post_trade_matching/setr.030.001.03.xsd) | xsd | 2024-2025 | 81cd08bfa8e934b0e81791429f58ab1226c625fc95d2bd0464dcee00b1fb1e68; 1 |
| [src-000187](../../../../../../raw-input/post_trade_matching/setr.044.001.04.xsd) | xsd | 2024-2025 | d1cba41826b33649873a2e42397c72553bf1cfb49dd3e828b278fd321d03d9f9; 1 |

## Canonical message definitions

| Family | Exact definition | Membership evidence | Schema source |
| --- | --- | --- | --- |
| semt.023 | [semt.023.001.02](../../../messages/semt.023.001.02/index.md) | src-000181, src-000183 | src-000183 |
| setr.027 | [setr.027.001.05](../../../messages/setr.027.001.05/index.md) | src-000181, src-000184 | src-000184 |
| setr.029 | [setr.029.001.02](../../../messages/setr.029.001.02/index.md) | src-000181, src-000185 | src-000185 |
| setr.030 | [setr.030.001.03](../../../messages/setr.030.001.03/index.md) | src-000181, src-000186 | src-000186 |
| setr.044 | [setr.044.001.04](../../../messages/setr.044.001.04/index.md) | src-000181, src-000187 | src-000187 |

## Focused evidence and context

| Reference | Kind | Review |
| --- | --- | --- |
| [src-000180](documents/src-000180/index.md) | documents | needs-review |
| [src-000181](documents/src-000181/index.md) | documents | needs-review |
| [src-000182](workbooks/src-000182/index.md) | workbooks | needs-review |
| [participants-narrative](participants-narrative.md) | curated context | see page |
| [participants](participants.md) | curated context | see page |
| [Flows](flows/index.md) | curated context | see page |

## Gaps

- All source tables and figures require recorded visual reconciliation before this set can be reviewed.

[Extraction coverage](coverage.md) · [Catalog](../../../../../../catalog/README.md)
