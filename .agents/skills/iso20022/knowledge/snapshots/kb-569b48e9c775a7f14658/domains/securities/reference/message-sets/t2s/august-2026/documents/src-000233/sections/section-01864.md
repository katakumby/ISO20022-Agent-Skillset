---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.18 TransactionDetails <TxDtls>", "72.4.3.4.18.29 Linkages <Lnkgs>", "72.4.3.4.18.29.3 Reference <Ref>", "72.4.3.4.18.29.3.3 IntraBalanceMovementIdentification <IntraBalMvmntId>"]
file_pages: [2557]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.18.29.3.3 IntraBalanceMovementIdentification <IntraBalMvmntId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2557 to 2557.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2557

```text
Definition: Unambiguous identification of the intra-position movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 3328
72.4.3.4.18.29.3.3  IntraBalanceMovementIdentification <IntraBalMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra-balance movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 3328
72.4.3.4.18.29.3.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 3328
72.4.3.4.18.29.3.5  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 3328
72.4.3.4.18.29.3.6  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
72.4.3.4.18.29.3.7  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 3328
72.4.3.4.18.29.4  ReferenceOwner <RefOwnr>
Presence: [0..1]
Definition: Party responsible for generating the reference.
ReferenceOwner <RefOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 3059 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 3059
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 3060
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2557 August 2026
```

