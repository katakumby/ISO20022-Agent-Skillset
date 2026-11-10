---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.39 ForeignExchangeTerms23", "82.1.19.39.4 ResultingAmount <RsltgAmt>"]
file_pages: [3023]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.39.4 ResultingAmount <RsltgAmt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3023 to 3023.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3023

```text
82.1.19.39.4  ResultingAmount <RsltgAmt>
Presence: [1..1]
Definition: Counter value of a foreign exchange conversion.
Impacted by: C1 "ActiveCurrency", C4 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
82.1.19.40  ModificationCancellationAllowed4Choice
Definition: Choice of format for the modification cancellation information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 3023
Or}   Proprietary <Prtry> [1..1] ± 3023
82.1.19.40.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether a third party is allowed to modify or cancel the transaction.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.19.40.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Modification, cancellation allowed information expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3023 August 2026
```

