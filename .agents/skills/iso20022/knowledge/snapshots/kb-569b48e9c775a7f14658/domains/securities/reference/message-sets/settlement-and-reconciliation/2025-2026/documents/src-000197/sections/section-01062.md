---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.17 GenericIdentification1", "35.1.14.17.2 SchemeName <SchmeNm>"]
file_pages: [1501]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.17.2 SchemeName <SchmeNm>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1501 to 1501.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1501

```text
35.1.14.17.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 2192
35.1.14.17.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 2192
35.1.14.18  SettlementTypeAndIdentification18
Definition: Provides transaction type and identification information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 1501
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1501
   Payment <Pmt> [1..1] CodeSet 1501
35.1.14.18.1  TransactionIdentification <TxId>
Presence: [1..1]
Definition: Provides unambiguous transaction identification information.
Datatype: "Max35Text" on page 2192
35.1.14.18.2  SecuritiesMovementType <SctiesMvmntTp>
Presence: [1..1]
Definition: Specifies if the movement on a securities account results from a deliver or a receive
instruction.
Datatype: "ReceiveDelivery1Code" on page 2113
CodeName Name Definition
DELI Delivery Financial instruments will be debited
from the safekeeping account.
RECE Receive Financial instruments will be credited to
the safekeeping account.
35.1.14.18.3  Payment <Pmt>
Presence: [1..1]
Definition: Specifies how the transaction is to be settled, for example, against payment.
Datatype: "DeliveryReceiptType2Code" on page 2058
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1501 March 2026
```

