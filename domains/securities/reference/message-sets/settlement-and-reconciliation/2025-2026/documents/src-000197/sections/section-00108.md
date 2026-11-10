---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 semt.013.001.07 IntraPositionMovementInstructionV07", "5.4 Message Building Blocks"]
file_pages: [153]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.014.001.09"]
---

# 5.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 153 to 153.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 153

```text
C14 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
5.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
5.4.1 TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unambiguous identification of a transaction as per the account owner (or the instructing party
managing the account).
Impacted by: C8 "NoAccountOwnerTransactionIdentificationRule"
TransactionIdentification <TxId> contains the following elements (see "TransactionIdentifications29"
on page 1485 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1486
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1486
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1486
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1486
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
5.4.2 Linkage <Lkg>
Presence: [0..1]
Definition: Link to another transaction that triggered the intra-position movement.
Linkage <Lkg> contains the following Linkages75 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 153
5.4.2.1  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
Presence: [1..1]
Definition: Unambiguous identification of a securities settlement transaction as known by the account
owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
Approved by the Securities SEG on 27 January 2026 semt.014.001.09
IntraPositionMovementStatusAdviceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 153 March 2026
```

