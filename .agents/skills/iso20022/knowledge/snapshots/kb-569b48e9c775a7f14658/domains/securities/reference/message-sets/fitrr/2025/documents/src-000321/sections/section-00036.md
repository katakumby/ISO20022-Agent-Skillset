---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01", "4.4 Message Building Blocks", "4.4.1 StatusAdvice <StsAdvc>", "4.4.1.3 RecordStatus <RcrdSts>", "4.4.1.3.2 Status <Sts>"]
file_pages: [45]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.031.001.01"]
---

# 4.4.1.3.2 Status <Sts>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 45 to 45.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 45

```text
4.4.1.3.2  Status <Sts>
Presence: [1..1]
Definition: Defines status of the reported transaction.
Datatype: "ReportingRecordStatus1Code" on page 444
CodeName Name Definition
ACPT Accepted Record has been accepted.
ACPD AcceptedAfterPending Record has been accepted, following a
pending status.
PDNG Pending Processing of the record is pending
(some validation rules have been
executed but some have not and the
final status is not known yet).
RCVD Received Recrod has been received but not
processed yet.
RJCT Rejected Record has been rejected.
RJPD RejectedAfterPending Record has been rejected, following a
pending status.
WARN Warning Record has been accepted with
warnings.
4.4.1.3.3  ValidationRule <VldtnRule>
Presence: [0..*]
Definition: Provides the details of the rule which could not be validated.
ValidationRule <VldtnRule> contains the following elements (see
"GenericValidationRuleIdentification1" on page 340 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 340
   Description <Desc> [0..1] Text 340
   SchemeName <SchmeNm> [0..1] ± 340
   Issuer <Issr> [0..1] Text 341
4.4.1.3.4  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C1 "SupplementaryDataRule"
Approved by the Securities SEG on 17 July 2025 auth.031.001.01
FinancialInstrumentReportingStatusAdviceV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
45 July 2025
```

