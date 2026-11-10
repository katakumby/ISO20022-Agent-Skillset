---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks"]
file_pages: [272, 273, 274]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4 Message Building Blocks

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 272 to 274.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 272

```text
Following Must be True
    /TransactionInformation[*]/ReturnedInterbankSettlementAmount/
attribute::Currency Must be equal to /GroupHeader/
TotalReturnedInterbankSettlementAmount/attribute::Currency
This constraint is defined at the MessageDefinition level.
C74 TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
C75 TransactionInterbankSettlementDateRule
If GroupHeader/InterbankSettlementDate is not present, then TransactionInformation/
InterbankSettlementDate must be present.
On Condition
    /GroupHeader/InterbankSettlementDate is absent
Following Must be True
    /TransactionInformation[*]/InterbankSettlementDate Must be present
This constraint is defined at the MessageDefinition level.
C76 UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
C77 UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
C78 UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
C79 UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
C80 UnderlyingAllocationGuideline
UnderlyingAllocation may only be present if bilaterally agreed.
C81 UnderlyingCustomerCreditTransferRule
The UnderlyingCustomerCreditTransfer element can only be present if present in the original
transaction being returned.
C82 UnderlyingFinancialInstitutionCreditTransferRule
The UnderlyingFinancialInstitutionCreditTransfer element can only be present if present in the
original transaction being returned.
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
4.4.1 GroupHeader <GrpHdr>
Presence: [1..1]
Definition: Set of characteristics shared by all individual transactions included in the message.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
272 March 2026
```

## File page 273

```text
Impacted by: C8 "ControlSumAndGroupReturnRule", C71
"TotalInterbankSettlementAmountAndDateRule", C15
"GroupReturnAndNumberOfTransactionsGuideline"
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
273 March 2026
```

## File page 274

```text
GroupHeader <GrpHdr> contains the following GroupHeader123 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 275
   CreationDateTime <CreDtTm> [1..1] DateTime 275
   Authorisation <Authstn> [0..2] ± 275
   BatchBooking <BtchBookg> [0..1] Indicator 276
   NumberOfTransactions <NbOfTxs> [1..1] Text 276
   ControlSum <CtrlSum> [0..1] Quantity 276
   GroupReturn <GrpRtr> [0..1] Indicator 276
   TotalReturnedInterbankSettlementAmount
<TtlRtrdIntrBkSttlmAmt>
[0..1] Amount C1, C11 276
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 277
   SettlementInformation <SttlmInf> [1..1]  C24,
C26,
C63,
C64,
C65,
C66,
C69,
C70
277
     SettlementMethod <SttlmMtd> [1..1] CodeSet 279
     SettlementAccount <SttlmAcct> [0..1] ± C22,
C21
280
     ClearingSystem <ClrSys> [0..1]  280
{Or       Code <Cd> [1..1] CodeSet 281
Or}       Proprietary <Prtry> [1..1] Text 281
     InstructingReimbursementAgent
<InstgRmbrsmntAgt>
[0..1] ± 281
     InstructingReimbursementAgentAccount
<InstgRmbrsmntAgtAcct>
[0..1] ± C22,
C21
282
     InstructedReimbursementAgent <InstdRmbrsmntAgt> [0..1] ± 282
     InstructedReimbursementAgentAccount
<InstdRmbrsmntAgtAcct>
[0..1] ± C22,
C21
283
     ThirdReimbursementAgent <ThrdRmbrsmntAgt> [0..1] ± 284
     ThirdReimbursementAgentAccount
<ThrdRmbrsmntAgtAcct>
[0..1] ± C22,
C21
284
   PaymentTypeInformation <PmtTpInf> [0..1] ± 285
   InstructingAgent <InstgAgt> [0..1] ± 286
   InstructedAgent <InstdAgt> [0..1] ± 287
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
274 March 2026
```

