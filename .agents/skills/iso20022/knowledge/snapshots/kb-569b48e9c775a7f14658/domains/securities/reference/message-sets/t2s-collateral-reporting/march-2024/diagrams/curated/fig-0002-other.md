---
template: false
document_kind: "diagram-detail"
manual_curated: true
review_status: "reviewed"
domain: "securities"
diagram_id: "fig-0002-other"
title: "Other query-category detail"
diagram_kind: "taxonomy"
content_origin: "source-reconstruction"
source_ids: ["src-000356"]
source_editions: ["march-2024"]
source_locations: [{"source_id": "src-000356", "locator": "BusinessProcess Description / BusinessProcess Diagram; direct-body paragraph P130; word/media/image2.png"}]
participants: ["participant-src-000356-central-system", "participant-src-000356-system-user", "participant-src-000356-central-securities-depositories-csd", "participant-src-000356-settlement-bank", "participant-src-000356-payment-bank", "participant-src-000356-national-central-bank-ncb"]
flow_ids: []
message_ids: []
message_sets: ["t2s-collateral-reporting"]
render_status: "pass"
visual_review: "pass"
issue_ids: []
limitations: ["Visible artwork reconstructed with native Mermaid notation; exact decorative symbols and source geometry retained in original. Native embedded Visio originals/static inspection are preserved separately; hidden content is not certified by preview review."]
parent_diagram: "fig-0002"
mermaid_version: "12.3.0"
review_date: "2026-11-09"
---



# Other query-category detail

Focused view of [the complete source query taxonomy](fig-0002.md). Source src-000356, direct-body P130, word/media/image2.png. This view partitions the artwork for readable retrieval; it adds no new query permissions or message bindings.

```mermaid
flowchart LR
 Ins["Instructions"]
 Sec["Security account"]
 Day["Settlement day"]
 Dyn["Dynamic data queries"]
 Static["Static data"]
 Ins --> Ins0["Settlement Instruction"]
 Ins --> Ins1["Settlement Instruction Current Status"]
 Ins --> Ins2["Settlement Instruction Status Audit Trail"]
 Ins --> Ins3["Settlement Instruction Audit Trail"]
 Ins --> Ins4["Settlement Transaction"]
 Sec --> Sec0["Security Account Position"]
 Sec --> Sec1["Security Account Position History"]
 Day --> Day0["T2S Calendar"]
 Day --> Day1["T2S Diary"]
 Dyn --> Dyn0["Report"]
 Static --> Static0["Several queries available (e.g. Liquidity Transfer Orders and Liquidity Transfer Order Link Set)"]
```

[Complete unchanged source](../../../../../../../../evidence/omitted/dba44d7482ed3e96fd408d58.md).

## Review evidence

Compared with original image2.png and Word page13: every included label and edge checked; all25 query leaves are preserved across the focused details. Mermaid12.3.0 / Chromium156.0.8078.81 render and visual comparison passed2026-11-09. [Compared focused reconstruction](../../../../../../../../evidence/omitted/69c142000b65f97bb7a28516.md).
