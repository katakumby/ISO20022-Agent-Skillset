---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["74 semt.029.001.01 IntraPositionMovementQueryResponseV01", "74.4 Message Building Blocks", "74.4.3 Movements <Mvmnts>", "74.4.3.4 Movement <Mvmnt>"]
file_pages: [2624, 2625]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 74.4.3.4 Movement <Mvmnt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2624 to 2625.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2624

```text
Settled <Sttld> contains the following elements (see "ProprietaryReason4" on page 3139 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 3140
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3140
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
74.4.3.4  Movement <Mvmnt>
Presence: [1..*]
Definition: Identifies the individual transaction.
Impacted by: C14 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2624 August 2026
```

## File page 2625

```text
Movement <Mvmnt> contains the following IntraPositionMovement10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1] ± 2626
   SafekeepingAccount <SfkpgAcct> [0..1] ± 2627
   StatusAndReason <StsAndRsn> [0..1]  2627
     ProcessingStatus <PrcgSts> [0..*] ± 2627
     SettlementStatus <SttlmSts> [0..*] ± C16 2627
     Settled <Sttld> [0..1] ± C6 2628
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 2628
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 2628
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2629
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2629
   PoolIdentification <PoolId> [0..1] Text 2629
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 2629
   MovementDetails <MvmntDtls> [0..1]  2629
     BalanceFrom <BalFr> [1..1] ± 2631
     BalanceTo <BalTo> [1..1] ± 2631
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C9, C10,
C12,
C13,
C15
2631
     FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C5, C17 2632
     SettlementQuantity <SttlmQty> [1..1] ± 2634
     SettledQuantity <SttldQty> [0..1] ± 2634
     PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± 2635
     RemainingToBeSettledQuantity
<RmngToBeSttldQty>
[0..1] ± 2635
     IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 2635
     EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 2636
     StatusDate <StsDt> [0..1] DateTime 2636
     AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 2636
     Linkages <Lnkgs> [0..*]  2636
       ProcessingPosition <PrcgPos> [0..1] ± C25 2637
       MessageNumber <MsgNb> [0..1] ± C22 2637
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2625 August 2026
```

