---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.2 Message Datatypes", "17.2.1 Amount", "17.2.1.2 ImpliedCurrencyAndAmount"]
file_pages: [474]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.2.1.2 ImpliedCurrencyAndAmount

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 474 to 474.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 474

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
17.2.1.2  ImpliedCurrencyAndAmount
Definition: Number of monetary units specified in a currency where the unit of currency is implied by the
context and compliant with ISO 4217. The decimal separator is a dot.
Note: a zero amount is considered a positive amount.
Type: Amount
Format
minInclusive 0
totalDigits 18
fractionDigits 5
17.2.2 CodeSet
17.2.2.1  AcknowledgementReason3Code
Definition: Specifies additional information about the processed instruction.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
SMPG MarketPracticeRuleDiscrepency Instruction is accepted but does not
comply with the market practice rule
published for the concerned market or
process.
OTHR Other Other. See Narrative.
17.2.2.2  AcknowledgementReason5Code
Definition: Specifies additional information about the processed instruction.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
474 March 2024
```

