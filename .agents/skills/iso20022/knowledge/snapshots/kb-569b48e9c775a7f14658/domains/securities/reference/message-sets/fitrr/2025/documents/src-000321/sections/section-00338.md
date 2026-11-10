---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.12 AdditionalAttributes <AddtlAttrbts>", "22.1.13.2.12.4 RiskReducingTransaction <RskRdcgTx>"]
file_pages: [392]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.12.4 RiskReducingTransaction <RskRdcgTx>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 392 to 392.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 392

```text
Datatype: "ReportingWaiverType3Code" on page 445
CodeName Name Definition
BENC BenchmarkTransaction Benchmark transaction.
ACTX AgencyCrossTransaction Agency cross transaction.
ILQD IlliquidInstrumentTransaction Pre-trade waiver was for an illiquid
instrument transaction. Applicable to
non-equity instruments.
SIZE AboveSpecificSizeTransaction Pre-trade waiver was for an above
specific size transaction. Applicable to
non-equity instruments.
CANC Cancellations Cancellations.
AMND Amendments Amendments.
SDIV SpecialDividendTransaction Special dividend transactions.
RPRI TransactionWithPriceImprovment Transactions which have received price
improvement. Applicable to equity
instruments.
DUPL DuplicativeTradeReport Duplicative trade reports.
LRGS LargeInScale Large-in-scale transactions. Applicable
for all instruments.
TNCP TransactionNotContributingToPriceDiscovery Transactions not contributing to the price
discovery process.
TPAC PackageTransaction Package transaction.
XFPH ExchangeForPhysical Transaction where the contract on a
commodity is exchanged for the actual
physical good.
22.1.13.2.12.4  RiskReducingTransaction <RskRdcgTx>
Presence: [0..1]
Definition: Indicates whether the transaction is objectively measurable as reducing risks directly relating
to the commercial activity of the entity executing the transaction.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
22.1.13.2.12.5  SecuritiesFinancingTransactionIndicator <SctiesFincgTxInd>
Presence: [1..1]
Definition: Indicates whether the transaction falls within the scope of activity to be reported under the
Securities Financing Transactions Regulation.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
392 July 2025
```

