---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.8 CalculationData <ClctnData>", "81.4.6.11.4.8.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "81.4.6.11.4.8.3.7 SecuritiesPenaltyRateData <SctiesPnltyRateData>", "81.4.6.11.4.8.3.7.2 SMEGrowthMarket <SMEGrwthMkt>"]
file_pages: [2807]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.8.3.7.2 SMEGrowthMarket <SMEGrwthMkt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2807 to 2807.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2807

```text
MarketIdentification <MktId> contains one of the following elements (see
"MarketIdentification1Choice" on page 2971 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 2971
Or}   Description <Desc> [1..1] Text 2971
81.4.6.11.4.8.3.7.2  SMEGrowthMarket <SMEGrwthMkt>
Presence: [0..1]
Definition: Binary classification whether the security was traded in a SME Growth Market or not.
Usage: If not provided, the indicator is not relevant for the calculation of the penalty.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
81.4.6.11.4.8.3.7.3  Rate <Rate>
Presence: [1..1]
Definition: Penalty rate applicable for the asset type.
Datatype: "PercentageRate" on page 3325
81.4.6.11.4.8.4  DiscountRate <DscntRate>
Presence: [0..1]
Definition: Discount rate for the currency of the penalty, provided if the Security is subject to penalties
and if the calculation method code is cash, mixed or both.
DiscountRate <DscntRate> contains one of the following PriceRateOrAmount4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 2807
Or}   Amount <Amt> [1..1] Amount C1, C5 2807
81.4.6.11.4.8.4.1  Rate <Rate>
Presence: [1..1]
Definition: Price expressed as a rate, that is, percentage.
Datatype: "PercentageRate" on page 3325
81.4.6.11.4.8.4.2  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2807 August 2026
```

