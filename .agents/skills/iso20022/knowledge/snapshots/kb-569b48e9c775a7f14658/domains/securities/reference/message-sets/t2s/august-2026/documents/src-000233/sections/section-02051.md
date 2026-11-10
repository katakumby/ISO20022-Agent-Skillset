---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.8 CalculationData <ClctnData>", "81.4.6.11.4.8.1 Date <Dt>"]
file_pages: [2800]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.8.1 Date <Dt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2800 to 2800.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2800

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     QuotationDate <QtnDt> [0..1] ± 2809
   SubAmountPenaltyBreakdown <SubAmtPnltyBrkdwn> [0..*]  2809
     Amount <Amt> [1..1] Amount C1, C5 2809
     Type <Tp> [0..1] CodeSet 2810
81.4.6.11.4.8.1  Date <Dt>
Presence: [1..1]
Definition: Date for which the penalty applies.
Datatype: "ISODate" on page 3319
81.4.6.11.4.8.2  MissingReferenceData <MssngRefData>
Presence: [0..1]
Definition: Information provided for penalties where there is missing reference data on this business
day.
Usage: When not present, there are no missing reference data.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
81.4.6.11.4.8.3  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [1..1]
Definition: Further details on the financial instrument reported.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2800 August 2026
```

