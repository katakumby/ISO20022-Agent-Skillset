---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "18.2 Structure"]
file_pages: [558, 559]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.024.001.14"]
---

# 18.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 558 to 559.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 558

```text
18.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmTxStsAdvc> [1..1]  C12,
C17,
C25,
C34,
C35,
C32
   TransactionIdentification <TxId> [1..1] ± C18 0
   Linkages <Lnkgs> [0..1] ± 0
   ProcessingStatus <PrcgSts> [0..1]  0
{Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 568
Or     PendingProcessing <PdgPrcg> [1..1]  569
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 569
Or}       Reason <Rsn> [1..*]  569
         Code <Cd> [1..1]  569
{Or           Code <Cd> [1..1] CodeSet 570
Or}           Proprietary <Prtry> [1..1] ± 571
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 571
Or     Rejected <Rjctd> [1..1] ± 572
Or     Repair <Rpr> [1..1] ± 572
Or     Cancelled <Canc> [1..1] ± 572
Or     PendingCancellation <PdgCxl> [1..1]  573
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 573
Or}       Reason <Rsn> [1..*]  573
         Code <Cd> [1..1]  574
{Or           Code <Cd> [1..1] CodeSet 574
Or}           Proprietary <Prtry> [1..1] ± 574
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 575
Or     Proprietary <Prtry> [1..1] ± 575
Or     CancellationRequested <CxlReqd> [1..1] ± C3 575
Or}     ModificationRequested <ModReqd> [1..1] ± C3 576
   InferredMatchingStatus <IfrrdMtchgSts> [0..1] ± 576
   MatchingStatus <MtchgSts> [0..1] ± 0
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 558 March 2026
```

## File page 559

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
   SettlementStatus <SttlmSts> [0..1] ± C24 0
   TransactionDetails <TxDtls> [0..1]  C13,
C26,
C28,
C30,
C37,
C38
0
     TradeIdentification <TradId> [0..*] Text 583
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 583
     PoolIdentification <PoolId> [0..1] Text 584
     CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 584
     TripartyAgentServiceProviderCollateralTransactionIdentific
ation <TrptyAgtSvcPrvdrCollTxId>
[0..1] Text 584
     ClientTripartyCollateralTransactionIdentification
<ClntTrptyCollTxId>
[0..1] Text 584
     ClientCollateralInstructionIdentification <ClntCollInstrId> [0..1] Text 584
     TripartyAgentServiceProviderCollateralInstructionIdentificat
ion <TrptyAgtSvcPrvdrCollInstrId>
[0..1] Text 584
     NonceIdentification <NonceId> [0..1] Text 584
     AccountOwner <AcctOwnr> [0..1] ± 585
     SafekeepingAccount <SfkpgAcct> [0..1] ± 585
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 585
     SafekeepingPlace <SfkpgPlc> [0..1] ± C31 585
     PlaceOfTrade <PlcOfTrad> [0..1] ± 586
     PlaceOfClearing <PlcOfClr> [0..1] ± 586
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C9, C10,
C14,
C15,
C19
586
     SettlementQuantity <SttlmQty> [1..1] ± 587
     PartiallyReleasedQuantity <PrtlyRlsdQty> [0..1] ± 588
     SettlementAmount <SttlmAmt> [0..1] ± 588
     DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  588
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C9, C10,
C14,
C15,
C19
589
       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 590
       CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  590
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 559 March 2026
```

