---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [5, 6, 7]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.016.001.03", "auth.017.001.02", "auth.031.001.01", "auth.032.001.01", "auth.033.001.03", "auth.035.001.01", "auth.036.001.03", "auth.039.001.01", "auth.040.001.01", "auth.041.001.01", "auth.042.001.02", "auth.043.001.01", "auth.044.001.03", "auth.045.001.03", "auth.047.001.01", "auth.048.001.01", "auth.049.001.02", "auth.050.001.01", "auth.053.001.01", "auth.102.001.01"]
---

# 1 Message Set Overview

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 5 to 7.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5

```text
1 Message Set Overview
Introduction
This document describes the Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) message set. It includes the new version of
the MessageDefinition that has been added as part of the fast track maintenance 2025 (See MCR
#267) and approved by the Securities Standards Evaluation Group on 17 July 2025.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
auth.016.001.03
FinancialInstrumentReportingTransactionReport
V03
The FinancialInstrumentReportingTransactionReport
message is sent by the reporting agent to the
competent authority to report on the securities
transactions or by the competent authority to another
competent authority when the transaction needs to be
exchanged between the competent authorities.
auth.017.001.02
FinancialInstrumentReportingReferenceDataRe
portV02
This
FinancialInstrumentReportingReferenceDataReport
message is sent by the trading venue to the national
competent authority to report on the reference data
used in the securities transactions.
auth.031.001.01
FinancialInstrumentReportingStatusAdviceV01
The FinancialInstrumentReportingStatusAdvice
message is sent by the national competent authority to
the reporting agent to provide a status advice for the
correctness, issues or errors that arise from the
submitted report.
auth.032.001.01
FinancialInstrumentReportingEquityTransparen
cyDataReportV01
The
FinancialInstrumentReportingEquityTransparencyData
Report message is sent by the trading venues to the
national competent authority to report on the
transparency data for equity financial instruments.
auth.033.001.03
FinancialInstrumentReportingNonEquityTranspa
rencyDataReportV03
The
FinancialInstrumentReportingNonEquityTransparency
DataReport message is sent by the trading venue to
the national competent authority to submit non equity
specific details as part of classifying and applying
necessary transparency non equity computations.
auth.035.001.01
FinancialInstrumentReportingTradingVolumeCa
pDataReportV01
The
FinancialInstrumentReportingTradingVolumeCapData
Report message is sent by the trading venue to the
national competent authority to report the total volume
of trading and volumes of trading under reference price
waiver and negotiated transactions waiver.
auth.036.001.03
FinancialInstrumentReportingReferenceDataDel
taReportV03
The
FinancialInstrumentReportingReferenceDataDeltaRep
ort message is sent by the trading venues to the
national competent authority to report on changes that
have occurred in the base data between reference
data file generation.
auth.039.001.01
FinancialInstrumentReportingNonWorkingDayR
eportV01
The
FinancialInstrumentReportingNonWorkingDayReport
Approved by the Securities SEG on 17 July 2025 Message Set Overview
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
5 July 2025
```

## File page 6

```text
MessageDefinition Definition
message is sent by the reporting entity to the
competent authority to report on non-working days.
auth.040.001.01
FinancialInstrumentReportingEquityTradingActi
vityReportV01
The
FinancialInstrumentReportingEquityTradingActivityRep
ort message is sent by the trading venue to the
national competent authority to report on equity
specific trading activity data, used for the transparency
calculations.
auth.041.001.01
FinancialInstrumentReportingNonEquityTrading
ActivityReportV01
The
FinancialInstrumentReportingNonEquityTradingActivity
Report message is sent by the trading venue to the
national competent authority to report on non-equity
specific trading activity aggregated quantitative data,
used for the transparency calculations.
auth.042.001.02
FinancialInstrumentReportingInvalidReferenceD
ataReportV02
The
FinancialInstrumentReportingInvalidReferenceDataRe
port message is sent by the trading venue to the
national competent authority to report on all records
that have become invalid based on updates that have
been received or that have passed the termination date
original set for the instrument.
auth.043.001.01
FinancialInstrumentReportingReferenceDataInd
exReportV01
This
FinancialInstrumentReportingReferenceDataIndexRep
ort message is sent by National Competent Authorities
to express an interest in receiving data on European
indices.
auth.044.001.03
FinancialInstrumentReportingEquityTradingActi
vityResultV03
The
FinancialInstrumentReportingEquityTradingActivityRes
ult message is used by an entity or an authority to
provide information on computed results data of an
equity specific trading activity.
auth.045.001.03
FinancialInstrumentReportingNonEquityTrading
ActivityResultV03
The
FinancialInstrumentReportingNonEquityTradingActivity
Result message is sent by the trading venue to the
national competent authority to report on computed
results data of non-equity specific trading activity.
auth.047.001.01
FinancialInstrumentReportingCountryCodeRepo
rtV01
The FinancialInstrumentReportingCountryCodeReport
message provides the details of the two character
country codes and is created by ESMA for distribution
to national competent authorities.
auth.048.001.01
FinancialInstrumentReportingCurrencyCodeRep
ortV01
The MiFIRCurrencyCodeReport message provides the
details the ISO 4217 currency codes and is created by
ESMA for distribution to National Competent
Authorities.
auth.049.001.02
FinancialInstrumentReportingMarketIdentificatio
nCodeReportV02
The FinancialInstrumentReportingMarket
IdentificationCodeReport provides the valid market
identification code (MIC) of venues that are valid and
registered to operate as a trading venue. This
message is generated by ESMA for distribution to
national competent authorities.
auth.050.001.01
FinancialInstrumentReportingInstrumentClassifi
cationReportV01
The
FinancialInstrumentReportingInstrumentClassificationR
eport message is sent by ESMA to all national
competent authorities and provides all valid
combinations for classification of financial instruments
(CFI) as per ISO 10962.
Approved by the Securities SEG on 17 July 2025 Message Set Overview
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
6 July 2025
```

## File page 7

```text
MessageDefinition Definition
auth.053.001.01
FinancialInstrumentReportingTradingVolumeCa
pResultReportV01
The
FinancialInstrumentReportingTradingVolumeCapResul
tReport provides volume of trading and percentage of
trading under waivers for equity instruments over a
period. This message is generated by the supervisory
authority for public distribution.
auth.102.001.01
FinancialInstrumentReportingCancellationRepor
tV01
This FinancialInstrumentReportingCancellationReport
message is sent by the trading venue to the national
competent authority to cancel reference data
previously reported by mistake.
Approved by the Securities SEG on 17 July 2025 Message Set Overview
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
7 July 2025
```

