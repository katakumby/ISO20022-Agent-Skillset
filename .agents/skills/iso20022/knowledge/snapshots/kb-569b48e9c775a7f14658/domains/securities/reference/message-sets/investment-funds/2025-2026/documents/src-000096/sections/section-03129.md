---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.2 StatementOfInvestmentFundTransactions2", "66.1.5.2.4 SubAccountDetails <SubAcctDtls>", "66.1.5.2.4.1 Identification <Id>"]
file_pages: [4355]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.2.4.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4355 to 4355.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4355

```text
Constraints
• TransactionOnSubAccountRule
If ActivityIndicator is "true" or "1" (Yes), then TransactionOnSubAccount must be present. If
ActivityIndicator is "false" or "0" (No), then TransactionOnSubAccount is not allowed.
66.1.5.2.4.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains one of the following elements (see "AccountIdentificationFormatChoice" on
page 4335 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SimpleIdentification <SmplId> [1..1] ± 4335
Or   IdentificationAndPurpose <IdAndPurp> [1..1]  4335
     Identification <Id> [1..1] ± 4336
     Purpose <Purp> [1..1] CodeSet 4336
Or}   IdentificationAsDSS <IdAsDSS> [1..1] ± 4336
66.1.5.2.4.2  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.5.2.4.3  TransactionOnSubAccount <TxOnSubAcct>
Presence: [0..*]
Definition: Creation/cancellation of investment units on the books of the fund or its designated agent, as
a result of executing an investment fund order.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4355 May 2026
```

