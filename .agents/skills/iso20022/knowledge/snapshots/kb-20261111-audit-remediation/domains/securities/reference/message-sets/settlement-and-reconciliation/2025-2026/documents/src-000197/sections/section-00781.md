---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.1 Addition <Addtn>"]
file_pages: [1176, 1177, 1178]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.1 Addition <Addtn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1176 to 1178.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1176

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
     AdditionalPhysicalOrRegistrationDetails
<AddtlPhysOrRegnDtls>
[0..1]  1297
       CertificationIdentification <CertfctnId> [0..1] Text 1297
       CertificationDateTime <CertfctnDtTm> [0..1] ± 1298
       RegistrarAccount <RegarAcct> [0..1] Text 1298
       CertificateNumber <CertNb> [0..*] ± C31 1298
     SupplementaryData <SplmtryData> [0..*] ± C78 1298
32.4.2.1  Addition <Addtn>
Presence: [1..1]
Definition: Addition of information to the securities transaction.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1176 March 2026
```

## File page 1177

```text
Addition <Addtn> contains the following SecuritiesSettlementTransactionDetails59 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementTypeAndAdditionalParameters
<SttlmTpAndAddtlParams>
[0..1] ± 1179
   Linkages <Lnkgs> [0..*]  C35 1180
     ProcessingPosition <PrcgPos> [0..1] ± C85 1180
     MessageNumber <MsgNb> [0..1] ± C77 1180
     Reference <Ref> [1..1] ± 1181
     LinkedQuantity <LkdQty> [0..1]  1181
{Or       PairedOffQuantity <PairdOffQty> [1..1] ± C23 1181
Or}       TurnedQuantity <TrndQty> [1..1] ± C23 1182
   TradeDetails <TradDtls> [0..1]  C3, C16,
C26,
C32,
C54,
C79,
C81
1182
     TradeIdentification <TradId> [0..1] Text 1185
     UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 1185
     CollateralTransactionIdentification <CollTxId> [0..*] Text 1185
     PlaceOfTrade <PlcOfTrad> [0..1] ± 1185
     PlaceOfClearing <PlcOfClr> [0..1] ± 1185
     TradeDate <TradDt> [0..1] ± 1186
     LateDeliveryDate <LateDlvryDt> [0..1] ± 1186
     DealPrice <DealPric> [0..1] ± 1186
     NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C38 1187
     OpeningClosing <OpngClsg> [0..1] ± 1187
     Reporting <Rptg> [0..*] ± 1187
     TradeTransactionCondition <TradTxCond> [0..*] ± 1187
     InvestorCapacity <InvstrCpcty> [0..1] ± 1188
     TradeOriginatorRole <TradOrgtrRole> [0..1] ± 1188
     TypeOfPrice <TpOfPric> [0..1] ± 1188
     CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 1188
     MatchingStatus <MtchgSts> [0..1] ± 1189
     AffirmationStatus <AffirmSts> [0..1] ± 1189
     FXAdditionalDetails <FxAddtlDtls> [0..1] Text 1189
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1177 March 2026
```

## File page 1178

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 1189
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C53 1189
   QuantityAndAccountDetails <QtyAndAcctDtls> [0..1] ± C18,
C71
1191
   SettlementParameters <SttlmParams> [0..1] ± C12,
C39,
C76
1192
   StandingSettlementInstructionDetails
<StgSttlmInstrDtls>
[0..1]  C84 1196
     SettlementStandingInstructionDatabase
<SttlmStgInstrDB>
[1..1] ± 1196
     Counterparty <CtrPty> [1..1] ± 1197
     Vendor <Vndr> [0..1] ± 1197
     OtherDeliveringSettlementParties
<OthrDlvrgSttlmPties>
[0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1197
     OtherReceivingSettlementParties
<OthrRcvgSttlmPties>
[0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1199
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C11,
C45,
C48,
C51
1201
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C11,
C45,
C48,
C51
1202
   CashParties <CshPties> [0..1] ± 1203
   SettlementAmount <SttlmAmt> [0..1] ± 1203
   OtherAmounts <OthrAmts> [0..1] ± 1204
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..2]  1205
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C21,
C22,
C29,
C30,
C40
1206
     Quantity <Qty> [1..1]  1207
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1178 March 2026
```

