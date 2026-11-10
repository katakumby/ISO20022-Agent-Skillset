---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.5 AccountServicer <AcctSvcr>"]
file_pages: [190, 191, 192, 193, 194]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.5 AccountServicer <AcctSvcr>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 190 to 194.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 190

```text
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification136" on
page 413 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 414
   LEI <LEI> [0..1] IdentifierSet 414
6.4.5 AccountServicer <AcctSvcr>
Presence: [1..1]
Definition: Party that manages the sub-level account on behalf of the account owner, that is manages
the registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification136" on
page 413 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 414
   LEI <LEI> [0..1] IdentifierSet 414
6.4.6 Penalty <Pnlty>
Presence: [0..*]
Definition: Claims (penalties) in a currency and of a date reported for a given party.
If there are no penalties in a given currency for a party, this block will not be informed.
Impacted by: C3 "CounterpartyCSDPresenceRule"
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 190 March 2026
```

## File page 191

```text
Penalty <Pnlty> contains the following Penalty4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Currency <Ccy> [1..1] CodeSet C1 195
   Date <Dt> [0..1] ± 195
   PartyIdentification <PtyId> [1..1]  195
     Identification <Id> [1..1] ± 196
     Type <Tp> [0..1]  196
{Or       Code <Cd> [1..1] CodeSet 196
Or}       Proprietary <Prtry> [1..1] ± 196
   CounterpartyCSD <CtrPtyCSD> [0..1] ± 197
   CSDDepository <CSDDpstry> [0..1] ± 197
   AggregatedAmount <AggtdAmt> [0..1]  197
     AggregatedDebitAmount <AggtdDbtAmt> [0..1] Amount C1, C5 198
     AggregatedCreditAmount <AggtdCdtAmt> [0..1] Amount C1, C5 198
     GlobalNetAmount <GblNetAmt> [0..1] ± 199
     CounterpartyCSDAggregatedAmount
<CtrPtyCSDAggtdAmt>
[0..*]  199
       PartyIdentification <PtyId> [1..1] ± 199
       AggregatedDebitAmount <AggtdDbtAmt> [0..1] Amount C1, C5 200
       AggregatedCreditAmount <AggtdCdtAmt> [0..1] Amount C1, C5 200
       GlobalNetAmount <GblNetAmt> [0..1] ± 200
   CashAccount <CshAcct> [0..1] ± 201
   CashSettlementDate <CshSttlmDt> [0..1] Date 201
   CashPenaltyIdentification <CshPnltyId> [0..1] Text 201
   NumberOfCounterparties <NbOfCtrPties> [0..1] Quantity 201
   PenaltyPerCounterparty <PnltyPerCtrPty> [0..*]  201
     AccountServicer <AcctSvcr> [0..1] ± 205
     PartyIdentification <PtyId> [1..1]  205
       Identification <Id> [1..1] ± 205
       Type <Tp> [0..1]  206
{Or         Code <Cd> [1..1] CodeSet 206
Or}         Proprietary <Prtry> [1..1] ± 206
     AggregatedNetAmount <AggtdNetAmt> [1..1] ± 206
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 191 March 2026
```

## File page 192

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PenaltyDetails <PnltyDtls> [0..*]  207
       Identification <Id> [1..1]  211
         MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] Text 211
         Identification <Id> [0..1] Text 211
         ReallocationIdentification <RallcnId> [0..1]  211
           MarketInfrastructureIdentification
<MktInfrstrctrId>
[1..1] Text 211
           Identification <Id> [0..1] Text 212
       Type <Tp> [1..1] CodeSet 212
       Insolvency <Inslvncy> [0..1] Indicator 212
       Status <Sts> [0..1]  212
         Status <Sts> [1..1]  213
{Or           Code <Cd> [1..1] CodeSet 213
Or}           Proprietary <Prtry> [1..1] ± 213
         Reason <Rsn> [0..*]  214
           Reason <Rsn> [1..1]  214
{Or             Code <Cd> [1..1] CodeSet 214
Or}             Proprietary <Prtry> [1..1] ± 215
           AdditionalStatusReason <AddtlStsRsn> [0..1] Text 215
       ComputedAmount <CmptdAmt> [1..1] ± 216
       CalculationMethod <ClctnMtd> [0..1] CodeSet 216
       NumberOfDays <NbOfDays> [0..1] Quantity 216
       CalculationData <ClctnData> [0..*]  216
         Date <Dt> [1..1] Date 218
         MissingReferenceData <MssngRefData> [0..1] Indicator 218
         FinancialInstrumentAttributes <FinInstrmAttrbts> [1..1]  218
           Identification <Id> [1..1] ± C6, C7,
