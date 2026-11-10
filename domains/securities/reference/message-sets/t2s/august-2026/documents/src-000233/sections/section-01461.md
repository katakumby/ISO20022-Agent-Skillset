---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["36 reda.016.001.01 PartyStatusAdviceV01", "36.4 Message Building Blocks", "36.4.2 PartyStatus <PtySts>", "36.4.2.1 Status <Sts>"]
file_pages: [2075]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.016.001.01"]
---

# 36.4.2.1 Status <Sts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2075 to 2075.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2075

```text
Impacted by: C3 "PartyPresenceRule", C4 "StatusReasonRule"
PartyStatus <PtySts> contains the following PartyStatus2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 2075
   StatusReason <StsRsn> [0..*]  2075
     Reason <Rsn> [1..1]  2076
{Or       Code <Cd> [1..1] CodeSet 2076
Or}       Proprietary <Prtry> [1..1] Text 2076
     AdditionalInformation <AddtlInf> [0..1] Text 2076
   SystemPartyIdentification <SysPtyId> [0..1] ± 2076
Constraints
• PartyPresenceRule
If Status equals 'Completed' then RelatedPartyIdentification must be present and
ResponsiblePartyIdentification must be present.
• StatusReasonRule
If Status equals 'Rejected' then StatusReason must be present.
36.4.2.1  Status <Sts>
Presence: [1..1]
Definition: Status of the party maintenance instruction.
Datatype: "Status6Code" on page 3305
CodeName Name Definition
REJT Rejected Instruction has been rejected.
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
36.4.2.2  StatusReason <StsRsn>
Presence: [0..*]
Definition: Specifies the underlying reason for the status of an object.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.016.001.01 PartyStatusAdviceV01
Target2-Securities 2075 August 2026
```

