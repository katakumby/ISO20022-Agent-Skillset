---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.3 SecuritiesReferenceDataReport7", "22.1.13.3.6 DerivativeInstrumentAttributes <DerivInstrmAttrbts>", "22.1.13.3.6.8 AssetClassSpecificAttributes <AsstClssSpcfcAttrbts>", "22.1.13.3.6.8.2 Interest <Intrst>", "22.1.13.3.6.8.2.2 FirstLegInterestRate <FrstLegIntrstRate>"]
file_pages: [407]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.3.6.8.2.2 FirstLegInterestRate <FrstLegIntrstRate>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 407 to 407.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 407

```text
InterestRate <IntrstRate> contains the following elements (see "FloatingInterestRate8" on page 363
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferenceRate <RefRate> [1..1] ± 364
   Term <Term> [0..1] ± 364
22.1.13.3.6.8.2.2  FirstLegInterestRate <FrstLegIntrstRate>
Presence: [0..1]
Definition: Interest rate of the notional currency.
FirstLegInterestRate <FrstLegIntrstRate> contains one of the following elements (see
"InterestRate8Choice" on page 362 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Fixed <Fxd> [1..1] Rate 362
Or}   Floating <Fltg> [1..1] ± 362
22.1.13.3.6.8.2.3  OtherNotionalCurrency <OthrNtnlCcy>
Presence: [0..1]
Definition: Notional currency in which leg 2 of the contract is denominated, in case of multi-currency or
cross-currency swaps.
Notional currency in which leg 2 of the swap is denominated, in case of swaptions where the underlying
swap is multi-currency.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
22.1.13.3.6.8.2.4  OtherLegInterestRate <OthrLegIntrstRate>
Presence: [0..1]
Definition: Indication of the interest rate used for leg 2, if applicable.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
407 July 2025
```

