---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.7 ChequeInstruction <ChqInstr>"]
file_pages: [55]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.7 ChequeInstruction <ChqInstr>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 55 to 55.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 55

```text
MandateRelatedInformation <MndtRltdInf> contains the following elements (see
"CreditTransferMandateData1" on page 535 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateIdentification <MndtId> [0..1] Text 535
   Type <Tp> [0..1] ± 535
   DateOfSignature <DtOfSgntr> [0..1] Date 536
   DateOfVerification <DtOfVrfctn> [0..1] DateTime 536
   ElectronicSignature <ElctrncSgntr> [0..1] Binary 536
   FirstPaymentDate <FrstPmtDt> [0..1] Date 536
   FinalPaymentDate <FnlPmtDt> [0..1] Date 536
   Frequency <Frqcy> [0..1] ± 537
   Reason <Rsn> [0..1]  537
{Or     Code <Cd> [1..1] CodeSet 537
Or}     Proprietary <Prtry> [1..1] Text 537
2.4.2.19.7  ChequeInstruction <ChqInstr>
Presence: [0..1]
Definition: Set of elements needed to issue a cheque.
Impacted by: C16 "ChequeMaturityDateRule"
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 55 March 2026
```

