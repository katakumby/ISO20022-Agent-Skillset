---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["11 seev.039.001.13 CorporateActionCancellationAdviceV13", "11.4 Message Building Blocks", "11.4.4 CorporateActionDetails <CorpActnDtls>", "11.4.4.2 EventStage <EvtStag>"]
file_pages: [714]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.039.001.13"]
---

# 11.4.4.2 EventStage <EvtStag>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 714 to 714.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 714

```text
ExDividendDate <ExDvddDt> contains one of the following elements (see "DateFormat30Choice" on
page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
11.4.4.2  EventStage <EvtStag>
Presence: [0..1]
Definition: Stage in the corporate action event life cycle.
EventStage <EvtStag> contains one of the following elements (see
"CorporateActionEventStageFormat14Choice" on page 968 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 968
Or}   Proprietary <Prtry> [1..1] ± 969
11.4.4.3  AdditionalBusinessProcessIndicator <AddtlBizPrcInd>
Presence: [0..*]
Definition: Specifies the type of the additional business process linked to a corporate action event such
as a claim compensation or tax refund.
AdditionalBusinessProcessIndicator <AddtlBizPrcInd> contains one of the following elements (see
"AdditionalBusinessProcessFormat15Choice" on page 941 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 941
Or}   Proprietary <Prtry> [1..1] ± 942
11.4.4.4  LotteryType <LtryTp>
Presence: [0..1]
Definition: Specifies the type of lottery announced.
LotteryType <LtryTp> contains one of the following elements (see "LotteryTypeFormat4Choice" on
page 979 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 979
Or}   Proprietary <Prtry> [1..1] ± 979
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 714 February 2026
```

