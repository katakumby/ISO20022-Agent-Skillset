---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.13 Miscellaneous", "17.1.13.2 AdditionalParameters16", "17.1.13.2.1 PartialSettlement <PrtlSttlm>"]
file_pages: [411]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.13.2.1 PartialSettlement <PrtlSttlm>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 411 to 411.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 411

```text
17.1.13.2.1  PartialSettlement <PrtlSttlm>
Presence: [0..1]
Definition: Specifies partial settlement information.
Datatype: "PartialSettlement2Code" on page 486
CodeName Name Definition
PAIN PartialSettlement Confirmation is for partial settlement.
Part of the transaction remains
unsettled.
PARC PartiallyConfirmed Confirmation is for partial settlement. No
additional settlement will take place.
17.1.13.2.2  PreviousPartialConfirmationIdentification <PrvsPrtlConfId>
Presence: [0..1]
Definition: Identification of the confirmation previously sent to confirm the partial settlement of a
transaction.
Datatype: "Max35Text" on page 497
17.1.13.2.3  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 497
17.1.13.2.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 497
17.1.13.2.5  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 497
17.1.13.2.6  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 497
17.1.13.2.7  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
411 March 2024
```

