---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.7 AmountAndDirection94", "35.1.3.7.6 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [1367]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.7.6 CreditDebitIndicator <CdtDbtInd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1367 to 1367.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1367

```text
Note: The decimal separator is a dot.
35.1.3.7.6  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether an entry is a credit or a debit.
Datatype: "CreditDebitCode" on page 2057
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
35.1.3.7.7  OriginalCurrencyAndOrderedAmount <OrgnlCcyAndOrdrdAmt>
Presence: [0..1]
Definition: Posting/settlement amount in its original currency when conversion from/into another
currency has occurred.
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
35.1.3.7.8  ForeignExchangeDetails <FXDtls>
Presence: [0..1]
Definition: Information needed to process a currency exchange or conversion.
ForeignExchangeDetails <FXDtls> contains the following elements (see "ForeignExchangeTerms23"
on page 1581 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 1581
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 1582
   ExchangeRate <XchgRate> [1..1] Rate 1582
   ResultingAmount <RsltgAmt> [1..1] Amount C1, C9 1582
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1367 March 2026
```

