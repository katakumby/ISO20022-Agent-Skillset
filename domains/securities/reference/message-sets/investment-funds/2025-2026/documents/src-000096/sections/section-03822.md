---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.34 Price", "66.1.34.1 UnitPrice22", "66.1.34.1.6 TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd>"]
file_pages: [5111]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.34.1.6 TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5111 to 5111.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5111

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.34.1.6  TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd>
Presence: [0..1]
Definition: Specifies whether the fund calculates a taxable interest per share (TIS).
TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd> contains one of the following
TaxableIncomePerShareCalculated2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5111
Or}   Proprietary <Prtry> [1..1] ± 5111
66.1.34.1.6.1  Code <Cd>
Presence: [1..1]
Definition: Taxable income per share (TIS) calculated expressed as a code.
Datatype: "TaxableIncomePerShareCalculated2Code" on page 5366
CodeName Name Definition
TSIY FundCalculates Fund is calculating the taxable interest
per share with the NAV.
TSIN FundDoesNotCalculate Fund is not calculating the taxable
interest per share with the NAV.
UKWN FundCalculatesUnknown Unknown whether the fund is calculating
the taxable interest per share with the
NAV.
66.1.34.1.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Taxable income per share calculated (TIS) expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5111 May 2026
```

