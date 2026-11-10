---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["74 semt.029.001.01 IntraPositionMovementQueryResponseV01", "74.4 Message Building Blocks", "74.4.3 Movements <Mvmnts>", "74.4.3.4 Movement <Mvmnt>", "74.4.3.4.6 MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>"]
file_pages: [2629, 2630]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 74.4.3.4.6 MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2629 to 2630.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2629

```text
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 3328
74.4.3.4.6  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 3328
74.4.3.4.7  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction as assigned by the processor.
Datatype: "Max35Text" on page 3328
74.4.3.4.8  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
74.4.3.4.9  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 3328
74.4.3.4.10  MovementDetails <MvmntDtls>
Presence: [0..1]
Definition: Identifies additional details of the transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2629 August 2026
```

## File page 2630

```text
MovementDetails <MvmntDtls> contains the following IntraPositionMovement8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
   RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± 2635
   IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 2635
   EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 2636
   StatusDate <StsDt> [0..1] DateTime 2636
   AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 2636
   Linkages <Lnkgs> [0..*]  2636
     ProcessingPosition <PrcgPos> [0..1] ± C25 2637
     MessageNumber <MsgNb> [0..1] ± C22 2637
     Reference <Ref> [1..1]  2638
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 2638
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 2638
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 2639
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2639
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2639
Or       PoolIdentification <PoolId> [1..1] Text 2639
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 2639
     ReferenceOwner <RefOwnr> [0..1] ± 2639
   SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 2640
   Priority <Prty> [0..1] ± 2640
   CorporateActionEventType <CorpActnEvtTp> [0..1] ± C11 2640
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2630 August 2026
```

