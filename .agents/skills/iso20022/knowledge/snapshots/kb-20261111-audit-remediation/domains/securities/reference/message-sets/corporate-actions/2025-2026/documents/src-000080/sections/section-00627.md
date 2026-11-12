---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13", "15.4 Message Building Blocks", "15.4.2 CorporateActionGeneralInformation <CorpActnGnlInf>"]
file_pages: [818]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.044.001.13"]
---

# 15.4.2 CorporateActionGeneralInformation <CorpActnGnlInf>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 818 to 818.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 818

```text
15.4.2 CorporateActionGeneralInformation
<CorpActnGnlInf>
Presence: [1..1]
Definition: General information about the corporate action event.
Impacted by: C8 "OfficialCorporateActionEventReference"
CorporateActionGeneralInformation <CorpActnGnlInf> contains the following
CorporateActionGeneralInformation177 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 818
   OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 818
   ClassActionNumber <ClssActnNb> [0..1] Text 818
   EventType <EvtTp> [1..1] ± C5 819
   MandatoryVoluntaryEventType <MndtryVlntryEvtTp> [1..1] ± 819
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C6, C7,
C9
819
Constraints
• OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice recommendations on
the structure and usage of the Official Corporate Action Event Reference (COAF). Those
recommendations are available in the SMPG Global Market Practices Part 1 document on
www.smpg.info.
15.4.2.1  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [1..1]
Definition: Reference assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 1251
15.4.2.2  OfficialCorporateActionEventIdentification <OffclCorpActnEvtId>
Presence: [0..1]
Definition: Official and unique reference assigned by the official central body/entity within each market
at the beginning of a corporate action event.
Datatype: "Max35Text" on page 1251
15.4.2.3  ClassActionNumber <ClssActnNb>
Presence: [0..1]
Definition: Reference assigned by a court to a class action.
Approved by the Securities SEG on 27 January 2026 seev.044.001.13
CorporateActionMovementPreliminaryAdviceCancel
lationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 818 February 2026
```

