---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.26 RemittanceInformation <RmtInf>", "2.4.2.19.26.2 Structured <Strd>", "2.4.2.19.26.2.1 ReferredDocumentInformation <RfrdDocInf>", "2.4.2.19.26.2.1.1 Type <Tp>"]
file_pages: [97]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.26.2.1.1 Type <Tp>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 97 to 97.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 97

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Reason <Rsn> [0..1] Text 104
         AdditionalInformation <AddtlInf> [0..1] Text 104
2.4.2.19.26.2.1.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of referred document.
Type <Tp> contains the following DocumentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  97
{Or     Code <Cd> [1..1] CodeSet 97
Or}     Proprietary <Prtry> [1..1] Text 97
   Issuer <Issr> [0..1] Text 97
2.4.2.19.26.2.1.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Coded or proprietary format referred document type.
CodeOrProprietary <CdOrPrtry> contains one of the following DocumentType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 97
Or}   Proprietary <Prtry> [1..1] Text 97
2.4.2.19.26.2.1.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of remittance document, as published in an external document type code set.
Datatype: "ExternalDocumentType1Code" on page 594
2.4.2.19.26.2.1.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of remittance document, in a proprietary form.
Datatype: "Max35Text" on page 609
2.4.2.19.26.2.1.1.2  Issuer <Issr>
Presence: [0..1]
Definition: Identification of the issuer of the reference document type.
Datatype: "Max35Text" on page 609
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 97 March 2026
```

