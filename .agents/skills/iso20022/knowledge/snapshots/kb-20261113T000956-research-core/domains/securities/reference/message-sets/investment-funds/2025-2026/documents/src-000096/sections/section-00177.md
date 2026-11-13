---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.14 PriceDetails <PricDtls>", "14.4.10.1.14.13 EUDividendStatus <EUDvddSts>", "14.4.10.1.14.13.2 Proprietary <Prtry>"]
file_pages: [263]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.14.13.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 263 to 263.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 263

```text
Definition: EU dividend status expressed as an ISO 20022 code.
Datatype: "EUDividendStatus1Code" on page 5297
CodeName Name Definition
DIVI DividendInScope Dividend is in the scope of the directive.
DIVO DividendOutScope Dividend is out of the scope of the
directive.
UKWN DividendUnknown Unknown whether the dividend is in or
out of the scope of the directive.
14.4.10.1.14.13.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade conditions expressed as an extended code.
Datatype: "Max350Text" on page 5403
14.4.10.1.14.14  ChargeDetails <ChrgDtls>
Presence: [0..*]
Definition: Amount of money associated with a service.
ChargeDetails <ChrgDtls> contains the following Charge33 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  263
{Or     Code <Cd> [1..1] CodeSet 263
Or}     Proprietary <Prtry> [1..1] Text 264
   ChargesFees <ChrgsFees> [1..1] ± 264
   CalculationBasis <ClctnBsis> [0..1]  264
{Or     Code <Cd> [1..1] CodeSet 265
Or}     Proprietary <Prtry> [1..1] Text 265
14.4.10.1.14.14.1  Type <Tp>
Presence: [1..1]
Definition: Type of service for which a charge is asked or paid.
Type <Tp> contains one of the following ChargeType11Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 263
Or}   Proprietary <Prtry> [1..1] Text 264
14.4.10.1.14.14.1.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 263 May 2026
```

