---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.7 SecuritiesFinancingDetails <SctiesFincgDtls>", "29.4.7.6 EarliestCallBackDate <EarlstCallBckDt>"]
file_pages: [1026]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.7.6 EarliestCallBackDate <EarlstCallBckDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1026 to 1026.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1026

```text
RateChangeDate <RateChngDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
29.4.7.6  EarliestCallBackDate <EarlstCallBckDt>
Presence: [0..1]
Definition: Earliest date/time at which the call back can take place.
EarliestCallBackDate <EarlstCallBckDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
29.4.7.7  CommissionCalculationDate <ComssnClctnDt>
Presence: [0..1]
Definition: Date/time at which the commission is calculated.
CommissionCalculationDate <ComssnClctnDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
29.4.7.8  RateType <RateTp>
Presence: [0..1]
Definition: Specifies whether the rate is fixed or variable.
RateType <RateTp> contains one of the following elements (see "RateType35Choice" on page 1747
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1748
Or}   Proprietary <Prtry> [1..1] ± 1748
29.4.7.9  Revaluation <Rvaltn>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1026 March 2026
```

