---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.22 ElectionTypeFormat3Choice"]
file_pages: [921]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.22 ElectionTypeFormat3Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 921 to 921.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 921

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.22  ElectionTypeFormat3Choice
Definition: Choice between a standard code or proprietary code to specify the type of election
movement.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 921
Or}   Proprietary <Prtry> [1..1] ± 921
16.1.15.22.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the effect on the holdings of electing a corporate action option.
Datatype: "ElectionMovementType2Code" on page 1208
CodeName Name Definition
DRCT Direct Direct movement of resource, that is,
cash or security that is directly credited
to the paying agent account.
SEQD Sequestered Election results in a change of balance
type that transfers control of the
securities rather than the securities
themselves.
16.1.15.22.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of election of a corporate action option.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 921 February 2026
```

