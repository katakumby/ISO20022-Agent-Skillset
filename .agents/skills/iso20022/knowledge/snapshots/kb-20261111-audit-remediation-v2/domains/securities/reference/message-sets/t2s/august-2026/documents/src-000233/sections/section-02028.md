---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.2 Structure"]
file_pages: [2762, 2763, 2764, 2765]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2762 to 2765.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2762

```text
81.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesTxPnltiesRpt> [1..1]  
   ReportPagination <RptPgntn> [0..1] ± 2768
   ReportGeneralDetails <RptGnlDtls> [1..1]  C14 2768
     ReportIdentification <RptId> [1..1] Text 2769
     ReportDate <RptDt> [0..1] ± 2769
     ReportPeriod <RptPrd> [0..1] ± 2769
     Frequency <Frqcy> [0..1] ± 2769
     PenaltyListType <PnltyListTp> [0..1]  2770
{Or       Code <Cd> [1..1] CodeSet 2770
Or}       Proprietary <Prtry> [1..1] ± 2770
     UpdateType <UpdTp> [0..1] ± 2771
     ActivityIndicator <ActvtyInd> [1..1] Indicator 2771
   SafekeepingAccount <SfkpgAcct> [0..1] ± 2771
   AccountOwner <AcctOwnr> [0..1] ± 2771
   AccountServicer <AcctSvcr> [1..1] ± 2772
   Penalty <Pnlty> [0..*]  C3 2772
     Currency <Ccy> [1..1] CodeSet C1 2777
     Date <Dt> [0..1] ± 2777
     PartyIdentification <PtyId> [1..1]  2777
       Identification <Id> [1..1] ± 2778
       Type <Tp> [0..1]  2778
{Or         Code <Cd> [1..1] CodeSet 2778
Or}         Proprietary <Prtry> [1..1] ± 2778
     CounterpartyCSD <CtrPtyCSD> [0..1] ± 2779
     CSDDepository <CSDDpstry> [0..1] ± 2779
     AggregatedAmount <AggtdAmt> [0..1]  2779
       AggregatedDebitAmount <AggtdDbtAmt> [0..1] Amount C1, C5 2780
       AggregatedCreditAmount <AggtdCdtAmt> [0..1] Amount C1, C5 2780
       GlobalNetAmount <GblNetAmt> [0..1] ± 2781
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2762 August 2026
```

## File page 2763

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       CounterpartyCSDAggregatedAmount
<CtrPtyCSDAggtdAmt>
[0..*]  2781
         PartyIdentification <PtyId> [1..1] ± 2781
         AggregatedDebitAmount <AggtdDbtAmt> [0..1] Amount C1, C5 2782
         AggregatedCreditAmount <AggtdCdtAmt> [0..1] Amount C1, C5 2782
         GlobalNetAmount <GblNetAmt> [0..1] ± 2782
     CashAccount <CshAcct> [0..1] ± 2783
     CashSettlementDate <CshSttlmDt> [0..1] Date 2783
     CashPenaltyIdentification <CshPnltyId> [0..1] Text 2783
     NumberOfCounterparties <NbOfCtrPties> [0..1] Quantity 2783
     PenaltyPerCounterparty <PnltyPerCtrPty> [0..*]  2783
       AccountServicer <AcctSvcr> [0..1] ± 2787
       PartyIdentification <PtyId> [1..1]  2787
         Identification <Id> [1..1] ± 2787
         Type <Tp> [0..1]  2788
{Or           Code <Cd> [1..1] CodeSet 2788
Or}           Proprietary <Prtry> [1..1] ± 2788
       AggregatedNetAmount <AggtdNetAmt> [1..1] ± 2788
       PenaltyDetails <PnltyDtls> [0..*]  2789
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
{Or             Code <Cd> [1..1] CodeSet 2795
Or}             Proprietary <Prtry> [1..1] ± 2795
           Reason <Rsn> [0..*]  2796
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2763 August 2026
```

## File page 2764

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Reason <Rsn> [1..1]  2796
{Or               Code <Cd> [1..1] CodeSet 2796
Or}               Proprietary <Prtry> [1..1] ± 2797
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
               Value <Val> [1..1]  2803
{Or                 Rate <Rate> [1..1] Rate 2804
Or}                 Amount <Amt> [1..1] Amount C1, C5 2804
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2764 August 2026
```

## File page 2765

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           DiscountRate <DscntRate> [0..1]  2807
{Or             Rate <Rate> [1..1] Rate 2807
Or}             Amount <Amt> [1..1] Amount C1, C5 2807
           ForeignExchangeData <FXData> [0..*]  2808
             ExchangeRate <XchgRate> [1..1] Rate 2808
             UnitCurrency <UnitCcy> [0..1] CodeSet C1 2808
             QuotedCurrency <QtdCcy> [0..1] CodeSet C1 2809
             QuotationDate <QtnDt> [0..1] ± 2809
           SubAmountPenaltyBreakdown <SubAmtPnltyBrkdwn> [0..*]  2809
             Amount <Amt> [1..1] Amount C1, C5 2809
             Type <Tp> [0..1] CodeSet 2810
         RelatedTransaction <RltdTx> [0..1]  2810
           Reference <Ref> [1..1] ± C12 2812
           ReferenceOwner <RefOwnr> [0..1] ± 2812
           TransactionDetails <TxDtls> [0..1]  2813
             SettlementTransactionOrCorporateActionEventType
<SttlmTxOrCorpActnEvtTp>
[1..1] ± 2814
             SettlementDate <SttlmDt> [1..1] ± 2815
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
{Or               NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2819
Or}               Reason <Rsn> [1..*]  2819
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2765 August 2026
```

