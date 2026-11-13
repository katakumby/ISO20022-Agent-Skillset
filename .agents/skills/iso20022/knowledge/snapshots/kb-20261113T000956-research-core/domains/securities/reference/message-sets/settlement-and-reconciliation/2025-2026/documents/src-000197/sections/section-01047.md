---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.4 TransactionIdentifications29", "35.1.14.4.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>"]
file_pages: [1486]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.4.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1486 to 1486.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1486

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1486
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1486
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1486
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1486
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
35.1.14.4.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 2192
35.1.14.4.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 2192
35.1.14.4.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
35.1.14.4.4  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction assigned by the processor of the instruction other than the
account owner the account servicer and the market infrastructure.
Datatype: "Max35Text" on page 2192
35.1.14.5  GenericIdentification80
Definition: Identification expressed as a proprietary type and narrative description.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1487
   Identification <Id> [0..1] Text 1487
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1486 March 2026
```

