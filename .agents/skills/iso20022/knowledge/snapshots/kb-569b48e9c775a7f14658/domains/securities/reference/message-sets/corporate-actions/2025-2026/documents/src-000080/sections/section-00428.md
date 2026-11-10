---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.11 CorporateActionDetails <CorpActnDtls>"]
file_pages: [573]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.11 CorporateActionDetails <CorpActnDtls>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 573 to 573.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 573

```text
UnaffectedBalance <UafctdBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
8.4.11 CorporateActionDetails <CorpActnDtls>
Presence: [0..1]
Definition: Information about the corporate action event.
CorporateActionDetails <CorpActnDtls> contains the following CorporateAction92 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateDetails <DtDtls> [0..1]  573
     RecordDate <RcrdDt> [0..1] ± 573
     ExDividendDate <ExDvddDt> [0..1] ± 574
   EventStage <EvtStag> [0..1] ± 574
   AdditionalBusinessProcessIndicator <AddtlBizPrcInd> [0..*] ± 574
   FollowingEventTypeIndicator <FllwngEvtTpInd> [0..1] ± 575
   LotteryType <LtryTp> [0..1] ± 575
8.4.11.1  DateDetails <DtDtls>
Presence: [0..1]
Definition: Provides information about the dates related to a corporate action event.
DateDetails <DtDtls> contains the following CorporateActionDate86 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RecordDate <RcrdDt> [0..1] ± 573
   ExDividendDate <ExDvddDt> [0..1] ± 574
8.4.11.1.1  RecordDate <RcrdDt>
Presence: [0..1]
Definition: Date/time at which positions are struck at the end of the day to note which parties will receive
the relevant amount of entitlement, due to be distributed on payment date.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 573 February 2026
```

