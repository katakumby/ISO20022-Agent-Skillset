---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.14 PriceDetails <PricDtls>", "13.4.9.14.13 EUDividendStatus <EUDvddSts>", "13.4.9.14.13.1 Code <Cd>"]
file_pages: [194]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.14.13.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 194 to 194.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 194

```text
EUDividendStatus <EUDvddSts> contains one of the following EUDividendStatusType3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 194
Or}   Proprietary <Prtry> [1..1] Text 194
13.4.9.14.13.1  Code <Cd>
Presence: [1..1]
Definition: EU dividend status expressed as an ISO 20022 code.
Datatype: "EUDividendStatus1Code" on page 5297
CodeName Name Definition
DIVI DividendInScope Dividend is in the scope of the directive.
DIVO DividendOutScope Dividend is out of the scope of the
directive.
UKWN DividendUnknown Unknown whether the dividend is in or
out of the scope of the directive.
13.4.9.14.13.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade conditions expressed as an extended code.
Datatype: "Max350Text" on page 5403
13.4.9.14.14  ChargeDetails <ChrgDtls>
Presence: [0..*]
Definition: Amount of money associated with a service.
ChargeDetails <ChrgDtls> contains the following Charge33 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  194
{Or     Code <Cd> [1..1] CodeSet 195
Or}     Proprietary <Prtry> [1..1] Text 195
   ChargesFees <ChrgsFees> [1..1] ± 195
   CalculationBasis <ClctnBsis> [0..1]  196
{Or     Code <Cd> [1..1] CodeSet 196
Or}     Proprietary <Prtry> [1..1] Text 196
13.4.9.14.14.1  Type <Tp>
Presence: [1..1]
Definition: Type of service for which a charge is asked or paid.
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 194 May 2026
```

