---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.35 PendingReason34", "9.1.21.35.1 Code <Cd>", "9.1.21.35.1.1 Code <Cd>"]
file_pages: [307]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.35.1.1 Code <Cd>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 307 to 307.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 307

```text
9.1.21.35.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Datatype: "PendingReason31Code" on page 332
CodeName Name Definition
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
PART TradeSettlesInPartials Trade will settle in partials.
COLL SecuritiesPledgedAsCollateral Financial instruments are not deliverable
as they are pledged as collateral.
LINK PendingLinkedInstruction Your instruction is pending settlement
because the instruction linked to it is
pending.
FUTU AwaitingSettlementDate Awaiting settlement date. No settlement
problems to be reported.
LACK LackOfSecurities Insufficient financial instruments in your
account.
SBLO SecuritiesBlocked Financial instruments are blocked due to
a corporate action event, realignment,
etc.
OTHR Other Other. See Narrative.
PRSY SystemOnHold Transaction was put on hold/frozen by
the system.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
9.1.21.35.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.21.35.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 344
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 307 September 2025
```

