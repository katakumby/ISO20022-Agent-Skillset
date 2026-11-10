---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.5 Tax35", "66.1.47.5.5 RecipientIdentification <RcptId>"]
file_pages: [5249]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.5.5 RecipientIdentification <RcptId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5249 to 5249.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5249

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.47.5.5  RecipientIdentification <RcptId>
Presence: [0..1]
Definition: Party that receives the tax. The recipient of, and the party entitled to, the tax may be two
different parties.
RecipientIdentification <RcptId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
66.1.47.5.6  TaxCalculationDetails <TaxClctnDtls>
Presence: [0..1]
Definition: Information used to calculate the tax.
TaxCalculationDetails <TaxClctnDtls> contains the following TaxCalculationInformation10
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Basis <Bsis> [0..1]  5249
{Or     Code <Cd> [1..1] CodeSet 5249
Or}     Proprietary <Prtry> [1..1] ± 5250
   TaxableAmount <TaxblAmt> [1..1] Amount C1, C13 5250
66.1.47.5.6.1  Basis <Bsis>
Presence: [0..1]
Definition: Form of the rebate, for example, cash.
Basis <Bsis> contains one of the following TaxBasis1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5249
Or}   Proprietary <Prtry> [1..1] ± 5250
66.1.47.5.6.1.1  Code <Cd>
Presence: [1..1]
Definition: Tax basis expressed as a code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5249 May 2026
```

