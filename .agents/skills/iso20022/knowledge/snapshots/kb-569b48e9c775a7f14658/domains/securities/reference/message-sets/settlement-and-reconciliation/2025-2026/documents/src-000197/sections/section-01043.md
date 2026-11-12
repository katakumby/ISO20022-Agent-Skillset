---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.1 TransactionTypeAndAdditionalParameters23", "35.1.14.1.4 Payment <Pmt>"]
file_pages: [1482]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.1.4 Payment <Pmt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1482 to 1482.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1482

```text
Datatype: "SecuritiesFinancingTransactionType2Code" on page 2142
CodeName Name Definition
REPU Repo Relates to a repurchase agreement
transaction.
RVPO ReverseRepo Relates to a reverse repurchase
agreement transaction.
SECB SecuritiesBorrowing Relates to a securities borrowing
operation.
SECL SecuritiesLending Relates to a securities lending operation.
BSBK BuySellBack Relates to a buy sell back transaction.
SBBK SellBuyBack Relates to a sell buy back transaction.
35.1.14.1.4  Payment <Pmt>
Presence: [1..1]
Definition: Specifies how the transaction is to be settled, for example, against payment.
Datatype: "DeliveryReceiptType2Code" on page 2058
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
35.1.14.1.5  ModificationType <ModTp>
Presence: [0..1]
Definition: Identifies the type of securities financing modification requested.
ModificationType <ModTp> contains one of the following elements (see "RepurchaseType21Choice"
on page 1552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1552
Or}   Proprietary <Prtry> [1..1] ± 1553
35.1.14.1.6  CommonIdentification <CmonId>
Presence: [0..1]
Definition: Unique reference agreed upon by the two trade counterparties to identify the trade.
Datatype: "Max35Text" on page 2192
35.1.14.1.7  PoolIdentification <PoolId>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1482 March 2026
```

