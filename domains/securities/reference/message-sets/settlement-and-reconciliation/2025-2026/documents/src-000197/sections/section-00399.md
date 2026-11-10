---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13", "19.2 Structure"]
file_pages: [601, 602, 603]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.025.001.13"]
---

# 19.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 601 to 603.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 601

```text
19.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmTxConf> [1..1]  C10,
C15,
C41,
C55,
C56,
C62,
C63,
C54
   TransactionIdentificationDetails <TxIdDtls> [1..1] ± C29 0
   Linkages <Lnkgs> [0..1] ± 614
   AdditionalParameters <AddtlParams> [0..1] ± C32 0
   TradeDetails <TradDtls> [1..1]  C3, C23,
C39,
C61,
C60
0
     TradeIdentification <TradId> [0..*] Text 617
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 617
     CollateralTransactionIdentification <CollTxId> [0..*] Text 617
     PlaceOfTrade <PlcOfTrad> [0..1] ± 617
     PlaceOfClearing <PlcOfClr> [0..1] ± 617
     TradeDate <TradDt> [0..1] ± 618
     SettlementDate <SttlmDt> [0..1] ± 618
     EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 618
     DealPrice <DealPric> [0..1] ± 618
     NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C30 619
     OpeningClosing <OpngClsg> [0..1] ± 619
     Reporting <Rptg> [0..*] ± 619
     TradeTransactionCondition <TradTxCond> [0..*] ± 620
     InvestorCapacity <InvstrCpcty> [0..1] ± 620
     TradeOriginatorRole <TradOrgtrRole> [0..1] ± 620
     TypeOfPrice <TpOfPric> [0..1] ± 620
     FXAdditionalDetails <FxAddtlDtls> [0..1] Text 621
     SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 621
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C18,
C19,
C25,
0
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 601 March 2026
```

## File page 602

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
C26,
C31
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C38 0
   QuantityAndAccountDetails <QtyAndAcctDtls> [1..1]  C16,
C33,
C42,
C46,
C50,
C52,
C53
0
     SettledQuantity <SttldQty> [1..1] ± 626
     PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± C20 626
     RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± C20 627
     PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 627
     RemainingToBeSettledAmount <RmngToBeSttldAmt> [0..1] ± 628
     DenominationChoice <DnmtnChc> [0..1] Text 628
     AccountOwner <AcctOwnr> [0..1] ± 628
     SafekeepingAccount <SfkpgAcct> [0..1] ± 628
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 629
     CashAccount <CshAcct> [0..1] ± 629
     QuantityBreakdown <QtyBrkdwn> [0..*] ± 629
     SafekeepingPlace <SfkpgPlc> [0..1] ± C51 630
   SettlementParameters <SttlmParams> [1..1] ± C11,
C58
0
   StandingSettlementInstructionDetails <StgSttlmInstrDtls> [0..1]  C64 0
     SettlementStandingInstructionDatabase <SttlmStgInstrDB> [1..1] ± 632
     Counterparty <CtrPty> [1..1] ± 633
     Vendor <Vndr> [0..1] ± 633
     OtherDeliveringSettlementParties <OthrDlvrgSttlmPties> [0..1] ± C9, C17,
C34,
C35,
C36,
C37,
C57
633
     OtherReceivingSettlementParties <OthrRcvgSttlmPties> [0..1] ± C9, C17,
C34,
C35,
C36,
C37,
C57
635
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C9, C17,
C34,
C35,
0
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 602 March 2026
```

## File page 603

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
C36,
C37,
C57
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C9, C17,
C34,
C35,
C36,
C37,
C57
0
   CashParties <CshPties> [0..1] ± 641
   SettledAmount <SttldAmt> [0..1] ± 642
   OtherAmounts <OthrAmts> [0..1] ± 642
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..2]  644
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C18,
C19,
C25,
C26,
C31
644
     Quantity <Qty> [1..1]  645
{Or       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 645
Or}       NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 646
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  646
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 646
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C7 646
Or}       LEI <LEI> [1..1] IdentifierSet 646
   OtherBusinessParties <OthrBizPties> [0..1]  C24,
C40
646
     Investor <Invstr> [0..*] ± C22,
C44,
C48
647
     QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C45,
C49
648
     StockExchange <StockXchg> [0..1] ± 649
     TradeRegulator <TradRgltr> [0..1] ± 649
     TripartyAgent <TrptyAgt> [0..1] ± C45,
C49
650
     Broker <Brkr> [0..1] ± C45,
C49
651
   AdditionalPhysicalOrRegistrationDetails
<AddtlPhysOrRegnDtls>
[0..1]  0
     CertificationIdentification <CertfctnId> [0..1] Text 652
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 603 March 2026
```

