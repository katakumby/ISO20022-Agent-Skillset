---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.6 CorporateActionGeneralInformation <CorpActnGnlInf>", "9.4.6.1 CorporateActionEventIdentification <CorpActnEvtId>"]
file_pages: [675]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.6.1 CorporateActionEventIdentification <CorpActnEvtId>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 675 to 675.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 675

```text
CorporateActionGeneralInformation <CorpActnGnlInf> contains the following
CorporateActionGeneralInformation179 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 675
   OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 675
   ClassActionNumber <ClssActnNb> [0..1] Text 675
   EventType <EvtTp> [1..1] ± C10 675
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C13,
C14,
C18
676
   FractionalQuantity <FrctnlQty> [0..1] ± C9 677
Constraints
• OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice recommendations on
the structure and usage of the Official Corporate Action Event Reference (COAF). Those
recommendations are
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
9.4.6.1  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [1..1]
Definition: Reference assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 1251
9.4.6.2  OfficialCorporateActionEventIdentification <OffclCorpActnEvtId>
Presence: [0..1]
Definition: Official and unique reference assigned by the official central body/entity within each market
at the beginning of a corporate action event.
Datatype: "Max35Text" on page 1251
9.4.6.3  ClassActionNumber <ClssActnNb>
Presence: [0..1]
Definition: Reference assigned by a court to a class action.
Datatype: "Max35Text" on page 1251
9.4.6.4  EventType <EvtTp>
Presence: [1..1]
Definition: Type of corporate action event.
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 675 February 2026
```

