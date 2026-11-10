---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.41 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>", "7.4.2.41.39 UnderlyingAllocation <UndrlygAllcn>", "7.4.2.41.39.6 RelatedReferences <RltdRefs>"]
file_pages: [1014]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.41.39.6 RelatedReferences <RltdRefs>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1014 to 1014.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1014

```text
7.4.2.41.39.6  RelatedReferences <RltdRefs>
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
7.4.2.42  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C64 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1190 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1191
   Envelope <Envlp> [1..1] (External Schema) 1191
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
1014 March 2026
```

