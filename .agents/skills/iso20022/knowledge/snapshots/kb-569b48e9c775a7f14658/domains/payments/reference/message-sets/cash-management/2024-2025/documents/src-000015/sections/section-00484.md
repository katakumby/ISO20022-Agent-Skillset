---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["25 camt.047.001.08 ReturnReservationV08", "25.4 Message Building Blocks", "25.4.2 ReportOrError <RptOrErr>", "25.4.2.1 BusinessReport <BizRpt>", "25.4.2.1.1 CurrentReservation <CurRsvatn>", "25.4.2.1.1.2 ReservationOrError <RsvatnOrErr>", "25.4.2.1.1.2.1 Reservation <Rsvatn>"]
file_pages: [646]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.047.001.08"]
---

# 25.4.2.1.1.2.1 Reservation <Rsvatn>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 646 to 646.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 646

```text
ReservationOrError <RsvatnOrErr> contains one of the following ReservationOrError9Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reservation <Rsvatn> [1..1] ± 646
Or}   BusinessError <BizErr> [1..*]  646
     Error <Err> [1..1]  646
{Or       Code <Cd> [1..1] CodeSet 647
Or}       Proprietary <Prtry> [1..1] Text 647
     Description <Desc> [0..1] Text 647
25.4.2.1.1.2.1  Reservation <Rsvatn>
Presence: [1..1]
Definition: Requested information on the limit.
Reservation <Rsvatn> contains the following elements (see "Reservation3" on page 841 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] ± 842
   Status <Sts> [0..1]  842
{Or     Code <Cd> [1..1] CodeSet 842
Or}     Proprietary <Prtry> [1..1] Text 843
   StartDateTime <StartDtTm> [0..1] ± 843
25.4.2.1.1.2.2  BusinessError <BizErr>
Presence: [1..*]
Definition: Reason the requested business information is not given.
BusinessError <BizErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  646
{Or     Code <Cd> [1..1] CodeSet 647
Or}     Proprietary <Prtry> [1..1] Text 647
   Description <Desc> [0..1] Text 647
25.4.2.1.1.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Approved by the Payments SEG on 04 February 2025 camt.047.001.08 ReturnReservationV08
Cash Management - Maintenance 2024 - 2025 646 February 2025
```

