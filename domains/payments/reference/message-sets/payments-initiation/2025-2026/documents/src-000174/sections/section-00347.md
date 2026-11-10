---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>", "5.4.2.18.17.2 Structured <Strd>", "5.4.2.18.17.2.1 ReferredDocumentInformation <RfrdDocInf>", "5.4.2.18.17.2.1.4 LineDetails <LineDtls>"]
file_pages: [496]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17.2.1.4 LineDetails <LineDtls>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 496 to 496.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 496

```text
5.4.2.18.17.2.1.4  LineDetails <LineDtls>
Presence: [0..*]
Definition: Set of elements used to provide the content of the referred document line.
LineDetails <LineDtls> contains the following DocumentLineInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..*]  496
     Type <Tp> [0..1]  497
       CodeOrProprietary <CdOrPrtry> [1..1]  497
{Or         Code <Cd> [1..1] CodeSet 497
Or}         Proprietary <Prtry> [1..1] Text 497
       Issuer <Issr> [0..1] Text 498
     Number <Nb> [0..1] Text 498
     RelatedDate <RltdDt> [0..1] Date 498
   Description <Desc> [0..1] Text 498
   Amount <Amt> [0..1]  C18 498
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  499
       Type <Tp> [1..1]  499
{Or         Code <Cd> [1..1] CodeSet 500
Or}         Proprietary <Prtry> [1..1] Text 500
       Amount <Amt> [1..1] Amount C2, C12 500
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  500
       Amount <Amt> [1..1] Amount C2, C12 500
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 501
       Reason <Rsn> [0..1] Text 501
       AdditionalInformation <AddtlInf> [0..1] Text 501
5.4.2.18.17.2.1.4.1  Identification <Id>
Presence: [1..*]
Definition: Provides identification of the document line.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 496 March 2026
```

