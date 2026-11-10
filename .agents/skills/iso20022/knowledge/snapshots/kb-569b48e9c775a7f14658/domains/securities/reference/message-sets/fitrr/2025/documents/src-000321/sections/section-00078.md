---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks"]
file_pages: [99, 100, 101, 102, 103, 104]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4 Message Building Blocks

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 99 to 104.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 99

```text
C29 ValidTerminationDateRule
TerminationDate cannot be a date earlier than FirstTradeDate, RequestForAdmissionDate or
AdmissionApprovalDate.
C30 ValidTerminationDateRule
TerminationDate cannot be a date earlier than FirstTradeDate, RequestForAdmissionDate or
AdmissionApprovalDate.
8.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
8.4.1 ReportHeader <RptHdr>
Presence: [1..1]
Definition: Header information related to the global report.
ReportHeader <RptHdr> contains the following elements (see "SecuritiesMarketReportHeader1" on
page 411 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportingEntity <RptgNtty> [1..1] ± C19 411
   ReportingPeriod <RptgPrd> [1..1] ± 411
   SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 411
8.4.2 FinancialInstrument <FinInstrm>
Presence: [0..*]
Definition: Provides the details of the reference data that have been updated (since the last report).
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
99 July 2025
```

## File page 100

```text
FinancialInstrument <FinInstrm> contains one of the following
SecuritiesReferenceDeltaStatusReport5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ModifiedRecord <ModfdRcrd> [1..1]  C18,
C20
105
     TechnicalRecordIdentification <TechRcrdId> [0..1] Text 107
     FinancialInstrumentGeneralAttributes
<FinInstrmGnlAttrbts>
[1..1]  C16,
C22,
C27
108
       Identification <Id> [1..1] IdentifierSet 108
       FullName <FullNm> [1..1] Text 108
       ShortName <ShrtNm> [0..1] Text 108
       ClassificationType <ClssfctnTp> [1..1] IdentifierSet 109
       NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 109
       CommodityDerivativeIndicator <CmmdtyDerivInd> [1..1] Indicator 109
     Issuer <Issr> [1..1] IdentifierSet 109
     TradingVenueRelatedAttributes <TradgVnRltdAttrbts> [1..*] ± C14,
C25,
C29
109
     DebtInstrumentAttributes <DebtInstrmAttrbts> [0..1]  110
       TotalIssuedNominalAmount <TtlIssdNmnlAmt> [1..1] Amount C2, C5 110
       MaturityDate <MtrtyDt> [0..1] Date 111
       NominalValuePerUnit <NmnlValPerUnit> [1..1] Amount C2, C5 111
       InterestRate <IntrstRate> [1..1] ± 111
       DebtSeniority <DebtSnrty> [0..1] CodeSet 112
     DerivativeInstrumentAttributes <DerivInstrmAttrbts> [0..1]  C9 112
       ExpiryDate <XpryDt> [0..1] Date 114
       PriceMultiplier <PricMltplr> [0..1] Quantity C6 114
       UnderlyingInstrument <UndrlygInstrm> [0..1]  114
{Or         Single <Sngl> [1..1] ± 114
Or}         Basket <Bskt> [1..1] ± C3, C10 115
       OptionType <OptnTp> [0..1] CodeSet 115
       StrikePrice <StrkPric> [0..1] ± 115
       OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 116
       DeliveryType <DlvryTp> [0..1] CodeSet 116
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
100 July 2025
```

