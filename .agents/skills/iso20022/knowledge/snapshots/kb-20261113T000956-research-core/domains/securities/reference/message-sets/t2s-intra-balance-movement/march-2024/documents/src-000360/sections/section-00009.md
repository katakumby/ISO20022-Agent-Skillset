---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 camt.066.001.02 IntraBalanceMovementInstructionV02", "2.4 Message Building Blocks", "2.4.2 CorporateActionEventIdentification <CorpActnEvtId>"]
file_pages: [17]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.066.001.02"]
---

# 2.4.2 CorporateActionEventIdentification <CorpActnEvtId>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 17 to 17.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 17

```text
Definition: Party that is the final destination of the message, if other than the receiver.
MessageRecipient <MsgRcpt> contains the following elements (see "PartyIdentification136" on
page 417 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 418
   LEI <LEI> [0..1] IdentifierSet 418
2.4.2 CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 497
2.4.3 NumberCounts <NbCounts>
Presence: [0..1]
Definition: Count of the number of transactions linked.
Impacted by: C10 "CurrentInstructionNumberRule"
NumberCounts <NbCounts> contains one of the following elements (see "NumberCount1Choice" on
page 416 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrentInstructionNumber <CurInstrNb> [1..1] Text 416
Or}   TotalNumber <TtlNb> [1..1]  C11, C7 417
     CurrentInstructionNumber <CurInstrNb> [1..1] Text 417
     TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 417
Constraints
• CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement instruction,
then the CurrentInstructionNumber must be specified.
2.4.4 Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.066.001.02
IntraBalanceMovementInstructionV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
17 March 2024
```

