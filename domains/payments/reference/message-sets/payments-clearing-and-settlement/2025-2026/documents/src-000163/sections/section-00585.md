---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.47 RemittanceInformation <RmtInf>", "6.4.2.47.2 Structured <Strd>", "6.4.2.47.2.1 ReferredDocumentInformation <RfrdDocInf>", "6.4.2.47.2.1.1 Type <Tp>"]
file_pages: [797]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.47.2.1.1 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 797 to 797.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 797

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Reason <Rsn> [0..1] Text 804
         AdditionalInformation <AddtlInf> [0..1] Text 804
6.4.2.47.2.1.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of referred document.
Type <Tp> contains the following DocumentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  797
{Or     Code <Cd> [1..1] CodeSet 797
Or}     Proprietary <Prtry> [1..1] Text 797
   Issuer <Issr> [0..1] Text 797
6.4.2.47.2.1.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Coded or proprietary format referred document type.
CodeOrProprietary <CdOrPrtry> contains one of the following DocumentType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 797
Or}   Proprietary <Prtry> [1..1] Text 797
6.4.2.47.2.1.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of remittance document, as published in an external document type code set.
Datatype: "ExternalDocumentType1Code" on page 1230
6.4.2.47.2.1.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of remittance document, in a proprietary form.
Datatype: "Max35Text" on page 1246
6.4.2.47.2.1.1.2  Issuer <Issr>
Presence: [0..1]
Definition: Identification of the issuer of the reference document type.
Datatype: "Max35Text" on page 1246
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
797 March 2026
```

