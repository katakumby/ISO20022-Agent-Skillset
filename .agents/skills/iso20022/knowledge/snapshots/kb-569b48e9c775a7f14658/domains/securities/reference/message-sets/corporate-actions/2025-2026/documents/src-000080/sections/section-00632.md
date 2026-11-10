---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13", "15.4 Message Building Blocks", "15.4.4 CorporateActionDetails <CorpActnDtls>"]
file_pages: [823]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.044.001.13"]
---

# 15.4.4 CorporateActionDetails <CorpActnDtls>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 823 to 823.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 823

```text
SafekeepingPlace <SfkpgPlc> contains one of the following elements (see
"SafekeepingPlaceFormat42Choice" on page 1130 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  1130
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1130
     Identification <Id> [0..1] Text 1131
Or   Country <Ctry> [1..1] CodeSet C3 1131
Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1131
Or   TypeAndIdentification <TpAndId> [1..1]  1131
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1132
     Identification <Id> [1..1] IdentifierSet C1 1132
Or}   Proprietary <Prtry> [1..1] ± 1132
15.4.4 CorporateActionDetails <CorpActnDtls>
Presence: [0..1]
Definition: Information about the corporate action event.
CorporateActionDetails <CorpActnDtls> contains the following CorporateAction71 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateDetails <DtDtls> [0..1]  823
     RecordDate <RcrdDt> [0..1] ± 823
     ExDividendDate <ExDvddDt> [0..1] ± 824
   EventStage <EvtStag> [0..1] ± 824
   LotteryType <LtryTp> [0..1] ± 824
15.4.4.1  DateDetails <DtDtls>
Presence: [0..1]
Definition: Provides information about the dates related to a corporate action event.
DateDetails <DtDtls> contains the following CorporateActionDate86 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RecordDate <RcrdDt> [0..1] ± 823
   ExDividendDate <ExDvddDt> [0..1] ± 824
15.4.4.1.1  RecordDate <RcrdDt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.044.001.13
CorporateActionMovementPreliminaryAdviceCancel
lationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 823 February 2026
```

