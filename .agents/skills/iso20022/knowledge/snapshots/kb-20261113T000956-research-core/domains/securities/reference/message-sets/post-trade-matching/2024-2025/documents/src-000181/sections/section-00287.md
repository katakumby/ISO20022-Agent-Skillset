---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.43 Order23", "7.1.19.43.24 TypeOfPrice <TpOfPric>"]
file_pages: [347]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.43.24 TypeOfPrice <TpOfPric>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 347 to 347.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 347

```text
DealPrice <DealPric> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.19.43.24  TypeOfPrice <TpOfPric>
Presence: [0..1]
Definition: Specifies the type of transaction price.
TypeOfPrice <TpOfPric> contains one of the following elements (see "TypeOfPrice47Choice" on
page 506 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 506
Or}   Proprietary <Prtry> [1..1] ± 506
7.1.19.43.25  CashMargin <CshMrgn>
Presence: [0..1]
Definition: Identifies whether an order is a margin order or a non-margin order. This is primarily used
when sending orders to Japanese exchanges to indicate sell margin or buy to cover. The same tag
could be assigned also by buy-side to indicate the intent to sell or buy margin and the sell-side to
accept or reject (base on some validation criteria) the margin request.
Datatype: "CashMarginOrder1Code" on page 619
CodeName Name Definition
CASH Cash The principal owns the cash in case of a
purchase, or the securities in case of a
sale so the execution, if it occurs, will not
generate any margin account opening or
margin call.
MRGO MarginOpen The principal order, if executed, will
generate a margin account opening or
margin call because the principal does
not have the cash in case of a purchase
or the securities in case of a sale.
MRGC MarginClose The principal order, if executed, will
enable the margin position to be closed
and the positions to be covered (for
example: purchase of securities that
have previously been short-sold, or sale
of securities that have been bought on
margin).
7.1.19.43.26  Commission <Comssn>
Presence: [0..1]
Definition: Amount of money due to a party as compensation for a service.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 347 February 2025
```

