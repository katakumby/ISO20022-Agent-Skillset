---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.2 IndividualOrderDetailsReport <IndvOrdrDtlsRpt>", "56.4.3.2.10 OrderData <OrdrData>", "56.4.3.2.10.2 FinancialInstrumentDetails <FinInstrmDtls>", "56.4.3.2.10.2.9 SeriesIdentification <SrsId>", "56.4.3.2.10.2.9.1 SeriesDate <SrsDt>"]
file_pages: [4164]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.2.10.2.9.1 SeriesDate <SrsDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4164 to 4164.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4164

```text
Constraints
• SeriesElementRule
Either SeriesDate or SeriesName must be present. Both may be present.
56.4.3.2.10.2.9.1  SeriesDate <SrsDt>
Presence: [0..1]
Definition: Issue date of the fund series. It is typically applicable to a redemption order, subscription
order confirmation or redemption order confirmation, but may be specified in the subscription order, if
known.
SeriesDate <SrsDt> contains one of the following elements (see "DateFormat42Choice" on page 4467
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   YearMonth <YrMnth> [1..1] YearMonth 4467
Or}   YearMonthDay <YrMnthDay> [1..1] Date 4467
56.4.3.2.10.2.9.2  SeriesName <SrsNm>
Presence: [0..1]
Definition: Name of the fund series. It is typically applicable to a redemption order, subscription order
confirmation or redemption order confirmation, but may be specified in the subscription, if known.
Datatype: "Max35Text" on page 5403
56.4.3.2.10.3  UnitsNumber <UnitsNb>
Presence: [0..1]
Definition: Number of investment fund units subscribed or redeemed.
Datatype: "DecimalNumber" on page 5400
56.4.3.2.10.4  DigitalTokenUnit <DgtlTknUnit>
Presence: [0..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
56.4.3.2.10.5  NetAmount <NetAmt>
Presence: [0..1]
Definition: When the status message is used for a subscription, this is the amount of money to be
invested in the fund.
Net Amount = Quantity * Price.
When the status message is used for a redemption, this is the amount of money to be received
following redemption of fund units.
Net Amount = (Quantity * Price) - (Fees + Taxes).
Impacted by: C2 "ActiveOrHistoricCurrency", C9 "CurrencyAmount"
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4164 May 2026
```

