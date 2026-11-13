---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.1 Commodity <Cmmdty>"]
file_pages: [68]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.1 Commodity <Cmmdty>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 68 to 68.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 68

```text
6.4.2.12.1  Commodity <Cmmdty>
Presence: [1..1]
Definition: Details specific for commodity derivatives.
Commodity <Cmmdty> contains the following CommodityDerivative4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClassSpecific <ClssSpcfc> [0..1]  68
{Or     Freight <Frght> [1..1]  68
       Size <Sz> [1..1] Text 68
       AverageTimeCharter <AvrgTmChrtr> [1..1] Text 69
Or}     Energy <Nrgy> [1..1]  69
       SettlementLocation <SttlmLctn> [1..1] Text 69
   NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 69
6.4.2.12.1.1  ClassSpecific <ClssSpcfc>
Presence: [0..1]
Definition: Provides specific information related to commodity derivatives.
ClassSpecific <ClssSpcfc> contains one of the following CommodityDerivative2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Freight <Frght> [1..1]  68
     Size <Sz> [1..1] Text 68
     AverageTimeCharter <AvrgTmChrtr> [1..1] Text 69
Or}   Energy <Nrgy> [1..1]  69
     SettlementLocation <SttlmLctn> [1..1] Text 69
6.4.2.12.1.1.1  Freight <Frght>
Presence: [1..1]
Definition: Details specific to freight derivatives.
Freight <Frght> contains the following CommodityDerivative5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Size <Sz> [1..1] Text 68
   AverageTimeCharter <AvrgTmChrtr> [1..1] Text 69
6.4.2.12.1.1.1.1  Size <Sz>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
68 July 2025
```

