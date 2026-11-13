---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.4 Message Building Blocks"]
file_pages: [103]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
preceding_topic_continuations: [{"constraint_ids": ["C27", "C28", "C29"], "until_heading": "5.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 103, "topic": "5.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00078.md"}]
---

# 5.4 Message Building Blocks

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 103 to 103.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 103, C27–C29 before **5.4 Message Building Blocks** continue [5.3 Constraints](section-00078.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 103

```text
C27 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C28 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C29 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
5.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
5.4.1 Pagination <Pgntn>
Presence: [1..1]
Definition: Pagination of the message.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 229 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 229
   LastPageIndicator <LastPgInd> [1..1] Indicator 229
5.4.2 ReportGeneralDetails <RptGnlDtls>
Presence: [1..1]
Definition: General characteristics related to the report information.
Impacted by: C24 "ReportNumberRule"
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 103 September 2025
```

