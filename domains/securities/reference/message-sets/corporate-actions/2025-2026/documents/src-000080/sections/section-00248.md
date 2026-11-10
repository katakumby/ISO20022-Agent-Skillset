---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.3 CorporateActionGeneralInformation <CorpActnGnlInf>", "6.4.3.1 CorporateActionEventIdentification <CorpActnEvtId>"]
file_pages: [332]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.3.1 CorporateActionEventIdentification <CorpActnEvtId>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 332 to 332.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 332

```text
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
6.4.3.1  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [1..1]
Definition: Reference assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 1251
6.4.3.2  OfficialCorporateActionEventIdentification <OffclCorpActnEvtId>
Presence: [0..1]
Definition: Official and unique reference assigned by the official central body/entity within each market
at the beginning of a corporate action event.
Datatype: "Max35Text" on page 1251
6.4.3.3  ClassActionNumber <ClssActnNb>
Presence: [0..1]
Definition: Reference assigned by a court to a class action.
Datatype: "Max35Text" on page 1251
6.4.3.4  BuyerProtectionInstructionIdentification <BuyrPrtcnInstrId>
Presence: [0..1]
Definition: Buyer Protection instruction identification assigned by the CSD when an instruction has been
entered by the buyer.
Datatype: "Max35Text" on page 1251
6.4.3.5  EventType <EvtTp>
Presence: [1..1]
Definition: Type of corporate action event.
Impacted by: C17 "EventTypeRule"
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
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 332 February 2026
```

