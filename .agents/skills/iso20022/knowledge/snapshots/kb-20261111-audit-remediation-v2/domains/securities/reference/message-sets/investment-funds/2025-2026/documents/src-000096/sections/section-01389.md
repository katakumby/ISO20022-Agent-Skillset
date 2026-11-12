---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.22 InterimProfitAmount <IntrmPrftAmt>"]
file_pages: [1955]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.22 InterimProfitAmount <IntrmPrftAmt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1955 to 1955.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1955

```text
43.4.5.9.22  InterimProfitAmount <IntrmPrftAmt>
Presence: [0..1]
Definition: Part of the price deemed as accrued income or profit rather than capital. The interim profit
amount is used for tax purposes.
InterimProfitAmount <IntrmPrftAmt> contains one of the following elements (see
"ProfitAndLoss2Choice" on page 5116 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Profit <Prft> [1..1] Amount C1, C13 5116
Or}   Loss <Loss> [1..1] Amount C1, C13 5116
43.4.5.9.23  ForeignExchangeDetails <FXDtls>
Presence: [0..*]
Definition: Information needed to process a currency exchange or conversion.
How the exchange rate is expressed determines which currency is the Unit Currency and Quoted
Currency. If the amounts concerned are EUR 1000 and USD 1300, the exchange rate may be
expressed as per either of the following examples:
EXAMPLE 1
UnitCurrency EUR
QuotedCurrency USD
ExchangeRate 1.300
EXAMPLE 2
UnitCurrency USD
QuotedCurrency EUR
ExchangeRate 0.769.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1955 May 2026
```

