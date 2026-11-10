---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.8 CalculationData <ClctnData>", "6.4.6.11.4.8.1 Date <Dt>"]
file_pages: [218]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.8.1 Date <Dt>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 218 to 218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 218

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     QuotationDate <QtnDt> [0..1] ± 227
   SubAmountPenaltyBreakdown <SubAmtPnltyBrkdwn> [0..*]  227
     Amount <Amt> [1..1] Amount C1, C5 227
     Type <Tp> [0..1] CodeSet 228
6.4.6.11.4.8.1  Date <Dt>
Presence: [1..1]
Definition: Date for which the penalty applies.
Datatype: "ISODate" on page 550
6.4.6.11.4.8.2  MissingReferenceData <MssngRefData>
Presence: [0..1]
Definition: Information provided for penalties where there is missing reference data on this business
day.
Usage: When not present, there are no missing reference data.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 553):
• Meaning When True: True
• Meaning When False: False
6.4.6.11.4.8.3  FinancialInstrumentAttributes <FinInstrmAttrbts>
Presence: [1..1]
Definition: Further details on the financial instrument reported.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 218 March 2026
```

