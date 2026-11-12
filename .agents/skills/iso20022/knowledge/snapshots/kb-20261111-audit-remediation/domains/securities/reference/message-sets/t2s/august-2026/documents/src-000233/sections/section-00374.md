---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02", "20.4 Message Building Blocks", "20.4.1 Identification <Id>", "20.4.1.4 MessageOriginator <MsgOrgtr>"]
file_pages: [481]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.082.001.02"]
---

# 20.4.1.4 MessageOriginator <MsgOrgtr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 481 to 481.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 481

```text
20.4.1.4  MessageOriginator <MsgOrgtr>
Presence: [0..1]
Definition: Party that originated the message, if other than the sender.
MessageOriginator <MsgOrgtr> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
20.4.1.5  MessageRecipient <MsgRcpt>
Presence: [0..1]
Definition: Party that is the final destination of the message, if other than the receiver.
MessageRecipient <MsgRcpt> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
20.4.2 QueryDefinition <QryDef>
Presence: [1..1]
Definition: Defines the intra-balance movement cancellation query criteria.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.082.001.02
IntraBalanceMovementCancellationQueryV02
Target2-Securities 481 August 2026
```

