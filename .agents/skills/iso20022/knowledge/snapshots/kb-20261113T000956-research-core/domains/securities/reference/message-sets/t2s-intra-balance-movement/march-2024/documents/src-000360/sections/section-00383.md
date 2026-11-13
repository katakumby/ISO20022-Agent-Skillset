---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.19 ModificationProcessingStatus9Choice", "17.1.16.19.2 Proprietary <Prtry>"]
file_pages: [449]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.19.2 Proprietary <Prtry>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 449 to 449.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 449

```text
CodeName Name Definition
MODC Completed Modification has been completed.
DEND Denied Modification will not be executed.
MODP Pending Modification is pending. It is not known
at this time whether modified can be
executed.
REPR InRepair Modification request is in repair.
17.1.16.19.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of a modification request.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 409 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
17.1.16.20  SettlementStatus26Choice
Definition: Choice of format for the settlement status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 449
Or}   Proprietary <Prtry> [1..1] ± 449
17.1.16.20.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of settlement of an instruction/financial instrument movement.
Datatype: "SecuritiesSettlementStatus1Code" on page 492
CodeName Name Definition
PEND Pending Instruction is pending. Settlement at the
instructed settlement date is still
possible.
PENF Failing Instruction is failing. Settlement at the
instructed settlement date is no longer
possible.
17.1.16.20.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of settlement of an instruction/financial instrument movement.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
449 March 2024
```

