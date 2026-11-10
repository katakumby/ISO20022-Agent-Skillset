---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.6 AmountAndDirection95", "35.1.3.6.1 AccruedInterestIndicator <AcrdIntrstInd>"]
file_pages: [1363]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.6.1 AccruedInterestIndicator <AcrdIntrstInd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1363 to 1363.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1363

```text
35.1.3.6.1  AccruedInterestIndicator <AcrdIntrstInd>
Presence: [0..1]
Definition: Indicates whether the net proceeds include interest accrued on the financial instrument.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.3.6.2  StampDutyIndicator <StmpDtyInd>
Presence: [0..1]
Definition: Whether the net proceeds include stamp duty amount.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.3.6.3  BrokerageAmountIndicator <BrkrgAmtInd>
Presence: [0..1]
Definition: Indicates whether the net proceeds include brokerage fees for the transaction. If absent,
element is not required.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.3.6.4  ResearchFeeIndicator <RsrchFeeInd>
Presence: [0..1]
Definition: Indicates whether the net proceeds include research fees for the transaction.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.3.6.5  Amount <Amt>
Presence: [0..1]
Definition: Amount of money in the cash entry.
Impacted by: C1 "ActiveCurrency", C9 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 2040
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1363 March 2026
```

