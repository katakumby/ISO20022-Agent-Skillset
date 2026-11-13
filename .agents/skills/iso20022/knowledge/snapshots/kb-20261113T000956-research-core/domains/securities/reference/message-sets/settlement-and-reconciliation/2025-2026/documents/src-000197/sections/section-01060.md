---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.16 References44Choice", "35.1.14.16.1 OtherTransactionIdentification <OthrTxId>"]
file_pages: [1499]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.16.1 OtherTransactionIdentification <OthrTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1499 to 1499.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1499

```text
35.1.14.16.1  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Reference to a transaction that cannot be identified using a standard reference element
present in the message.
OtherTransactionIdentification <OthrTxId> contains the following GenericDocumentIdentification4
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageNumber <MsgNb> [0..1] ± C20 1499
   Identification <Id> [1..1] Text 1499
35.1.14.16.1.1  MessageNumber <MsgNb>
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
35.1.14.16.1.2  Identification <Id>
Presence: [1..1]
Definition: Identification of the document.
Datatype: "Max35Text" on page 2192
35.1.14.16.2  SecuritiesFinancingTransactionIdentification <SctiesFincgTxId>
Presence: [1..1]
Definition: Unambiguous identification of the underlying securities financing transaction (not the
underlying securities financing trade) as assigned by the instructing party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1499 March 2026
```

