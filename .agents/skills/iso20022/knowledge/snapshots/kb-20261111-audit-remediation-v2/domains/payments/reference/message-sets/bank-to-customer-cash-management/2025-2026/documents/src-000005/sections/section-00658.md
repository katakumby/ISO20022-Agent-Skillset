---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.2 CodeSet", "6.2.2.11 ClearingChannel2Code"]
file_pages: [891]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.2.11 ClearingChannel2Code

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 891 to 891.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 891

```text
CodeName Name Definition
DEBT BorneByDebtor All transaction charges are to be borne
by the debtor.
CRED BorneByCreditor All transaction charges are to be borne
by the creditor.
SHAR Shared In a credit transfer context, means that
transaction charges on the sender side
are to be borne by the debtor,
transaction charges on the receiver side
are to be borne by the creditor. In a
direct debit context, means that
transaction charges on the sender side
are to be borne by the creditor,
transaction charges on the receiver side
are to be borne by the debtor.
SLEV FollowingServiceLevel Charges are to be applied following the
rules agreed in the service level and/or
scheme.
6.2.2.11  ClearingChannel2Code
Definition: Specifies the clearing channel for the routing of the transaction, as part of the payment type
identification.
Type: CodeSet
CodeName Name Definition
RTGS RealTimeGrossSettlementSystem Clearing channel is a real-time gross
settlement system.
RTNS RealTimeNetSettlementSystem Clearing channel is a real-time net
settlement system.
MPNS MassPaymentNetSystem Clearing channel is a mass payment net
settlement system.
BOOK BookTransfer Payment through internal book transfer.
6.2.2.12  CopyDuplicate1Code
Definition: Specifies if this document is a copy, a duplicate, or a duplicate of a copy.
Type: CodeSet
CodeName Name Definition
CODU CopyDuplicate Message is being sent as a copy to a
party other than the account owner, for
information purposes and the message
is a duplicate of a message previously
sent.
COPY Copy Message is being sent as a copy to a
party other than the account owner, for
information purposes.
DUPL Duplicate Message is for information/confirmation
purposes. It is a duplicate of a message
previously sent.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
891 March 2026
```

