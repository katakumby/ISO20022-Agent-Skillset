---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.27 TransactionIdentifications52", "35.1.14.27.5 NonceIdentification <NonceId>"]
file_pages: [1516]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.27.5 NonceIdentification <NonceId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1516 to 1516.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1516

```text
Datatype: "Max35Text" on page 2192
35.1.14.27.5  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 2192
35.1.14.27.6  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
AccountOwnerTransactionIdentification <AcctOwnrTxId> contains one of the following elements
(see "References44Choice" on page 1498 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OtherTransactionIdentification <OthrTxId> [1..1]  1499
     MessageNumber <MsgNb> [0..1] ± C20 1499
     Identification <Id> [1..1] Text 1499
Or   SecuritiesFinancingTransactionIdentification
<SctiesFincgTxId>
[1..1] ± 1499
Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] ± 1500
Or}   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 1500
35.1.14.28  SettlementTypeAndIdentification29
Definition: Provides transaction type and identification information.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1516 March 2026
```

