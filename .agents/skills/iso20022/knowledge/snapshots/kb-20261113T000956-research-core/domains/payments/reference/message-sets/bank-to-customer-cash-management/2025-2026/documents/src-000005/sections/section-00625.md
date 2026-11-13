---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.11 TransactionIdentifier1"]
file_pages: [858]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.11 TransactionIdentifier1

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 858 to 858.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 858

```text
Definition: Total of all individual entries included in the report.
Datatype: "DecimalNumber" on page 912
6.1.15.11  TransactionIdentifier1
Definition: Identification of the transaction in an unambiguous way.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionDateTime <TxDtTm> [1..1] DateTime 858
   TransactionReference <TxRef> [1..1] Text 858
6.1.15.11.1  TransactionDateTime <TxDtTm>
Presence: [1..1]
Definition: Local date and time of the transaction assigned by the POI (Point Of Interaction).
Datatype: "ISODateTime" on page 908
6.1.15.11.2  TransactionReference <TxRef>
Presence: [1..1]
Definition: Identification of the transaction that has to be unique for a time period.
Datatype: "Max35Text" on page 916
6.1.15.12  OriginalBusinessQuery1
Definition: Unique identification, as assigned by the original requestor, to unambiguously identify the
business query message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 858
   MessageNameIdentification <MsgNmId> [0..1] Text 858
   CreationDateTime <CreDtTm> [0..1] DateTime 859
6.1.15.12.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the original initiating party, to unambiguously identify
the original query message.
Datatype: "Max35Text" on page 916
6.1.15.12.2  MessageNameIdentification <MsgNmId>
Presence: [0..1]
Definition: Specifies the query message name identifier to which the message refers.
Datatype: "Max35Text" on page 916
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
858 March 2026
```

