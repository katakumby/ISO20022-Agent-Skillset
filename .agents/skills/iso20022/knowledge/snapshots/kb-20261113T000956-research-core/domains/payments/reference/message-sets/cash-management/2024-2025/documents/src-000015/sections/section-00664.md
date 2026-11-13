---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.15 Reservation"]
file_pages: [841]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.15 Reservation

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 841 to 841.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 841

```text
Constraints
• StreetNameAndOrPostOfficeBoxRule
If StreetName is not present, then PostOfficeBox is mandatory. If StreetName is present, then
PostOfficeBox is optional.
37.1.15 Reservation
37.1.15.1  Reservation4
Definition: Liquidity set aside by the account owner for specific purposes.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StartDateTime <StartDtTm> [0..1] ± 841
   Amount <Amt> [1..1] ± 841
37.1.15.1.1  StartDateTime <StartDtTm>
Presence: [0..1]
Definition: Date and time at which the reservation becomes effective.
StartDateTime <StartDtTm> contains one of the following elements (see "DateAndDateTime2Choice"
on page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 801
Or}   DateTime <DtTm> [1..1] DateTime 801
37.1.15.1.2  Amount <Amt>
Presence: [1..1]
Definition: Amount of money of the limit, expressed in an eligible currency.
Amount <Amt> contains one of the following elements (see "Amount2Choice" on page 788 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
37.1.15.2  Reservation3
Definition: Liquidity set aside by the account owner for specific purposes.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 841 February 2025
```

