---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["21 auth.102.001.01 FinancialInstrumentReportingCancellationReportV01"]
file_pages: [268, 269]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.102.001.01"]
---

# 21 auth.102.001.01 FinancialInstrumentReportingCancellationReportV01

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 268 to 269.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 268

```text
21 auth.102.001.01
FinancialInstrumentReportingCancellationRe
portV01
21.1 MessageDefinition Functionality
This FinancialInstrumentReportingCancellationReport message is sent by the trading venue to the
national competent authority to cancel reference data previously reported by mistake.
Outline
The FinancialInstrumentReportingCancellationReportV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. ReportHeader
Header information related to the global report.
B. CancellationData
Details of the financial instrument previously reported by mistake by the trading venue.
C. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
21.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FinInstrmRptgCxlRpt> [1..1]  
   ReportHeader <RptHdr> [1..1] ± 270
   CancellationData <CxlData> [1..*] ± C16,
C17
270
   SupplementaryData <SplmtryData> [0..*] ± C13 272
21.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 17 July 2025 auth.102.001.01
FinancialInstrumentReportingCancellationReportV0
1
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
268 July 2025
```

## File page 269

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 BasketInstrumentUniquenessRule
Where an underlying instrument basket is populated, all ISINs or LEIs must be unique.
C4 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C5 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C6 MultiplierRule
Price Multiplier must not be zero.
C7 NumberRule
If Number is negative, then Sign must be present.
C8 NumberRule
If Number is negative, then Sign must be present.
C9 OneElementPresentRule
At least one of 5 elements must be present.
C10 OneElementPresentRule
At least one of 5 elements must be present.
C11 OneElementPresentRule
At least one of the 3 elements must be present.
C12 OneElementPresentRule
At least one of the 5 elements must be present.
C13 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C14 ValidateAdmissionIssuerRule
When IssuerRequest is equal to true, then AdmissionApprovalDateByIssuer must be present.
C15 ValidCFIRule
The CFI code must be a valid CFI code as defined by 10962.
C16 ValidDebtMaturityDateRule
DebtInstrumentAttributes/MaturityDate cannot be a date earlier than
TradingVenueRelatedAttributes/FirstTradeDate, TradingVenueRelatedAttributes/
RequestForAdmissionDate or TradingVenueRelatedAttributes/AdmissionApprovalDate.
Approved by the Securities SEG on 17 July 2025 auth.102.001.01
FinancialInstrumentReportingCancellationReportV0
1
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
269 July 2025
```

