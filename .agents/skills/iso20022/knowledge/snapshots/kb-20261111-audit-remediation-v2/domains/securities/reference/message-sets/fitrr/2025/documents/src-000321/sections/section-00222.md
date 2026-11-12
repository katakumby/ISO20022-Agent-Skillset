---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["21 auth.102.001.01 FinancialInstrumentReportingCancellationReportV01", "21.4 Message Building Blocks"]
file_pages: [270, 271]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.102.001.01"]
---

# 21.4 Message Building Blocks

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 270 to 271.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 270

```text
C17 ValidDerivativeExpiryDateRule
DerivativesInstrumentAttributes/ExpiryDate cannot be a date earlier than
TradingVenueRelatedAttributes/FirstTradeDate, TradingVenueRelatedAttributes/
RequestForAdmissionDate or TradingVenueRelatedAttributes/AdmissionApprovalDate.
C18 ValidISINRule
ISIN code must pass checksum validation.
C19 ValidMICRule
Market Identification code must be an active market at the time of reporting.
C20 ValidMICRule
Market Identification code must be an active market at the time of reporting.
C21 ValidShortNameRule
ShortName must conform with ISO 18774.
C22 ValidTerminationDateRule
TerminationDate cannot be a date earlier than FirstTradeDate, RequestForAdmissionDate or
AdmissionApprovalDate.
21.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
21.4.1 ReportHeader <RptHdr>
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
21.4.2 CancellationData <CxlData>
Presence: [1..*]
Definition: Details of the financial instrument previously reported by mistake by the trading venue.
Impacted by: C16 "ValidDebtMaturityDateRule", C17 "ValidDerivativeExpiryDateRule"
Approved by the Securities SEG on 17 July 2025 auth.102.001.01
FinancialInstrumentReportingCancellationReportV0
1
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
270 July 2025
```

## File page 271

```text
CancellationData <CxlData> contains the following elements (see "SecuritiesReferenceDataReport7"
on page 393 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TechnicalRecordIdentification <TechRcrdId> [0..1] Text 395
   FinancialInstrumentGeneralAttributes
<FinInstrmGnlAttrbts>
[1..1] ± C15,
C18,
C21
395
   Issuer <Issr> [0..1] IdentifierSet 396
   TradingVenueRelatedAttributes <TradgVnRltdAttrbts> [1..*] ± C14,
C20,
C22
396
   DebtInstrumentAttributes <DebtInstrmAttrbts> [0..1]  397
     TotalIssuedNominalAmount <TtlIssdNmnlAmt> [1..1] Amount C2, C5 397
     MaturityDate <MtrtyDt> [0..1] Date 398
     NominalValuePerUnit <NmnlValPerUnit> [1..1] Amount C2, C5 398
     InterestRate <IntrstRate> [1..1] ± 398
     DebtSeniority <DebtSnrty> [0..1] CodeSet 399
   DerivativeInstrumentAttributes <DerivInstrmAttrbts> [0..1]  C9 399
     ExpiryDate <XpryDt> [0..1] Date 401
     PriceMultiplier <PricMltplr> [0..1] Quantity C6 401
     UnderlyingInstrument <UndrlygInstrm> [0..1]  401
{Or       Single <Sngl> [1..1] ± 401
Or}       Basket <Bskt> [1..1] ± C3, C10 402
     OptionType <OptnTp> [0..1] CodeSet 402
     StrikePrice <StrkPric> [0..1] ± 402
     OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 403
     DeliveryType <DlvryTp> [0..1] CodeSet 403
     AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  C11 404
       Commodity <Cmmdty> [0..1]  404
         Product <Pdct> [1..1] ± 405
         TransactionType <TxTp> [0..1] CodeSet 405
         FinalPriceType <FnlPricTp> [0..1] CodeSet 406
       Interest <Intrst> [0..1]  406
         InterestRate <IntrstRate> [1..1] ± 406
         FirstLegInterestRate <FrstLegIntrstRate> [0..1] ± 407
Approved by the Securities SEG on 17 July 2025 auth.102.001.01
FinancialInstrumentReportingCancellationReportV0
1
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
271 July 2025
```

