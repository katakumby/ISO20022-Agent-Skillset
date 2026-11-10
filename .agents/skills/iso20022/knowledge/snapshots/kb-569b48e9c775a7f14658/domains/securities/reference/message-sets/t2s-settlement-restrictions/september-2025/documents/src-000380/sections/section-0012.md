---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["Scope and Functionality", "Scope", "Securities Transaction Cancellation Request Query/Report"]
content_origin: "source-transcription"
---

# Securities Transaction Cancellation Request Query/Report

Source: [src-000380](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Locator: heading path Scope and Functionality / Scope / Securities Transaction Cancellation Request Query/Report.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P111** Securities Transaction Cancellation Request Query/Report

**P112** The scope of the Securities Transaction Cancellation Query and Report is supported by the following messages:

**P113** semt.032: Securities Transaction Cancellation Request Query.

**P114** semt.033: Securities Transaction Cancellation Report.

**P115** The communication flow can be represented as follows:

**P116**   Servicing PartyInstructing Party Instruct Securities Transaction Cancellation Request (sese.020)   Request Securities Transaction Cancellation Request Query (semt.032)Securities Transaction Cancellation Report (semt.033)PUSH/PULLReport processing status (sese.027)  Servicing PartyInstructing Party Instruct Securities Transaction Cancellation Request (sese.020)   Request Securities Transaction Cancellation Request Query (semt.032)Securities Transaction Cancellation Report (semt.033)PUSH/PULLReport processing status (sese.027)

[fig-0003 - original figure evidence](../diagrams/fig-0003.md)

**P117** The Securities Transaction Cancellation Request Query and Report provide a T2S participant with the ability to query and report details of any previously sent Cancellation of Settlement or Intra Position Movement Instructions. This business activity is performed either in pull or push mode.

**P119** These messages are to be used with the ISO 20022 Business Application Header (head.001). The schema and more information about the Business Application Header (BAH) can be found on the www.iso20022.org web site

