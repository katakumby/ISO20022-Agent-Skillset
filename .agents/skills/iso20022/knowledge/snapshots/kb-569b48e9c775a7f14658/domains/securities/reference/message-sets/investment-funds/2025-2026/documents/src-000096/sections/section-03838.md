---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.34 Price", "66.1.34.10 UnitPrice23", "66.1.34.10.7 TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd>"]
file_pages: [5127]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.34.10.7 TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5127 to 5127.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5127

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.34.10.7  TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd>
Presence: [0..1]
Definition: Specifies whether the fund calculates a taxable interest per share (TIS).
TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd> contains one of the following
TaxableIncomePerShareCalculated2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5127
Or}   Proprietary <Prtry> [1..1] ± 5127
66.1.34.10.7.1  Code <Cd>
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
66.1.34.10.7.2  Proprietary <Prtry>
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
66.1.35 Price Value
66.1.35.1  PriceValue1
Definition: Value given to a price.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5127 May 2026
```

