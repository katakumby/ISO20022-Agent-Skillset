---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.1.1 MessageIdentification <MsgId>"]
file_pages: [275]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.1.1 MessageIdentification <MsgId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 275 to 275.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 275

```text
Constraints
• ControlSumAndGroupReturnRule
If GroupReturn is true, then ControlSum is not allowed.
On Condition
    /GroupReturn is present
 And    /GroupReturn is equal to value 'true'
Following Must be True
    /ControlSum Must be absent
• GroupReturnAndNumberOfTransactionsGuideline
If GroupReturn is true, then NumberOfTransactions equals the number of transactions in the original
message.
• TotalInterbankSettlementAmountAndDateRule
If TotalReturnedInterbankSettlementAmount is present, then InterbankSettlementDate must be
present.
On Condition
    /TotalReturnedInterbankSettlementAmount is present
Following Must be True
    /InterbankSettlementDate Must be present
4.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the instructing party and sent to the next party in the
chain, to unambiguously identify the message.
Usage: The instructing party has to make sure that MessageIdentification is unique per instructed party
for a pre-agreed period.
Datatype: "Max35Text" on page 1246
4.4.1.2  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 1239
4.4.1.3  Authorisation <Authstn>
Presence: [0..2]
Definition: User identification or any user key to be used to check whether the initiating party is allowed
to initiate transactions from the account specified in the message.
Usage: The content is not of a technical nature, but reflects the organisational structure at the initiating
side.
The authorisation element can typically be used in relay scenarios, payment initiations, payment returns
or payment reversals that are initiated on behalf of a party different from the initiating party.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
275 March 2026
```

