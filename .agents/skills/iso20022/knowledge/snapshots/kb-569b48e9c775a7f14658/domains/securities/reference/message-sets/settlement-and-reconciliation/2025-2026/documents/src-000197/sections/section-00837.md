---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.3 Modification <Mod>"]
file_pages: [1252, 1253, 1254, 1255]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.3 Modification <Mod>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1252 to 1255.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1252

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1565
   Envelope <Envlp> [1..1] (External Schema) 1565
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
32.4.2.3  Modification <Mod>
Presence: [1..1]
Definition: Modification of information in the securities transaction.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1252 March 2026
```

## File page 1253

```text
Modification <Mod> contains the following SecuritiesSettlementTransactionDetails61 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementTypeAndAdditionalParameters
<SttlmTpAndAddtlParams>
[0..1] ± 1256
   Linkages <Lnkgs> [0..*]  C35 1256
     ProcessingPosition <PrcgPos> [0..1] ± C85 1257
     MessageNumber <MsgNb> [0..1] ± C77 1257
     Reference <Ref> [1..1] ± 1258
     LinkedQuantity <LkdQty> [0..1]  1258
{Or       PairedOffQuantity <PairdOffQty> [1..1] ± C23 1258
Or}       TurnedQuantity <TrndQty> [1..1] ± C23 1259
   TradeDetails <TradDtls> [0..1]  C6, C17,
C27,
C33,
C55,
C80,
C82
1259
     TradeIdentification <TradId> [0..1] Text 1262
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 1262
     CollateralTransactionIdentification <CollTxId> [0..*] Text 1262
     PlaceOfTrade <PlcOfTrad> [0..1] ± 1262
     PlaceOfClearing <PlcOfClr> [0..1] ± 1262
     TradeDate <TradDt> [0..1] ± 1263
     SettlementDate <SttlmDt> [0..1] ± 1263
     LateDeliveryDate <LateDlvryDt> [0..1] ± 1263
     DealPrice <DealPric> [0..1] ± 1263
     NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C38 1264
     OpeningClosing <OpngClsg> [0..1] ± 1264
     Reporting <Rptg> [0..*] ± 1264
     TradeTransactionCondition <TradTxCond> [0..*] ± 1264
     InvestorCapacity <InvstrCpcty> [0..1] ± 1265
     TradeOriginatorRole <TradOrgtrRole> [0..1] ± 1265
     TypeOfPrice <TpOfPric> [0..1] ± 1265
     CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 1265
     MatchingStatus <MtchgSts> [0..1] ± 1266
     AffirmationStatus <AffirmSts> [0..1] ± 1266
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1253 March 2026
```

## File page 1254

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     FXAdditionalDetails <FxAddtlDtls> [0..1] Text 1266
     SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 1266
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C21,
C22,
C29,
C30,
C40
1266
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C53 1268
   QuantityAndAccountDetails <QtyAndAcctDtls> [0..1]  C19,
C62,
C68,
C72,
C73
1270
     SettlementQuantity <SttlmQty> [0..1] ± 1272
     DenominationChoice <DnmtnChc> [0..1] Text 1272
     AccountOwner <AcctOwnr> [0..1] ± 1272
     SafekeepingAccount <SfkpgAcct> [0..1] ± 1272
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1273
     CashAccount <CshAcct> [0..1] ± 1273
     SafekeepingPlace <SfkpgPlc> [0..1] ± C70 1273
     QuantityBreakdown <QtyBrkdwn> [0..*] ± 1274
   SettlementParameters <SttlmParams> [0..1] ± C12,
C39,
C76
1274
   StandingSettlementInstructionDetails
<StgSttlmInstrDtls>
[0..1]  C84 1278
     SettlementStandingInstructionDatabase
<SttlmStgInstrDB>
[1..1] ± 1278
     Counterparty <CtrPty> [1..1] ± 1279
     Vendor <Vndr> [0..1] ± 1279
     OtherDeliveringSettlementParties
<OthrDlvrgSttlmPties>
[0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1279
     OtherReceivingSettlementParties
<OthrRcvgSttlmPties>
[0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1281
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1254 March 2026
```

## File page 1255

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1283
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1285
   CashParties <CshPties> [0..1] ± 1287
   SettlementAmount <SttlmAmt> [0..1] ± 1287
   OtherAmounts <OthrAmts> [0..1] ± 1288
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..2]  1289
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C21,
C22,
C29,
C30,
C40
1290
     Quantity <Qty> [1..1]  1291
{Or       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1291
Or}       NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 1291
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1291
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1292
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C8 1292
Or}       LEI <LEI> [1..1] IdentifierSet 1292
   OtherBusinessParties <OthrBizPties> [0..1]  C28,
C56
1292
     Investor <Invstr> [0..*] ± C25,
C60,
C66
1293
     QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C61,
C67
1294
     StockExchange <StockXchg> [0..1] ± 1295
     TradeRegulator <TradRgltr> [0..1] ± 1295
     TripartyAgent <TrptyAgt> [0..1] ± C61,
C67
1295
     Broker <Brkr> [0..1] ± C61,
C67
1296
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1255 March 2026
```

