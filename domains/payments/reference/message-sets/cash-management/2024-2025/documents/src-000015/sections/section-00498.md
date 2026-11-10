---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["26 camt.048.001.07 ModifyReservationV07", "26.4 Message Building Blocks", "26.4.2 ReservationIdentification <RsvatnId>", "26.4.2.2 Default <Dflt>", "26.4.2.2.1 ReservationIdentification <RsvatnId>"]
file_pages: [660]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.048.001.07"]
---

# 26.4.2.2.1 ReservationIdentification <RsvatnId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 660 to 660.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 660

```text
Default <Dflt> contains the following ReservationIdentification4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReservationIdentification <RsvatnId> [0..1] Text 660
   SystemIdentification <SysId> [0..1] ± 660
   Type <Tp> [1..1]  660
{Or     Code <Cd> [1..1] CodeSet 660
Or}     Proprietary <Prtry> [1..1] Text 661
   AccountOwner <AcctOwnr> [0..1] ± 661
   AccountIdentification <AcctId> [0..1] ± 661
26.4.2.2.1  ReservationIdentification <RsvatnId>
Presence: [0..1]
Definition: Unique identification of the reservation.
Datatype: "Max35Text" on page 889
26.4.2.2.2  SystemIdentification <SysId>
Presence: [0..1]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
26.4.2.2.3  Type <Tp>
Presence: [1..1]
Definition: Nature of the reservation.
Type <Tp> contains one of the following ReservationType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 660
Or}   Proprietary <Prtry> [1..1] Text 661
26.4.2.2.3.1  Code <Cd>
Presence: [1..1]
Definition: Liquidity transfer request type, in a coded form.
Datatype: "ExternalReservationType1Code" on page 856
Approved by the Payments SEG on 04 February 2025 camt.048.001.07 ModifyReservationV07
Cash Management - Maintenance 2024 - 2025 660 February 2025
```

