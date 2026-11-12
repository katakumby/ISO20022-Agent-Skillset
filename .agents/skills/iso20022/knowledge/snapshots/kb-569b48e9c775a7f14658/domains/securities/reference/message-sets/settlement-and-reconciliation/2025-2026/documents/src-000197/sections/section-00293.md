---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.2 QueryReference <QryRef>"]
file_pages: [437]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.2 QueryReference <QryRef>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 437 to 437.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 437

```text
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 1538 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 1539
   LastPageIndicator <LastPgInd> [1..1] Indicator 1539
13.4.2 QueryReference <QryRef>
Presence: [0..1]
Definition: Identification of the message sent to request this report.
Datatype: "Max35Text" on page 2192
13.4.3 TransactionIdentification <TxId>
Presence: [0..1]
Definition: Provides unambiguous transaction identification information.
Impacted by: C3 "NoAccountOwnerTransactionIdentificationRule"
TransactionIdentification <TxId> contains the following elements (see "TransactionIdentifications56"
on page 1506 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeIdentification <TradId> [0..*] Text 1506
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 1506
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1506
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1506
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1507
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1507
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
13.4.4 SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 437 March 2026
```

