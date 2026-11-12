---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.18 TransactionDetails <TxDtls>", "4.4.3.4.18.29 Linkages <Lnkgs>", "4.4.3.4.18.29.3 Reference <Ref>", "4.4.3.4.18.29.3.3 IntraBalanceMovementIdentification <IntraBalMvmntId>"]
file_pages: [161]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.18.29.3.3 IntraBalanceMovementIdentification <IntraBalMvmntId>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 161 to 161.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 161

```text
Definition: Unambiguous identification of the intra-position movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 557
4.4.3.4.18.29.3.3  IntraBalanceMovementIdentification <IntraBalMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra-balance movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 557
4.4.3.4.18.29.3.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 557
4.4.3.4.18.29.3.5  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 557
4.4.3.4.18.29.3.6  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 557
4.4.3.4.18.29.3.7  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 557
4.4.3.4.18.29.4  ReferenceOwner <RefOwnr>
Presence: [0..1]
Definition: Party responsible for generating the reference.
ReferenceOwner <RefOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 413 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 413
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 413
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 161 March 2026
```

