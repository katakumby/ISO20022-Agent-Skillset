---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.7 PendingReason28Choice", "9.1.21.7.2 Proprietary <Prtry>"]
file_pages: [274]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.7.2 Proprietary <Prtry>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 274 to 274.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 274

```text
CodeName Name Definition
CDCY ConditionalCurrency Execution is conditional to the execution
of a process linked to the currency of the
transaction.
CDRE ConditionalRealignement Execution is conditional to the execution
of a process of realignment at the issuer
CSD.
9.1.21.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason code why the instruction or request is pending, using a proprietary
format.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.21.8  PendingReason30Choice
Definition: Choice of format for the pending reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 274
Or}   Proprietary <Prtry> [1..1] ± 275
9.1.21.8.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the cancellation request is pending.
Datatype: "PendingReason9Code" on page 333
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. Processed
on best effort basis.
CONF AwaitingConfirmation Awaiting confirmation from the
counterparty.
OTHR Other Other. See Narrative.
CDRG ConditionalRegistrar Execution is conditional to the execution
of a process at the registrar.
CDCY ConditionalCurrency Execution is conditional to the execution
of a process linked to the currency of the
transaction.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 274 September 2025
```

