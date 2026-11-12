---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.5 AmountAndDirection6", "35.1.3.5.1 Amount <Amt>"]
file_pages: [1362]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.5.1 Amount <Amt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1362 to 1362.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1362

```text
35.1.3.5.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money in the cash entry.
Impacted by: C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 2041
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
35.1.3.5.2  Sign <Sgn>
Presence: [1..1]
Definition: Indicates that the amount value is positive or negative.
Datatype: One of the following values must be used (see "PlusOrMinusIndicator" on page 2188):
• Meaning When True: Plus
• Meaning When False: Minus
35.1.3.6  AmountAndDirection95
Definition: Posting of an item to a cash account, in the context of a cash transaction, that results in an
increase or decrease to the balance of the account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccruedInterestIndicator <AcrdIntrstInd> [0..1] Indicator 1363
   StampDutyIndicator <StmpDtyInd> [0..1] Indicator 1363
   BrokerageAmountIndicator <BrkrgAmtInd> [0..1] Indicator 1363
   ResearchFeeIndicator <RsrchFeeInd> [0..1] Indicator 1363
   Amount <Amt> [0..1] Amount C1, C9 1363
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1364
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1364
   ForeignExchangeDetails <FXDtls> [0..1] ± 1364
   ValueDate <ValDt> [0..1] ± 1365
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1362 March 2026
```

