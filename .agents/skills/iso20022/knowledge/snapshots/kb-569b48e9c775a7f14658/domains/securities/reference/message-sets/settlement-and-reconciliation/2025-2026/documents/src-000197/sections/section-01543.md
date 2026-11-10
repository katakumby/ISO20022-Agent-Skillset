---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.1 Amount", "35.2.1.4 ImpliedCurrencyAndAmount"]
file_pages: [2042]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.1.4 ImpliedCurrencyAndAmount

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2042 to 2042.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2042

```text
This data type contains the following XML attribute:
Name Attribute XML Name Datatype
Currency Ccy "ActiveOrHistoricCurrencyCode" on page 2044
Format
minInclusive 0
totalDigits 18
fractionDigits 5
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
35.2.1.4  ImpliedCurrencyAndAmount
Definition: Number of monetary units specified in a currency where the unit of currency is implied by the
context and compliant with ISO 4217. The decimal separator is a dot.
Note: a zero amount is considered a positive amount.
Type: Amount
Format
minInclusive 0
totalDigits 18
fractionDigits 5
35.2.2 CodeSet
35.2.2.1  AcknowledgementReason11Code
Definition: Specifies additional information about the processed instruction.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
OTHR Other Other. See Narrative.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2042 March 2026
```

