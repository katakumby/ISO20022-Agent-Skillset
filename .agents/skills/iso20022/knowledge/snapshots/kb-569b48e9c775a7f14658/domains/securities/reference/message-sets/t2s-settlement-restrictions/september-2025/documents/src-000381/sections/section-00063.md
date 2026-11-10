---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "3.4 Message Building Blocks", "3.4.3 Movements <Mvmnts>", "3.4.3.4 Movement <Mvmnt>", "3.4.3.4.10 MovementDetails <MvmntDtls>", "3.4.3.4.10.13 Linkages <Lnkgs>", "3.4.3.4.10.13.3 Reference <Ref>", "3.4.3.4.10.13.3.3 IntraBalanceMovementIdentification <IntraBalMvmntId>"]
file_pages: [84]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 3.4.3.4.10.13.3.3 IntraBalanceMovementIdentification <IntraBalMvmntId>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 84 to 84.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 84

```text
Definition: Unambiguous identification of the intra-position movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 345
3.4.3.4.10.13.3.3  IntraBalanceMovementIdentification <IntraBalMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra-balance movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 345
3.4.3.4.10.13.3.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 345
3.4.3.4.10.13.3.5  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 345
3.4.3.4.10.13.3.6  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 345
3.4.3.4.10.13.3.7  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 345
3.4.3.4.10.13.4  ReferenceOwner <RefOwnr>
Presence: [0..1]
Definition: Party responsible for generating the reference.
ReferenceOwner <RefOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 253 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C6 253
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 253
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 84 September 2025
```

