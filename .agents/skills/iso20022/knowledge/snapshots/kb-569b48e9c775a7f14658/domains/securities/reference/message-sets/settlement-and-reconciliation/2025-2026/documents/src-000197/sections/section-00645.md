---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "28.4 Message Building Blocks", "28.4.6 RepoCallRequestStatus <RepoCallReqSts>", "28.4.7.1 SecuritiesFinancingTradeIdentification <SctiesFincgTradId>"]
file_pages: [975]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28.4.7.1 SecuritiesFinancingTradeIdentification <SctiesFincgTradId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 975 to 975.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 975

```text
SecuritiesFinancingTransactionType: SecuritiesLending (SECL)
Securities Lending Return
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: SecuritiesLending (SECL)
Securities Borrowing Initiation
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: SecuritiesBorrowing (SECB)
Securities Borrowing Return
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: SecuritiesBorrowing (SECB).
28.4.7.1  SecuritiesFinancingTradeIdentification <SctiesFincgTradId>
Presence: [0..1]
Definition: Unambiguous identification of the underlying securities financing trade as assigned by the
instructing party. The identification is common to all collateral pieces (one or many).
Datatype: "Max35Text" on page 2192
28.4.7.2  SecuritiesFinancingUniqueTransactionIdentifier <SctiesFincgUnqTxIdr>
Presence: [0..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 2188
28.4.7.3  ClosingLegIdentification <ClsgLegId>
Presence: [0..1]
Definition: Unambiguous identification of the second leg of the transaction as known by the account
owner (or the instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
28.4.7.4  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 2192
28.4.7.5  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 975 March 2026
```

