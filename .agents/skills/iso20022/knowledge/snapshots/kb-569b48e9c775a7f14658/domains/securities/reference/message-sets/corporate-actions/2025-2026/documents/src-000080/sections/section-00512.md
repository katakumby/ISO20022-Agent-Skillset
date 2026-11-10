---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.6 CorporateActionGeneralInformation <CorpActnGnlInf>", "9.4.6.5 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [676]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.6.5 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 676 to 676.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 676

```text
Impacted by: C10 "EventTypeRule"
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
9.4.6.5  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of the security concerned by the corporate action.
Impacted by: C7 "DescriptionPresenceRule", C8 "DescriptionUsageRule", C13 "ISINGuideline", C14
"ISINPresenceRule", C18 "OtherIdentificationPresenceRule"
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
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 676 February 2026
```

