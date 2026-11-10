---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["11 seev.039.001.13 CorporateActionCancellationAdviceV13", "11.4 Message Building Blocks", "11.4.1 CancellationAdviceGeneralInformation <CxlAdvcGnlInf>", "11.4.1.3 ProcessingStatus <PrcgSts>", "11.4.1.3.2 EventConfirmationStatus <EvtConfSts>"]
file_pages: [707]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.039.001.13"]
---

# 11.4.1.3.2 EventConfirmationStatus <EvtConfSts>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 707 to 707.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 707

```text
CodeName Name Definition
COMP Complete Event details are complete.
INCO Incomplete Event details are not complete.
11.4.1.3.2  EventConfirmationStatus <EvtConfSts>
Presence: [1..1]
Definition: Indicates the status of the occurrence of an event.
Datatype: "EventConfirmationStatus1Code" on page 1208
CodeName Name Definition
CONF Confirmed Occurrence of the event has been
confirmed.
UCON Unconfirmed Occurrence of the event has not been
confirmed.
11.4.2 CorporateActionGeneralInformation
<CorpActnGnlInf>
Presence: [1..1]
Definition: General information about the corporate action event.
Impacted by: C8 "OfficialCorporateActionEventReference"
CorporateActionGeneralInformation <CorpActnGnlInf> contains the following
CorporateActionGeneralInformation174 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 708
   OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 708
   ClassActionNumber <ClssActnNb> [0..1] Text 708
   EventType <EvtTp> [1..1] ± C5 708
   MandatoryVoluntaryEventType <MndtryVlntryEvtTp> [1..1] ± 709
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C3, C4,
C6, C7,
C9
709
Constraints
• OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice recommendations on
the structure and usage of the Official Corporate Action Event Reference (COAF). Those
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 707 February 2026
```

