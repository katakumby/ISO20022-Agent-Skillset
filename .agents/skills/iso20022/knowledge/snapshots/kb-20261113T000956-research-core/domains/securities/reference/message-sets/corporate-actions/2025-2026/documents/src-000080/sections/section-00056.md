---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.1 DateDetails <DtDtls>", "3.4.10.1.13 ProrationDate <PrratnDt>"]
file_pages: [102]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.1.13 ProrationDate <PrratnDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 102 to 102.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 102

```text
MarginFixingDate <MrgnFxgDt> contains one of the following elements (see "DateFormat30Choice"
on page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
3.4.10.1.13  ProrationDate <PrratnDt>
Presence: [0..1]
Definition: Date/time (and time) at which an issuer will determine the proration amount/quantity of an
offer.
ProrationDate <PrratnDt> contains one of the following elements (see "DateFormat30Choice" on
page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
3.4.10.1.14  RecordDate <RcrdDt>
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
3.4.10.1.15  RegistrationDeadline <RegnDdln>
Presence: [0..1]
Definition: Date/time on which instructions to register or registration details will be accepted.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 102 February 2026
```

