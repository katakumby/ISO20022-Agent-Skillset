---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.8 Charge", "66.1.8.1 Fees2", "66.1.8.1.2 IndividualFee <IndvFee>", "66.1.8.1.2.2 Basis <Bsis>", "66.1.8.1.2.2.2 Proprietary <Prtry>"]
file_pages: [4438]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.8.1.2.2.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4438 to 4438.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4438

```text
CodeName Name Definition
GRAM GrossAmount Charge/Commission/tax basis is based
on the gross amount.
NEAM NetAmount Charge/commission/tax basis is based
on the net amount.
NAVP NetAssetValuePrice Charge/tax basis is the price.
PERU PerUnit Charges/tax basis is per unit of financial
instrument.
66.1.8.1.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Fee (charge/commission) basis expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.8.1.2.3  Amount <Amt>
Presence: [1..1]
Definition: Fee amount.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.8.1.2.4  DiscountDetails <DscntDtls>
Presence: [0..1]
Definition: Discount or waiver applied to the fee.
Impacted by: C16 "DiscountElementRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4438 May 2026
```

