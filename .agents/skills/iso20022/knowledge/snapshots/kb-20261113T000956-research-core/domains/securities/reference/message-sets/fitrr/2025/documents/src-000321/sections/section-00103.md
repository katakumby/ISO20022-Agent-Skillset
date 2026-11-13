---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.2 NewRecord <NewRcrd>", "8.4.2.2.6 DerivativeInstrumentAttributes <DerivInstrmAttrbts>", "8.4.2.2.6.1 ExpiryDate <XpryDt>"]
file_pages: [133]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.2.6.1 ExpiryDate <XpryDt>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 133 to 133.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 133

```text
 Or    /AssetClassSpecificAttributes Must be present
 Or    /DeliveryType Must be present
8.4.2.2.6.1  ExpiryDate <XpryDt>
Presence: [0..1]
Definition: Expiry date of the financial instrument.
Datatype: "ISODate" on page 449
8.4.2.2.6.2  PriceMultiplier <PricMltplr>
Presence: [0..1]
Definition: Number of units of the underlying instrument represented by a single derivative contract. For
a future or option on an index, the amount per index point.
Impacted by: C6 "MultiplierRule"
Datatype: "NonNegativeDecimalNumber" on page 453
Constraints
• MultiplierRule
Price Multiplier must not be zero.
8.4.2.2.6.3  UnderlyingInstrument <UndrlygInstrm>
Presence: [0..1]
Definition: Choice to specify the type(s) of underlying instrument(s) that make up the financial
instrument.
UnderlyingInstrument <UndrlygInstrm> contains one of the following
FinancialInstrumentIdentification5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Single <Sngl> [1..1] ± 133
Or}   Basket <Bskt> [1..1] ± C3, C10 134
8.4.2.2.6.3.1  Single <Sngl>
Presence: [1..1]
Definition: Instrument consists of single instrument.
Single <Sngl> contains one of the following elements (see "FinancialInstrument48Choice" on page 327
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 327
Or   LEI <LEI> [1..1] IdentifierSet 327
Or}   Index <Indx> [1..1] ± 327
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
133 July 2025
```

