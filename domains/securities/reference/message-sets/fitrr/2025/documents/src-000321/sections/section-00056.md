---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.2 InterestRate <IntrstRate>", "6.4.2.12.2.2 UnderlyingBond <UndrlygBd>", "6.4.2.12.2.2.3 IssuanceDate <IssncDt>"]
file_pages: [72]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.2.2.3 IssuanceDate <IssncDt>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 72 to 72.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 72

```text
Datatype: "ISODate" on page 449
6.4.2.12.2.2.3  IssuanceDate <IssncDt>
Presence: [0..1]
Definition: Populated with the issuance date of the underlying bond.
Datatype: "ISODate" on page 449
6.4.2.12.2.3  SwaptionNotionalCurrency <SwptnNtnlCcy>
Presence: [0..1]
Definition: Notional currency of a swaption.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 417
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
6.4.2.12.2.4  UnderlyingSwapMaturityDate <UndrlygSwpMtrtyDt>
Presence: [0..1]
Definition: Maturity date of the underlying swap, populated for swaptions, futures on swaps and
forwards on a swap only.
Datatype: "ISODate" on page 449
6.4.2.12.2.5  InflationIndex <InfltnIndx>
Presence: [0..1]
Definition: Populated to define the inflation index.
Impacted by: C7 "ValidISINRule"
InflationIndex <InfltnIndx> contains one of the following InflationIndex1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 72
Or}   Name <Nm> [1..1] Text 73
Constraints
• ValidISINRule
ISIN code must pass checksum validation.
6.4.2.12.2.5.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN) of the inflation index.
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
72 July 2025
```

