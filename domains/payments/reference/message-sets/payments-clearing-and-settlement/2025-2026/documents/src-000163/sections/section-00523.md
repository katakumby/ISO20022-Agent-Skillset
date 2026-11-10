---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks"]
file_pages: [716, 717]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4 Message Building Blocks

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 716 to 717.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 716

```text
C49 TotalInterbankSettlementAmountAndDateRule
If TotalInterbankSettlementAmount is present, then InterbankSettlementDate must be present.
C50 TotalInterbankSettlementAmountAndSumRule
If GroupHeader/TotalInterbankSettlementAmount is present, then it must equal the sum of all
occurrences of CreditTransferTransactionInformation/InterbankSettlementAmount.
On Condition
    /GroupHeader/TotalInterbankSettlementAmount is present
Following Must be True
    /GroupHeader/TotalInterbankSettlementAmount Must be equal to value 'sum 
of /CreditTransferTransactionInformation/InterbankSettlementAmount'
This constraint is defined at the MessageDefinition level.
C51 TotalInterbankSettlementAmountRule
If GroupHeader/TotalInterbankSettlementAmount is present, then all occurrences of
CreditTransferTransactionInformation/InterbankSettlementAmount must have the same
currency as the currency of GroupHeader/TotalInterbankSettlementAmount.
On Condition
    /GroupHeader/TotalInterbankSettlementAmount is present
Following Must be True
    /CreditTransferTransactionInformation[*]/InterbankSettlementAmount/
attribute::Currency Must be equal to /GroupHeader/
TotalInterbankSettlementAmount/attribute::Currency
This constraint is defined at the MessageDefinition level.
C52 TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
C53 TransactionInterbankSettlementDateRule
If GroupHeader/InterbankSettlementDate is not present, then
CreditTransferTransactionInformation/InterbankSettlementDate must be present.
On Condition
    /GroupHeader/InterbankSettlementDate is absent
Following Must be True
    /CreditTransferTransactionInformation[*]/InterbankSettlementDate Must be 
present
This constraint is defined at the MessageDefinition level.
C54 UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
C55 UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
6.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
6.4.1 GroupHeader <GrpHdr>
Presence: [1..1]
Definition: Set of characteristics shared by all individual transactions included in the message.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
716 March 2026
```

## File page 717

```text
Impacted by: C49 "TotalInterbankSettlementAmountAndDateRule"
GroupHeader <GrpHdr> contains the following GroupHeader131 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 718
   CreationDateTime <CreDtTm> [1..1] DateTime 718
   ExpiryDateTime <XpryDtTm> [0..1] DateTime 718
   BatchBooking <BtchBookg> [0..1] Indicator 718
   NumberOfTransactions <NbOfTxs> [1..1] Text 718
   ControlSum <CtrlSum> [0..1] Quantity 719
   TotalInterbankSettlementAmount <TtlIntrBkSttlmAmt> [0..1] Amount C1, C11 719
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 719
   SettlementInformation <SttlmInf> [1..1]  C22,
C24,
C41,
C42,
C43,
C44,
C47,
C48
719
     SettlementMethod <SttlmMtd> [1..1] CodeSet 721
     SettlementAccount <SttlmAcct> [0..1] ± C17,
C16
722
     ClearingSystem <ClrSys> [0..1]  722
{Or       Code <Cd> [1..1] CodeSet 723
Or}       Proprietary <Prtry> [1..1] Text 723
     InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 723
     InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C17,
C16
724
     InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 724
     InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C17,
C16
725
     ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 726
     ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C17,
C16
726
   PaymentTypeInformation <PmtTpInf> [0..1] ± 727
   InstructingAgent <InstgAgt> [0..1] ± 728
   InstructedAgent <InstdAgt> [0..1] ± 729
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
717 March 2026
```

