---
template: false
document_kind: "diagram-detail"
manual_curated: true
review_status: "reviewed"
domain: "securities"
diagram_id: "fig-0002-cash"
title: "Fourteen cash-account queries"
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



# Fourteen cash-account queries

Focused view of [the complete source query taxonomy](fig-0002.md). Source src-000356, direct-body P130, word/media/image2.png. This view partitions the artwork for readable retrieval; it adds no new query permissions or message bindings.

```mermaid
flowchart LR
 Cash["Cash account"]
 Cash --> Cash0["T2S Dedicated Cash Account Balance"]
 Cash --> Cash1["T2S Dedicated Cash Account Posting Query"]
 Cash --> Cash2["Outstanding Auto-Collateralisation Credit"]
 Cash --> Cash3["Overall Liquidity"]
 Cash --> Cash4["Cash Forecast"]
 Cash --> Cash5["Limit"]
 Cash --> Cash6["Immediate Liquidity Transfer Order List Query"]
 Cash --> Cash7["Limit Utilisation Journal"]
 Cash --> Cash8["Limit Utilisation"]
 Cash --> Cash9["Total Collateral Value"]
 Cash --> Cash10["Collateral Value per Cash Account"]
 Cash --> Cash11["Collateral Value of a Security"]
 Cash --> Cash12["Cash Account List"]
 Cash --> Cash13["Immediate Liquidity Transfer Order Detail Query"]
```

[Complete unchanged source](../../../../../../assets/src-000356/originals/image2.png).

## Review evidence

Compared with original image2.png and Word page13: every included label and edge checked; all25 query leaves are preserved across the focused details. Mermaid12.3.0 / Chromium156.0.8078.81 render and visual comparison passed2026-11-09. [Compared focused reconstruction](../../../../../../assets/src-000356/reconstructed/fig-0002-cash.png).
