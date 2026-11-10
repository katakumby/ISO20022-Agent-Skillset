---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "18.4 Message Building Blocks"]
file_pages: [566, 567]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.024.001.14"]
---

# 18.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 566 to 567.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 566

```text
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: BuySellBack (BSBK)
Buy-Sell Back: Sell Back
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: BuySellBack (BSBK)
Collateral (giver) Out Initiation
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralOut (COLO)
Collateral (giver) Out Return
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: CollateralOut (COLO)
Collateral (taker) In Initiation
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI)
Collateral (taker) In Return
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI).
18.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
18.4.1 TransactionIdentification <TxId>
Presence: [1..1]
Definition: Provides unambiguous transaction identification information.
Impacted by: C18 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 566 March 2026
```

## File page 567

```text
TransactionIdentification <TxId> contains the following elements (see "TransactionIdentifications47"
on page 1483 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1483
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1483
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1483
   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 1484
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1484
   CommonIdentification <CmonId> [0..1] Text 1484
   NettingServiceProviderIdentification <NetgSvcPrvdrId> [0..1] Text 1484
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
18.4.2 Linkages <Lnkgs>
Presence: [0..1]
Definition: Link to another transaction - provided for information only.
Linkages <Lnkgs> contains the following elements (see "Linkages41" on page 1545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± 1545
   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 1545
18.4.3 ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Provides details on the processing status of the transaction.
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 567 March 2026
```

