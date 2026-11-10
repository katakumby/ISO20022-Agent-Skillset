---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.1.1 MessageIdentification <MsgId>"]
file_pages: [414]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.1.1 MessageIdentification <MsgId>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 414 to 414.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 414

```text
5.4.1 GroupHeader <GrpHdr>
Presence: [1..1]
Definition: Set of characteristics shared by all individual transactions included in the message.
GroupHeader <GrpHdr> contains the following GroupHeader118 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 414
   CreationDateTime <CreDtTm> [1..1] DateTime 414
   Authorisation <Authstn> [0..2] ± 414
   NumberOfTransactions <NbOfTxs> [1..1] Text 415
   ControlSum <CtrlSum> [0..1] Quantity 415
   InitiatingParty <InitgPty> [1..1] ± 415
   ForwardingAgent <FwdgAgt> [0..1] ± 416
5.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, assigned by the instructing party and sent to the next party in the
chain, to unambiguously identify the message.
Usage: The instructing party has to make sure that MessageIdentification is unique per instructed party
for a pre-agreed period.
Datatype: "Max35Text" on page 609
5.4.1.2  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 603
5.4.1.3  Authorisation <Authstn>
Presence: [0..2]
Definition: User identification or any user key that allows to check if the initiating party is allowed to
initiate transactions from the account specified in the initiation.
Usage: The content is not of a technical nature, but reflects the organisational structure at the initiating
side. The authorisation element can typically be used in relay scenarios, payment initiations, payment
returns or payment reversals that are initiated on behalf of a different party than the initiating party.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 414 March 2026
```

