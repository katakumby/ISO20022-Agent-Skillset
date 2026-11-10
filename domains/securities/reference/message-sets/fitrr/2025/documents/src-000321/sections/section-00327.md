---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.9 FinancialInstrument <FinInstrm>", "22.1.13.2.9.3 Other <Othr>", "22.1.13.2.9.3.1 FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts>", "22.1.13.2.9.3.1.1 Identification <Id>"]
file_pages: [381]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.9.3.1.1 Identification <Id>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 381 to 381.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 381

```text
Definition: Attributes and characteristics of the financial instrument.
FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts> contains the following
SecurityInstrumentDescription23 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] IdentifierSet 381
   OtherIdentification <OthrId> [0..*]  381
     Identification <Id> [1..1] Text 381
     Suffix <Sfx> [0..1] Text 381
     Type <Tp> [1..1] ± 382
   FullName <FullNm> [1..1] Text 382
   ClassificationType <ClssfctnTp> [1..1] IdentifierSet 382
   NotionalCurrency <NtnlCcy> [0..1] CodeSet C2 382
22.1.13.2.9.3.1.1  Identification <Id>
Presence: [0..1]
Definition: Identifies the financial instrument using an ISIN.
Datatype: "ISINOct2015Identifier" on page 450
22.1.13.2.9.3.1.2  OtherIdentification <OthrId>
Presence: [0..*]
Definition: Identification of a security by proprietary or domestic identification scheme.
OtherIdentification <OthrId> contains the following OtherIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 381
   Suffix <Sfx> [0..1] Text 381
   Type <Tp> [1..1] ± 382
22.1.13.2.9.3.1.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a security.
Datatype: "Max35Text" on page 456
22.1.13.2.9.3.1.2.2  Suffix <Sfx>
Presence: [0..1]
Definition: Identifies the suffix of the security identification.
Datatype: "Max16Text" on page 455
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
381 July 2025
```

