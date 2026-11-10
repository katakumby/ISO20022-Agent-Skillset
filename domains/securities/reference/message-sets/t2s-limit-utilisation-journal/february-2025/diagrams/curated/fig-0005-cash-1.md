---
template: false
document_kind: "diagram-detail"
manual_curated: true
review_status: "reviewed"
domain: "securities"
diagram_id: "fig-0005-cash-1"
title: "Cash-query taxonomy detail 1"
diagram_kind: "taxonomy"
content_origin: "source-reconstruction"
source_ids: ["src-000362", "src-000363"]
source_editions: ["february-2025"]
source_locations: [{"source_id": "src-000362", "locator": "BusinessProcess Description; direct-body paragraph P131; word/media/image5.jpeg"}, {"source_id": "src-000363", "locator": "2 camt.064.001.01 LimitUtilisationJournalQueryV01; file pages4-8"}, {"source_id": "src-000363", "locator": "3 camt.065.001.01 LimitUtilisationJournalReportV01; file pages9-28"}, {"source_id": "src-000362", "locator": "Word rendered file/printed page13"}]
participants: ["participant-src-000362-central-securities-depositories-csd", "participant-src-000362-direct-connected-participant-dcp", "participant-src-000362-csd-participant", "participant-src-000362-payment-bank", "participant-src-000362-national-central-bank-ncb"]
flow_ids: ["flow-src-000362-p132-query-report-process"]
message_ids: []
message_sets: ["t2s-limit-utilisation-journal"]
render_status: "pass"
visual_review: "pass"
issue_ids: []
limitations: ["Visible artwork reconstructed with native Mermaid notation; exact decorative symbols and source geometry retained in original. Native embedded Visio originals/static inspection are preserved separately; hidden content is not certified by preview review."]
parent_diagram: "fig-0005"
mermaid_version: "12.3.0"
review_date: "2026-11-09"
---



# Cash-query taxonomy detail 1

[Complete source context and query taxonomy](fig-0005.md); source src-000362, P131, word/media/image5.jpeg; Word13. Each query node branches from the common cash-account category, sends a solid labelled link rightward and receives a dashed labelled link leftward. Only the source green journal pair belongs to the supplied camt.064/065 scope. No version or family is inferred for other pairs.

```mermaid
flowchart LR
 Cash["Cash accounts — source common branch"]
 Cash --> Q0["T2S Dedicated Cash Account Balance Query"]
 Q0 -->|GetAccount| R0["T2S Dedicated Cash Account Balance query response"]
 R0 -.->|ReturnAccount| Q0
 Cash --> Q1["T2S Dedicated Cash Account Posting Query"]
 Q1 -->|GetTransaction| R1["T2S Dedicated Cash Account Posting Query Response"]
 R1 -.->|ReturnTransaction| Q1
 Cash --> Q2["Immediate Liquidity Transfer Order List Query"]
 Q2 -->|GetTransaction| R2["Immediate Liquidity Transfer Order List Query Response"]
 R2 -.->|ReturnTransaction| Q2
 Cash --> Q3["Immediate Liquidity Transfer Order Detail Query"]
 Q3 -->|GetTransaction| R3["Immediate Liquidity Transfer Order Detail Query Response"]
 R3 -.->|ReturnTransaction| Q3
 Cash --> Q4["Outstanding AutoCollateralisation Credit Query"]
 Q4 -->|GetAccount| R4["Outstanding Auto Collateralisation Credit query response"]
 R4 -.->|ReturnAccount| Q4
 Cash --> Q5["T2S Overall Liquidity Query"]
 Q5 -->|GetAccount| R5["T2S Overall Liquidity query response"]
 R5 -.->|ReturnAccount| Q5
 Cash --> Q6["Cash Forecast Query"]
 Q6 -->|GetAccount| R6["Cash Forecast query response"]
 R6 -.->|ReturnAccount| Q6
```

| Source row | Query label | Forward link label | Response label | Return link label | Scope |
| --- | --- | --- | --- | --- | --- |
| 1 | T2S Dedicated Cash Account Balance Query | GetAccount | T2S Dedicated Cash Account Balance query response | ReturnAccount | Other context |
| 2 | T2S Dedicated Cash Account Posting Query | GetTransaction | T2S Dedicated Cash Account Posting Query Response | ReturnTransaction | Other context |
| 3 | Immediate Liquidity Transfer Order List Query | GetTransaction | Immediate Liquidity Transfer Order List Query Response | ReturnTransaction | Other context |
| 4 | Immediate Liquidity Transfer Order Detail Query | GetTransaction | Immediate Liquidity Transfer Order Detail Query Response | ReturnTransaction | Other context |
| 5 | Outstanding AutoCollateralisation Credit Query | GetAccount | Outstanding Auto Collateralisation Credit query response | ReturnAccount | Other context |
| 6 | T2S Overall Liquidity Query | GetAccount | T2S Overall Liquidity query response | ReturnAccount | Other context |
| 7 | Cash Forecast Query | GetAccount | Cash Forecast query response | ReturnAccount | Other context |



## Review evidence

Original image5.jpeg, enlarged source-label crops and complete Word13 compared with every query/response and exchange-link label. Native Mermaid12.3.0 / Chromium156.0.8078.81 rendering passed; visual comparison2026-11-09. [Compared detail](../../../../../../assets/src-000362/reconstructed/fig-0005-cash-1.png).
