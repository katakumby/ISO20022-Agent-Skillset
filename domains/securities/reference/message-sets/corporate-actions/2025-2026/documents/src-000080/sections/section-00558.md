---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13", "12.4 Message Building Blocks", "12.4.3 CorporateActionGeneralInformation <CorpActnGnlInf>", "12.4.3.3 EventType <EvtTp>"]
file_pages: [726]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.040.001.13"]
---

# 12.4.3.3 EventType <EvtTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 726 to 726.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 726

```text
Definition: Official and unique reference assigned by the official central body/entity within each market
at the beginning of a corporate action event.
Datatype: "Max35Text" on page 1251
12.4.3.3  EventType <EvtTp>
Presence: [1..1]
Definition: Type of corporate action event.
Impacted by: C10 "EventTypeRule"
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
If Code is present, the code REDM must only be used when the redemption is decided by the issuer
and not by the securities holders.
12.4.3.4  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: Identification of the security concerned by the corporate action.
Impacted by: C6 "DescriptionPresenceRule", C7 "DescriptionUsageRule", C11 "ISINGuideline", C12
"ISINPresenceRule", C16 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 seev.040.001.13
CorporateActionInstructionCancellationRequestV13
Corporate Actions - Maintenance 2025 - 2026 726 February 2026
```

