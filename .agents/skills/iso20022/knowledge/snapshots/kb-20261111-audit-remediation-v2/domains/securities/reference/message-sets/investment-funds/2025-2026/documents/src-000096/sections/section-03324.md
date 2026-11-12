---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.3 InvestmentAccount74", "66.1.24.3.9 TaxExemption <TaxXmptn>"]
file_pages: [4563]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.3.9 TaxExemption <TaxXmptn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4563 to 4563.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4563

```text
66.1.24.3.9  TaxExemption <TaxXmptn>
Presence: [0..1]
Definition: Tax advantage specific to the account.
TaxExemption <TaxXmptn> contains one of the following elements (see
"TaxExemptionReason2Choice" on page 5250 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5251
Or}   Proprietary <Prtry> [1..1] ± 5254
66.1.24.3.10  StatementFrequency <StmtFrqcy>
Presence: [0..1]
Definition: Frequency at which a statement is issued.
StatementFrequency <StmtFrqcy> contains one of the following elements (see
"StatementFrequencyReason2Choice" on page 4534 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4535
Or}   Proprietary <Prtry> [1..1] ± 4535
66.1.24.3.11  ReferenceCurrency <RefCcy>
Presence: [0..1]
Definition: Currency chosen for reporting purposes by the account owner in agreement with the account
servicer.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.24.3.12  Language <Lang>
Presence: [0..1]
Definition: Language for all communication concerning the account.
Impacted by: C34 "ValidationByTable"
Datatype: "LanguageCode" on page 5328
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4563 May 2026
```

