---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.5 ContractForDifference <CtrctForDiff>"]
file_pages: [76]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.5 ContractForDifference <CtrctForDiff>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 76 to 76.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 76

```text
CodeName Name Definition
PRBP PriceReturnBasicPerformanceParameter Equity derivative parameter Price Return
Basis Performance.
6.4.2.12.5  ContractForDifference <CtrctForDiff>
Presence: [1..1]
Definition: Details specific for Contract for difference (CFDs).
ContractForDifference <CtrctForDiff> contains the following ContractForDifference2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnderlyingType <UndrlygTp> [1..1] CodeSet 76
   NotionalCurrency1 <NtnlCcy1> [0..1] CodeSet C2 76
   NotionalCurrency2 <NtnlCcy2> [0..1] CodeSet C2 77
6.4.2.12.5.1  UnderlyingType <UndrlygTp>
Presence: [1..1]
Definition: Underlying type of the contract for difference.
Datatype: "UnderlyingContractForDifferenceType3Code" on page 447
CodeName Name Definition
BOND Bond Underlying is a bond.
COMM Commodity Underlying is a commodity.
CURR Currency Underlying is a currency.
EMAL EmissionAllowance Underlying is an emission allowance.
EQUI Equity Underlying is an equity.
FTEQ FutureOnEquity Underlying is a future on equity.
OPEQ OptionOnEquity Underlying is an option on equity.
OTHR Other Underlying is of other type.
6.4.2.12.5.2  NotionalCurrency1 <NtnlCcy1>
Presence: [0..1]
Definition: Currency 1 of the underlying currency pair.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
76 July 2025
```

