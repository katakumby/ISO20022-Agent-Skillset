---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.9 AccountStatusUpdateInstruction1Code"]
file_pages: [5275]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.9 AccountStatusUpdateInstruction1Code

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5275 to 5275.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5275

```text
66.2.2.9  AccountStatusUpdateInstruction1Code
Definition: Specifies the type of account status update instructed.
Type: CodeSet
CodeName Name Definition
CLOS Close Account is to be closed.
REAC Reactive Account is to be reactivated, any
previous instruction to close the account
is rescinded.
66.2.2.10  AccountStatusUpdateRequestReason1Code
Definition: Sepcifes the reason for a request for a change to an account status.
Type: CodeSet
CodeName Name Definition
CLOE AccountClosureInstructionError Previous account closure instruction was
sent in error.
66.2.2.11  AccountUsageType2Code
Definition: Specifies the type of usage of the account.
Type: CodeSet
CodeName Name Definition
INVE Investor Investor.
ISSP IssuingParticipant Issuing participant.
SETP SettlementParticipant Settlement participant.
TRDP TradingParticipant Trading participant.
66.2.2.12  ActiveCurrencyCode
Definition: A code allocated to a currency by a Maintenance Agency under an international identification
scheme as described in the latest edition of the international standard ISO 4217 "Codes for the
representation of currencies and funds".
Type: CodeSet
Format
pattern [A-Z]{3,3}
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5275 May 2026
```

