---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.12 Linkages41"]
file_pages: [1545]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.12 Linkages41

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1545 to 1545.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1545

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.12  Linkages41
Definition: Information related to a linked transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± 1545
   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 1545
35.1.16.12.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: When the transaction is to be executed relative to a linked transaction - for information only.
ProcessingPosition <PrcgPos> contains one of the following elements (see
"ProcessingPosition9Choice" on page 1558 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1558
Or}   Proprietary <Prtry> [1..1] ± 1558
35.1.16.12.2  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
Presence: [1..1]
Definition: Unambiguous identification of a securities settlement transaction as known by the account
owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
35.1.16.13  RevaluationIndicator3Choice
Definition: Choice of format for the revaluation.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1545
Or}   Proprietary <Prtry> [1..1] ± 1546
35.1.16.13.1  Indicator <Ind>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1545 March 2026
```

