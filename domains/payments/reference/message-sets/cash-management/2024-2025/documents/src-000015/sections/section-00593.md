---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["35 camt.103.001.03 CreateReservationV03", "35.4 Message Building Blocks"]
file_pages: [769]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.103.001.03"]
---

# 35.4 Message Building Blocks

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 769 to 769.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 769

```text
C6 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
35.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
35.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 811 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 812
   CreationDateTime <CreDtTm> [0..1] DateTime 812
35.4.2 ReservationIdentification <RsvatnId>
Presence: [1..1]
Definition: Identification of the default reservation.
ReservationIdentification <RsvatnId> contains the following ReservationIdentification4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReservationIdentification <RsvatnId> [0..1] Text 769
   SystemIdentification <SysId> [0..1] ± 769
   Type <Tp> [1..1]  770
{Or     Code <Cd> [1..1] CodeSet 770
Or}     Proprietary <Prtry> [1..1] Text 770
   AccountOwner <AcctOwnr> [0..1] ± 770
   AccountIdentification <AcctId> [0..1] ± 771
35.4.2.1  ReservationIdentification <RsvatnId>
Presence: [0..1]
Definition: Unique identification of the reservation.
Datatype: "Max35Text" on page 889
35.4.2.2  SystemIdentification <SysId>
Presence: [0..1]
Approved by the Payments SEG on 04 February 2025 camt.103.001.03 CreateReservationV03
Cash Management - Maintenance 2024 - 2025 769 February 2025
```

