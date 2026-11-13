---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.15 Reservation", "37.1.15.2 Reservation3", "37.1.15.2.1 Amount <Amt>"]
file_pages: [842]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.15.2.1 Amount <Amt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 842 to 842.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 842

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 842
   Status <Sts> [0..1]  842
{Or     Code <Cd> [1..1] CodeSet 842
Or}     Proprietary <Prtry> [1..1] Text 843
   StartDateTime <StartDtTm> [0..1] ± 843
37.1.15.2.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money of the limit, expressed in an eligible currency.
Amount <Amt> contains one of the following elements (see "Amount2Choice" on page 788 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
37.1.15.2.2  Status <Sts>
Presence: [0..1]
Definition: Status of the limit, such as enabled or disabled.
Status <Sts> contains one of the following ReservationStatus1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 842
Or}   Proprietary <Prtry> [1..1] Text 843
37.1.15.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Liquidity transfer request type, in a coded form.
Datatype: "ReservationStatus1Code" on page 873
CodeName Name Definition
ENAB Enabled Reservation is currently in effect.
DISA Disabled Reservation is not currently in effect.
.
DELD Deleted Reservation has been deleted or
suspended.
REQD Requested Reservation has been asked for and is
not yet enabled.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 842 February 2025
```

