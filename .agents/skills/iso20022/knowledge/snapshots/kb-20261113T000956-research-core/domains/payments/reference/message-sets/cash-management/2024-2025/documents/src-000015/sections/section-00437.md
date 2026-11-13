---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["22 camt.024.001.08 ModifyStandingOrderV08", "22.4 Message Building Blocks", "22.4.1 MessageHeader <MsgHdr>"]
file_pages: [594]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.024.001.08"]
---

# 22.4.1 MessageHeader <MsgHdr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 594 to 594.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 594

```text
22.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 811 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 812
   CreationDateTime <CreDtTm> [0..1] DateTime 812
22.4.2 StandingOrderIdentification <StgOrdrId>
Presence: [1..1]
Definition: Identifies the standing order.
StandingOrderIdentification <StgOrdrId> contains the following StandingOrderIdentification8
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 594
   Account <Acct> [1..1] ± C8, C7 594
   AccountOwner <AcctOwnr> [0..1] ± 595
22.4.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification for a standing order, as assigned by the account
servicer or the account owner.
Datatype: "Max35Text" on page 889
22.4.2.2  Account <Acct>
Presence: [1..1]
Definition: Business relationship between two entities; one entity is the account owner, the other entity
is the account servicer.
Impacted by: C8 "IdentificationOrProxyPresenceRule", C7 "IdentificationAndProxyGuideline"
Approved by the Payments SEG on 04 February 2025 camt.024.001.08 ModifyStandingOrderV08
Cash Management - Maintenance 2024 - 2025 594 February 2025
```

