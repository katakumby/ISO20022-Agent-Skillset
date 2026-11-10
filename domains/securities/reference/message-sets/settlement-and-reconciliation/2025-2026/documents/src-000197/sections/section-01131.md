---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.40 Linkages59", "35.1.16.40.4 ReferenceOwner <RefOwnr>"]
file_pages: [1576]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.40.4 ReferenceOwner <RefOwnr>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1576 to 1576.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1576

```text
Reference <Ref> contains one of the following elements (see "References41Choice" on page 1495 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 1496
Or   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 1496
Or   IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 1496
Or   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 1496
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 1496
Or   PoolIdentification <PoolId> [1..1] Text 1497
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 1497
35.1.16.40.4  ReferenceOwner <RefOwnr>
Presence: [0..1]
Definition: Party that generates the reference.
ReferenceOwner <RefOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1664
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1665
35.1.16.41  RateOrName1Choice
Definition: Choice between a percentage rate or a rate name.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] ± C53 1576
Or}   RateName <RateNm> [1..1] ± 1577
35.1.16.41.1  Rate <Rate>
Presence: [1..1]
Definition: Pricing expressed as a rate.
Impacted by: C53 "SignRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1576 March 2026
```

