---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["25 colr.002.001.02 CollateralValueReportV02", "25.4 Message Building Blocks", "25.4.2 ReportOrError <RptOrErr>", "25.4.2.1 BusinessReport <BizRpt>", "25.4.2.1.6 CollateralValueReport <CollValRpt>", "25.4.2.1.6.2 CollateralValue <CollVal>", "25.4.2.1.6.2.4 Securities <Scties>", "25.4.2.1.6.2.4.3 ValuationPrice <ValtnPric>", "25.4.2.1.6.2.4.3.4 PriceFixingDate <PricFxgDt>"]
file_pages: [612]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 25.4.2.1.6.2.4.3.4 PriceFixingDate <PricFxgDt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 612 to 612.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 612

```text
25.4.2.1.6.2.4.3.4  PriceFixingDate <PricFxgDt>
Presence: [1..1]
Definition: Date at which the actual price for a financial instrument is fixed.
Datatype: "ISODate" on page 3319
25.4.2.1.6.2.4.4  CollateralValue <CollVal>
Presence: [1..1]
Definition: Specifies the value of the security for collateral purposes.
Impacted by: C1 "ActiveCurrency", C6 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
25.4.2.2  OperationalError <OprlErr>
Presence: [1..*]
Definition: Indicates whether an operational error has been issued during the processing of the related
request.
OperationalError <OprlErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  612
{Or     Code <Cd> [1..1] CodeSet 613
Or}     Proprietary <Prtry> [1..1] Text 613
   Description <Desc> [0..1] Text 613
25.4.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 612 August 2026
```

