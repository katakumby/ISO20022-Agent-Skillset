---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.7 OrderTransmission <OrdrTrnsmssn>", "22.1.13.2.7.1 TransmissionIndicator <TrnsmssnInd>"]
file_pages: [371]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.7.1 TransmissionIndicator <TrnsmssnInd>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 371 to 371.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 371

```text
22.1.13.2.7.1  TransmissionIndicator <TrnsmssnInd>
Presence: [1..1]
Definition: Indication as to whether the transaction results from an order transmitted by the reporting of
a client to a third party.
Usage: Only applicable when the conditions for transmission are not satisfied.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
22.1.13.2.7.2  TransmittingBuyer <TrnsmttgBuyr>
Presence: [0..1]
Definition: Identifies the buyer transmitting the order to the reporting firm.
Usage: Only required for reporting firms reporting transactions on behalf of order transmitting firm.
Datatype: "LEIIdentifier" on page 451
22.1.13.2.7.3  TransmittingSeller <TrnsmttgSellr>
Presence: [0..1]
Definition: Identifies the seller transmitting the order to the reporting firm.
Usage: Only required for reporting firms reporting transactions on behalf of order transmitting firm.
Datatype: "LEIIdentifier" on page 451
22.1.13.2.8  Transaction <Tx>
Presence: [1..1]
Definition: Provides the details of the reported transaction.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
371 July 2025
```

