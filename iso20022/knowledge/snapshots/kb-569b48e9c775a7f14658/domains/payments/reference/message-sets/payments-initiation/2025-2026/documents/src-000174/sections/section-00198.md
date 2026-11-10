---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.1.1 MessageIdentification <MsgId>"]
file_pages: [284]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.1.1 MessageIdentification <MsgId>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 284 to 284.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 284

```text
GroupHeader <GrpHdr> contains the following GroupHeader124 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 284
   CreationDateTime <CreDtTm> [1..1] DateTime 284
   Authorisation <Authstn> [0..2] ± 285
   NumberOfTransactions <NbOfTxs> [1..1] Text 285
   ControlSum <CtrlSum> [0..1] Quantity 285
   GroupReversal <GrpRvsl> [0..1] Indicator 285
   InitiatingParty <InitgPty> [0..1] ± 285
   ForwardingAgent <FwdgAgt> [0..1] ± 286
   DebtorAgent <DbtrAgt> [0..1] ± 287
   CreditorAgent <CdtrAgt> [0..1] ± 288
Constraints
• ControlSumAndGroupReversalRule
If GroupReversal is true, then ControlSum is not allowed.
On Condition
    /GroupReversal is present
 And    /GroupReversal is equal to value 'true'
Following Must be True
    /ControlSum Must be absent
• GroupReversalAndNumberOfTransactionsGuideline
If GroupReversal is true, then NumberOfTransactions equals the number of transactions in the
original message.
4.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the instructing party, and sent to the next party in the
chain to unambiguously identify the message.
Usage: The instructing party has to make sure that MessageIdentification is unique per instructed party
for a pre-agreed period.
Datatype: "Max35Text" on page 609
4.4.1.2  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 603
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 284 March 2026
```

