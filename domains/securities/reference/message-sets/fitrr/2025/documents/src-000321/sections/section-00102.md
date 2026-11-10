---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.2 NewRecord <NewRcrd>", "8.4.2.2.5 DebtInstrumentAttributes <DebtInstrmAttrbts>", "8.4.2.2.5.5 DebtSeniority <DebtSnrty>"]
file_pages: [131, 132]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.2.5.5 DebtSeniority <DebtSnrty>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 131 to 132.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 131

```text
InterestRate <IntrstRate> contains one of the following elements (see "InterestRate6Choice" on
page 359 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Fixed <Fxd> [1..1] Rate 359
Or}   Floating <Fltg> [1..1] ± 359
8.4.2.2.5.5  DebtSeniority <DebtSnrty>
Presence: [0..1]
Definition: Seniority for a specific debt instrument.
Datatype: "DebtInstrumentSeniorityType1Code" on page 435
CodeName Name Definition
SBOD SubordinatedDebt Debt owed to an unsecured creditor that
can only be paid, in the event of a
liquidation, after the claims of secured
creditors have been met.
SNDB SeniorDebt Debt that takes priority over other
unsecured or otherwise more junior debt
owed by the issuer.
MZZD MezzanineDebt Subordinated debt or preferred equity
instrument that represents a claim on a
company's assets which is senior only to
that of the common shares.
JUND JuniorDebt Debt that is either unsecured or has a
lower priority than of another debt claim
on the same asset or property.
8.4.2.2.6  DerivativeInstrumentAttributes <DerivInstrmAttrbts>
Presence: [0..1]
Definition: Attributes specific to derivative instruments.
Impacted by: C9 "OneElementPresentRule"
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
131 July 2025
```

## File page 132

```text
DerivativeInstrumentAttributes <DerivInstrmAttrbts> contains the following DerivativeInstrument5
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExpiryDate <XpryDt> [0..1] Date 133
   PriceMultiplier <PricMltplr> [0..1] Quantity C6 133
   UnderlyingInstrument <UndrlygInstrm> [0..1]  133
{Or     Single <Sngl> [1..1] ± 133
Or}     Basket <Bskt> [1..1] ± C3, C10 134
   OptionType <OptnTp> [0..1] CodeSet 134
   StrikePrice <StrkPric> [0..1] ± 134
   OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 135
   DeliveryType <DlvryTp> [0..1] CodeSet 135
   AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  C11 136
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
       OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 140
Constraints
• OneElementPresentRule
At least one of 5 elements must be present.
Following Must be True
    /ExpiryDate Must be present
 Or    /PriceMultiplier Must be present
 Or    /UnderlyingInstrument Must be present
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
132 July 2025
```

