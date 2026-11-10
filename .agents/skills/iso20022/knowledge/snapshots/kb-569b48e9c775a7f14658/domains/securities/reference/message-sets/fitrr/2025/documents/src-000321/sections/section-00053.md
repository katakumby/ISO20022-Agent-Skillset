---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.1 Commodity <Cmmdty>", "6.4.2.12.1.1 ClassSpecific <ClssSpcfc>", "6.4.2.12.1.1.1 Freight <Frght>", "6.4.2.12.1.1.1.2 AverageTimeCharter <AvrgTmChrtr>"]
file_pages: [69]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.1.1.1.2 AverageTimeCharter <AvrgTmChrtr>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 69 to 69.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 69

```text
Definition: Specification of the size related to the freight sub type. Field to be populated when the base
product field is equal to freight.
Datatype: "Max25Text" on page 455
6.4.2.12.1.1.1.2  AverageTimeCharter <AvrgTmChrtr>
Presence: [1..1]
Definition: Details the specific route or time charter average. Field to be populated when the base
product field is equal to freight.
Datatype: "Max25Text" on page 455
6.4.2.12.1.1.2  Energy <Nrgy>
Presence: [1..1]
Definition: Details specific to energy derivatives.
Energy <Nrgy> contains the following CommodityDerivative6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementLocation <SttlmLctn> [1..1] Text 69
6.4.2.12.1.1.2.1  SettlementLocation <SttlmLctn>
Presence: [1..1]
Definition: Place where the delivery and the cash settlement of the base product occurs.
Datatype: "Max25Text" on page 455
6.4.2.12.1.2  NotionalCurrency <NtnlCcy>
Presence: [1..1]
Definition: Currency in which the notional is denominated.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
6.4.2.12.2  InterestRate <IntrstRate>
Presence: [1..1]
Definition: Details specific for Interest rate.
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
69 July 2025
```

