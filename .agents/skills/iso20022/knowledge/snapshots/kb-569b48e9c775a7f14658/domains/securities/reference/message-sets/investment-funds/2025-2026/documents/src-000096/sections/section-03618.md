---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.30 AdditiononalInformation13", "66.1.28.30.3 AccountValidation <AcctVldtn>"]
file_pages: [4868]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.30.3 AccountValidation <AcctVldtn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4868 to 4868.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4868

```text
Definition: Additional information such as remarks or notes that must be conveyed about the account
management activity or party.
Datatype: "Max350Text" on page 5403
66.1.28.30.3  AccountValidation <AcctVldtn>
Presence: [0..1]
Definition: Information or instructions for the by-passing of validations in the account registration
process.
Datatype: "Max350Text" on page 5403
66.1.28.30.4  Type <Tp>
Presence: [0..1]
Definition: Type or identification of the remark, note, limitation or restriction.
Datatype: "Max35Text" on page 5403
66.1.28.30.5  Regulator <Rgltr>
Presence: [0..1]
Definition: Regulator that may have to be informed about the remark, note, limitation or restriction.
Regulator <Rgltr> contains one of the following elements (see "PartyIdentification125Choice" on
page 4909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4909
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4909
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4910
66.1.28.30.6  Status <Sts>
Presence: [0..1]
Definition: Status of the remark, note, limitation or restriction.
Status <Sts> contains one of the following RestrictionStatus1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4868
Or}   Proprietary <Prtry> [1..1] ± 4869
66.1.28.30.6.1  Code <Cd>
Presence: [1..1]
Definition: Status of the restriction expressed as a code.
Datatype: "RestrictionStatus1Code" on page 5357
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4868 May 2026
```

