---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["5 auth.032.001.01 FinancialInstrumentReportingEquityTransparencyDataReportV01", "5.4 Message Building Blocks", "5.4.2 EquityTransparencyData <EqtyTrnsprncyData>", "5.4.2.9 IssuanceSize <IssncSz>"]
file_pages: [53, 54]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.032.001.01"]
---

# 5.4.2.9 IssuanceSize <IssncSz>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 53 to 54.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 53

```text
5.4.2.9  IssuanceSize <IssncSz>
Presence: [0..1]
Definition: Issuance size of the certificate expressed in Euros.
Impacted by: C1 "ActiveCurrency", C3 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 415
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
5.4.2.10  InstrumentPrice <InstrmPric>
Presence: [0..1]
Definition: Before the first admission to trading of the instrument, the price of the instrument as it will
stand at the start of the first day of trading.
After the first admission to trading of the instrument, the price of the instrument at the last trading day of
the previous year, or at the end of the day on which a corporate action is effective. The price should be
expressed in Euros. To be reported for shares and depositary receipts.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 415
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
5.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C4 "SupplementaryDataRule"
Approved by the Securities SEG on 17 July 2025 auth.032.001.01
FinancialInstrumentReportingEquityTransparencyD
ataReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
53 July 2025
```

## File page 54

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 341 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 341
   Envelope <Envlp> [1..1] (External Schema) 341
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 17 July 2025 auth.032.001.01
FinancialInstrumentReportingEquityTransparencyD
ataReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
54 July 2025
```

