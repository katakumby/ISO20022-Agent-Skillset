---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.1.1 MessageIdentification <MsgId>"]
file_pages: [283]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.1.1 MessageIdentification <MsgId>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 283 to 283.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 283

```text
Definition: Common information for the message.
GroupHeader <GrpHdr> contains the following GroupHeader116 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 283
   CreationDateTime <CreDtTm> [1..1] DateTime 283
   MessageRecipient <MsgRcpt> [0..1] ± 283
   MessagePagination <MsgPgntn> [0..1] ± 284
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 285
   AdditionalInformation <AddtlInf> [0..1] Text 285
3.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the account servicing institution, and sent to the
account owner or the party authorised to receive the message, to unambiguously identify the message.
Usage: The account servicing institution has to make sure that MessageIdentification is unique per
account owner for a pre-agreed period.
Datatype: "Max35Text" on page 916
3.4.1.2  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 908
3.4.1.3  MessageRecipient <MsgRcpt>
Presence: [0..1]
Definition: Party authorised by the account owner to receive information about movements on the
account.
Usage: MessageRecipient should only be identified when different from the account owner.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
283 March 2026
```

