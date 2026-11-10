---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.6 CorporateActionGeneralInformation <CorpActnGnlInf>", "5.4.6.1 CorporateActionEventIdentification <CorpActnEvtId>"]
file_pages: [286]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.6.1 CorporateActionEventIdentification <CorpActnEvtId>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 286 to 286.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 286

```text
EventType/Code CHAN must only be used in case no other corporate action event code is
appropriate and only for an event which relates to a change.
EventType/Code REDM must only be used when the redemption is decided by the issuer and not by
the securities holders.
• OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice recommendations on
the structure and usage of the Official Corporate Action Event Reference (COAF). Those
recommendations are
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
5.4.6.1  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [1..1]
Definition: Reference assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 1251
5.4.6.2  OfficialCorporateActionEventIdentification <OffclCorpActnEvtId>
Presence: [0..1]
Definition: Official and unique reference assigned by the official central body/entity within each market
at the beginning of a corporate action event.
Datatype: "Max35Text" on page 1251
5.4.6.3  EventType <EvtTp>
Presence: [1..1]
Definition: Type of corporate action event.
Impacted by: C14 "EventTypeRule"
EventType <EvtTp> contains one of the following elements (see
"CorporateActionEventType112Choice" on page 989 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 989
Or}   Proprietary <Prtry> [1..1] ± 995
Constraints
• EventTypeRule
If Code is present, the code OTHR must only be used in case no other corporate action event code
is appropriate.
If Code is present, the code CHAN must only be used in case no other corporate action event code
is appropriate and only for an event which relates to a change.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 286 February 2026
```

