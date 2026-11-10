---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.8 CorporateActionDetails <CorpActnDtls>"]
file_pages: [679]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.8 CorporateActionDetails <CorpActnDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 679 to 679.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 679

```text
ConfirmedBalance <ConfdBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
9.4.8 CorporateActionDetails <CorpActnDtls>
Presence: [0..1]
Definition: Information about the corporate action event.
CorporateActionDetails <CorpActnDtls> contains the following CorporateAction93 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateDetails <DtDtls> [0..1]  679
     RecordDate <RcrdDt> [0..1] ± 679
     ExDividendDate <ExDvddDt> [0..1] ± 680
   EventStage <EvtStag> [0..1] ± 680
   AdditionalBusinessProcessIndicator <AddtlBizPrcInd> [0..1] ± 680
   FollowingEventTypeIndicator <FllwngEvtTpInd> [0..1] ± 681
   LotteryType <LtryTp> [0..1] ± 681
9.4.8.1  DateDetails <DtDtls>
Presence: [0..1]
Definition: Provides information about the dates related to a corporate action event.
DateDetails <DtDtls> contains the following CorporateActionDate86 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RecordDate <RcrdDt> [0..1] ± 679
   ExDividendDate <ExDvddDt> [0..1] ± 680
9.4.8.1.1  RecordDate <RcrdDt>
Presence: [0..1]
Definition: Date/time at which positions are struck at the end of the day to note which parties will receive
the relevant amount of entitlement, due to be distributed on payment date.
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 679 February 2026
```

