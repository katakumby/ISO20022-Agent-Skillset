---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.4 FractionDisposition <FrctnDspstn>"]
file_pages: [584]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.4 FractionDisposition <FrctnDspstn>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 584 to 584.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 584

```text
8.4.12.4  FractionDisposition <FrctnDspstn>
Presence: [0..1]
Definition: Specifies how fractions resulting from derived securities will be processed or how prorated
decisions will be rounding, if provided with a pro ration rate.
FractionDisposition <FrctnDspstn> contains one of the following elements (see
"FractionDispositionType27Choice" on page 894 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 894
Or}   Proprietary <Prtry> [1..1] ± 894
8.4.12.5  CurrencyOption <CcyOptn>
Presence: [0..1]
Definition: Currency in which cash proceeds are to be credited or debited.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 1157
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
8.4.12.6  DateDetails <DtDtls>
Presence: [0..1]
Definition: Provides information about the dates related to a corporate action option.
DateDetails <DtDtls> contains the following CorporateActionDate88 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CoverExpirationDeadline <CoverXprtnDdln> [0..1] ± 584
   TradingDate <TradgDt> [0..1] ± 585
8.4.12.6.1  CoverExpirationDeadline <CoverXprtnDdln>
Presence: [0..1]
Definition: Last day a holder can deliver the securities that it had elected on and/or previously protected.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 584 February 2026
```

