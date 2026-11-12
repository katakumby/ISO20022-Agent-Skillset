---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.11 CorporateActionDetails <CorpActnDtls>", "8.4.11.1 DateDetails <DtDtls>", "8.4.11.1.2 ExDividendDate <ExDvddDt>"]
file_pages: [574]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.11.1.2 ExDividendDate <ExDvddDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 574 to 574.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 574

```text
RecordDate <RcrdDt> contains one of the following elements (see "DateFormat30Choice" on
page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
8.4.11.1.2  ExDividendDate <ExDvddDt>
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
8.4.11.2  EventStage <EvtStag>
Presence: [0..1]
Definition: Stage in the corporate action event life cycle.
EventStage <EvtStag> contains one of the following elements (see
"CorporateActionEventStageFormat14Choice" on page 968 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 968
Or}   Proprietary <Prtry> [1..1] ± 969
8.4.11.3  AdditionalBusinessProcessIndicator <AddtlBizPrcInd>
Presence: [0..*]
Definition: Indicates that the additional business process relates to a claim on the associated corporate
action event.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 574 February 2026
```