## File page 101

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AssetClassSpecificAttributes
<AsstClssSpcfcAttrbts>
[0..1]  C11 117
         Commodity <Cmmdty> [0..1]  117
           Product <Pdct> [1..1] ± 118
           TransactionType <TxTp> [0..1] CodeSet 118
           FinalPriceType <FnlPricTp> [0..1] CodeSet 119
         Interest <Intrst> [0..1]  119
           InterestRate <IntrstRate> [1..1] ± 119
           FirstLegInterestRate <FrstLegIntrstRate> [0..1] ± 120
           OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 120
           OtherLegInterestRate <OthrLegIntrstRate> [0..1] ± 120
         ForeignExchange <FX> [0..1]  121
           FXType <FxTp> [0..1] CodeSet 121
           OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 121
     TechnicalAttributes <TechAttrbts> [0..1]  C12 122
       InconsistencyIndicator <IncnsstncyInd> [0..1] Indicator 122
       LastUpdate <LastUpd> [0..1] DateTime 122
       SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 122
       RelevantCompetentAuthority <RlvntCmptntAuthrty> [0..1] CodeSet C4 123
       PublicationPeriod <PblctnPrd> [0..1] ± 123
       NeverPublished <NvrPblshd> [0..1] Indicator 123
       RelevantTradingVenue <RlvntTradgVn> [0..1] IdentifierSet 123
Or   NewRecord <NewRcrd> [1..1]  C18,
C20
124
     TechnicalRecordIdentification <TechRcrdId> [0..1] Text 126
     FinancialInstrumentGeneralAttributes
<FinInstrmGnlAttrbts>
[1..1]  C16,
C22,
C27
127
       Identification <Id> [1..1] IdentifierSet 127
       FullName <FullNm> [1..1] Text 127
       ShortName <ShrtNm> [0..1] Text 127
       ClassificationType <ClssfctnTp> [1..1] IdentifierSet 128
       NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 128
       CommodityDerivativeIndicator <CmmdtyDerivInd> [1..1] Indicator 128
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
101 July 2025
```

## File page 102

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Issuer <Issr> [1..1] IdentifierSet 128
     TradingVenueRelatedAttributes <TradgVnRltdAttrbts> [1..*] ± C14,
C25,
C29
128
     DebtInstrumentAttributes <DebtInstrmAttrbts> [0..1]  129
       TotalIssuedNominalAmount <TtlIssdNmnlAmt> [1..1] Amount C2, C5 129
       MaturityDate <MtrtyDt> [0..1] Date 130
       NominalValuePerUnit <NmnlValPerUnit> [1..1] Amount C2, C5 130
       InterestRate <IntrstRate> [1..1] ± 130
       DebtSeniority <DebtSnrty> [0..1] CodeSet 131
     DerivativeInstrumentAttributes <DerivInstrmAttrbts> [0..1]  C9 131
       ExpiryDate <XpryDt> [0..1] Date 133
       PriceMultiplier <PricMltplr> [0..1] Quantity C6 133
       UnderlyingInstrument <UndrlygInstrm> [0..1]  133
{Or         Single <Sngl> [1..1] ± 133
Or}         Basket <Bskt> [1..1] ± C3, C10 134
       OptionType <OptnTp> [0..1] CodeSet 134
       StrikePrice <StrkPric> [0..1] ± 134
       OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 135
       DeliveryType <DlvryTp> [0..1] CodeSet 135
       AssetClassSpecificAttributes
<AsstClssSpcfcAttrbts>
[0..1]  C11 136
         Commodity <Cmmdty> [0..1]  136
           Product <Pdct> [1..1] ± 137
           TransactionType <TxTp> [0..1] CodeSet 137
           FinalPriceType <FnlPricTp> [0..1] CodeSet 138
         Interest <Intrst> [0..1]  138
           InterestRate <IntrstRate> [1..1] ± 138
           FirstLegInterestRate <FrstLegIntrstRate> [0..1] ± 139
           OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 139
           OtherLegInterestRate <OthrLegIntrstRate> [0..1] ± 139
         ForeignExchange <FX> [0..1]  140
           FXType <FxTp> [0..1] CodeSet 140
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
102 July 2025
```

