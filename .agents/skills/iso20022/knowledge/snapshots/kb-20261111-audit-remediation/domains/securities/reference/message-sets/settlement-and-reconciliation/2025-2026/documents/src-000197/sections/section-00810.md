---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.2 Deletion <Deltn>"]
file_pages: [1215, 1216, 1217]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.2 Deletion <Deltn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1215 to 1217.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1215

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
32.4.2.2  Deletion <Deltn>
Presence: [1..1]
Definition: Deletion of information in the securities transaction.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1215 March 2026
```

## File page 1216

```text
Deletion <Deltn> contains the following SecuritiesSettlementTransactionDetails60 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementTypeAndAdditionalParameters
<SttlmTpAndAddtlParams>
[0..1] ± 1218
   Linkages <Lnkgs> [0..*] ± 1218
   TradeDetails <TradDtls> [0..1]  C3, C16,
C26,
C32,
C54,
C79,
C81
1219
     TradeIdentification <TradId> [0..1] Text 1221
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 1221
     CollateralTransactionIdentification <CollTxId> [0..*] Text 1221
     PlaceOfTrade <PlcOfTrad> [0..1] ± 1221
     PlaceOfClearing <PlcOfClr> [0..1] ± 1221
     TradeDate <TradDt> [0..1] ± 1222
     LateDeliveryDate <LateDlvryDt> [0..1] ± 1222
     DealPrice <DealPric> [0..1] ± 1222
     NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C38 1223
     OpeningClosing <OpngClsg> [0..1] ± 1223
     Reporting <Rptg> [0..*] ± 1223
     TradeTransactionCondition <TradTxCond> [0..*] ± 1223
     InvestorCapacity <InvstrCpcty> [0..1] ± 1224
     TradeOriginatorRole <TradOrgtrRole> [0..1] ± 1224
     TypeOfPrice <TpOfPric> [0..1] ± 1224
     CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 1224
     MatchingStatus <MtchgSts> [0..1] ± 1225
     AffirmationStatus <AffirmSts> [0..1] ± 1225
     FXAdditionalDetails <FxAddtlDtls> [0..1] Text 1225
     SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 1225
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C53 1225
   QuantityAndAccountDetails <QtyAndAcctDtls> [0..1] ± C18,
C71
1228
   SettlementParameters <SttlmParams> [0..1] ± C12,
C39,
C76
1229
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1216 March 2026
```

## File page 1217

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StandingSettlementInstructionDetails
<StgSttlmInstrDtls>
[0..1]  C84 1233
     SettlementStandingInstructionDatabase
<SttlmStgInstrDB>
[1..1] ± 1233
     Counterparty <CtrPty> [1..1] ± 1234
     Vendor <Vndr> [0..1] ± 1234
     OtherDeliveringSettlementParties
<OthrDlvrgSttlmPties>
[0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1234
     OtherReceivingSettlementParties
<OthrRcvgSttlmPties>
[0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1236
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C11,
C45,
C48,
C51
1238
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C11,
C45,
C48,
C51
1239
   CashParties <CshPties> [0..1] ± 1240
   SettlementAmount <SttlmAmt> [0..1] ± 1240
   OtherAmounts <OthrAmts> [0..1] ± 1241
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..2]  1242
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C21,
C22,
C29,
C30,
C40
1243
     Quantity <Qty> [1..1]  1244
{Or       ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1244
Or}       NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 1244
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1244
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1245
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C8 1245
Or}       LEI <LEI> [1..1] IdentifierSet 1245
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1217 March 2026
```

