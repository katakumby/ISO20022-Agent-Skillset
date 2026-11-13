---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.6 EventsLinkage <EvtsLkg>", "3.4.7.1 CorporateActionEventIdentification <CorpActnEvtId>"]
file_pages: [65]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.7.1 CorporateActionEventIdentification <CorpActnEvtId>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 65 to 65.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 65

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     WarrantParity <WarrtParity> [0..1] ± 73
     MinimumNominalQuantity <MinNmnlQty> [0..1] ± C25 73
     ContractSize <CtrctSz> [0..1] ± C25 73
Constraints
• OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice recommendations on
the structure and usage of the Official Corporate Action Event Reference (COAF). These
recommendations are
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
3.4.7.1  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [1..1]
Definition: Reference assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 1251
3.4.7.2  OfficialCorporateActionEventIdentification <OffclCorpActnEvtId>
Presence: [0..1]
Definition: Official and unique reference assigned by the official central body/entity within each market
at the beginning of a corporate action event.
Datatype: "Max35Text" on page 1251
3.4.7.3  ClassActionNumber <ClssActnNb>
Presence: [0..1]
Definition: Reference assigned by a court to a class action.
Datatype: "Max35Text" on page 1251
3.4.7.4  EventProcessingType <EvtPrcgTp>
Presence: [0..1]
Definition: Type of processing involved by a corporate action.
EventProcessingType <EvtPrcgTp> contains one of the following elements (see
"CorporateActionEventProcessingType2Choice" on page 971 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 971
Or}   Proprietary <Prtry> [1..1] ± 972
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 65 February 2026
```

