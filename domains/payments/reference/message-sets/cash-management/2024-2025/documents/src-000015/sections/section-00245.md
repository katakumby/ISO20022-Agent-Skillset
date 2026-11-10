---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 camt.008.001.11 CancelTransactionV11", "7.4 Message Building Blocks", "7.4.4 CancellationReason <CxlRsn>", "7.4.4.3 AdditionalInformation <AddtlInf>"]
file_pages: [363]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.008.001.11"]
---

# 7.4.4.3 AdditionalInformation <AddtlInf>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 363 to 363.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 363

```text
Reason <Rsn> contains one of the following elements (see "CancellationReason33Choice" on
page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 843
Or}   Proprietary <Prtry> [1..1] Text 843
7.4.4.3  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Further details on the cancellation request reason.
Datatype: "Max105Text" on page 887
7.4.5 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C8 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 816
   Envelope <Envlp> [1..1] (External Schema) 816
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 04 February 2025 camt.008.001.11 CancelTransactionV11
Cash Management - Maintenance 2024 - 2025 363 February 2025
```

