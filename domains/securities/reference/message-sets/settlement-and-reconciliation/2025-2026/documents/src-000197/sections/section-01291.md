---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.22 Rate", "35.1.22.2 RateType35Choice", "35.1.22.2.1 Code <Cd>"]
file_pages: [1748]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.22.2.1 Code <Cd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1748 to 1748.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1748

```text
35.1.22.2.1  Code <Cd>
Presence: [1..1]
Definition: Rate expressed as an ISO 20022 code.
Datatype: "RateType1Code" on page 2113
CodeName Name Definition
FIXE Fixed Rate is fixed.
FORF Forfeit No specific repurchase rate applies to
the transaction Repo, only a forfeit.
VARI Variable Rate is variable.
35.1.22.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Rate expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.22.3  Rate2
Definition: Set of elements qualifying the interest rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 1748
   Rate <Rate> [1..1] Rate 1749
Constraints
• SignRule
When Sign is present, rate must not be zero.
35.1.22.3.1  Sign <Sgn>
Presence: [0..1]
Definition: Indicates the sign of the rate.
Datatype: One of the following values must be used (see "PlusOrMinusIndicator" on page 2188):
• Meaning When True: Plus
• Meaning When False: Minus
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1748 March 2026
```

