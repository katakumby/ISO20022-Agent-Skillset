---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["23 camt.025.001.09 ReceiptV09", "23.4 Message Building Blocks", "23.4.2 ReceiptDetails <RctDtls>", "23.4.2.3 RequestHandling <ReqHdlg>", "23.4.2.3.2 StatusReason <StsRsn>", "23.4.2.3.2.2 Reason <Rsn>", "23.4.2.3.2.2.1 Code <Cd>"]
file_pages: [622, 623]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.025.001.09"]
---

# 23.4.2.3.2.2.1 Code <Cd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 622 to 623.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 622

```text
Reason <Rsn> contains one of the following StatusReason6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 622
Or}   Proprietary <Prtry> [1..1] Text 622
23.4.2.3.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the status, as published in an external reason code list.
Datatype: "ExternalStatusReason1Code" on page 856
23.4.2.3.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status, in a proprietary form.
Datatype: "Max35Text" on page 889
23.4.2.3.2.3  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Further details on the status reason.
Usage: Additional information can be used for several purposes such as the reporting of repaired
information.
Datatype: "Max105Text" on page 887
23.4.2.3.3  Description <Desc>
Presence: [0..1]
Definition: Description of the status, in free format text.
Datatype: "Max140Text" on page 888
23.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C6 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 816
   Envelope <Envlp> [1..1] (External Schema) 816
Approved by the Payments SEG on 04 February 2025 camt.025.001.09 ReceiptV09
Cash Management - Maintenance 2024 - 2025 622 February 2025
```

## File page 623

```text
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 04 February 2025 camt.025.001.09 ReceiptV09
Cash Management - Maintenance 2024 - 2025 623 February 2025
```

