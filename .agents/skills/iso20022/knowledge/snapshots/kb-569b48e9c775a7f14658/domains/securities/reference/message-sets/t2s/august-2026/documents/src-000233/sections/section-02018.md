---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["79 semt.034.001.01 IntraPositionMovementPendingReportV01", "79.4 Message Building Blocks", "79.4.5 Movements <Mvmnts>", "79.4.5.2 Movement <Mvmnt>", "79.4.5.2.19 CorporateActionEventType <CorpActnEvtTp>"]
file_pages: [2746]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 79.4.5.2.19 CorporateActionEventType <CorpActnEvtTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2746 to 2746.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2746

```text
79.4.5.2.19  CorporateActionEventType <CorpActnEvtTp>
Presence: [0..1]
Definition: Specifies the type of corporate event.
Impacted by: C10 "EventTypeRule"
CorporateActionEventType <CorpActnEvtTp> contains one of the following elements (see
"CorporateActionEventType56Choice" on page 2986 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2986
Or}   Proprietary <Prtry> [1..1] ± 2993
Constraints
• EventTypeRule
The use of a specific corporate action event type code is allowed only if this specific event triggers a
securities movement as per the Event Interpretation Grid published by the Securities Market Practice
Group (SMPG).
The corporate action event indicator code OTHR must only be used in case no other corporate
action event code is appropriate.
The corporate action event indicator code CHAN must only be used in case no other corporate
action event code is appropriate and only for an event which relates to a change.
The corporate action event indicator code REDM must only be used when the redemption is decided
by the issuer and not by the holders.
79.4.5.2.20  MessageOriginator <MsgOrgtr>
Presence: [0..1]
Definition: Party that originated the message, if other than the sender.
MessageOriginator <MsgOrgtr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
79.4.5.2.21  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Specifies the creation date/time of the intra-position movement.
Datatype: "ISODateTime" on page 3320
79.4.5.2.22  InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities 2746 August 2026
```

