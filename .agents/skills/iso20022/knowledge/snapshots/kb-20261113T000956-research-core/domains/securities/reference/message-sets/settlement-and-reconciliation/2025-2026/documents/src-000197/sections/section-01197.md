---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.95 Linkages73", "35.1.16.95.4 ReferenceOwner <RefOwnr>"]
file_pages: [1648]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.95.4 ReferenceOwner <RefOwnr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1648 to 1648.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1648

```text
Reference <Ref> contains one of the following elements (see "References80Choice" on page 1520 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 1521
Or   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 1521
Or   IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 1521
Or   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 1521
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 1522
Or   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[1..1] Text 1522
Or   PoolIdentification <PoolId> [1..1] Text 1522
Or   CommonIdentification <CmonId> [1..1] Text 1522
Or   TradeIdentification <TradId> [1..1] Text 1522
Or   UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 1522
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 1522
35.1.16.95.4  ReferenceOwner <RefOwnr>
Presence: [0..1]
Definition: Party that generates the reference.
ReferenceOwner <RefOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1664
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1665
35.1.16.96  SafekeepingPlaceFormat41Choice
Definition: Choice between formats for the place of safekeeping.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1648 March 2026
```

