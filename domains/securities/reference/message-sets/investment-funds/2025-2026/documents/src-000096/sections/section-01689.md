---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.21 CumDividendIndicator <CumDvddInd>"]
file_pages: [2375]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.21 CumDividendIndicator <CumDvddInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2375 to 2375.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2375

```text
CodeName Name Definition
BTEX Best Best execution rules were followed.
46.4.5.10.21  CumDividendIndicator <CumDvddInd>
Presence: [1..1]
Definition: Indicates whether the dividend is included, that is, cum-dividend, in the executed price. When
the dividend is not included, the price will be ex-dividend.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
46.4.5.10.22  InterimProfitAmount <IntrmPrftAmt>
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
46.4.5.10.23  ForeignExchangeDetails <FXDtls>
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
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2375 May 2026
```

