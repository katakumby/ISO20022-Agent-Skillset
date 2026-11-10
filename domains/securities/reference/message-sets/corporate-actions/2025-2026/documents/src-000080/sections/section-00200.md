---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["4 seev.032.001.09 CorporateActionEventProcessingStatusAdviceV09", "4.2 Structure"]
file_pages: [267]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.032.001.09"]
---

# 4.2 Structure

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 267 to 267.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 267

```text
Additional information that can not be captured in the structured fields and/or any other specific
block.
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CorpActnEvtPrcgStsAdvc> [1..1]  
   NotificationIdentification <NtfctnId> [0..1] ± 268
   OtherDocumentIdentification <OthrDocId> [0..*] ± 268
   CorporateActionGeneralInformation <CorpActnGnlInf> [1..1]  C3, C5 269
     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 270
     OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 270
     ClassActionNumber <ClssActnNb> [0..1] Text 270
     EventType <EvtTp> [1..1] ± C4 270
   EventProcessingStatus <EvtPrcgSts> [1..*]  270
{Or     Complete <Cmplt> [1..1] ± 271
Or     Reconciled <Rcncld> [1..1] ± 271
Or     Pending <Pdg> [1..1] ± 271
Or}     ProprietaryStatus <PrtrySts> [1..1] ± 272
   AdditionalInformation <AddtlInf> [0..1]  272
     AdditionalText <AddtlTxt> [0..*] Text 272
     PartyContactNarrative <PtyCtctNrrtv> [0..*] Text 272
   SupplementaryData <SplmtryData> [0..*] ± C7 272
4.3 Constraints
C1 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C2 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C3 EventTypeRule
EventType/Code OTHR must only be used in case no other corporate action event code is
appropriate.
Approved by the Securities SEG on 27 January 2026 seev.032.001.09
CorporateActionEventProcessingStatusAdviceV09
Corporate Actions - Maintenance 2025 - 2026 267 February 2026
```

