---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.13 Identification Information", "16.1.13.2 CorporateActionEventReference3"]
file_pages: [876]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.13.2 CorporateActionEventReference3

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 876 to 876.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 876

```text
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification36" on
page 878 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 878
   Issuer <Issr> [1..1] Text 878
   SchemeName <SchmeNm> [0..1] Text 879
16.1.13.2  CorporateActionEventReference3
Definition: Identification of a linked corporate action event.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EventIdentification <EvtId> [1..1]  876
{Or     LinkedOfficialCorporateActionEventIdentification
<LkdOffclCorpActnEvtId>
[1..1] Text 876
Or}     LinkedCorporateActionIdentification <LkdCorpActnId> [1..1] Text 876
   LinkageType <LkgTp> [0..1] ± C22 877
16.1.13.2.1  EventIdentification <EvtId>
Presence: [1..1]
Definition: Identification of the linked corporate action event.
EventIdentification <EvtId> contains one of the following CorporateActionEventReference3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   LinkedOfficialCorporateActionEventIdentification
<LkdOffclCorpActnEvtId>
[1..1] Text 876
Or}   LinkedCorporateActionIdentification <LkdCorpActnId> [1..1] Text 876
16.1.13.2.1.1  LinkedOfficialCorporateActionEventIdentification <LkdOffclCorpActnEvtId>
Presence: [1..1]
Definition: Official and unique reference assigned by the official central body/ entity within each market
at the beginning of a corporate action event.
Datatype: "Max35Text" on page 1251
16.1.13.2.1.2  LinkedCorporateActionIdentification <LkdCorpActnId>
Presence: [1..1]
Definition: Reference assigned by the account servicer to unambiguously identify a related corporate
action event.
Datatype: "Max35Text" on page 1251
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 876 February 2026
```

