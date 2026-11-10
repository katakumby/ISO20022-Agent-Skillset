---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["74 semt.029.001.01 IntraPositionMovementQueryResponseV01", "74.4 Message Building Blocks", "74.4.3 Movements <Mvmnts>"]
file_pages: [2619, 2620, 2621]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 74.4.3 Movements <Mvmnts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2619 to 2621.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2619

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
74.4.3 Movements <Mvmnts>
Presence: [0..*]
Definition: Identifies the intra-position movements.
Impacted by: C1 "AccountOwnerRule", C21 "SafekeepingAccountRule", C23 "StatusAndReasonRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2619 August 2026
```

## File page 2620

```text
Movements <Mvmnts> contains the following IntraPositionMovements6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1] ± 2622
   SafekeepingAccount <SfkpgAcct> [0..1] ± 2622
   StatusAndReason <StsAndRsn> [0..1]  2622
     ProcessingStatus <PrcgSts> [0..*] ± 2622
     SettlementStatus <SttlmSts> [0..*] ± C16 2623
     Settled <Sttld> [0..1] ± C6 2623
   Movement <Mvmnt> [1..*]  C14 2624
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2620 August 2026
```

## File page 2621

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 2635
       EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 2636
       StatusDate <StsDt> [0..1] DateTime 2636
       AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 2636
       Linkages <Lnkgs> [0..*]  2636
         ProcessingPosition <PrcgPos> [0..1] ± C25 2637
         MessageNumber <MsgNb> [0..1] ± C22 2637
         Reference <Ref> [1..1]  2638
{Or           SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 2638
Or           IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 2638
Or           IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 2639
Or           AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2639
Or           MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2639
Or           PoolIdentification <PoolId> [1..1] Text 2639
Or}           OtherTransactionIdentification <OthrTxId> [1..1] Text 2639
         ReferenceOwner <RefOwnr> [0..1] ± 2639
       SecuritiesSubBalanceIdentification
<SctiesSubBalId>
[0..1] ± 2640
       Priority <Prty> [0..1] ± 2640
       CorporateActionEventType <CorpActnEvtTp> [0..1] ± C11 2640
       MessageOriginator <MsgOrgtr> [0..1] ± 2641
       CreationDateTime <CreDtTm> [1..1] DateTime 2641
       InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 2641
       SupplementaryData <SplmtryData> [0..*] ± C24 2641
Constraints
• AccountOwnerRule
AccountOwner must be present or Movement(*)/AccountOwner must be present, but not both.
• SafekeepingAccountRule
SafekeepingAccount must be present or Movement(*)/SafekeepingAccount must be present, but not
both.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2621 August 2026
```

