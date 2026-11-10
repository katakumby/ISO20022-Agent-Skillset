---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.7 ChequeInstruction <ChqInstr>", "2.4.2.19.7.1 ChequeType <ChqTp>"]
file_pages: [56]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.7.1 ChequeType <ChqTp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 56 to 56.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 56

```text
ChequeInstruction <ChqInstr> contains the following Cheque19 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ChequeType <ChqTp> [0..1] CodeSet 56
   ChequeNumber <ChqNb> [0..1] Text 57
   ChequeFrom <ChqFr> [0..1]  57
     Name <Nm> [1..1] Text 57
     Address <Adr> [1..1] ± 58
   DeliveryMethod <DlvryMtd> [0..1]  58
{Or     Code <Cd> [1..1] CodeSet 59
Or}     Proprietary <Prtry> [1..1] Text 59
   DeliverTo <DlvrTo> [0..1]  59
     Name <Nm> [1..1] Text 60
     Address <Adr> [1..1] ± 60
   InstructionPriority <InstrPrty> [0..1] CodeSet 60
   ChequeMaturityDate <ChqMtrtyDt> [0..1] Date 61
   FormsCode <FrmsCd> [0..1] Text 61
   MemoField <MemoFld> [0..2] Text 61
   RegionalClearingZone <RgnlClrZone> [0..1] Text 61
   PrintLocation <PrtLctn> [0..1] Text 61
   Signature <Sgntr> [0..5] Text 61
Constraints
• ChequeMaturityDateRule
If ChequeMaturityDate is present, then ChequeType must be present and equal to DRFT or ELDR.
On Condition
    /ChequeMaturityDate is present
Following Must be True
    /ChequeType Must be present
 And    /ChequeType Must be within DataType <<Code>> ChequeType3Code
2.4.2.19.7.1  ChequeType <ChqTp>
Presence: [0..1]
Definition: Specifies the type of cheque to be issued.
Datatype: "ChequeType2Code" on page 589
CodeName Name Definition
CCHQ CustomerCheque Cheque drawn on the account of the
debtor, and debited on the debtor's
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 56 March 2026
```

