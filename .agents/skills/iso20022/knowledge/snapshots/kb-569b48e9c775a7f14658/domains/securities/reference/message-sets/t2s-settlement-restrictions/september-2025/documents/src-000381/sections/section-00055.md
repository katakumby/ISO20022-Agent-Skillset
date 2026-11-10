---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "3.4 Message Building Blocks", "3.4.3 Movements <Mvmnts>", "3.4.3.4 Movement <Mvmnt>", "3.4.3.4.6 MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>"]
file_pages: [74, 75]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 3.4.3.4.6 MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 74 to 75.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 74

```text
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 345
3.4.3.4.6  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 345
3.4.3.4.7  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction as assigned by the processor.
Datatype: "Max35Text" on page 345
3.4.3.4.8  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 345
3.4.3.4.9  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 345
3.4.3.4.10  MovementDetails <MvmntDtls>
Presence: [0..1]
Definition: Identifies additional details of the transaction.
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 74 September 2025
```

## File page 75

```text
MovementDetails <MvmntDtls> contains the following IntraPositionMovement8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BalanceFrom <BalFr> [1..1] ± 76
   BalanceTo <BalTo> [1..1] ± 76
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C9, C10,
C12,
C13,
C15
76
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C5, C17 77
   SettlementQuantity <SttlmQty> [1..1] ± 79
   SettledQuantity <SttldQty> [0..1] ± 79
   PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± 80
   RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± 80
   IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 80
   EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 81
   StatusDate <StsDt> [0..1] DateTime 81
   AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 81
   Linkages <Lnkgs> [0..*]  81
     ProcessingPosition <PrcgPos> [0..1] ± C25 82
     MessageNumber <MsgNb> [0..1] ± C22 82
     Reference <Ref> [1..1]  83
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 83
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 83
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 84
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 84
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 84
Or       PoolIdentification <PoolId> [1..1] Text 84
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 84
     ReferenceOwner <RefOwnr> [0..1] ± 84
   SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 85
   Priority <Prty> [0..1] ± 85
   CorporateActionEventType <CorpActnEvtTp> [0..1] ± C11 85
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 75 September 2025
```

