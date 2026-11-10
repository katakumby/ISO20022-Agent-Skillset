---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.2 NewRecord <NewRcrd>", "8.4.2.2.6 DerivativeInstrumentAttributes <DerivInstrmAttrbts>", "8.4.2.2.6.8 AssetClassSpecificAttributes <AsstClssSpcfcAttrbts>", "8.4.2.2.6.8.2 Interest <Intrst>", "8.4.2.2.6.8.2.2 FirstLegInterestRate <FrstLegIntrstRate>"]
file_pages: [139]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.2.6.8.2.2 FirstLegInterestRate <FrstLegIntrstRate>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 139 to 139.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 139

```text
InterestRate <IntrstRate> contains the following elements (see "FloatingInterestRate8" on page 363
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferenceRate <RefRate> [1..1] ± 364
   Term <Term> [0..1] ± 364
8.4.2.2.6.8.2.2  FirstLegInterestRate <FrstLegIntrstRate>
Presence: [0..1]
Definition: Interest rate of the notional currency.
FirstLegInterestRate <FrstLegIntrstRate> contains one of the following elements (see
"InterestRate8Choice" on page 362 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Fixed <Fxd> [1..1] Rate 362
Or}   Floating <Fltg> [1..1] ± 362
8.4.2.2.6.8.2.3  OtherNotionalCurrency <OthrNtnlCcy>
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
8.4.2.2.6.8.2.4  OtherLegInterestRate <OthrLegIntrstRate>
Presence: [0..1]
Definition: Indication of the interest rate used for leg 2, if applicable.
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
139 July 2025
```

