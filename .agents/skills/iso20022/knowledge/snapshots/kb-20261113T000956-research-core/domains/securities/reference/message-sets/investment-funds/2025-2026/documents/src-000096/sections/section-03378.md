---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.9 InvestmentAccount73", "66.1.24.9.8 ReferenceCurrency <RefCcy>"]
file_pages: [4622]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.9.8 ReferenceCurrency <RefCcy>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4622 to 4622.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4622

```text
StatementFrequency <StmtFrqcy> contains one of the following elements (see
"StatementFrequencyReason2Choice" on page 4534 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4535
Or}   Proprietary <Prtry> [1..1] ± 4535
66.1.24.9.8  ReferenceCurrency <RefCcy>
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
66.1.24.9.9  Language <Lang>
Presence: [0..1]
Definition: Language for all communication concerning the account.
Impacted by: C34 "ValidationByTable"
Datatype: "LanguageCode" on page 5328
Constraints
• ValidationByTable
Must be a valid terrestrial language.
66.1.24.9.10  IncomePreference <IncmPref>
Presence: [0..1]
Definition: Dividend option chosen by the account owner based on the options offered in the
prospectus.
Datatype: "IncomePreference2Code" on page 5310
CodeName Name Definition
CASH Cash Distribution in cash.
SECU Securities Distribution in securities.
66.1.24.9.11  ReinvestmentDetails <RinvstmtDtls>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4622 May 2026
```

