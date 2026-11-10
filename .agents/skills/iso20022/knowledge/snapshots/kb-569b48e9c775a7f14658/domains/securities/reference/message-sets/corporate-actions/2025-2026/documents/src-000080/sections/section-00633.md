---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13", "15.4 Message Building Blocks", "15.4.4 CorporateActionDetails <CorpActnDtls>", "15.4.4.1 DateDetails <DtDtls>", "15.4.4.1.2 ExDividendDate <ExDvddDt>"]
file_pages: [824]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.044.001.13"]
---

# 15.4.4.1.2 ExDividendDate <ExDvddDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 824 to 824.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 824

```text
Definition: Date/time at which positions are struck at the end of the day to note which parties will receive
the relevant amount of entitlement, due to be distributed on payment date.
RecordDate <RcrdDt> contains one of the following elements (see "DateFormat30Choice" on
page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
15.4.4.1.2  ExDividendDate <ExDvddDt>
Presence: [0..1]
Definition: Date/time as from which trading (including exchange and OTC trading) occurs on the
underlying security without the benefit.
ExDividendDate <ExDvddDt> contains one of the following elements (see "DateFormat30Choice" on
page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
15.4.4.2  EventStage <EvtStag>
Presence: [0..1]
Definition: Stage in the corporate action event life cycle.
EventStage <EvtStag> contains one of the following elements (see
"CorporateActionEventStageFormat14Choice" on page 968 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 968
Or}   Proprietary <Prtry> [1..1] ± 969
15.4.4.3  LotteryType <LtryTp>
Presence: [0..1]
Definition: Specifies the type of lottery announced.
Approved by the Securities SEG on 27 January 2026 seev.044.001.13
CorporateActionMovementPreliminaryAdviceCancel
lationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 824 February 2026
```

