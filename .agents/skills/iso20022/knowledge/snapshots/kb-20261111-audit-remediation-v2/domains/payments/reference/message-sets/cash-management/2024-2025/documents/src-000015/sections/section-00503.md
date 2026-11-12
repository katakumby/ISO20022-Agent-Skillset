---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["27 camt.049.001.07 DeleteReservationV07", "27.4 Message Building Blocks", "27.4.2 CurrentReservation <CurRsvatn>"]
file_pages: [665]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.049.001.07"]
---

# 27.4.2 CurrentReservation <CurRsvatn>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 665 to 665.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 665

```text
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 811 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 812
   CreationDateTime <CreDtTm> [0..1] DateTime 812
27.4.2 CurrentReservation <CurRsvatn>
Presence: [0..1]
Definition: Identifies the current reservation to delete.
CurrentReservation <CurRsvatn> contains the following ReservationIdentification4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReservationIdentification <RsvatnId> [0..1] Text 665
   SystemIdentification <SysId> [0..1] ± 665
   Type <Tp> [1..1]  665
{Or     Code <Cd> [1..1] CodeSet 666
Or}     Proprietary <Prtry> [1..1] Text 666
   AccountOwner <AcctOwnr> [0..1] ± 666
   AccountIdentification <AcctId> [0..1] ± 667
27.4.2.1  ReservationIdentification <RsvatnId>
Presence: [0..1]
Definition: Unique identification of the reservation.
Datatype: "Max35Text" on page 889
27.4.2.2  SystemIdentification <SysId>
Presence: [0..1]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
27.4.2.3  Type <Tp>
Presence: [1..1]
Approved by the Payments SEG on 04 February 2025 camt.049.001.07 DeleteReservationV07
Cash Management - Maintenance 2024 - 2025 665 February 2025
```

