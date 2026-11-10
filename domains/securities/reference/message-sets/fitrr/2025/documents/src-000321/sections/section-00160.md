---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02", "12.4 Message Building Blocks", "12.4.3 FinancialInstruments <FinInstrms>", "12.4.3.1 FinancialInstrument <FinInstrm>", "12.4.3.1.5 DebtInstrumentAttributes <DebtInstrmAttrbts>", "12.4.3.1.5.5 DebtSeniority <DebtSnrty>"]
file_pages: [198, 199]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.042.001.02"]
---

# 12.4.3.1.5.5 DebtSeniority <DebtSnrty>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 198 to 199.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 198

```text
InterestRate <IntrstRate> contains one of the following elements (see "InterestRate6Choice" on
page 359 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Fixed <Fxd> [1..1] Rate 359
Or}   Floating <Fltg> [1..1] ± 359
12.4.3.1.5.5  DebtSeniority <DebtSnrty>
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
12.4.3.1.6  DerivativeInstrumentAttributes <DerivInstrmAttrbts>
Presence: [0..1]
Definition: Attributes specific to derivative instruments.
Impacted by: C9 "OneElementPresentRule"
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
198 July 2025
```

## File page 199

```text
DerivativeInstrumentAttributes <DerivInstrmAttrbts> contains the following DerivativeInstrument5
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExpiryDate <XpryDt> [0..1] Date 200
   PriceMultiplier <PricMltplr> [0..1] Quantity C6 200
   UnderlyingInstrument <UndrlygInstrm> [0..1]  200
{Or     Single <Sngl> [1..1] ± 200
Or}     Basket <Bskt> [1..1] ± C3, C10 201
   OptionType <OptnTp> [0..1] CodeSet 201
   StrikePrice <StrkPric> [0..1] ± 201
   OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 202
   DeliveryType <DlvryTp> [0..1] CodeSet 202
   AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  C11 203
     Commodity <Cmmdty> [0..1]  203
       Product <Pdct> [1..1] ± 204
       TransactionType <TxTp> [0..1] CodeSet 204
       FinalPriceType <FnlPricTp> [0..1] CodeSet 205
     Interest <Intrst> [0..1]  205
       InterestRate <IntrstRate> [1..1] ± 205
       FirstLegInterestRate <FrstLegIntrstRate> [0..1] ± 206
       OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 206
       OtherLegInterestRate <OthrLegIntrstRate> [0..1] ± 206
     ForeignExchange <FX> [0..1]  207
       FXType <FxTp> [0..1] CodeSet 207
       OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 207
Constraints
• OneElementPresentRule
At least one of 5 elements must be present.
Following Must be True
    /ExpiryDate Must be present
 Or    /PriceMultiplier Must be present
 Or    /UnderlyingInstrument Must be present
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
199 July 2025
```

