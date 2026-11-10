---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.11 QuotationType1Choice"]
file_pages: [4512]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.11 QuotationType1Choice

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4512 to 4512.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4512

```text
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.18.11  QuotationType1Choice
Definition: Choice of formats for a type of quotation
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4512
Or}   Proprietary <Prtry> [1..1] ± 4512
66.1.18.11.1  Code <Cd>
Presence: [1..1]
Definition: Type of quotation expressed as a code.
Datatype: "QuotationType1Code" on page 5346
CodeName Name Definition
ACTU ActualAmount Quotation expressed as a currency and
amount.
PRCT Percentage Quotation is expressed as percentage.
66.1.18.11.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of quotation expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.18.12  FinancialInstrument71
Definition: Security that is a sub-set of an investment fund, and is governed by the same investment
fund policy, for example, dividend option or valuation currency.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4512 May 2026
```

