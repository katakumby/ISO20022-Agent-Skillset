---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["26 camt.048.001.07 ModifyReservationV07", "26.4 Message Building Blocks", "26.4.2 ReservationIdentification <RsvatnId>", "26.4.2.1 Current <Cur>", "26.4.2.1.1 ReservationIdentification <RsvatnId>"]
file_pages: [658]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.048.001.07"]
---

# 26.4.2.1.1 ReservationIdentification <RsvatnId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 658 to 658.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 658

```text
26.4.2.1.1  ReservationIdentification <RsvatnId>
Presence: [0..1]
Definition: Unique identification of the reservation.
Datatype: "Max35Text" on page 889
26.4.2.1.2  SystemIdentification <SysId>
Presence: [0..1]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
26.4.2.1.3  Type <Tp>
Presence: [1..1]
Definition: Nature of the reservation.
Type <Tp> contains one of the following ReservationType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 658
Or}   Proprietary <Prtry> [1..1] Text 658
26.4.2.1.3.1  Code <Cd>
Presence: [1..1]
Definition: Liquidity transfer request type, in a coded form.
Datatype: "ExternalReservationType1Code" on page 856
26.4.2.1.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Liquidity transfer request type, in a proprietary form.
Datatype: "Max35Text" on page 889
26.4.2.1.4  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Owner of the account which is being queried.
Approved by the Payments SEG on 04 February 2025 camt.048.001.07 ModifyReservationV07
Cash Management - Maintenance 2024 - 2025 658 February 2025
```

