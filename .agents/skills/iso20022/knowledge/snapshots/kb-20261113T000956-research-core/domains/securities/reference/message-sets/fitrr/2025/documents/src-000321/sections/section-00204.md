---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01", "17.3 Constraints"]
file_pages: [248]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.048.001.01"]
---

# 17.3 Constraints

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 248 to 248.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 248

```text
17.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
17.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
17.4.1 CurrencyData <CcyData>
Presence: [1..*]
Definition: Report all currencies and countries which use that currency.
CurrencyData <CcyData> contains the following SecuritiesCurrencyIdentification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Currency <Ccy> [1..1]  248
     Code <Cd> [1..1] CodeSet C1 249
     Name <Nm> [1..1] Text 249
   FractionalDigit <FrctnlDgt> [0..1] Quantity 249
   CountryDetails <CtryDtls> [1..1] ± 249
   PreEuro <PreEuro> [1..1] Indicator 249
   Modification <Mod> [0..1] CodeSet 250
   ValidityPeriod <VldtyPrd> [1..1] ± 250
   LastUpdated <LastUpdtd> [0..1] Date 250
17.4.1.1  Currency <Ccy>
Presence: [1..1]
Definition: Details the currency name and ISO 4217 currency code.
Approved by the Securities SEG on 17 July 2025 auth.048.001.01
FinancialInstrumentReportingCurrencyCodeReportV
01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
248 July 2025
```

