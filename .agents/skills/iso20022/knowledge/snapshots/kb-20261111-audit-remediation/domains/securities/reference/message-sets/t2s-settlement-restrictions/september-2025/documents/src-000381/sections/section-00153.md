---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["8 semt.034.001.01 IntraPositionMovementPendingReportV01", "8.4 Message Building Blocks", "8.4.5 Movements <Mvmnts>", "8.4.5.2 Movement <Mvmnt>", "8.4.5.2.16 Linkages <Lnkgs>", "8.4.5.2.16.3 Reference <Ref>", "8.4.5.2.16.3.6 PoolIdentification <PoolId>"]
file_pages: [190]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 8.4.5.2.16.3.6 PoolIdentification <PoolId>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 190 to 190.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 190

```text
8.4.5.2.16.3.6  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 345
8.4.5.2.16.3.7  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 345
8.4.5.2.16.4  ReferenceOwner <RefOwnr>
Presence: [0..1]
Definition: Party responsible for generating the reference.
ReferenceOwner <RefOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 253 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C6 253
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 253
8.4.5.2.17  SecuritiesSubBalanceIdentification <SctiesSubBalId>
Presence: [0..1]
Definition: Number identifying a lot constituting the sub-balance.
SecuritiesSubBalanceIdentification <SctiesSubBalId> contains the following elements (see
"GenericIdentification37" on page 225 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 226
   Issuer <Issr> [0..1] Text 226
8.4.5.2.18  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction is to be executed with a high priority.
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 230 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 230
Or}   Proprietary <Prtry> [1..1] ± 230
Approved by the Securities SEG on 21 August 2025 semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities - Settlement Restrictions 190 September 2025
```

