---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "28.4 Message Building Blocks"]
file_pages: [960]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 960 to 960.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 960

```text
SecuritiesFinancingTransactionType: SecuritiesBorrowing (SECB)
Securities Borrowing Return
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: SecuritiesBorrowing (SECB).
28.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
28.4.1 TransactionIdentification <TxId>
Presence: [1..1]
Definition: Provides unambiguous transaction identification information.
Impacted by: C19 "NoAccountOwnerTransactionIdentificationRule"
TransactionIdentification <TxId> contains the following elements (see "TransactionIdentifications53"
on page 1522 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1523
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1523
   CommonIdentification <CmonId> [0..1] Text 1523
   NonceIdentification <NonceId> [0..1] Text 1523
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
28.4.2 ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Processing status of the transaction.
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 960 March 2026
```

