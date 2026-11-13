---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 camt.007.001.10 ModifyTransactionV10"]
file_pages: [326, 327]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.007.001.10"]
---

# 6 camt.007.001.10 ModifyTransactionV10

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 326 to 327.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 326

```text
6 camt.007.001.10
ModifyTransactionV10
6.1 MessageDefinition Functionality
Scope
The ModifyTransaction message is sent by a member to the transaction administrator.
It is used to request one modification in one payment instruction held at the transaction administrator
and sent by the member, debiting or crediting its account at the transaction administrator.
Usage
Following normal business flows, transactions registered by the transaction administrator may be
queued for later settlement (because of insufficient funds available, or because of risk or liquidity limits,
etc.). A transaction may have a series of statuses. These can be transient (such as pending or related
types) and final (such as rejected, revoked and/or settled).
Members of a system need to have information about the payments queue(s) and must have the ability
to take action (that is, to cancel or modify the transaction(s) to be settled). Note, however, that actions
by a member will always concern transactions in a transient status.
For this reason, at any time during the operating hours of the system, the member can request
modifications to the features of transient transactions.
The member will submit a message requesting modifications in one or more of the following criteria:
- instruction given, related to the processing of the transaction
- type of payment instructed
- priority of payment period in which the payment instruction should be processed (processing validity
time)
The ModifyTransaction message will contain the new values that the member wants to see applied to
the features of the transaction identified in the message.
Based on the criteria received within the ModifyTransaction message, the transaction administrator will
execute or reject the requested modifications.
The transaction administrator may send a Receipt message as a reply to the ModifyTransaction
request.
To verify the outcome of the request, the member may submit a GetTransaction message with the
appropriate search criteria.
Outline
The ModifyTransactionV10 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 326 February 2025
```

## File page 327

```text
Common business identification for the message.
B. Modification
Identifies the list of modifications to be executed.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 327 February 2025
```

