---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["74 semt.029.001.01 IntraPositionMovementQueryResponseV01", "74.4 Message Building Blocks"]
file_pages: [2617]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 74.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2617 to 2617.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2617

```text
C20 ReportIdentificationRule
If the report has multiple pages, then the ReportIdentification must remain the same through all
the pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different report identifications. For example, a daily
report sent on day 1 would have ReportIdentification 001, on day 2, 002, etc.
C21 SafekeepingAccountRule
SafekeepingAccount must be present or Movement(*)/SafekeepingAccount must be present,
but not both.
C22 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C23 StatusAndReasonRule
StatusAndReason must be present or Movement(*)/StatusAndReason must be present, but not
both.
C24 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C25 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
74.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
74.4.1 Pagination <Pgntn>
Presence: [1..1]
Definition: Pagination of the message.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 2980 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 2980
   LastPageIndicator <LastPgInd> [1..1] Indicator 2980
74.4.2 ReportGeneralDetails <RptGnlDtls>
Presence: [1..1]
Definition: General characteristics related to the report information.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2617 August 2026
```

