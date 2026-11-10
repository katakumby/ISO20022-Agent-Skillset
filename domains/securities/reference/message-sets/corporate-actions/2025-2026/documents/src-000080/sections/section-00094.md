---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.19 DateDetails <DtDtls>", "3.4.11.19.3 ProtectDeadline <PrtctDdln>"]
file_pages: [149]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.19.3 ProtectDeadline <PrtctDdln>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 149 to 149.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 149

```text
CoverExpirationDeadline <CoverXprtnDdln> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.11.19.3  ProtectDeadline <PrtctDdln>
Presence: [0..1]
Definition: Last date/time a holder can request to defer delivery of securities pursuant to a notice of
guaranteed delivery or other required documentation.
ProtectDeadline <PrtctDdln> contains one of the following elements (see "DateFormat43Choice" on
page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.11.19.4  MarketDeadline <MktDdln>
Presence: [0..1]
Definition: Issuer or issuer's agent deadline to respond with an instruction to an outstanding offer or
privilege.
MarketDeadline <MktDdln> contains one of the following elements (see "DateFormat43Choice" on
page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.11.19.5  ResponseDeadline <RspnDdln>
Presence: [0..1]
Definition: Date/time at which the account servicer has set as the deadline to respond, with instructions,
to an outstanding event.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 149 February 2026
```

