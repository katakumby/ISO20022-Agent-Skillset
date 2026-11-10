---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12", "20.2 Structure"]
file_pages: [656, 657, 658]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.026.001.12"]
---

# 20.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 656 to 658.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 656

```text
20.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmTxRvslAdvc> [1..1]  C10,
C15,
C40,
C53,
C54
   TransactionIdentificationDetails <TxIdDtls> [1..1] ± C29 0
   ConfirmationReference <ConfRef> [1..1] Text 666
   AdditionalParameters <AddtlParams> [0..1] ± 666
   TradeDetails <TradDtls> [1..1]  C3, C23,
C38,
C59,
C58
0
     TradeIdentification <TradId> [0..*] Text 669
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 669
     CollateralTransactionIdentification <CollTxId> [0..*] Text 669
     PlaceOfTrade <PlcOfTrad> [0..1] ± 669
     PlaceOfClearing <PlcOfClr> [0..1] ± 669
     TradeDate <TradDt> [0..1] ± 670
     SettlementDate <SttlmDt> [0..1] ± 670
     EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 670
     DealPrice <DealPric> [0..1] ± 670
     NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C30 671
     OpeningClosing <OpngClsg> [0..1] ± 671
     Reporting <Rptg> [0..*] ± 671
     TradeTransactionCondition <TradTxCond> [0..*] ± 672
     InvestorCapacity <InvstrCpcty> [0..1] ± 672
     TradeOriginatorRole <TradOrgtrRole> [0..1] ± 672
     TypeOfPrice <TpOfPric> [0..1] ± 672
     FXAdditionalDetails <FxAddtlDtls> [0..1] Text 673
     SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 673
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C18,
C19,
C25,
C26,
C31
0
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 656 March 2026
```

## File page 657

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C37 674
   QuantityAndAccountDetails <QtyAndAcctDtls> [1..1]  C16,
C32,
C41,
C45,
C49,
C51,
C52
676
     SettledQuantity <SttldQty> [1..1] ± 678
     PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± C20 678
     RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± C20 679
     PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 679
     RemainingToBeSettledAmount <RmngToBeSttldAmt> [0..1] ± 680
     DenominationChoice <DnmtnChc> [0..1] Text 680
     AccountOwner <AcctOwnr> [0..1] ± 680
     SafekeepingAccount <SfkpgAcct> [0..1] ± 680
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 681
     CashAccount <CshAcct> [0..1] ± 681
     QuantityBreakdown <QtyBrkdwn> [0..*] ± 681
     SafekeepingPlace <SfkpgPlc> [0..1] ± C50 682
   SettlementParameters <SttlmParams> [1..1] ± C11,
C56
682
   StandingSettlementInstructionDetails <StgSttlmInstrDtls> [0..1]  C60 0
     SettlementStandingInstructionDatabase <SttlmStgInstrDB> [1..1] ± 684
     Counterparty <CtrPty> [1..1] ± 685
     Vendor <Vndr> [0..1] ± 685
     OtherDeliveringSettlementParties <OthrDlvrgSttlmPties> [0..1] ± C9, C17,
C33,
C34,
C35,
C36,
C55
685
     OtherReceivingSettlementParties <OthrRcvgSttlmPties> [0..1] ± C9, C17,
C33,
C34,
C35,
C36,
C55
687
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C9, C17,
C33,
C34,
C35,
0
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 657 March 2026
```

## File page 658

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
C36,
C55
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C9, C17,
C33,
C34,
C35,
C36,
C55
691
   CashParties <CshPties> [0..1]  693
     Debtor <Dbtr> [0..1] ± 693
     DebtorAgent <DbtrAgt> [0..1] ± 694
     Creditor <Cdtr> [0..1] ± 694
     CreditorAgent <CdtrAgt> [0..1] ± 695
   SettledAmount <SttldAmt> [0..1] ± 0
   OtherAmounts <OthrAmts> [0..1] ± 0
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..2]  698
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C18,
C19,
C25,
C26,
C31
698
     Quantity <Qty> [1..1]  699
{Or       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 699
Or}       NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 700
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  700
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 700
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C7 700
Or}       LEI <LEI> [1..1] IdentifierSet 700
   OtherBusinessParties <OthrBizPties> [0..1]  C24,
C39
0
     Investor <Invstr> [0..*] ± C22,
C43,
C47
701
     QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C44,
C48
702
     StockExchange <StockXchg> [0..1] ± 703
     TradeRegulator <TradRgltr> [0..1] ± 703
     TripartyAgent <TrptyAgt> [0..1] ± C44,
C48
704
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 658 March 2026
```

