---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["Scope and Functionality", "Background"]
content_origin: "source-transcription"
---

# Background

Source: [src-000347](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`. Locator: heading path Scope and Functionality / Background.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P63** Background

**P64** This Message Definition Report covers a set of two MessageDefinitions developed by Banca d'Italia on behalf of 4CB in close collaboration with SWIFT and approved by the Securities SEG on 20 November 2025 and the Payments SEG on 01 December 2025, under the lead of the Securities SEG. These messages are specifically designed to support T2S Community for Billing and Invoice management. T2S (TARGET2-Securities) is a European securities settlement engine which offers centralised settlement in central bank money across all European securities markets. The fundamental objective of T2S is to integrate and harmonise the highly fragmented securities settlement infrastructure in Europe. It aims to reduce the costs of cross-border securities settlement and increase competition and choice among providers of post-trading services in Europe.

**P65** The Billing module (such as in T2S) provides the functionality to generate invoices for CSDs and NCBs to invoice their participants and customers respectively, based on the information that T2S provides and that CSDs and NCBs may complement with additional data. This module automatically produces monthly bills containing all billable events (e.g. events related to the lifecycle of an instruction), fixed and variable fees. At the end of a billing period, an invoice is sent and sums up all the relevant billing information per T2S Party. All invoices are stored electronically and are available for later inquiries.

