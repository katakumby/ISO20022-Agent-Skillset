---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.11 Commission", "66.1.11.1 Commission21", "66.1.11.1.1 CommissionType <ComssnTp>", "66.1.11.1.1.2 Proprietary <Prtry>"]
file_pages: [4463]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.11.1.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4463 to 4463.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4463

```text
CodeName Name Definition
CDPL CommissionDePlacement Amount of cash due to an intermediary
for selling a product, or services, to a
third party.
66.1.11.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Commission type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.11.1.2  CommissionApplied <ComssnApld>
Presence: [1..1]
Definition: Commission amount or commission rate applied.
CommissionApplied <ComssnApld> contains one of the following AmountOrRate3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 4463
Or}   Rate <Rate> [1..1] Rate 4463
66.1.11.1.2.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.11.1.2.2  Rate <Rate>
Presence: [1..1]
Definition: Rate used to calculate the amount.
Datatype: "PercentageRate" on page 5401
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4463 May 2026
```

