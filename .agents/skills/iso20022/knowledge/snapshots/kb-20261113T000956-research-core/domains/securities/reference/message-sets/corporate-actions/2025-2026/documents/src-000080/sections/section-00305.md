---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.12 CorporateActionDetails <CorpActnDtls>", "7.4.12.1 DateDetails <DtDtls>", "7.4.12.1.1 RecordDate <RcrdDt>"]
file_pages: [416]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.12.1.1 RecordDate <RcrdDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 416 to 416.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 416

```text
7.4.12.1.1  RecordDate <RcrdDt>
Presence: [0..1]
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
7.4.12.1.2  ExDividendDate <ExDvddDt>
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
7.4.12.1.3  LotteryDate <LtryDt>
Presence: [0..1]
Definition: Date/time on which the lottery is run and applied to the holder's positions. This is also
applicable to partial calls.
LotteryDate <LtryDt> contains one of the following elements (see "DateFormat30Choice" on page 842
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 416 February 2026
```

