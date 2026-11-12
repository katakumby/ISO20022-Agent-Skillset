---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.1 Amount", "7.2.1.2 ImpliedCurrencyAndAmount"]
file_pages: [172]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.1.2 ImpliedCurrencyAndAmount

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 172 to 172.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 172

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.2.1.2  ImpliedCurrencyAndAmount
Definition: Number of monetary units specified in a currency where the unit of currency is implied by the
context and compliant with ISO 4217. The decimal separator is a dot.
Note: a zero amount is considered a positive amount.
Type: Amount
Format
minInclusive 0
totalDigits 18
fractionDigits 5
7.2.2 Binary
7.2.2.1  Max10KBinary
Definition: Binary data of 10K maximum.
Type: Binary
Format
minLength 1
maxLength 10240
7.2.3 CodeSet
7.2.3.1  AccountStatus3Code
Definition: Qualifies further the current state of an account.
Type: CodeSet
CodeName Name Definition
ENAB Enabled Account can be used for its intended
purpose.
DISA Disabled Account cannot be used for its intended
purpose, either temporarily or
permanently.
DELE Deleted Account cannot be used any longer.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 172 August 2026
```

