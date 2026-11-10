---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.16 References44Choice", "35.1.14.16.3 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>"]
file_pages: [1500]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.16.3 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1500 to 1500.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1500

```text
SecuritiesFinancingTransactionIdentification <SctiesFincgTxId> contains the following elements
(see "SettlementTypeAndIdentification18" on page 1501 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 1501
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1501
   Payment <Pmt> [1..1] CodeSet 1501
35.1.14.16.3  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
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
35.1.14.16.4  IntraPositionMovementIdentification <IntraPosMvmntId>
Presence: [1..1]
Definition: Reference to the intra-position movement transaction requested to be cancelled as known by
the account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
35.1.14.17  GenericIdentification1
Definition: Information related to an identification, for example party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1500
   SchemeName <SchmeNm> [0..1] Text 1501
   Issuer <Issr> [0..1] Text 1501
35.1.14.17.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max35Text" on page 2192
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1500 March 2026
```

