---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["8 semt.034.001.01 IntraPositionMovementPendingReportV01", "8.4 Message Building Blocks", "8.4.5 Movements <Mvmnts>", "8.4.5.2 Movement <Mvmnt>", "8.4.5.2.19 CorporateActionEventType <CorpActnEvtTp>"]
file_pages: [191]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 8.4.5.2.19 CorporateActionEventType <CorpActnEvtTp>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 191 to 191.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 191

```text
8.4.5.2.19  CorporateActionEventType <CorpActnEvtTp>
Presence: [0..1]
Definition: Specifies the type of corporate event.
Impacted by: C10 "EventTypeRule"
CorporateActionEventType <CorpActnEvtTp> contains one of the following elements (see
"CorporateActionEventType56Choice" on page 231 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 231
Or}   Proprietary <Prtry> [1..1] ± 237
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
8.4.5.2.20  MessageOriginator <MsgOrgtr>
Presence: [0..1]
Definition: Party that originated the message, if other than the sender.
MessageOriginator <MsgOrgtr> contains the following elements (see "SystemPartyIdentification8" on
page 257 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 257
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 257
8.4.5.2.21  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Specifies the creation date/time of the intra-position movement.
Datatype: "ISODateTime" on page 340
8.4.5.2.22  InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls>
Presence: [0..1]
Approved by the Securities SEG on 21 August 2025 semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities - Settlement Restrictions 191 September 2025
```

