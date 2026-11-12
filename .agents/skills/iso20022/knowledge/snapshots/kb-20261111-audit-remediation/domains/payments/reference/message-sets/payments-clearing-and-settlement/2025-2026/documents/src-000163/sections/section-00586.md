---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.47 RemittanceInformation <RmtInf>", "6.4.2.47.2 Structured <Strd>", "6.4.2.47.2.1 ReferredDocumentInformation <RfrdDocInf>", "6.4.2.47.2.1.2 Number <Nb>"]
file_pages: [798]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.47.2.1.2 Number <Nb>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 798 to 798.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 798

```text
6.4.2.47.2.1.2  Number <Nb>
Presence: [0..1]
Definition: Unique and unambiguous identification of the referred document.
Datatype: "Max35Text" on page 1246
6.4.2.47.2.1.3  RelatedDate <RltdDt>
Presence: [0..1]
Definition: Date and date type associated with the referred document.
RelatedDate <RltdDt> contains the following DateAndType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  798
{Or     Code <Cd> [1..1] CodeSet 798
Or}     Proprietary <Prtry> [1..1] Text 798
   Date <Dt> [1..1] Date 798
6.4.2.47.2.1.3.1  Type <Tp>
Presence: [1..1]
Definition: Type of date associated with the referred document.
Type <Tp> contains one of the following DateType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 798
Or}   Proprietary <Prtry> [1..1] Text 798
6.4.2.47.2.1.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the date type, as published in an external date type code set.
Datatype: "ExternalDateType1Code" on page 1229
6.4.2.47.2.1.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the date type, in a free-text form.
Datatype: "Max35Text" on page 1246
6.4.2.47.2.1.3.2  Date <Dt>
Presence: [1..1]
Definition: Date associated with the referred document.
Datatype: "ISODate" on page 1239
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
798 March 2026
```

