---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.2 NewRecord <NewRcrd>", "8.4.2.2.6 DerivativeInstrumentAttributes <DerivInstrmAttrbts>", "8.4.2.2.6.8 AssetClassSpecificAttributes <AsstClssSpcfcAttrbts>", "8.4.2.2.6.8.1 Commodity <Cmmdty>", "8.4.2.2.6.8.1.3 FinalPriceType <FnlPricTp>"]
file_pages: [138]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.2.6.8.1.3 FinalPriceType <FnlPricTp>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 138 to 138.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 138

```text
CodeName Name Definition
MINI Minis Minis.
OPTN Options Options.
OTCT OTC Over-The-Counter.
ORIT Outright Outright.
SWAP Swaps Swaps.
TAPO TAPOS TAPOS.
OTHR Other Other.
8.4.2.2.6.8.1.3  FinalPriceType <FnlPricTp>
Presence: [0..1]
Definition: Final price type as specified by the trading venue.
Datatype: "AssetPriceType1Code" on page 431
CodeName Name Definition
ARGM ArgusMcCloskey Argus / Mc Closkey price.
BLTC Baltic Baltic price.
EXOF Exchange Exchange price.
GBCL GlobalCoal Global coal price.
IHSM IHSMcCloskey IHS Mc Closkey price.
OTHR Other Other price.
PLAT Platts Platts price.
8.4.2.2.6.8.2  Interest <Intrst>
Presence: [0..1]
Definition: The fields in this section should only be populated for instruments that have non-financial
instrument of type interest rates as underlying.
Interest <Intrst> contains the following DerivativeInterest3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InterestRate <IntrstRate> [1..1] ± 138
   FirstLegInterestRate <FrstLegIntrstRate> [0..1] ± 139
   OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 139
   OtherLegInterestRate <OthrLegIntrstRate> [0..1] ± 139
8.4.2.2.6.8.2.1  InterestRate <IntrstRate>
Presence: [1..1]
Definition: Provides the interest rate in number of days, weeks, months or years.
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
138 July 2025
```

