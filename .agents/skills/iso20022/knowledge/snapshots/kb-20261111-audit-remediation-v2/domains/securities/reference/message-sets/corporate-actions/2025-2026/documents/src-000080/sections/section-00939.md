---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.1 Amount", "16.2.1.3 ImpliedCurrencyAndAmount"]
file_pages: [1157]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.1.3 ImpliedCurrencyAndAmount

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1157 to 1157.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1157

```text
16.2.1.3  ImpliedCurrencyAndAmount
Definition: Number of monetary units specified in a currency where the unit of currency is implied by the
context and compliant with ISO 4217. The decimal separator is a dot.
Note: a zero amount is considered a positive amount.
Type: Amount
Format
minInclusive 0
totalDigits 18
fractionDigits 5
16.2.2 CodeSet
16.2.2.1  AcknowledgementReason7Code
Definition: Specifies additional information about the processed instruction.
Type: CodeSet
CodeName Name Definition
NSTP NotStraightThroughProcessing Instruction was not straight through
processing and had to be processed
manually.
OTHR Other Other. See Narrative.
16.2.2.2  ActiveCurrencyCode
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
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.2.2.3  ActiveOrHistoricCurrencyCode
Definition: A code allocated to a currency by a Maintenance Agency under an international identification
scheme, as described in the latest edition of the international standard ISO 4217 "Codes for the
representation of currencies and funds".
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1157 February 2026
```

