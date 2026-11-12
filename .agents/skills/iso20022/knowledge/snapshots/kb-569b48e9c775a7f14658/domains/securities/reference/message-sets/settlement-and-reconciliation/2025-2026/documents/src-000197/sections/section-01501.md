---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.77 RejectionStatus30Choice", "35.1.29.77.2 Reason <Rsn>", "35.1.29.77.2.1 Code <Cd>"]
file_pages: [1994]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.77.2.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1994 to 1994.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1994

```text
35.1.29.77.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a rejected or repair status.
Code <Cd> contains one of the following RejectionReason37Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1994
Or}   Proprietary <Prtry> [1..1] ± 1994
35.1.29.77.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RejectionReason55Code" on page 2114
CodeName Name Definition
BENO BeneficialOwnershipDisagreement Disagreement in beneficial ownership.
CAEV CorporateActionRejection Corporate action pending on the
financial instrument instructed.
DQUA QuantityRejection Unrecognised or invalid instructed
quantity.
OTHR Other Other. See Narrative.
PODU PossibleDuplicate Instruction has not been matched. It is a
possible duplicate instruction.
SAFE SafekeepingAccountRejection Unrecognised or invalid message
sender's safekeeping account.
SSID StandingSettlementInstructionRejection Standing Settlement Instruction is
unknown or invalid.
DSEC InvalidSecurity Unrecognised or invalid financial
instrument identification.
35.1.29.77.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1994 March 2026
```

