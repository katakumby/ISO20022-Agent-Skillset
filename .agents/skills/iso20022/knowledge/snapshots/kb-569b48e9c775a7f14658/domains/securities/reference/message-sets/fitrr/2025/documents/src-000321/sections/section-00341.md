---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.3 SecuritiesReferenceDataReport7", "22.1.13.3.3 Issuer <Issr>"]
file_pages: [396]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.3.3 Issuer <Issr>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 396 to 396.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 396

```text
FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts> contains the following elements (see
"SecurityInstrumentDescription17" on page 364 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] IdentifierSet 365
   FullName <FullNm> [0..1] Text 365
   ShortName <ShrtNm> [0..1] Text 365
   ClassificationType <ClssfctnTp> [0..1] IdentifierSet 365
   NotionalCurrency <NtnlCcy> [0..1] CodeSet C2 365
   CommodityDerivativeIndicator <CmmdtyDerivInd> [0..1] Indicator 366
Constraints
• ValidCFIRule
The CFI code must be a valid CFI code as defined by 10962.
• ValidISINRule
ISIN code must pass checksum validation.
• ValidShortNameRule
ShortName must conform with ISO 18774.
22.1.13.3.3  Issuer <Issr>
Presence: [0..1]
Definition: LEI of Issuer or trading venue operator.
Datatype: "LEIIdentifier" on page 451
22.1.13.3.4  TradingVenueRelatedAttributes <TradgVnRltdAttrbts>
Presence: [1..*]
Definition: Traded venue related attributes.
Impacted by: C14 "ValidateAdmissionIssuerRule", C20 "ValidMICRule", C22
"ValidTerminationDateRule"
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
396 July 2025
```

