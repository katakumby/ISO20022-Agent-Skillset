---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03", "15.4 Message Building Blocks", "15.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "15.4.2.9 PreTradeInstrumentSizeSpecificThreshold <PreTradInstrmSzSpcfcThrshld>"]
file_pages: [242]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.045.001.03"]
---

# 15.4.2.9 PreTradeInstrumentSizeSpecificThreshold <PreTradInstrmSzSpcfcThrshld>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 242 to 242.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 242

```text
15.4.2.9  PreTradeInstrumentSizeSpecificThreshold <PreTradInstrmSzSpcfcThrshld>
Presence: [0..1]
Definition: The pre-trade Size Specific to an Instrument threshold.
PreTradeInstrumentSizeSpecificThreshold <PreTradInstrmSzSpcfcThrshld> contains one of the
following elements (see "TonsOrCurrency2Choice" on page 338 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Number <Nb> [1..1] Quantity 338
Or}   Amount <Amt> [1..1] Amount C2, C5 338
15.4.2.10  PostTradeInstrumentSizeSpecificThreshold
<PstTradInstrmSzSpcfcThrshld>
Presence: [0..1]
Definition: The post-trade Size Specific to an Instrument threshold.
PostTradeInstrumentSizeSpecificThreshold <PstTradInstrmSzSpcfcThrshld> contains one of the
following elements (see "TonsOrCurrency2Choice" on page 338 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Number <Nb> [1..1] Quantity 338
Or}   Amount <Amt> [1..1] Amount C2, C5 338
15.4.2.11  Statistics <Sttstcs>
Presence: [0..1]
Definition: Statistics for a financial instrument generated as part of transparency calculations.
Statistics <Sttstcs> contains the following StatisticsTransparency2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalNumberOfTransactionsExecuted
<TtlNbOfTxsExctd>
[1..1] Quantity 242
   TotalVolumeOfTransactionsExecuted
<TtlVolOfTxsExctd>
[1..1] Quantity 242
15.4.2.11.1  TotalNumberOfTransactionsExecuted <TtlNbOfTxsExctd>
Presence: [1..1]
Definition: Total number of transactions that have been performed on this market.
Datatype: "Number" on page 453
15.4.2.11.2  TotalVolumeOfTransactionsExecuted <TtlVolOfTxsExctd>
Presence: [1..1]
Definition: Total volume of transactions that have been performed on this market.
Datatype: "DecimalNumber" on page 451
Approved by the Securities SEG on 17 July 2025 auth.045.001.03
FinancialInstrumentReportingNonEquityTradingActi
vityResultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
242 July 2025
```

