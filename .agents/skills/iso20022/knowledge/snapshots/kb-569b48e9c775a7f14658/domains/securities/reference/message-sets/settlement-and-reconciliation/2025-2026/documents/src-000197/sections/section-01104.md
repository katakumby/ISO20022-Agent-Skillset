---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.13 RevaluationIndicator3Choice", "35.1.16.13.2 Proprietary <Prtry>"]
file_pages: [1546]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.13.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1546 to 1546.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1546

```text
Definition: Specifies whether the collateral position should be subject to automatic revaluation by the
account servicer.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.13.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Revaluation information provided as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.14  CentralCounterPartyEligibility4Choice
Definition: Choice of format for the CCP eligibility information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1546
Or}   Proprietary <Prtry> [1..1] ± 1546
35.1.16.14.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether the settlement transaction is CCP (Central Counterparty) eligible.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.14.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Central counterparty eligibility information expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1546 March 2026
```

