---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.34 SecuritiesTransactionType48Choice", "35.1.16.34.2 Proprietary <Prtry>"]
file_pages: [1568]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.34.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1568 to 1568.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1568

```text
CodeName Name Definition
ETFT ExchangeTradedFunds Relates to an ETF creation or
redemption.
REBL Rebalancing Relates to a rebalanced transaction.
TRIN TransferIn Transaction is an incoming credit to an
account on the shareholders register,
and is not linked to a shift in investment
(subscription or switch), but to account
management.
TOUT TransferOut Transaction is a debit to an account on
the shareholders register, and is not
linked to a shift in investment
(redemption or switch), but to account
management.
35.1.16.34.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Securities transaction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.35  CurrencyToBuyOrSell1Choice
Definition: Choice of counterparty type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrencyToBuy <CcyToBuy> [1..1] CodeSet C1 1568
Or}   CurrencyToSell <CcyToSell> [1..1] CodeSet C1 1569
35.1.16.35.1  CurrencyToBuy <CcyToBuy>
Presence: [1..1]
Definition: Account servicer is instructed to buy the indicated currency after the receipt of cash
proceeds.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 2044
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1568 March 2026
```

