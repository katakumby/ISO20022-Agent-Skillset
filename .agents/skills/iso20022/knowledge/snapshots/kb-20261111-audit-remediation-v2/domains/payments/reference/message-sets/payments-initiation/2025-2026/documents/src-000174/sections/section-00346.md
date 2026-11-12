---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>", "5.4.2.18.17.2 Structured <Strd>", "5.4.2.18.17.2.1 ReferredDocumentInformation <RfrdDocInf>", "5.4.2.18.17.2.1.2 Number <Nb>"]
file_pages: [495]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17.2.1.2 Number <Nb>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 495 to 495.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 495

```text
5.4.2.18.17.2.1.2  Number <Nb>
Presence: [0..1]
Definition: Unique and unambiguous identification of the referred document.
Datatype: "Max35Text" on page 609
5.4.2.18.17.2.1.3  RelatedDate <RltdDt>
Presence: [0..1]
Definition: Date and date type associated with the referred document.
RelatedDate <RltdDt> contains the following DateAndType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  495
{Or     Code <Cd> [1..1] CodeSet 495
Or}     Proprietary <Prtry> [1..1] Text 495
   Date <Dt> [1..1] Date 495
5.4.2.18.17.2.1.3.1  Type <Tp>
Presence: [1..1]
Definition: Type of date associated with the referred document.
Type <Tp> contains one of the following DateType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 495
Or}   Proprietary <Prtry> [1..1] Text 495
5.4.2.18.17.2.1.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the date type, as published in an external date type code set.
Datatype: "ExternalDateType1Code" on page 593
5.4.2.18.17.2.1.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the date type, in a free-text form.
Datatype: "Max35Text" on page 609
5.4.2.18.17.2.1.3.2  Date <Dt>
Presence: [1..1]
Definition: Date associated with the referred document.
Datatype: "ISODate" on page 603
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 495 March 2026
```

