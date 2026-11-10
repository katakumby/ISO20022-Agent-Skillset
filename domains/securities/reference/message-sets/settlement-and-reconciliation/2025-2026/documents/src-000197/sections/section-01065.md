---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.20 References45Choice", "35.1.14.20.4 OtherTransactionIdentification <OthrTxId>"]
file_pages: [1504]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.20.4 OtherTransactionIdentification <OthrTxId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1504 to 1504.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1504

```text
35.1.14.20.4  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Reference to a transaction that cannot be identified using a standard reference element
present in the message.
OtherTransactionIdentification <OthrTxId> contains the following GenericDocumentIdentification4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageNumber <MsgNb> [0..1] ± C20 1504
   Identification <Id> [1..1] Text 1504
35.1.14.20.4.1  MessageNumber <MsgNb>
Presence: [0..1]
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Impacted by: C20 "ShortLongNumberRule"
MessageNumber <MsgNb> contains one of the following elements (see "DocumentNumber5Choice"
on page 1444 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 1444
Or   LongNumber <LngNb> [1..1] Text 1445
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 1445
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
35.1.14.20.4.2  Identification <Id>
Presence: [1..1]
Definition: Identification of the document.
Datatype: "Max35Text" on page 2192
35.1.14.21  GenericIdentification78
Definition: Identification expressed as a proprietary type and narrative description.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1505
   Identification <Id> [0..1] Text 1505
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1504 March 2026
```

