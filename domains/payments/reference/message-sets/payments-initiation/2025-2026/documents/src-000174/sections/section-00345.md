---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>", "5.4.2.18.17.2 Structured <Strd>", "5.4.2.18.17.2.1 ReferredDocumentInformation <RfrdDocInf>", "5.4.2.18.17.2.1.1 Type <Tp>"]
file_pages: [494]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17.2.1.1 Type <Tp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 494 to 494.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 494

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Reason <Rsn> [0..1] Text 501
         AdditionalInformation <AddtlInf> [0..1] Text 501
5.4.2.18.17.2.1.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of referred document.
Type <Tp> contains the following DocumentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  494
{Or     Code <Cd> [1..1] CodeSet 494
Or}     Proprietary <Prtry> [1..1] Text 494
   Issuer <Issr> [0..1] Text 494
5.4.2.18.17.2.1.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Coded or proprietary format referred document type.
CodeOrProprietary <CdOrPrtry> contains one of the following DocumentType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 494
Or}   Proprietary <Prtry> [1..1] Text 494
5.4.2.18.17.2.1.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of remittance document, as published in an external document type code set.
Datatype: "ExternalDocumentType1Code" on page 594
5.4.2.18.17.2.1.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of remittance document, in a proprietary form.
Datatype: "Max35Text" on page 609
5.4.2.18.17.2.1.1.2  Issuer <Issr>
Presence: [0..1]
Definition: Identification of the issuer of the reference document type.
Datatype: "Max35Text" on page 609
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 494 March 2026
```

