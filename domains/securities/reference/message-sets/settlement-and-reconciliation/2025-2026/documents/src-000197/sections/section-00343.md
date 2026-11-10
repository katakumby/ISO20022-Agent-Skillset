---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "17.2 Structure"]
file_pages: [494, 495, 496]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.023.001.13"]
---

# 17.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 494 to 496.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 494

```text
17.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmTxInstr> [1..1]  C6, C12,
C13,
C19,
C20,
C23,
C41,
C44,
C52,
C53,
C66,
C68,
C69,
C77,
C78,
C38,
C67
   TransactionIdentification <TxId> [1..1] Text 0
   SettlementTypeAndAdditionalParameters
<SttlmTpAndAddtlParams>
[1..1] ± 0
   NumberCounts <NbCounts> [0..1] ± C21 0
   Linkages <Lnkgs> [0..*]  C39 0
     ProcessingPosition <PrcgPos> [0..1] ± C80 512
     MessageNumber <MsgNb> [0..1] ± C73 512
     Reference <Ref> [1..1] ± 513
     LinkedQuantity <LkdQty> [0..1]  513
{Or       PairedOffQuantity <PairdOffQty> [1..1] ± C28 514
Or}       TurnedQuantity <TrndQty> [1..1] ± C28 514
     ReferenceOwner <RefOwnr> [0..1] ± 514
   TradeDetails <TradDtls> [1..1]  C3, C18,
C32,
C37,
C50,
C76,
C75
0
     TradeIdentification <TradId> [0..*] Text 518
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 518
     CollateralTransactionIdentification <CollTxId> [0..*] Text 518
     PlaceOfTrade <PlcOfTrad> [0..1] ± 518
     PlaceOfClearing <PlcOfClr> [0..1] ± 518
     TradeDate <TradDt> [0..1] ± 519
     SettlementDate <SttlmDt> [1..1] ± 519
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 494 March 2026
```

## File page 495

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     LateDeliveryDate <LateDlvryDt> [0..1] ± 519
     DealPrice <DealPric> [0..1] ± 519
     NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C42 520
     OpeningClosing <OpngClsg> [0..1] ± 520
     Reporting <Rptg> [0..*] ± 520
     TradeTransactionCondition <TradTxCond> [0..*] ± 521
     InvestorCapacity <InvstrCpcty> [0..1] ± 521
     TradeOriginatorRole <TradOrgtrRole> [0..1] ± 521
     TypeOfPrice <TpOfPric> [0..1] ± 521
     CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 522
     MatchingStatus <MtchgSts> [0..1] ± 522
     AffirmationStatus <AffirmSts> [0..1] ± 522
     FXAdditionalDetails <FxAddtlDtls> [0..1] Text 522
     SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 522
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C26,
C27,
C34,
C35,
C43
0
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C49 0
   QuantityAndAccountDetails <QtyAndAcctDtls> [1..1]  C24,
C54,
C58,
C62,
C64,
C65
0
     SettlementQuantity <SttlmQty> [1..1] ± 528
     DenominationChoice <DnmtnChc> [0..1] Text 528
     AccountOwner <AcctOwnr> [0..1] ± 528
     SafekeepingAccount <SfkpgAcct> [0..1] ± 529
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 529
     CashAccount <CshAcct> [0..1] ± 529
     SafekeepingPlace <SfkpgPlc> [0..1] ± C63 530
     QuantityBreakdown <QtyBrkdwn> [0..*] ± 530
   SettlementParameters <SttlmParams> [1..1] ± C14,
C29,
531
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 495 March 2026
```

## File page 496

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
C71,
C72
   StandingSettlementInstructionDetails <StgSttlmInstrDtls> [0..1]  C79 0
     SettlementStandingInstructionDatabase <SttlmStgInstrDB> [1..1] ± 535
     Counterparty <CtrPty> [1..1] ± 535
     Vendor <Vndr> [0..1] ± 535
     OtherDeliveringSettlementParties <OthrDlvrgSttlmPties> [0..1] ± C11,
C25,
C45,
C46,
C47,
C48,
C70
535
     OtherReceivingSettlementParties <OthrRcvgSttlmPties> [0..1] ± C11,
C25,
C45,
C46,
C47,
C48,
C70
537
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C11,
C25,
C45,
C46,
C47,
C48,
C70
539
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C11,
C25,
C45,
C46,
C47,
C48,
C70
0
   CashParties <CshPties> [0..1] ± 0
   SettlementAmount <SttlmAmt> [0..1] ± 544
   OtherAmounts <OthrAmts> [0..1] ± 544
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..2]  0
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C26,
C27,
C34,
C35,
C43
546
     Quantity <Qty> [1..1]  547
{Or       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 547
Or}       NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 547
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 496 March 2026
```

