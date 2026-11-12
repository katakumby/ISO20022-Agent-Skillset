---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>"]
file_pages: [2789, 2790, 2791, 2792]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4 PenaltyDetails <PnltyDtls>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2789 to 2792.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2789

```text
AggregatedNetAmount <AggtdNetAmt> contains the following elements (see
"AmountAndDirection5" on page 2841 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C4 2841
   CreditDebit <CdtDbt> [0..1] CodeSet 2842
81.4.6.11.4  PenaltyDetails <PnltyDtls>
Presence: [0..*]
Definition: Further details on the penalty.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2789 August 2026
```

## File page 2790

```text
PenaltyDetails <PnltyDtls> contains the following PenaltyRecord4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  2793
     MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] Text 2793
     Identification <Id> [0..1] Text 2793
     ReallocationIdentification <RallcnId> [0..1]  2793
       MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] Text 2793
       Identification <Id> [0..1] Text 2794
   Type <Tp> [1..1] CodeSet 2794
   Insolvency <Inslvncy> [0..1] Indicator 2794
   Status <Sts> [0..1]  2794
     Status <Sts> [1..1]  2795
{Or       Code <Cd> [1..1] CodeSet 2795
Or}       Proprietary <Prtry> [1..1] ± 2795
     Reason <Rsn> [0..*]  2796
       Reason <Rsn> [1..1]  2796
{Or         Code <Cd> [1..1] CodeSet 2796
Or}         Proprietary <Prtry> [1..1] ± 2797
       AdditionalStatusReason <AddtlStsRsn> [0..1] Text 2797
   ComputedAmount <CmptdAmt> [1..1] ± 2798
   CalculationMethod <ClctnMtd> [0..1] CodeSet 2798
   NumberOfDays <NbOfDays> [0..1] Quantity 2798
   CalculationData <ClctnData> [0..*]  2798
     Date <Dt> [1..1] Date 2800
     MissingReferenceData <MssngRefData> [0..1] Indicator 2800
     FinancialInstrumentAttributes <FinInstrmAttrbts> [1..1]  2800
       Identification <Id> [1..1] ± C6, C7,
C10,
C11,
C13
2801
       SubjectToPenalties <SbjtToPnlties> [0..1] Indicator 2802
       ClassificationType <ClssfctnTp> [0..1] ± 2803
       Liquidity <Lqdty> [0..1] Indicator 2803
       PriceData <PricData> [0..1]  2803
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2790 August 2026
```

## File page 2791

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Value <Val> [1..1]  2803
{Or           Rate <Rate> [1..1] Rate 2804
Or}           Amount <Amt> [1..1] Amount C1, C5 2804
         SourceOfPrice <SrcOfPric> [0..1] ± 2804
         QuotationDate <QtnDt> [0..1] ± 2805
       ForeignExchangeData <FXData> [0..*]  2805
         ExchangeRate <XchgRate> [1..1] Rate 2805
         UnitCurrency <UnitCcy> [0..1] CodeSet C1 2805
         QuotedCurrency <QtdCcy> [0..1] CodeSet C1 2806
         QuotationDate <QtnDt> [0..1] ± 2806
       SecuritiesPenaltyRateData <SctiesPnltyRateData> [0..1]  2806
         MarketIdentification <MktId> [0..1] ± 2806
         SMEGrowthMarket <SMEGrwthMkt> [0..1] Indicator 2807
         Rate <Rate> [1..1] Rate 2807
     DiscountRate <DscntRate> [0..1]  2807
{Or       Rate <Rate> [1..1] Rate 2807
Or}       Amount <Amt> [1..1] Amount C1, C5 2807
     ForeignExchangeData <FXData> [0..*]  2808
       ExchangeRate <XchgRate> [1..1] Rate 2808
       UnitCurrency <UnitCcy> [0..1] CodeSet C1 2808
       QuotedCurrency <QtdCcy> [0..1] CodeSet C1 2809
       QuotationDate <QtnDt> [0..1] ± 2809
     SubAmountPenaltyBreakdown
<SubAmtPnltyBrkdwn>
[0..*]  2809
       Amount <Amt> [1..1] Amount C1, C5 2809
       Type <Tp> [0..1] CodeSet 2810
   RelatedTransaction <RltdTx> [0..1]  2810
     Reference <Ref> [1..1] ± C12 2812
     ReferenceOwner <RefOwnr> [0..1] ± 2812
     TransactionDetails <TxDtls> [0..1]  2813
       SettlementTransactionOrCorporateActionEventTyp
e <SttlmTxOrCorpActnEvtTp>
[1..1] ± 2814
       SettlementDate <SttlmDt> [1..1] ± 2815
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2791 August 2026
```

## File page 2792

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       CorporateActionRelatedDate <CorpActnRltdDt> [0..1] ± 2815
       SafekeepingAccount <SfkpgAcct> [1..1] ± 2815
       AccountOwner <AcctOwnr> [0..1] ± 2815
       SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 2816
       Payment <Pmt> [1..1] CodeSet 2816
       PostingQuantity <PstngQty> [1..1] ± 2816
       CashAccount <CshAcct> [0..1] ± 2817
       CashAccountOwner <CshAcctOwnr> [0..1] ± 2817
       PostingAmount <PstngAmt> [0..1] ± 2818
       AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 2819
       MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 2819
       SettlementStatusFailing <SttlmStsFlng> [0..1]  2819
{Or         NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2819
Or}         Reason <Rsn> [1..*]  2819
           Code <Cd> [1..1]  2820
{Or             Code <Cd> [1..1] CodeSet 2820
Or}             Proprietary <Prtry> [1..1] ± 2823
           AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2824
       BusinessDayEvent <BizDayEvt> [0..1]  2824
         Type <Tp> [1..1]  2824
{Or           Code <Cd> [1..1] CodeSet 2824
Or}           Proprietary <Prtry> [1..1] ± 2825
         ScheduledTime <SchdldTm> [1..1] DateTime 2825
         EffectiveTime <FctvTm> [0..1] DateTime 2825
         StartTime <StartTm> [0..1] DateTime 2825
         EndTime <EndTm> [0..1] DateTime 2825
     NetMovementDetails <NetMvmntDtls> [0..1]  2825
       SafekeepingAccount <SfkpgAcct> [0..1] ± 2826
       SecuritiesShortfall <SctiesShrtfll> [0..1] ± 2826
       ShortfallValuation <ShrtfllValtn> [0..1] ± 2826
       TradeTransactionCondition <TradTxCond> [0..*] ± 2827
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2792 August 2026
```

