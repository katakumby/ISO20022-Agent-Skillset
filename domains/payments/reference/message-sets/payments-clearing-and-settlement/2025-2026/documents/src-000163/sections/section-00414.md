---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.24 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>", "4.4.3.27.24.38 UnderlyingAllocation <UndrlygAllcn>", "4.4.3.27.24.38.5 Reference <Ref>"]
file_pages: [560]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.24.38.5 Reference <Ref>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 560 to 560.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 560

```text
Definition: Underlying reason for the allocation.
Usage: This applies to the allocation only, this is not the underlying reason for the payment.
Purpose <Purp> contains one of the following elements (see "Purpose2Choice" on page 1191 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1191
Or}   Proprietary <Prtry> [1..1] Text 1191
4.4.3.27.24.38.5  Reference <Ref>
Presence: [1..1]
Definition: Reference for the allocation.
Datatype: "Max35Text" on page 1246
4.4.3.27.24.38.6  RelatedReferences <RltdRefs>
Presence: [0..*]
Definition: Reference relating to the allocation which is meaningful to both parties (for example the
original Securities Settlement Transaction Identification).
RelatedReferences <RltdRefs> contains one of the following elements (see "References80Choice" on
page 1181 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 1182
Or   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 1182
Or   IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 1182
Or   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 1182
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 1182
Or   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[1..1] Text 1182
Or   PoolIdentification <PoolId> [1..1] Text 1182
Or   CommonIdentification <CmonId> [1..1] Text 1182
Or   TradeIdentification <TradId> [1..1] Text 1183
Or   UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 1183
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 1183
4.4.3.28  SupplementaryData <SplmtryData>
Presence: [0..*]
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
560 March 2026
```

