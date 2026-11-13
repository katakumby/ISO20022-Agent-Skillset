---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["26 camt.048.001.07 ModifyReservationV07", "26.4 Message Building Blocks", "26.4.2 ReservationIdentification <RsvatnId>", "26.4.2.1 Current <Cur>"]
file_pages: [657]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.048.001.07"]
---

# 26.4.2.1 Current <Cur>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 657 to 657.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 657

```text
ReservationIdentification <RsvatnId> contains one of the following
CurrentOrDefaultReservation4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Current <Cur> [1..1]  657
     ReservationIdentification <RsvatnId> [0..1] Text 658
     SystemIdentification <SysId> [0..1] ± 658
     Type <Tp> [1..1]  658
{Or       Code <Cd> [1..1] CodeSet 658
Or}       Proprietary <Prtry> [1..1] Text 658
     AccountOwner <AcctOwnr> [0..1] ± 658
     AccountIdentification <AcctId> [0..1] ± 659
Or}   Default <Dflt> [1..1]  659
     ReservationIdentification <RsvatnId> [0..1] Text 660
     SystemIdentification <SysId> [0..1] ± 660
     Type <Tp> [1..1]  660
{Or       Code <Cd> [1..1] CodeSet 660
Or}       Proprietary <Prtry> [1..1] Text 661
     AccountOwner <AcctOwnr> [0..1] ± 661
     AccountIdentification <AcctId> [0..1] ± 661
26.4.2.1  Current <Cur>
Presence: [1..1]
Definition: Identification of the current reservation.
Current <Cur> contains the following ReservationIdentification4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReservationIdentification <RsvatnId> [0..1] Text 658
   SystemIdentification <SysId> [0..1] ± 658
   Type <Tp> [1..1]  658
{Or     Code <Cd> [1..1] CodeSet 658
Or}     Proprietary <Prtry> [1..1] Text 658
   AccountOwner <AcctOwnr> [0..1] ± 658
   AccountIdentification <AcctId> [0..1] ± 659
Approved by the Payments SEG on 04 February 2025 camt.048.001.07 ModifyReservationV07
Cash Management - Maintenance 2024 - 2025 657 February 2025
```