## File page 103

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 140
     TechnicalAttributes <TechAttrbts> [0..1]  C12 141
       InconsistencyIndicator <IncnsstncyInd> [0..1] Indicator 141
       LastUpdate <LastUpd> [0..1] DateTime 141
       SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 141
       RelevantCompetentAuthority <RlvntCmptntAuthrty> [0..1] CodeSet C4 142
       PublicationPeriod <PblctnPrd> [0..1] ± 142
       NeverPublished <NvrPblshd> [0..1] Indicator 142
       RelevantTradingVenue <RlvntTradgVn> [0..1] IdentifierSet 142
Or   TerminatedRecord <TermntdRcrd> [1..1]  C18,
C20
143
     TechnicalRecordIdentification <TechRcrdId> [0..1] Text 145
     FinancialInstrumentGeneralAttributes
<FinInstrmGnlAttrbts>
[1..1]  C16,
C22,
C27
146
       Identification <Id> [1..1] IdentifierSet 146
       FullName <FullNm> [1..1] Text 146
       ShortName <ShrtNm> [0..1] Text 146
       ClassificationType <ClssfctnTp> [1..1] IdentifierSet 147
       NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 147
       CommodityDerivativeIndicator <CmmdtyDerivInd> [1..1] Indicator 147
     Issuer <Issr> [1..1] IdentifierSet 147
     TradingVenueRelatedAttributes <TradgVnRltdAttrbts> [1..*] ± C14,
C25,
C29
147
     DebtInstrumentAttributes <DebtInstrmAttrbts> [0..1]  148
       TotalIssuedNominalAmount <TtlIssdNmnlAmt> [1..1] Amount C2, C5 148
       MaturityDate <MtrtyDt> [0..1] Date 149
       NominalValuePerUnit <NmnlValPerUnit> [1..1] Amount C2, C5 149
       InterestRate <IntrstRate> [1..1] ± 149
       DebtSeniority <DebtSnrty> [0..1] CodeSet 150
     DerivativeInstrumentAttributes <DerivInstrmAttrbts> [0..1]  C9 150
       ExpiryDate <XpryDt> [0..1] Date 152
       PriceMultiplier <PricMltplr> [0..1] Quantity C6 152
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
103 July 2025
```

## File page 104

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       UnderlyingInstrument <UndrlygInstrm> [0..1]  152
{Or         Single <Sngl> [1..1] ± 152
Or}         Basket <Bskt> [1..1] ± C3, C10 153
       OptionType <OptnTp> [0..1] CodeSet 153
       StrikePrice <StrkPric> [0..1] ± 153
       OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 154
       DeliveryType <DlvryTp> [0..1] CodeSet 154
       AssetClassSpecificAttributes
<AsstClssSpcfcAttrbts>
[0..1]  C11 155
         Commodity <Cmmdty> [0..1]  155
           Product <Pdct> [1..1] ± 156
           TransactionType <TxTp> [0..1] CodeSet 156
           FinalPriceType <FnlPricTp> [0..1] CodeSet 157
         Interest <Intrst> [0..1]  157
           InterestRate <IntrstRate> [1..1] ± 157
           FirstLegInterestRate <FrstLegIntrstRate> [0..1] ± 158
           OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 158
           OtherLegInterestRate <OthrLegIntrstRate> [0..1] ± 158
         ForeignExchange <FX> [0..1]  159
           FXType <FxTp> [0..1] CodeSet 159
           OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 159
     TechnicalAttributes <TechAttrbts> [0..1]  C12 160
       InconsistencyIndicator <IncnsstncyInd> [0..1] Indicator 160
       LastUpdate <LastUpd> [0..1] DateTime 160
       SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 160
       RelevantCompetentAuthority <RlvntCmptntAuthrty> [0..1] CodeSet C4 161
       PublicationPeriod <PblctnPrd> [0..1] ± 161
       NeverPublished <NvrPblshd> [0..1] Indicator 161
       RelevantTradingVenue <RlvntTradgVn> [0..1] IdentifierSet 161
Or}   CancelledRecord <CancRcrd> [1..1] ± C19,
C21
162
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
104 July 2025
```

