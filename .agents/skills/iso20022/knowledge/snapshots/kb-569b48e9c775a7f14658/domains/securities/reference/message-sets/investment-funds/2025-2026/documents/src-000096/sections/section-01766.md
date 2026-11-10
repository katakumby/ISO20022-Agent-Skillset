---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.37 PartialSettlementOfCash <PrtlSttlmOfCsh>"]
file_pages: [2465]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.37 PartialSettlementOfCash <PrtlSttlmOfCsh>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2465 to 2465.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2465

```text
Datatype: "PercentageRate" on page 5401
46.4.5.10.37  PartialSettlementOfCash <PrtlSttlmOfCsh>
Presence: [0..1]
Definition: Percentage of cash partially settled.
Datatype: "PercentageRate" on page 5401
46.4.5.10.38  StaffClientBreakdown <StffClntBrkdwn>
Presence: [0..4]
Definition: Breakdown of the net amount per type of order.
StaffClientBreakdown <StffClntBrkdwn> contains the following elements (see
"InvestmentFundsOrderBreakdown2" on page 4733 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderBreakdownType <OrdrBrkdwnTp> [1..1]  4733
{Or     Code <Cd> [1..1] CodeSet 4733
Or}     Proprietary <Prtry> [1..1] ± 4733
   Amount <Amt> [1..1] Amount C1, C13 4734
46.4.5.10.39  PartialRedemptionWithholdingAmount <PrtlRedWhldgAmt>
Presence: [0..1]
Definition: Amount retained by the fund and paid out later at a time decided by the fund.
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
Note: The decimal separator is a dot.
46.4.5.10.40  FinancialAdvice <FinAdvc>
Presence: [0..1]
Definition: Specifies if advice has been received from an independent financial advisor.
Datatype: "FinancialAdvice1Code" on page 5302
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2465 May 2026
```

