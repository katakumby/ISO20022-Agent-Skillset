---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks"]
file_pages: [576, 577]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4 Message Building Blocks

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 576 to 577.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 576

```text
On Condition
    /GroupHeader/TotalReversedInterbankSettlementAmount is present
 And    /TransactionInformation[1] is present
 And    /TransactionInformation[*]/ReversedInterbankSettlementAmount is 
present
Following Must be True
    /TransactionInformation[*]/ReversedInterbankSettlementAmount/
attribute::Currency Must be equal to /GroupHeader/
TotalReversedInterbankSettlementAmount/attribute::Currency
This constraint is defined at the MessageDefinition level.
C41 TransactionInterbankSettlementDateRule
If GroupHeader/InterbankSettlementDate is not present, then TransactionInformation/
InterbankSettlementDate must be present.
On Condition
    /GroupHeader/InterbankSettlementDate is absent
Following Must be True
    /TransactionInformation[*]/InterbankSettlementDate Must be present
This constraint is defined at the MessageDefinition level.
5.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
5.4.1 GroupHeader <GrpHdr>
Presence: [1..1]
Definition: Set of characteristics shared by all individual transactions included in the message.
Impacted by: C8 "ControlSumAndGroupReversalRule", C38
"TotalInterbankSettlementAmountAndDateRule", C13
"GroupReversalAndNumberOfTransactionsGuideline"
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
576 March 2026
```

## File page 577

```text
GroupHeader <GrpHdr> contains the following GroupHeader127 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 578
   CreationDateTime <CreDtTm> [1..1] DateTime 578
   Authorisation <Authstn> [0..2] ± 578
   BatchBooking <BtchBookg> [0..1] Indicator 579
   NumberOfTransactions <NbOfTxs> [1..1] Text 579
   ControlSum <CtrlSum> [0..1] Quantity 579
   GroupReversal <GrpRvsl> [0..1] Indicator 579
   TotalReversedInterbankSettlementAmount
<TtlRvsdIntrBkSttlmAmt>
[0..1] Amount C1, C10 579
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 580
   SettlementInformation <SttlmInf> [1..1]  C22,
C24,
C30,
C31,
C32,
C33,
C36,
C37
580
     SettlementMethod <SttlmMtd> [1..1] CodeSet 582
     SettlementAccount <SttlmAcct> [0..1] ± C20,
C19
583
     ClearingSystem <ClrSys> [0..1]  583
{Or       Code <Cd> [1..1] CodeSet 584
Or}       Proprietary <Prtry> [1..1] Text 584
     InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 584
     InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C20,
C19
585
     InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 585
     InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C20,
C19
586
     ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 587
     ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C20,
C19
587
   InstructingAgent <InstgAgt> [0..1] ± 588
   InstructedAgent <InstdAgt> [0..1] ± 589
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
577 March 2026
```

