---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.18 DateDetails <DtDtls>", "7.4.13.18.5 ResponseDeadline <RspnDdln>"]
file_pages: [439]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.18.5 ResponseDeadline <RspnDdln>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 439 to 439.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 439

```text
MarketDeadline <MktDdln> contains one of the following elements (see "DateFormat43Choice" on
page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
7.4.13.18.5  ResponseDeadline <RspnDdln>
Presence: [0..1]
Definition: Date/time at which the account servicer has set as the deadline to respond, with instructions,
to an outstanding event.
ResponseDeadline <RspnDdln> contains one of the following elements (see "DateFormat44Choice"
on page 849 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 849
Or   DateCodeAndTime <DtCdAndTm> [1..1]  849
     DateCode <DtCd> [1..1]  850
{Or       Code <Cd> [1..1] CodeSet 850
Or}       Proprietary <Prtry> [1..1] ± 850
     Time <Tm> [1..1] Time 850
Or}   DateCode <DtCd> [1..1]  851
{Or     Code <Cd> [1..1] CodeSet 851
Or}     Proprietary <Prtry> [1..1] ± 851
7.4.13.18.6  ExpiryDate <XpryDt>
Presence: [0..1]
Definition: Date/time at which an order expires or on which a privilege or offer terminates.
ExpiryDate <XpryDt> contains one of the following elements (see "DateFormat43Choice" on page 843
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 439 February 2026
```

