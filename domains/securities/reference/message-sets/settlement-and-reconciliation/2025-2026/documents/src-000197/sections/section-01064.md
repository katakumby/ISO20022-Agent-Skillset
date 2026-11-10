---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.20 References45Choice", "35.1.14.20.1 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>"]
file_pages: [1503]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.20.1 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1503 to 1503.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1503

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] ± 1503
Or   SecuritiesFinancingTransactionIdentification
<SctiesFincgTxId>
[1..1] ± 1503
Or   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 1503
Or}   OtherTransactionIdentification <OthrTxId> [1..1]  1504
     MessageNumber <MsgNb> [0..1] ± C20 1504
     Identification <Id> [1..1] Text 1504
35.1.14.20.1  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
Presence: [1..1]
Definition: Unambiguous identification of the securities settlement transaction.
SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId> contains the following elements
(see "SettlementTypeAndIdentification18" on page 1501 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 1501
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1501
   Payment <Pmt> [1..1] CodeSet 1501
35.1.14.20.2  SecuritiesFinancingTransactionIdentification <SctiesFincgTxId>
Presence: [1..1]
Definition: Unambiguous identification of the underlying securities financing transaction (not the
underlying securities financing trade) as assigned by the instructing party.
SecuritiesFinancingTransactionIdentification <SctiesFincgTxId> contains the following elements
(see "SettlementTypeAndIdentification18" on page 1501 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 1501
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1501
   Payment <Pmt> [1..1] CodeSet 1501
35.1.14.20.3  IntraPositionMovementIdentification <IntraPosMvmntId>
Presence: [1..1]
Definition: Reference to the intra-position movement transaction requested to be cancelled as known by
the account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1503 March 2026
```

