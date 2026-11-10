---
template: false
document_kind: "diagram-detail"
manual_curated: true
review_status: "reviewed"
domain: "securities"
diagram_id: "fig-0005-cash-2"
title: "Cash-query taxonomy detail 2"
diagram_kind: "taxonomy"
content_origin: "source-reconstruction"
source_ids: ["src-000362", "src-000363"]
source_editions: ["february-2025"]
source_locations: [{"source_id": "src-000362", "locator": "BusinessProcess Description; direct-body paragraph P131; word/media/image5.jpeg"}, {"source_id": "src-000363", "locator": "2 camt.064.001.01 LimitUtilisationJournalQueryV01; file pages4-8"}, {"source_id": "src-000363", "locator": "3 camt.065.001.01 LimitUtilisationJournalReportV01; file pages9-28"}, {"source_id": "src-000362", "locator": "Word rendered file/printed page13"}]
participants: ["participant-src-000362-central-securities-depositories-csd", "participant-src-000362-direct-connected-participant-dcp", "participant-src-000362-csd-participant", "participant-src-000362-payment-bank", "participant-src-000362-national-central-bank-ncb"]
flow_ids: ["flow-src-000362-p132-query-report-process"]
message_ids: ["camt.064.001.01", "camt.065.001.01"]
message_sets: ["t2s-limit-utilisation-journal"]
render_status: "pass"
visual_review: "pass"
issue_ids: []
limitations: ["Visible artwork reconstructed with native Mermaid notation; exact decorative symbols and source geometry retained in original. Native embedded Visio originals/static inspection are preserved separately; hidden content is not certified by preview review."]
parent_diagram: "fig-0005"
mermaid_version: "12.3.0"
review_date: "2026-11-09"
---



# Cash-query taxonomy detail 2

[Complete source context and query taxonomy](fig-0005.md); source src-000362, P131, word/media/image5.jpeg; Word13. Each query node branches from the common cash-account category, sends a solid labelled link rightward and receives a dashed labelled link leftward. Only the source green journal pair belongs to the supplied camt.064/065 scope. No version or family is inferred for other pairs.

```mermaid
flowchart LR
 Cash["Cash accounts — source common branch"]
 Cash --> Q7["Liquidity Information Query"]
 Q7 -->|GetAccount| R7["Liquidity Information Query Response"]
 R7 -.->|ReturnAccount| Q7
 Cash --> Q8["Limit Utilisation Journal Query"]
 Q8 -->|LimitUtilisation<br/>JournalQuery| R8["Limit Utilisation Journal Report"]
 R8 -.->|LimitUtilisation<br/>JournalReport| Q8
 Cash --> Q9["Limit Utilisation Query"]
 Q9 -->|GetLimit| R9["Limit Utilisation Query Response"]
 R9 -.->|ReturnLimit| Q9
 Cash --> Q10["Total collateral value per T2S Dedicated Cash Account query"]
 Q10 -->|CollateralValue Query| R10["Total collateral value per T2S Dedicated Cash Account query response"]
 R10 -.->|CollateralValue Report| Q10
 Cash --> Q11["Collateral Value per T2S Dedicated Cash Account query"]
 Q11 -->|CollateralValue Query| R11["Collateral Value per T2S Dedicated Cash Account query response"]
 R11 -.->|CollateralValue Report| Q11
 Cash --> Q12["Collateral value of a security query"]
 Q12 -->|CollateralValue Query| R12["Collateral Value of a Security query response"]
 R12 -.->|CollateralValue Report| Q12
 Cash --> Q13["Cash Account List Query"]
 Q13 -->|AccountQueryList| R13["Cash Account List Query Response"]
 R13 -.->|AccountListReport| Q13
 classDef scope fill:#b1d39b,stroke:#739467
 class Q8,R8 scope
```

| Source row | Query label | Forward link label | Response label | Return link label | Scope |
| --- | --- | --- | --- | --- | --- |
| 8 | Liquidity Information Query | GetAccount | Liquidity Information Query Response | ReturnAccount | Other context |
| 9 | Limit Utilisation Journal Query | LimitUtilisationJournalQuery | Limit Utilisation Journal Report | LimitUtilisationJournalReport | In scope (green) |
| 10 | Limit Utilisation Query | GetLimit | Limit Utilisation Query Response | ReturnLimit | Other context |
| 11 | Total collateral value per T2S Dedicated Cash Account query | CollateralValue Query | Total collateral value per T2S Dedicated Cash Account query response | CollateralValue Report | Other context |
| 12 | Collateral Value per T2S Dedicated Cash Account query | CollateralValue Query | Collateral Value per T2S Dedicated Cash Account query response | CollateralValue Report | Other context |
| 13 | Collateral value of a security query | CollateralValue Query | Collateral Value of a Security query response | CollateralValue Report | Other context |
| 14 | Cash Account List Query | AccountQueryList | Cash Account List Query Response | AccountListReport | Other context |



## Review evidence

Original image5.jpeg, enlarged source-label crops and complete Word13 compared with every query/response and exchange-link label. Native Mermaid12.3.0 / Chromium156.0.8078.81 rendering passed; visual comparison2026-11-09. [Compared detail](../../../../../../assets/src-000362/reconstructed/fig-0005-cash-2.png).
