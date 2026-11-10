---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.2 NewRecord <NewRcrd>", "8.4.2.2.6 DerivativeInstrumentAttributes <DerivInstrmAttrbts>", "8.4.2.2.6.6 OptionExerciseStyle <OptnExrcStyle>"]
file_pages: [135]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.2.6.6 OptionExerciseStyle <OptnExrcStyle>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 135 to 135.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 135

```text
Usage:
Within the scope of MiFIR RTS 23, these are the fields 31 and 32. This field only applies to options,
warrants, spread bet on an option on an equity or contract for difference on an option on an equity.
Where price is currently not available but pending, the value shall be 'PNDG'. Where strike price is not
applicable it shall not be populated.
StrikePrice <StrkPric> contains one of the following elements (see
"SecuritiesTransactionPrice4Choice" on page 350 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Price <Pric> [1..1] ± 351
Or}   NoPrice <NoPric> [1..1] ± 351
8.4.2.2.6.6  OptionExerciseStyle <OptnExrcStyle>
Presence: [0..1]
Definition: Indication as to whether the option may be exercised only at a fixed date (European, and
Asian style), a series of pre-specified dates (Bermudan) or at any time during the life of the contract
(American style).
Usage:
Within the scope of MiFIR, RTS 23, this field is only applicable for options, warrants and entitlement
certificates.
Datatype: "OptionStyle7Code" on page 442
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
ASIA Asian Option where the payoff is not
determined by the underlying price at
maturity but by the average underlying
price over some pre-set period of time.
BERM Bermudan Option that can be exercised on multiple
discrete dates prior to, or on expiry date.
EURO European Option that can be exercised on expiry
date only.
OTHR Other Other type of option style.
8.4.2.2.6.7  DeliveryType <DlvryTp>
Presence: [0..1]
Definition: Indicates whether the transaction is settled physically or in cash.
Datatype: "PhysicalTransferType4Code" on page 443
CodeName Name Definition
PHYS Physical Physical transfer.
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
135 July 2025
```

