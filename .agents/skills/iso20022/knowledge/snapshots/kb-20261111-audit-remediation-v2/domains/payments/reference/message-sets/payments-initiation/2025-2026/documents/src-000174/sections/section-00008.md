---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.1.1 MessageIdentification <MsgId>"]
file_pages: [18]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.1.1 MessageIdentification <MsgId>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 18 to 18.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 18

```text
Definition: Set of characteristics shared by all individual transactions included in the message.
GroupHeader <GrpHdr> contains the following GroupHeader114 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 18
   CreationDateTime <CreDtTm> [1..1] DateTime 18
   Authorisation <Authstn> [0..2] ± 18
   NumberOfTransactions <NbOfTxs> [1..1] Text 19
   ControlSum <CtrlSum> [0..1] Quantity 19
   InitiatingParty <InitgPty> [1..1] ± 19
   ForwardingAgent <FwdgAgt> [0..1] ± 20
   InitiationSource <InitnSrc> [0..1]  21
     Name <Nm> [1..1] Text 21
     Provider <Prvdr> [0..1] Text 21
     Version <Vrsn> [0..1] Text 22
2.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the instructing party, and sent to the next party in the
chain to unambiguously identify the message.
Usage: The instructing party has to make sure that MessageIdentification is unique per instructed party
for a pre-agreed period.
Datatype: "Max35Text" on page 609
2.4.1.2  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 603
2.4.1.3  Authorisation <Authstn>
Presence: [0..2]
Definition: User identification or any user key to be used to check whether the initiating party is allowed
to initiate transactions from the account specified in the message.
Usage: The content is not of a technical nature, but reflects the organisational structure at the initiating
side.
The authorisation element can typically be used in relay scenarios, payment initiations, payment returns
or payment reversals that are initiated on behalf of a party different from the initiating party.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 18 March 2026
```

