---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["11 seev.039.001.13 CorporateActionCancellationAdviceV13", "11.4 Message Building Blocks", "11.4.2 CorporateActionGeneralInformation <CorpActnGnlInf>", "11.4.2.1 CorporateActionEventIdentification <CorpActnEvtId>"]
file_pages: [708]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.039.001.13"]
---

# 11.4.2.1 CorporateActionEventIdentification <CorpActnEvtId>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 708 to 708.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 708

```text
recommendations are available in the SMPG Global Market Practices Part 1 document on
www.smpg.info.
11.4.2.1  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [1..1]
Definition: Reference assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 1251
11.4.2.2  OfficialCorporateActionEventIdentification <OffclCorpActnEvtId>
Presence: [0..1]
Definition: Official and unique reference assigned by the official central body/entity within each market
at the beginning of a corporate action event.
Datatype: "Max35Text" on page 1251
11.4.2.3  ClassActionNumber <ClssActnNb>
Presence: [0..1]
Definition: Reference assigned by a court to a class action.
Datatype: "Max35Text" on page 1251
11.4.2.4  EventType <EvtTp>
Presence: [1..1]
Definition: Type of corporate action event.
Impacted by: C5 "EventTypeRule"
EventType <EvtTp> contains one of the following elements (see
"CorporateActionEventType107Choice" on page 1014 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1014
Or}   Proprietary <Prtry> [1..1] ± 1021
Constraints
• EventTypeRule
If Code is present, the code OTHR (Other) must only be used if no other corporate action event code
is appropriate.
If Code is present, the code CHAN (Change) must only be used if no other corporate action event
code is appropriate and only for an event which relates to a change.
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 708 February 2026
```