C10,
C11,
C13
219
           SubjectToPenalties <SbjtToPnlties> [0..1] Indicator 220
           ClassificationType <ClssfctnTp> [0..1] ± 221
           Liquidity <Lqdty> [0..1] Indicator 221
           PriceData <PricData> [0..1]  221
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 192 March 2026
```

## File page 193

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Value <Val> [1..1]  221
{Or               Rate <Rate> [1..1] Rate 222
Or}               Amount <Amt> [1..1] Amount C1, C5 222
             SourceOfPrice <SrcOfPric> [0..1] ± 222
             QuotationDate <QtnDt> [0..1] ± 223
           ForeignExchangeData <FXData> [0..*]  223
             ExchangeRate <XchgRate> [1..1] Rate 223
             UnitCurrency <UnitCcy> [0..1] CodeSet C1 223
             QuotedCurrency <QtdCcy> [0..1] CodeSet C1 224
             QuotationDate <QtnDt> [0..1] ± 224
           SecuritiesPenaltyRateData <SctiesPnltyRateData> [0..1]  224
             MarketIdentification <MktId> [0..1] ± 224
             SMEGrowthMarket <SMEGrwthMkt> [0..1] Indicator 225
             Rate <Rate> [1..1] Rate 225
         DiscountRate <DscntRate> [0..1]  225
{Or           Rate <Rate> [1..1] Rate 225
Or}           Amount <Amt> [1..1] Amount C1, C5 225
         ForeignExchangeData <FXData> [0..*]  226
           ExchangeRate <XchgRate> [1..1] Rate 226
           UnitCurrency <UnitCcy> [0..1] CodeSet C1 226
           QuotedCurrency <QtdCcy> [0..1] CodeSet C1 227
           QuotationDate <QtnDt> [0..1] ± 227
         SubAmountPenaltyBreakdown
<SubAmtPnltyBrkdwn>
[0..*]  227
           Amount <Amt> [1..1] Amount C1, C5 227
           Type <Tp> [0..1] CodeSet 228
       RelatedTransaction <RltdTx> [0..1]  228
         Reference <Ref> [1..1] ± C12 230
         ReferenceOwner <RefOwnr> [0..1] ± 230
         TransactionDetails <TxDtls> [0..1]  231
           SettlementTransactionOrCorporateActionEventT
ype <SttlmTxOrCorpActnEvtTp>
[1..1] ± 232
           SettlementDate <SttlmDt> [1..1] ± 233
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 193 March 2026
```

## File page 194

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           CorporateActionRelatedDate <CorpActnRltdDt> [0..1] ± 233
           SafekeepingAccount <SfkpgAcct> [1..1] ± 233
           AccountOwner <AcctOwnr> [0..1] ± 233
           SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 234
           Payment <Pmt> [1..1] CodeSet 234
           PostingQuantity <PstngQty> [1..1] ± 234
           CashAccount <CshAcct> [0..1] ± 235
           CashAccountOwner <CshAcctOwnr> [0..1] ± 235
           PostingAmount <PstngAmt> [0..1] ± 236
           AcknowledgedStatusTimeStamp
<AckdStsTmStmp>
[0..1] DateTime 237
           MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 237
           SettlementStatusFailing <SttlmStsFlng> [0..1]  237
{Or             NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 237
Or}             Reason <Rsn> [1..*]  237
               Code <Cd> [1..1]  238
{Or                 Code <Cd> [1..1] CodeSet 238
Or}                 Proprietary <Prtry> [1..1] ± 241
               AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 242
           BusinessDayEvent <BizDayEvt> [0..1]  242
             Type <Tp> [1..1]  242
{Or               Code <Cd> [1..1] CodeSet 242
Or}               Proprietary <Prtry> [1..1] ± 243
             ScheduledTime <SchdldTm> [1..1] DateTime 243
             EffectiveTime <FctvTm> [0..1] DateTime 243
             StartTime <StartTm> [0..1] DateTime 243
             EndTime <EndTm> [0..1] DateTime 243
         NetMovementDetails <NetMvmntDtls> [0..1]  243
           SafekeepingAccount <SfkpgAcct> [0..1] ± 244
           SecuritiesShortfall <SctiesShrtfll> [0..1] ± 244
           ShortfallValuation <ShrtfllValtn> [0..1] ± 244
           TradeTransactionCondition <TradTxCond> [0..*] ± 245
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 194 March 2026
```

