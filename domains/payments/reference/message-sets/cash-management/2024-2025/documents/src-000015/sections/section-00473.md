---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["24 camt.046.001.08 GetReservationV08", "24.4 Message Building Blocks", "24.4.2 ReservationQueryDefinition <RsvatnQryDef>", "24.4.2.2 ReservationCriteria <RsvatnCrit>", "24.4.2.2.2 NewCriteria <NewCrit>", "24.4.2.2.2.2 SearchCriteria <SchCrit>", "24.4.2.2.2.2.3 DefaultReservationType <DfltRsvatnTp>", "24.4.2.2.2.2.3.1 Code <Cd>"]
file_pages: [633]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.046.001.08"]
---

# 24.4.2.2.2.2.3.1 Code <Cd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 633 to 633.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 633

```text
DefaultReservationType <DfltRsvatnTp> contains one of the following ReservationType2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 633
Or}   Proprietary <Prtry> [1..1] Text 633
24.4.2.2.2.2.3.1  Code <Cd>
Presence: [1..1]
Definition: Liquidity transfer request type, in a coded form.
Datatype: "ExternalReservationType1Code" on page 856
24.4.2.2.2.2.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Liquidity transfer request type, in a proprietary form.
Datatype: "Max35Text" on page 889
24.4.2.2.2.2.4  CurrentReservationType <CurRsvatnTp>
Presence: [0..*]
Definition: Type of reservation applied by the system at the present time.
CurrentReservationType <CurRsvatnTp> contains one of the following ReservationType2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 633
Or}   Proprietary <Prtry> [1..1] Text 633
24.4.2.2.2.2.4.1  Code <Cd>
Presence: [1..1]
Definition: Liquidity transfer request type, in a coded form.
Datatype: "ExternalReservationType1Code" on page 856
24.4.2.2.2.2.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Liquidity transfer request type, in a proprietary form.
Datatype: "Max35Text" on page 889
24.4.2.2.2.2.5  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Owner of the account which is being queried.
Approved by the Payments SEG on 04 February 2025 camt.046.001.08 GetReservationV08
Cash Management - Maintenance 2024 - 2025 633 February 2025
```

