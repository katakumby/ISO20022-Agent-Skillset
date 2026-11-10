---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.1 ModifiedTransactionDetails <ModfdTxDtls>", "32.4.1.2 AccountServicerTransactionIdentification <AcctSvcrTxId>"]
file_pages: [1158]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.1.2 AccountServicerTransactionIdentification <AcctSvcrTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1158 to 1158.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1158

```text
AccountOwnerTransactionIdentification <AcctOwnrTxId> contains the following elements (see
"SettlementTypeAndIdentification18" on page 1501 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 1501
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1501
   Payment <Pmt> [1..1] CodeSet 1501
32.4.1.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 2192
32.4.1.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
32.4.1.4  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction assigned by the processor of the instruction other than the
account owner, the account servicer and the market infrastructure.
Datatype: "Max35Text" on page 2192
32.4.1.5  OtherTransactionIdentification <OthrTxId>
Presence: [0..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 2192
32.4.1.6  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification144" on
page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1664
   LEI <LEI> [0..1] IdentifierSet 1664
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1158 March 2026
```

