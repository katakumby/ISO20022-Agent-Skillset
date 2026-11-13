---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 camt.060.001.07 AccountReportingRequestV07", "5.4 Message Building Blocks", "5.4.1 GroupHeader <GrpHdr>", "5.4.1.1 MessageIdentification <MsgId>"]
file_pages: [784]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.060.001.07"]
---

# 5.4.1.1 MessageIdentification <MsgId>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 784 to 784.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 784

```text
GroupHeader <GrpHdr> contains the following GroupHeader117 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 784
   CreationDateTime <CreDtTm> [1..1] DateTime 784
   MessageSender <MsgSndr> [0..1]  784
{Or     Party <Pty> [1..1] ± 784
Or}     Agent <Agt> [1..1] ± 785
5.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the account owner or the party authorised to send
the message, and sent to the account servicing institution, to unambiguously identify the message.
Usage: The sender has to make sure that 'MessageIdentification' is unique per account servicing
institution for a pre-agreed period.
Datatype: "Max35Text" on page 916
5.4.1.2  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 908
5.4.1.3  MessageSender <MsgSndr>
Presence: [0..1]
Definition: Identification of the party that is sending the message, when different from the account
owner.
MessageSender <MsgSndr> contains one of the following Party50Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Party <Pty> [1..1] ± 784
Or}   Agent <Agt> [1..1] ± 785
5.4.1.3.1  Party <Pty>
Presence: [1..1]
Definition: Identification of a person or an organisation.
Approved by the Payments SEG on 12 January 2026 camt.060.001.07 AccountReportingRequestV07
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
784 March 2026
```

