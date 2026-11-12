---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.13 Miscellaneous", "17.1.13.4 ProcessingPosition7Choice", "17.1.13.4.1 Code <Cd>"]
file_pages: [413]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.13.4.1 Code <Cd>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 413 to 413.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 413

```text
Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/instructions/
notifications.
17.1.13.4.1  Code <Cd>
Presence: [1..1]
Definition: Processing position expressed as an ISO 20022 code.
Datatype: "ProcessingPosition3Code" on page 490
CodeName Name Definition
AFTE After Specifies that the transaction/instruction
is to be executed after the linked
transaction/instruction.
WITH With Specifies that the transaction/instruction
is to be executed with the linked
transaction/instruction.
BEFO Before Specifies that the transaction/instruction
is to be executed before the linked
transaction/instruction.
INFO Information Specifies that the transactions/
instructions are linked for information
purposes only.
17.1.13.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Processing position expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 409 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
17.1.13.5  LinkageType3Choice
Definition: Choice of format for the linkage type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 413
Or}   Proprietary <Prtry> [1..1] ± 414
17.1.13.5.1  Code <Cd>
Presence: [1..1]
Definition: Linkage type expressed as an ISO 20022 code.
Datatype: "LinkageType1Code" on page 485
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
413 March 2024
```

