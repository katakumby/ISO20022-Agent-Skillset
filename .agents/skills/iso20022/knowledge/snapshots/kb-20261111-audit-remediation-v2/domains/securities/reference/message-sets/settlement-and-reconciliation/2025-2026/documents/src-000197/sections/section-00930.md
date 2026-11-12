---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.7 AmountAndDirection94", "35.1.3.7.2 StampDutyIndicator <StmpDtyInd>"]
file_pages: [1366]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.7.2 StampDutyIndicator <StmpDtyInd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1366 to 1366.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1366

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.3.7.2  StampDutyIndicator <StmpDtyInd>
Presence: [0..1]
Definition: Whether the net proceeds include stamp duty amount.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.3.7.3  BrokerageAmountIndicator <BrkrgAmtInd>
Presence: [0..1]
Definition: Indicates whether the net proceeds include brokerage fees for the transaction. If absent,
element is not required.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.3.7.4  ResearchFeeIndicator <RsrchFeeInd>
Presence: [0..1]
Definition: Indicates whether the net proceeds include research fees for the transaction.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.3.7.5  Amount <Amt>
Presence: [1..1]
Definition: Amount of money in the cash entry.
Impacted by: C1 "ActiveCurrency", C9 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 2040
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1366 March 2026
```

