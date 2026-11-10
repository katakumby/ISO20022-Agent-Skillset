---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02", "12.4 Message Building Blocks"]
file_pages: [188]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.042.001.02"]
---

# 12.4 Message Building Blocks

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 188 to 188.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 188

```text
C16 ValidDebtMaturityDateRule
DebtInstrumentAttributes/MaturityDate cannot be a date earlier than
TradingVenueRelatedAttributes/FirstTradeDate, TradingVenueRelatedAttributes/
RequestForAdmissionDate or TradingVenueRelatedAttributes/AdmissionApprovalDate.
C17 ValidDerivativeExpiryDateRule
DerivativesInstrumentAttributes/ExpiryDate cannot be a date earlier than
TradingVenueRelatedAttributes/FirstTradeDate, TradingVenueRelatedAttributes/
RequestForAdmissionDate or TradingVenueRelatedAttributes/AdmissionApprovalDate.
C18 ValidISINRule
ISIN code must pass checksum validation.
C19 ValidMICRule
Market Identification code must be an active market at the time of reporting.
C20 ValidShortNameRule
ShortName must conform with ISO 18774.
C21 ValidTerminationDateRule
TerminationDate cannot be a date earlier than FirstTradeDate, RequestForAdmissionDate or
AdmissionApprovalDate.
12.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
12.4.1 DatePeriod <DtPrd>
Presence: [1..1]
Definition: Date period capturing when instruments in the report have been invalidated
Usage:
Within MiFIR, only the From Date To Date field will be used with the From Date corresponding to the
date the first instrument was added to this report while the To Date is the date the last instrument was
added to the file.
DatePeriod <DtPrd> contains one of the following elements (see "Period4Choice" on page 322 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 322
Or   FromDate <FrDt> [1..1] Date 323
Or   ToDate <ToDt> [1..1] Date 323
Or}   FromDateToDate <FrDtToDt> [1..1] ± 323
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
188 July 2025
```

