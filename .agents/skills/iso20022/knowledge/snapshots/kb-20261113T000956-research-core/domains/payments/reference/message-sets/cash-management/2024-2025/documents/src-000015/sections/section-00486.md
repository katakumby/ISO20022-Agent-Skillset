---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["25 camt.047.001.08 ReturnReservationV08", "25.4 Message Building Blocks", "25.4.2 ReportOrError <RptOrErr>", "25.4.2.1 BusinessReport <BizRpt>", "25.4.2.1.2 DefaultReservation <DfltRsvatn>", "25.4.2.1.2.1 ReservationIdentification <RsvatnId>"]
file_pages: [648]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.047.001.08"]
---

# 25.4.2.1.2.1 ReservationIdentification <RsvatnId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 648 to 648.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 648

```text
DefaultReservation <DfltRsvatn> contains the following ReservationReport8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReservationIdentification <RsvatnId> [1..1]  648
     ReservationIdentification <RsvatnId> [0..1] Text 648
     SystemIdentification <SysId> [0..1] ± 649
     Type <Tp> [1..1]  649
{Or       Code <Cd> [1..1] CodeSet 649
Or}       Proprietary <Prtry> [1..1] Text 649
     AccountOwner <AcctOwnr> [0..1] ± 649
     AccountIdentification <AcctId> [0..1] ± 650
   ReservationOrError <RsvatnOrErr> [1..1]  650
{Or     Reservation <Rsvatn> [1..1] ± 651
Or}     BusinessError <BizErr> [1..*]  651
       Error <Err> [1..1]  651
{Or         Code <Cd> [1..1] CodeSet 652
Or}         Proprietary <Prtry> [1..1] Text 652
       Description <Desc> [0..1] Text 652
25.4.2.1.2.1  ReservationIdentification <RsvatnId>
Presence: [1..1]
Definition: Identification of the reservation on which information is requested.
ReservationIdentification <RsvatnId> contains the following ReservationIdentification4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReservationIdentification <RsvatnId> [0..1] Text 648
   SystemIdentification <SysId> [0..1] ± 649
   Type <Tp> [1..1]  649
{Or     Code <Cd> [1..1] CodeSet 649
Or}     Proprietary <Prtry> [1..1] Text 649
   AccountOwner <AcctOwnr> [0..1] ± 649
   AccountIdentification <AcctId> [0..1] ± 650
25.4.2.1.2.1.1  ReservationIdentification <RsvatnId>
Presence: [0..1]
Definition: Unique identification of the reservation.
Approved by the Payments SEG on 04 February 2025 camt.047.001.08 ReturnReservationV08
Cash Management - Maintenance 2024 - 2025 648 February 2025
```

