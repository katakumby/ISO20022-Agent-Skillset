---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "7.4 Message Building Blocks"]
file_pages: [149]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
preceding_topic_continuations: [{"constraint_ids": ["C14", "C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23"], "until_heading": "7.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 149, "topic": "7.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00118.md"}]
---

# 7.4 Message Building Blocks

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 149 to 149.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 149, C14–C23 before **7.4 Message Building Blocks** continue [7.3 Constraints](section-00118.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 149

```text
C14 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C15 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C16 Party2PresenceRule
If Party2 is present, then Party1 must be present.
C17 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C18 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C19 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C20 ProcessingStatusRule
ProcessingStatus must be present or Cancellation(*)/ProcessingStatus must be present, but
not both.
C21 ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports
(UpdateType: DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different ReportNumbers. For example, a daily report
sent on day 1 would have ReportNumber 001, on day 2, 002, etc.
C22 SafekeepingAccountRule
SafekeepingAccount must be present or Cancellation(*)/SafekeepingAccount must be present,
but not both.
C23 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
7.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
7.4.1 Pagination <Pgntn>
Presence: [1..1]
Definition: Pagination of the message.
Approved by the Securities SEG on 21 August 2025 semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities - Settlement Restrictions 149 September 2025
```

