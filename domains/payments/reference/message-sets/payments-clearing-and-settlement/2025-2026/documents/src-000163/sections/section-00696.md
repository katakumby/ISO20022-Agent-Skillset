---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.30 RemittanceInformation <RmtInf>", "7.4.2.40.30.2 Structured <Strd>", "7.4.2.40.30.2.1 ReferredDocumentInformation <RfrdDocInf>", "7.4.2.40.30.2.1.1 Type <Tp>"]
file_pages: [951]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.30.2.1.1 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 951 to 951.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 951

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Reason <Rsn> [0..1] Text 958
         AdditionalInformation <AddtlInf> [0..1] Text 958
7.4.2.40.30.2.1.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of referred document.
Type <Tp> contains the following DocumentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  951
{Or     Code <Cd> [1..1] CodeSet 951
Or}     Proprietary <Prtry> [1..1] Text 951
   Issuer <Issr> [0..1] Text 951
7.4.2.40.30.2.1.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Coded or proprietary format referred document type.
CodeOrProprietary <CdOrPrtry> contains one of the following DocumentType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 951
Or}   Proprietary <Prtry> [1..1] Text 951
7.4.2.40.30.2.1.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of remittance document, as published in an external document type code set.
Datatype: "ExternalDocumentType1Code" on page 1230
7.4.2.40.30.2.1.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of remittance document, in a proprietary form.
Datatype: "Max35Text" on page 1246
7.4.2.40.30.2.1.1.2  Issuer <Issr>
Presence: [0..1]
Definition: Identification of the issuer of the reference document type.
Datatype: "Max35Text" on page 1246
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
951 March 2026
```

