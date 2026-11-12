---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.3 SecuritiesReferenceDataReport7", "22.1.13.3.6 DerivativeInstrumentAttributes <DerivInstrmAttrbts>", "22.1.13.3.6.8 AssetClassSpecificAttributes <AsstClssSpcfcAttrbts>", "22.1.13.3.6.8.3 ForeignExchange <FX>"]
file_pages: [408]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.3.6.8.3 ForeignExchange <FX>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 408 to 408.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 408

```text
OtherLegInterestRate <OthrLegIntrstRate> contains one of the following elements (see
"InterestRate8Choice" on page 362 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Fixed <Fxd> [1..1] Rate 362
Or}   Floating <Fltg> [1..1] ± 362
22.1.13.3.6.8.3  ForeignExchange <FX>
Presence: [0..1]
Definition: The fields in this section should only be populated for instruments that have non-financial
instrument of type foreign exchange as underlying.
ForeignExchange <FX> contains the following DerivativeForeignExchange3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FXType <FxTp> [0..1] CodeSet 408
   OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 408
22.1.13.3.6.8.3.1  FXType <FxTp>
Presence: [0..1]
Definition: Type of the underlying currency.
Datatype: "AssetFXSubProductType1Code" on page 431
CodeName Name Definition
FXCR ForeignExchangeCrossRate Commodity attribute of type foreign
exchange cross rate.
FXEM ForeignExchangeEmergingMarket Commodity attribute of type foreign
exchange emerging markets.
FXMJ ForeignExchangeMajor Commodity attribute of type foreign
exchange majors.
22.1.13.3.6.8.3.2  OtherNotionalCurrency <OthrNtnlCcy>
Presence: [0..1]
Definition: Underlying currency 2 of the currency pair (the currency 1 will be populated in the notional
currency).
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
408 July 2025
```

