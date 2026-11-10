---
template: false
document_kind: "diagram-detail"
manual_curated: true
review_status: "reviewed"
diagram_id: "fig-0004-processes"
title: "Reporting process hierarchy detail"
domain: "securities"
content_origin: "source-reconstruction"
diagram_kind: "process-context"
source_ids: ["src-000374"]
source_locations: [{"source_id": "src-000374", "locator": "P204/image6.png; Word14; lower process hierarchy"}]
message_sets: ["t2s-securities-and-penalty-reporting"]
render_status: "pass"
visual_review: "pass"
limitations: ["Source rectangles, diamond request nodes and dashed relationships retained; no exclusive decision semantics inferred from the request diamonds."]
mermaid_version: "12.3.0"
review_date: "2026-11-09"
source_editions: ["march-2026"]
---

# Reporting process hierarchy detail

[Actor-context parent](fig-0004.md); [Complete unchanged original](../../../../../../../../evidence/omitted/aefca1f7a8f298261593e1e6.md).

```mermaid
flowchart TB
 P(["«Processes»"]) -.-> I["Instruction"]
 P -.-> C["Confirmation"]
 P -.-> R["Reconciliation"]
 I -.-> M{"Modification Request"}
 I -.-> X{"Cancellation Request"}
 M -.-> S(["«Status reporting»"])
 X -.-> S
 C -.-> S
 R -.-> Q(["«Query / Response»"])
 R -.-> Rep(["«Reporting»"])
 classDef context fill:#d6e4fb,stroke:#7097cd
 classDef scope fill:#d4e3cd,stroke:#80b260
 class P,I,C,M,X,S context
 class R,Q,Rep scope
```

This detail preserves the lower source hierarchy, all dashed arrow directions and green Reconciliation/Query-Response/Reporting scope. Modification and Cancellation Request diamonds are source process labels; they are not asserted to form an exclusive choice. Native actor notation is preserved in the parent view.

## Actual review evidence

Compared all source labels, endpoints, direction and shapes with [Mermaid12.3.0 reconstruction](../../../../../../../../evidence/omitted/af9904ea6205742b8759160d.md) on2026-11-09. All nine lower process nodes and ten directed dashed connectors compared with source Word14, retaining rectangles, request diamonds and process ellipses in native flowchart form.
