---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["21 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "21.4 Message Building Blocks"]
file_pages: [496]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 21.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 496 to 496.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 496

```text
C19 QueryTypeFullRule
If ReportGeneralDetails/QueryType is equal to Full, then ReportOrError/Cancellations(*)/
Cancellation/TransactionIdentification and ReportOrError/Cancellations(*)/Cancellation/
UnderlyingIntraBalance must be present.
This constraint is defined at the MessageDefinition level.
C20 QueryTypeStatusRule
If ReportGeneralDetails/QueryType is equal to Status, then ReportOrError/Cancellations(*)/
Cancellation/TransactionIdentification and ReportOrError/Cancellations(*)/Cancellation/
UnderlyingIntraBalance must be absent.
This constraint is defined at the MessageDefinition level.
C21 ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports
(UpdateType: DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different ReportNumbers. For example, a daily report
sent on day 1 would have ReportNumber 001, on day 2, 002, etc.
C22 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
21.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
21.4.1 Identification <Id>
Presence: [0..1]
Definition: Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
Identification <Id> contains the following DocumentIdentification51 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 497
   CreationDateTime <CreDtTm> [0..1] ± 497
   CopyDuplicate <CpyDplct> [0..1] CodeSet 497
   MessageOriginator <MsgOrgtr> [0..1] ± 497
   MessageRecipient <MsgRcpt> [0..1] ± 498
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 496 August 2026
```

