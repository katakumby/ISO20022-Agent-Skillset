---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 reda.016.001.01 PartyStatusAdviceV01", "4.4 Message Building Blocks", "4.4.2 PartyStatus <PtySts>", "4.4.2.1 Status <Sts>"]
file_pages: [38]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.016.001.01"]
---

# 4.4.2.1 Status <Sts>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 38 to 38.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 38

```text
Impacted by: C3 "PartyPresenceRule", C4 "StatusReasonRule"
PartyStatus <PtySts> contains the following PartyStatus2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 38
   StatusReason <StsRsn> [0..*]  38
     Reason <Rsn> [1..1]  39
{Or       Code <Cd> [1..1] CodeSet 39
Or}       Proprietary <Prtry> [1..1] Text 39
     AdditionalInformation <AddtlInf> [0..1] Text 39
   SystemPartyIdentification <SysPtyId> [0..1] ± 39
Constraints
• PartyPresenceRule
If Status equals 'Completed' then RelatedPartyIdentification must be present and
ResponsiblePartyIdentification must be present.
• StatusReasonRule
If Status equals 'Rejected' then StatusReason must be present.
4.4.2.1  Status <Sts>
Presence: [1..1]
Definition: Status of the party maintenance instruction.
Datatype: "Status6Code" on page 184
CodeName Name Definition
REJT Rejected Instruction has been rejected.
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
4.4.2.2  StatusReason <StsRsn>
Presence: [0..*]
Definition: Specifies the underlying reason for the status of an object.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.016.001.01 PartyStatusAdviceV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
38 March 2024
```

