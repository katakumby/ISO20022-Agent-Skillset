---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.7 CashAccount <CshAcct>"]
file_pages: [2783, 2784, 2785, 2786]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.7 CashAccount <CshAcct>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2783 to 2786.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2783

```text
81.4.6.7  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account account to be debited/credited for the settlement of the penalty.
CashAccount <CshAcct> contains one of the following elements (see "AccountIdentification4Choice"
on page 2836 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 2837
Or}   Other <Othr> [1..1] ± 2837
81.4.6.8  CashSettlementDate <CshSttlmDt>
Presence: [0..1]
Definition: Date on which the payment of the penalty is due.
Datatype: "ISODate" on page 3319
81.4.6.9  CashPenaltyIdentification <CshPnltyId>
Presence: [0..1]
Definition: Reference of the penalty payment.
Datatype: "Max35Text" on page 3328
81.4.6.10  NumberOfCounterparties <NbOfCtrPties>
Presence: [0..1]
Definition: Number of counterparties involved in the penalty.
Datatype: "Number" on page 3324
81.4.6.11  PenaltyPerCounterparty <PnltyPerCtrPty>
Presence: [0..*]
Definition: Claims (penalties) in a currency and of a date reported for a given party.
If there are no penalties in a given currency for a party, this block will not be informed.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2783 August 2026
```

## File page 2784

```text
PenaltyPerCounterparty <PnltyPerCtrPty> contains the following PenaltyPerCounterparty4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountServicer <AcctSvcr> [0..1] ± 2787
   PartyIdentification <PtyId> [1..1]  2787
     Identification <Id> [1..1] ± 2787
     Type <Tp> [0..1]  2788
{Or       Code <Cd> [1..1] CodeSet 2788
Or}       Proprietary <Prtry> [1..1] ± 2788
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
{Or         Code <Cd> [1..1] CodeSet 2795
Or}         Proprietary <Prtry> [1..1] ± 2795
       Reason <Rsn> [0..*]  2796
         Reason <Rsn> [1..1]  2796
{Or           Code <Cd> [1..1] CodeSet 2796
Or}           Proprietary <Prtry> [1..1] ± 2797
         AdditionalStatusReason <AddtlStsRsn> [0..1] Text 2797
     ComputedAmount <CmptdAmt> [1..1] ± 2798
     CalculationMethod <ClctnMtd> [0..1] CodeSet 2798
     NumberOfDays <NbOfDays> [0..1] Quantity 2798
     CalculationData <ClctnData> [0..*]  2798
       Date <Dt> [1..1] Date 2800
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2784 August 2026
```

## File page 2785

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or             Rate <Rate> [1..1] Rate 2804
Or}             Amount <Amt> [1..1] Amount C1, C5 2804
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
{Or         Rate <Rate> [1..1] Rate 2807
Or}         Amount <Amt> [1..1] Amount C1, C5 2807
       ForeignExchangeData <FXData> [0..*]  2808
         ExchangeRate <XchgRate> [1..1] Rate 2808
         UnitCurrency <UnitCcy> [0..1] CodeSet C1 2808
         QuotedCurrency <QtdCcy> [0..1] CodeSet C1 2809
         QuotationDate <QtnDt> [0..1] ± 2809
       SubAmountPenaltyBreakdown
<SubAmtPnltyBrkdwn>
[0..*]  2809
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2785 August 2026
```

## File page 2786

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Amount <Amt> [1..1] Amount C1, C5 2809
         Type <Tp> [0..1] CodeSet 2810
     RelatedTransaction <RltdTx> [0..1]  2810
       Reference <Ref> [1..1] ± C12 2812
       ReferenceOwner <RefOwnr> [0..1] ± 2812
       TransactionDetails <TxDtls> [0..1]  2813
         SettlementTransactionOrCorporateActionEventTy
pe <SttlmTxOrCorpActnEvtTp>
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
         AcknowledgedStatusTimeStamp
<AckdStsTmStmp>
[0..1] DateTime 2819
         MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 2819
         SettlementStatusFailing <SttlmStsFlng> [0..1]  2819
{Or           NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2819
Or}           Reason <Rsn> [1..*]  2819
             Code <Cd> [1..1]  2820
{Or               Code <Cd> [1..1] CodeSet 2820
Or}               Proprietary <Prtry> [1..1] ± 2823
             AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2824
         BusinessDayEvent <BizDayEvt> [0..1]  2824
           Type <Tp> [1..1]  2824
{Or             Code <Cd> [1..1] CodeSet 2824
Or}             Proprietary <Prtry> [1..1] ± 2825
           ScheduledTime <SchdldTm> [1..1] DateTime 2825
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2786 August 2026
```

