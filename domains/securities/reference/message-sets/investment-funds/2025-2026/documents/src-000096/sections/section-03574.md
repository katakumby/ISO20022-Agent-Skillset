---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.9 TransactionChannelType1Choice"]
file_pages: [4824]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.9 TransactionChannelType1Choice

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4824 to 4824.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4824

```text
Definition: Settlement currency for the transaction.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.28.9  TransactionChannelType1Choice
Definition: Choice of formats for the specification of the type of transaction Channel.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4824
Or}   Proprietary <Prtry> [1..1] ± 4824
66.1.28.9.1  Code <Cd>
Presence: [1..1]
Definition: Type of transaction channel expressed as a code.
Datatype: "TransactionChannel2Code" on page 5378
CodeName Name Definition
FIAD FinancialAdvisor Financial advisor.
HOBA HomeBanking Home banking.
BRAN OfficeOrBranch Office or branch.
66.1.28.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of transaction channel expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.28.10  LetterIntent1
Definition: Specifies information about the letter of intent.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4824 May 2026
```

