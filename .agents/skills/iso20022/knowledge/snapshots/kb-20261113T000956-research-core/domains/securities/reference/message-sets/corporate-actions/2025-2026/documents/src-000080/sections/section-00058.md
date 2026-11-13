---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.1 DateDetails <DtDtls>", "3.4.10.1.19 TradingSuspendedDate <TradgSspdDt>"]
file_pages: [104]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.1.19 TradingSuspendedDate <TradgSspdDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 104 to 104.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 104

```text
DeadlineForTaxBreakdownInstruction <DdlnForTaxBrkdwnInstr> contains one of the following
elements (see "DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.10.1.19  TradingSuspendedDate <TradgSspdDt>
Presence: [0..1]
Definition: Date/time at which trading of a security is suspended as the result of an event.
TradingSuspendedDate <TradgSspdDt> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.10.1.20  UnconditionalDate <UcondlDt>
Presence: [0..1]
Definition: Date/time upon which the terms of the take-over become unconditional as to acceptances.
UnconditionalDate <UcondlDt> contains one of the following elements (see "DateFormat30Choice"
on page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
3.4.10.1.21  WhollyUnconditionalDate <WhlyUcondlDt>
Presence: [0..1]
Definition: Date/time at on which all conditions, including regulatory, legal etc. pertaining to the take-
over, have been met.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 104 February 2026
```

