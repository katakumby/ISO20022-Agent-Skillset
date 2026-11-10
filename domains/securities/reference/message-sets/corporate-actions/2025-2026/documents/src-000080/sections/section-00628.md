---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13", "15.4 Message Building Blocks", "15.4.2 CorporateActionGeneralInformation <CorpActnGnlInf>", "15.4.2.4 EventType <EvtTp>"]
file_pages: [819]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.044.001.13"]
---

# 15.4.2.4 EventType <EvtTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 819 to 819.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 819

```text
Datatype: "Max35Text" on page 1251
15.4.2.4  EventType <EvtTp>
Presence: [1..1]
Definition: Type of corporate action event.
Impacted by: C5 "EventTypeRule"
EventType <EvtTp> contains one of the following elements (see
"CorporateActionEventType108Choice" on page 1007 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1007
Or}   Proprietary <Prtry> [1..1] ± 1014
Constraints
• EventTypeRule
If Code is present, the code OTHR (Other) must only be used in case no other corporate action
event code is appropriate.
If Code is present, the code CHAN (Change) must only be used in case no other corporate action
event code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM (Final Maturity) must only be used when the redemption is
decided by the issuer and not by the securities holders.
15.4.2.5  MandatoryVoluntaryEventType <MndtryVlntryEvtTp>
Presence: [1..1]
Definition: Specifies whether the event is mandatory, mandatory with options or voluntary.
MandatoryVoluntaryEventType <MndtryVlntryEvtTp> contains one of the following elements (see
"CorporateActionMandatoryVoluntary3Choice" on page 975 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 975
Or}   Proprietary <Prtry> [1..1] ± 975
15.4.2.6  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of the security concerned by the corporate action.
Impacted by: C3 "DescriptionPresenceRule", C4 "DescriptionUsageRule", C6 "ISINGuideline", C7
"ISINPresenceRule", C9 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 seev.044.001.13
CorporateActionMovementPreliminaryAdviceCancel
lationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 819 February 2026
```

