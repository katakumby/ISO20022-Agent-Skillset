---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.10 CorporateActionGeneralInformation <CorpActnGnlInf>", "7.4.10.1 CorporateActionEventIdentification <CorpActnEvtId>"]
file_pages: [393]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.10.1 CorporateActionEventIdentification <CorpActnEvtId>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 393 to 393.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 393

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     WarrantParity <WarrtParity> [0..1] ± 401
     MinimumNominalQuantity <MinNmnlQty> [0..1] ± C19 401
     ContractSize <CtrctSz> [0..1] ± C19 401
Constraints
• OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice recommendations on
the structure and usage of the Official Corporate Action Event Reference (COAF). Those
recommendations are
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
7.4.10.1  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [1..1]
Definition: Reference assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 1251
7.4.10.2  OfficialCorporateActionEventIdentification <OffclCorpActnEvtId>
Presence: [0..1]
Definition: Official and unique reference assigned by the official central body/entity within each market
at the beginning of a corporate action event.
Datatype: "Max35Text" on page 1251
7.4.10.3  ClassActionNumber <ClssActnNb>
Presence: [0..1]
Definition: Reference assigned by a court to a class action.
Datatype: "Max35Text" on page 1251
7.4.10.4  EventProcessingType <EvtPrcgTp>
Presence: [0..1]
Definition: Type of processing involved by a corporate action.
EventProcessingType <EvtPrcgTp> contains one of the following elements (see
"CorporateActionEventProcessingType2Choice" on page 971 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 971
Or}   Proprietary <Prtry> [1..1] ± 972
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 393 February 2026
```

