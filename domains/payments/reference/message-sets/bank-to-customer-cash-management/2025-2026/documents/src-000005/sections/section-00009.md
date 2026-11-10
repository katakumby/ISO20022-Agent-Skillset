---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.1 GroupHeader <GrpHdr>", "2.4.1.1 MessageIdentification <MsgId>"]
file_pages: [24]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.1.1 MessageIdentification <MsgId>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 24 to 24.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 24

```text
Definition: Common information for the message.
GroupHeader <GrpHdr> contains the following GroupHeader116 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 24
   CreationDateTime <CreDtTm> [1..1] DateTime 24
   MessageRecipient <MsgRcpt> [0..1] ± 24
   MessagePagination <MsgPgntn> [0..1] ± 25
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 26
   AdditionalInformation <AddtlInf> [0..1] Text 26
2.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the account servicing institution, and sent to the
account owner or the party authorised to receive the message, to unambiguously identify the message.
Usage: The account servicing institution has to make sure that MessageIdentification is unique per
account owner for a pre-agreed period.
Datatype: "Max35Text" on page 916
2.4.1.2  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 908
2.4.1.3  MessageRecipient <MsgRcpt>
Presence: [0..1]
Definition: Party authorised by the account owner to receive information about movements on the
account.
Usage: MessageRecipient should only be identified when different from the account owner.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
24 March 2026
```

