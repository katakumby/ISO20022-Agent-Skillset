---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["79 semt.034.001.01 IntraPositionMovementPendingReportV01", "79.4 Message Building Blocks"]
file_pages: [2728]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 79.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2728 to 2728.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2728

```text
C13 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be
NONREF.
C14 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C15 PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
C16 PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO
10383 Market Identifier Code (MIC) must be used.
C17 ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports
(UpdateType: DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different ReportNumbers. For example, a daily report
sent on day 1 would have ReportNumber 001, on day 2, 002, etc.
C18 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C19 StatusAndReasonRule
StatusAndReason must be present or Movement(*)/StatusAndReason must be present, but not
both.
C20 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C21 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
79.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities 2728 August 2026
```

