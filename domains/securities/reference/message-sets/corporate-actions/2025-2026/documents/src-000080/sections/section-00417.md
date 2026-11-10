---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.9 CorporateActionGeneralInformation <CorpActnGnlInf>", "8.4.9.4 EventType <EvtTp>"]
file_pages: [562]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.9.4 EventType <EvtTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 562 to 562.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 562

```text
Definition: Reference assigned by a court to a class action.
Datatype: "Max35Text" on page 1251
8.4.9.4  EventType <EvtTp>
Presence: [1..1]
Definition: Type of corporate action event.
Impacted by: C18 "EventTypeRule"
EventType <EvtTp> contains one of the following elements (see
"CorporateActionEventType109Choice" on page 1000 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1000
Or}   Proprietary <Prtry> [1..1] ± 1007
Constraints
• EventTypeRule
If Code is present, the code OTHR (Other) must only be used in case no other corporate action
event code is appropriate.
If Code is present, the code CHAN (Change) must only be used in case no other corporate action
event code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM (Final Maturity) must only be used when the redemption is
decided by the issuer and not by the securities holders.
8.4.9.5  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of the security concerned by the corporate action.
Impacted by: C15 "DescriptionPresenceRule", C16 "DescriptionUsageRule", C36 "ISINGuideline", C37
"ISINPresenceRule", C48 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 869 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 870
   OtherIdentification <OthrId> [0..*]  870
     Identification <Id> [1..1] Text 870
     Suffix <Sfx> [0..1] Text 870
     Type <Tp> [1..1] ± 871
   Description <Desc> [0..1] Text 871
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 562 February 2026
```

