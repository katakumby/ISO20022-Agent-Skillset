---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.8 Units <Units>", "46.4.5.10.8.1 UnitsNumber <UnitsNb>"]
file_pages: [2371]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.8.1 UnitsNumber <UnitsNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2371 to 2371.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2371

```text
Units <Units> contains one of the following Unit1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 2371
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 2371
46.4.5.10.8.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Quantity of units.
Datatype: "DecimalNumber" on page 5400
46.4.5.10.8.2  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
46.4.5.10.9  Rounding <Rndg>
Presence: [0..1]
Definition: Indicates the rounding direction applied to nearest unit.
Datatype: "RoundingDirection2Code" on page 5358
CodeName Name Definition
RDUP RoundUp Round up to the nearest whole number.
RDWN RoundDown Round down to the nearest whole
number.
46.4.5.10.10  NetAmount <NetAmt>
Presence: [0..1]
Definition: Amount of money paid to the investor when redeeming fund units.
Net amount = (Quantity * Price) - (Fees + Taxes).
Impacted by: C3 "ActiveCurrency", C10 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2371 May 2026
```

