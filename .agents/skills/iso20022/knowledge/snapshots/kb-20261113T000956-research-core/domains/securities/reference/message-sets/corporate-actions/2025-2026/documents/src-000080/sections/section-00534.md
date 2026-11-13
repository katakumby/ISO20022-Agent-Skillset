---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["10 seev.038.001.09 CorporateActionNarrativeV09", "10.4 Message Building Blocks", "10.4.3 CorporateActionGeneralInformation <CorpActnGnlInf>", "10.4.3.1 CorporateActionEventIdentification <CorpActnEvtId>"]
file_pages: [699]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.038.001.09"]
---

# 10.4.3.1 CorporateActionEventIdentification <CorpActnEvtId>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 699 to 699.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 699

```text
Definition: General information about the corporate action event.
Impacted by: C8 "OfficialCorporateActionEventReference"
CorporateActionGeneralInformation <CorpActnGnlInf> contains the following
CorporateActionGeneralInformation92 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 699
   OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 699
   NarrativeType <NrrtvTp> [0..1] ± 699
Constraints
• OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice recommendations on
the structure and usage of the Official Corporate Action Event Reference (COAF). Those
recommendations are
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
10.4.3.1  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [1..1]
Definition: Reference assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 1251
10.4.3.2  OfficialCorporateActionEventIdentification <OffclCorpActnEvtId>
Presence: [0..1]
Definition: Official and unique reference assigned by the official central body/entity within each market
at the beginning of a corporate action event.
Datatype: "Max35Text" on page 1251
10.4.3.3  NarrativeType <NrrtvTp>
Presence: [0..1]
Definition: Specifies the type of narrative related to the message.
NarrativeType <NrrtvTp> contains one of the following elements (see
"CorporateActionNarrative3Choice" on page 983 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 983
Or}   Proprietary <Prtry> [1..1] ± 983
Approved by the Securities SEG on 27 January 2026 seev.038.001.09 CorporateActionNarrativeV09
Corporate Actions - Maintenance 2025 - 2026 699 February 2026
```

