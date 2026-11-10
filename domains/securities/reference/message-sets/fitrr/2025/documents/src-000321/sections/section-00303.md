---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.11 Price", "22.1.11.4 SecuritiesTransactionPrice6", "22.1.11.4.1 Pending <Pdg>"]
file_pages: [353]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.11.4.1 Pending <Pdg>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 353 to 353.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 353

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Pending <Pdg> [1..1] CodeSet 353
   Currency <Ccy> [0..1] CodeSet C2 353
   DigitalToken <DgtlTkn> [0..*]  353
     Identifier <Idr> [1..1] IdentifierSet 354
     Unit <Unit> [0..1] Quantity 354
     Description <Desc> [0..1] Text 354
22.1.11.4.1  Pending <Pdg>
Presence: [1..1]
Definition: Price is currently not available, but pending.
Datatype: "PriceStatus1Code" on page 443
CodeName Name Definition
PNDG Pending Price is pending.
NOAP NotApplicable No price for transaction (e.g. transfer
between accounts).
22.1.11.4.2  Currency <Ccy>
Presence: [0..1]
Definition: Currency that will be used but for which no price is yet known.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
22.1.11.4.3  DigitalToken <DgtlTkn>
Presence: [0..*]
Definition: Specifies the digital token when the number of units may not be known.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
353 July 2025
```

