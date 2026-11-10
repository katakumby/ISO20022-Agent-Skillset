---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.26 RemittanceInformation <RmtInf>", "2.4.2.19.26.2 Structured <Strd>", "2.4.2.19.26.2.1 ReferredDocumentInformation <RfrdDocInf>", "2.4.2.19.26.2.1.4 LineDetails <LineDtls>"]
file_pages: [99]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.26.2.1.4 LineDetails <LineDtls>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 99 to 99.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 99

```text
2.4.2.19.26.2.1.4  LineDetails <LineDtls>
Presence: [0..*]
Definition: Set of elements used to provide the content of the referred document line.
LineDetails <LineDtls> contains the following DocumentLineInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..*]  99
     Type <Tp> [0..1]  100
       CodeOrProprietary <CdOrPrtry> [1..1]  100
{Or         Code <Cd> [1..1] CodeSet 100
Or}         Proprietary <Prtry> [1..1] Text 100
       Issuer <Issr> [0..1] Text 101
     Number <Nb> [0..1] Text 101
     RelatedDate <RltdDt> [0..1] Date 101
   Description <Desc> [0..1] Text 101
   Amount <Amt> [0..1]  C33 101
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  102
       Type <Tp> [1..1]  102
{Or         Code <Cd> [1..1] CodeSet 103
Or}         Proprietary <Prtry> [1..1] Text 103
       Amount <Amt> [1..1] Amount C2, C19 103
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  103
       Amount <Amt> [1..1] Amount C2, C19 103
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 104
       Reason <Rsn> [0..1] Text 104
       AdditionalInformation <AddtlInf> [0..1] Text 104
2.4.2.19.26.2.1.4.1  Identification <Id>
Presence: [1..*]
Definition: Provides identification of the document line.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 99 March 2026
```

