---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.50 ModificationCancellationAllowed4Choice", "35.1.16.50.2 Proprietary <Prtry>"]
file_pages: [1589]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.50.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1589 to 1589.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1589

```text
35.1.16.50.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Modification, cancellation allowed information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.51  RestrictionIdentification1
Definition: Restriction References applied on the transaction for which the securities settlement
condition modification is requested.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet 1589
   Identification <Id> [1..1] Text 1590
35.1.16.51.1  Code <Cd>
Presence: [1..1]
Definition: Restriction identification removal or addition applied on the transaction expressed as a code.
Datatype: "RestrictionReference1Code" on page 2136
CodeName Name Definition
ADDC AddCashRestrictionReference Addition of a cash restriction reference
representing a cash sub-balance to be
utilised within the settlement instruction
for the debiting or crediting of cash.
ADDS AddSecuritiesRestrictionReference Addition of a securities restriction
reference representing a securities sub-
position to be utilised within the
settlement instruction for the delivery or
receipt of securities.
REMC RemoveCashRestrictionReference Removal of a cash restriction reference,
already present within the settlement
instruction, representing a cash sub-
balance to be utilised within the
settlement instruction for the debiting or
crediting of cash.
REMS RemoveSecuritiesRestrictionReference Removal of a securities restriction
reference, already present within the
settlement instruction, representing a
securities sub-position to be utilised
within the settlement instruction for the
delivery or receipt of securities.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1589 March 2026
```

