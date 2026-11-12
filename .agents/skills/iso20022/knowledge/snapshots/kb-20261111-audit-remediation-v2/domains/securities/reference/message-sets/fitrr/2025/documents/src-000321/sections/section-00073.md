---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["7 auth.035.001.01 FinancialInstrumentReportingTradingVolumeCapDataReportV01", "7.4 Message Building Blocks", "7.4.2 VolumeCapData <VolCapData>", "7.4.2.3 InstrumentReport <InstrmRpt>", "7.4.2.3.1 TechnicalRecordIdentification <TechRcrdId>"]
file_pages: [89]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.035.001.01"]
---

# 7.4.2.3.1 TechnicalRecordIdentification <TechRcrdId>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 89 to 89.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 89

```text
Constraints
• ValidISINRule
ISIN code must pass checksum validation.
7.4.2.3.1  TechnicalRecordIdentification <TechRcrdId>
Presence: [0..1]
Definition: Unique identifier of a record in a message used as part of error management and feedback
messages.
Usage:
This identification will be used in the status advice report sent back.
Datatype: "Max35Text" on page 456
7.4.2.3.2  Identification <Id>
Presence: [1..1]
Definition: Identifies the financial instrument using an ISIN.
Datatype: "ISINOct2015Identifier" on page 450
7.4.2.3.3  Currency <Ccy>
Presence: [1..1]
Definition: Currency of the transaction.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
7.4.2.3.4  TotalTradingVolume <TtlTradgVol>
Presence: [1..1]
Definition: Total traded volume of the instrument in this specific reporting period.
Datatype: "ImpliedCurrencyAndAmount" on page 416
7.4.2.3.5  TotalReferencePriceTradingVolume <TtlRefPricTradgVol>
Presence: [1..1]
Definition: Total volume of trading under reference price waiver as defined under the local regulation.
Datatype: "ImpliedCurrencyAndAmount" on page 416
Approved by the Securities SEG on 17 July 2025 auth.035.001.01
FinancialInstrumentReportingTradingVolumeCapDa
taReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
89 July 2025
```

