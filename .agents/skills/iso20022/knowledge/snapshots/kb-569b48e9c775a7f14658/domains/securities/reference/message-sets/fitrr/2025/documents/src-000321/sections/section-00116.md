---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.3 TerminatedRecord <TermntdRcrd>", "8.4.2.3.2 FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts>", "8.4.2.3.2.4 ClassificationType <ClssfctnTp>"]
file_pages: [147]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.3.2.4 ClassificationType <ClssfctnTp>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 147 to 147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 147

```text
Definition: Short name of financial instrument in accordance with ISO 18774.
Datatype: "Max35Text" on page 456
8.4.2.3.2.4  ClassificationType <ClssfctnTp>
Presence: [1..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification.
Datatype: "CFIOct2015Identifier" on page 450
8.4.2.3.2.5  NotionalCurrency <NtnlCcy>
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
8.4.2.3.2.6  CommodityDerivativeIndicator <CmmdtyDerivInd>
Presence: [1..1]
Definition: Indicates whether the financial instrument falls within the definition of commodities derivative
under the local regulation.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
8.4.2.3.3  Issuer <Issr>
Presence: [1..1]
Definition: LEI of Issuer or trading venue operator.
Datatype: "LEIIdentifier" on page 451
8.4.2.3.4  TradingVenueRelatedAttributes <TradgVnRltdAttrbts>
Presence: [1..*]
Definition: Traded venue related attributes.
Impacted by: C14 "ValidateAdmissionIssuerRule", C25 "ValidMICRule", C29
"ValidTerminationDateRule"
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
147 July 2025
```

