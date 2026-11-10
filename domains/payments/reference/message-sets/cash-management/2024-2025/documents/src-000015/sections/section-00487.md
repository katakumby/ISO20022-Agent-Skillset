---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["25 camt.047.001.08 ReturnReservationV08", "25.4 Message Building Blocks", "25.4.2 ReportOrError <RptOrErr>", "25.4.2.1 BusinessReport <BizRpt>", "25.4.2.1.2 DefaultReservation <DfltRsvatn>", "25.4.2.1.2.1 ReservationIdentification <RsvatnId>", "25.4.2.1.2.1.2 SystemIdentification <SysId>"]
file_pages: [649]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.047.001.08"]
---

# 25.4.2.1.2.1.2 SystemIdentification <SysId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 649 to 649.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 649

```text
Datatype: "Max35Text" on page 889
25.4.2.1.2.1.2  SystemIdentification <SysId>
Presence: [0..1]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
25.4.2.1.2.1.3  Type <Tp>
Presence: [1..1]
Definition: Nature of the reservation.
Type <Tp> contains one of the following ReservationType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 649
Or}   Proprietary <Prtry> [1..1] Text 649
25.4.2.1.2.1.3.1  Code <Cd>
Presence: [1..1]
Definition: Liquidity transfer request type, in a coded form.
Datatype: "ExternalReservationType1Code" on page 856
25.4.2.1.2.1.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Liquidity transfer request type, in a proprietary form.
Datatype: "Max35Text" on page 889
25.4.2.1.2.1.4  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Owner of the account which is being queried.
Approved by the Payments SEG on 04 February 2025 camt.047.001.08 ReturnReservationV08
Cash Management - Maintenance 2024 - 2025 649 February 2025
```

