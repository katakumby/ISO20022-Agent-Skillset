---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.12 CorporateActionDetails <CorpActnDtls>"]
file_pages: [415]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.12 CorporateActionDetails <CorpActnDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 415 to 415.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 415

```text
UnaffectedBalance <UafctdBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
7.4.12 CorporateActionDetails <CorpActnDtls>
Presence: [0..1]
Definition: Information about the corporate action event.
CorporateActionDetails <CorpActnDtls> contains the following CorporateAction91 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateDetails <DtDtls> [0..1]  415
     RecordDate <RcrdDt> [0..1] ± 416
     ExDividendDate <ExDvddDt> [0..1] ± 416
     LotteryDate <LtryDt> [0..1] ± 416
   SecuritiesQuantity <SctiesQty> [0..1]  417
     BaseDenomination <BaseDnmtn> [0..1] ± C20 417
     IncrementalDenomination <IncrmtlDnmtn> [0..1] ± C20 417
   EventStage <EvtStag> [0..1] ± 418
   AdditionalBusinessProcessIndicator <AddtlBizPrcInd> [0..*] ± 418
   FollowingEventTypeIndicator <FllwngEvtTpInd> [0..1] ± 418
   LotteryType <LtryTp> [0..1] ± 419
7.4.12.1  DateDetails <DtDtls>
Presence: [0..1]
Definition: Provides information about the dates related to a corporate action event.
DateDetails <DtDtls> contains the following CorporateActionDate85 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RecordDate <RcrdDt> [0..1] ± 416
   ExDividendDate <ExDvddDt> [0..1] ± 416
   LotteryDate <LtryDt> [0..1] ± 416
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 415 February 2026
```

