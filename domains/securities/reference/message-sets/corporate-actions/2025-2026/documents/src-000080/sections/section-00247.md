---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.3 CorporateActionGeneralInformation <CorpActnGnlInf>"]
file_pages: [331]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.3 CorporateActionGeneralInformation <CorpActnGnlInf>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 331 to 331.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 331

```text
Definition: Identification of other documents as well as the document number.
OtherDocumentIdentification <OthrDocId> contains the following elements (see
"DocumentIdentification33" on page 861 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  861
{Or     AccountServicerDocumentIdentification
<AcctSvcrDocId>
[1..1] Text 862
Or}     AccountOwnerDocumentIdentification
<AcctOwnrDocId>
[1..1] Text 862
   DocumentNumber <DocNb> [0..1] ± C6 862
6.4.3 CorporateActionGeneralInformation
<CorpActnGnlInf>
Presence: [1..1]
Definition: General information about the corporate action event.
Impacted by: C16 "EventTypeRule", C21 "OfficialCorporateActionEventReference"
CorporateActionGeneralInformation <CorpActnGnlInf> contains the following
CorporateActionGeneralInformation197 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 332
   OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 332
   ClassActionNumber <ClssActnNb> [0..1] Text 332
   BuyerProtectionInstructionIdentification
<BuyrPrtcnInstrId>
[0..1] Text 332
   EventType <EvtTp> [1..1] ± C17 332
Constraints
• EventTypeRule
EventType/Code OTHR must only be used in case no other corporate action event code is
appropriate.
EventType/Code CHAN must only be used in case no other corporate action event code is
appropriate and only for an event which relates to a change.
EventType/Code REDM must only be used when the redemption is decided by the issuer and not by
the securities holders.
• OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice recommendations on
the structure and usage of the Official Corporate Action Event Reference (COAF). Those
recommendations are
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 331 February 2026
```

