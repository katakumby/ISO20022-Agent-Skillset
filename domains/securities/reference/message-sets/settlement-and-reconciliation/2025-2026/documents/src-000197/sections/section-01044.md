---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.1 TransactionTypeAndAdditionalParameters23", "35.1.14.1.8 NonceIdentification <NonceId>"]
file_pages: [1483]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.1.8 NonceIdentification <NonceId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1483 to 1483.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1483

```text
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 2192
35.1.14.1.8  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 2192
35.1.14.2  TransactionIdentifications47
Definition: Provides transaction type and identification information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1483
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1483
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1483
   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 1484
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1484
   CommonIdentification <CmonId> [0..1] Text 1484
   NettingServiceProviderIdentification <NetgSvcPrvdrId> [0..1] Text 1484
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
35.1.14.2.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 2192
35.1.14.2.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 2192
35.1.14.2.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1483 March 2026
```

