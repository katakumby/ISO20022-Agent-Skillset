---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.26 RemittanceInformation <RmtInf>", "2.4.2.19.26.2 Structured <Strd>", "2.4.2.19.26.2.1 ReferredDocumentInformation <RfrdDocInf>", "2.4.2.19.26.2.1.4 LineDetails <LineDtls>", "2.4.2.19.26.2.1.4.1 Identification <Id>", "2.4.2.19.26.2.1.4.1.1 Type <Tp>"]
file_pages: [100]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.26.2.1.4.1.1 Type <Tp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 100 to 100.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 100

```text
Identification <Id> contains the following DocumentLineIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  100
     CodeOrProprietary <CdOrPrtry> [1..1]  100
{Or       Code <Cd> [1..1] CodeSet 100
Or}       Proprietary <Prtry> [1..1] Text 100
     Issuer <Issr> [0..1] Text 101
   Number <Nb> [0..1] Text 101
   RelatedDate <RltdDt> [0..1] Date 101
2.4.2.19.26.2.1.4.1.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of referred document line identification.
Type <Tp> contains the following DocumentLineType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  100
{Or     Code <Cd> [1..1] CodeSet 100
Or}     Proprietary <Prtry> [1..1] Text 100
   Issuer <Issr> [0..1] Text 101
2.4.2.19.26.2.1.4.1.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the referred document line identification.
CodeOrProprietary <CdOrPrtry> contains one of the following DocumentLineType1Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 100
Or}   Proprietary <Prtry> [1..1] Text 100
2.4.2.19.26.2.1.4.1.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Line identification type in a coded form.
Datatype: "ExternalDocumentLineType1Code" on page 594
2.4.2.19.26.2.1.4.1.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 100 March 2026
```

