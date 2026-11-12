---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02", "3.4 Message Building Blocks", "3.4.2 ReferenceData <RefData>", "3.4.2.2 FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts>", "3.4.2.2.4 ClassificationType <ClssfctnTp>"]
file_pages: [23]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.017.001.02"]
---

# 3.4.2.2.4 ClassificationType <ClssfctnTp>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 23 to 23.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 23

```text
Datatype: "Max35Text" on page 456
3.4.2.2.4  ClassificationType <ClssfctnTp>
Presence: [1..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification.
Datatype: "CFIOct2015Identifier" on page 450
3.4.2.2.5  NotionalCurrency <NtnlCcy>
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
3.4.2.2.6  CommodityDerivativeIndicator <CmmdtyDerivInd>
Presence: [1..1]
Definition: Indicates whether the financial instrument falls within the definition of commodities derivative
under the local regulation.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
3.4.2.3  Issuer <Issr>
Presence: [1..1]
Definition: LEI of Issuer or trading venue operator.
Datatype: "LEIIdentifier" on page 451
3.4.2.4  TradingVenueRelatedAttributes <TradgVnRltdAttrbts>
Presence: [1..*]
Definition: Traded venue related attributes.
Impacted by: C14 "ValidateAdmissionIssuerRule", C20 "ValidMICRule", C22
"ValidTerminationDateRule"
Approved by the Securities SEG on 17 July 2025 auth.017.001.02
FinancialInstrumentReportingReferenceDataReport
V02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
23 July 2025
```

