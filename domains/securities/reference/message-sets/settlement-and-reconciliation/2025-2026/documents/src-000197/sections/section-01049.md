---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.6 AdditionalReference10", "35.1.14.6.3 MessageName <MsgNm>"]
file_pages: [1488]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.6.3 MessageName <MsgNm>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1488 to 1488.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1488

```text
35.1.14.6.3  MessageName <MsgNm>
Presence: [0..1]
Definition: Name of the message.
Datatype: "Max35Text" on page 2192
35.1.14.7  References47Choice
Definition: Choice of reference.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 1488
Or   PoolIdentification <PoolId> [1..1] Text 1488
Or   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 1488
Or   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 1488
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 1488
35.1.14.7.1  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
Presence: [1..1]
Definition: Unambiguous identification of a securities settlement transaction as known by the account
owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
35.1.14.7.2  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 2192
35.1.14.7.3  IntraPositionMovementIdentification <IntraPosMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra-position movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
35.1.14.7.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 2192
35.1.14.7.5  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1488 March 2026
```

