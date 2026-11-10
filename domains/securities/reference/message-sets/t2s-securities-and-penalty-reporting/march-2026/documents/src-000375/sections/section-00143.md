---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.7 CashAccount <CshAcct>"]
file_pages: [201, 202, 203, 204]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.7 CashAccount <CshAcct>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 201 to 204.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 201

```text
6.4.6.7  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account account to be debited/credited for the settlement of the penalty.
CashAccount <CshAcct> contains one of the following elements (see "AccountIdentification4Choice"
on page 249 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C8 250
Or}   Other <Othr> [1..1] ± 250
6.4.6.8  CashSettlementDate <CshSttlmDt>
Presence: [0..1]
Definition: Date on which the payment of the penalty is due.
Datatype: "ISODate" on page 550
6.4.6.9  CashPenaltyIdentification <CshPnltyId>
Presence: [0..1]
Definition: Reference of the penalty payment.
Datatype: "Max35Text" on page 557
6.4.6.10  NumberOfCounterparties <NbOfCtrPties>
Presence: [0..1]
Definition: Number of counterparties involved in the penalty.
Datatype: "Number" on page 554
6.4.6.11  PenaltyPerCounterparty <PnltyPerCtrPty>
Presence: [0..*]
Definition: Claims (penalties) in a currency and of a date reported for a given party.
If there are no penalties in a given currency for a party, this block will not be informed.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 201 March 2026
```

## File page 202

```text
PenaltyPerCounterparty <PnltyPerCtrPty> contains the following PenaltyPerCounterparty4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountServicer <AcctSvcr> [0..1] ± 205
   PartyIdentification <PtyId> [1..1]  205
     Identification <Id> [1..1] ± 205
     Type <Tp> [0..1]  206
{Or       Code <Cd> [1..1] CodeSet 206
Or}       Proprietary <Prtry> [1..1] ± 206
   AggregatedNetAmount <AggtdNetAmt> [1..1] ± 206
   PenaltyDetails <PnltyDtls> [0..*]  207
     Identification <Id> [1..1]  211
       MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] Text 211
       Identification <Id> [0..1] Text 211
       ReallocationIdentification <RallcnId> [0..1]  211
         MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] Text 211
         Identification <Id> [0..1] Text 212
     Type <Tp> [1..1] CodeSet 212
     Insolvency <Inslvncy> [0..1] Indicator 212
     Status <Sts> [0..1]  212
       Status <Sts> [1..1]  213
{Or         Code <Cd> [1..1] CodeSet 213
Or}         Proprietary <Prtry> [1..1] ± 213
       Reason <Rsn> [0..*]  214
         Reason <Rsn> [1..1]  214
{Or           Code <Cd> [1..1] CodeSet 214
Or}           Proprietary <Prtry> [1..1] ± 215
         AdditionalStatusReason <AddtlStsRsn> [0..1] Text 215
     ComputedAmount <CmptdAmt> [1..1] ± 216
     CalculationMethod <ClctnMtd> [0..1] CodeSet 216
     NumberOfDays <NbOfDays> [0..1] Quantity 216
     CalculationData <ClctnData> [0..*]  216
       Date <Dt> [1..1] Date 218
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 202 March 2026
```

## File page 203

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
           Value <Val> [1..1]  221
{Or             Rate <Rate> [1..1] Rate 222
Or}             Amount <Amt> [1..1] Amount C1, C5 222
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
{Or         Rate <Rate> [1..1] Rate 225
Or}         Amount <Amt> [1..1] Amount C1, C5 225
       ForeignExchangeData <FXData> [0..*]  226
         ExchangeRate <XchgRate> [1..1] Rate 226
         UnitCurrency <UnitCcy> [0..1] CodeSet C1 226
         QuotedCurrency <QtdCcy> [0..1] CodeSet C1 227
         QuotationDate <QtnDt> [0..1] ± 227
       SubAmountPenaltyBreakdown
<SubAmtPnltyBrkdwn>
[0..*]  227
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 203 March 2026
```

## File page 204

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Amount <Amt> [1..1] Amount C1, C5 227
         Type <Tp> [0..1] CodeSet 228
     RelatedTransaction <RltdTx> [0..1]  228
       Reference <Ref> [1..1] ± C12 230
       ReferenceOwner <RefOwnr> [0..1] ± 230
       TransactionDetails <TxDtls> [0..1]  231
         SettlementTransactionOrCorporateActionEventTy
pe <SttlmTxOrCorpActnEvtTp>
[1..1] ± 232
         SettlementDate <SttlmDt> [1..1] ± 233
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
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 237
Or}           Reason <Rsn> [1..*]  237
             Code <Cd> [1..1]  238
{Or               Code <Cd> [1..1] CodeSet 238
Or}               Proprietary <Prtry> [1..1] ± 241
             AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 242
         BusinessDayEvent <BizDayEvt> [0..1]  242
           Type <Tp> [1..1]  242
{Or             Code <Cd> [1..1] CodeSet 242
Or}             Proprietary <Prtry> [1..1] ± 243
           ScheduledTime <SchdldTm> [1..1] DateTime 243
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 204 March 2026
```

