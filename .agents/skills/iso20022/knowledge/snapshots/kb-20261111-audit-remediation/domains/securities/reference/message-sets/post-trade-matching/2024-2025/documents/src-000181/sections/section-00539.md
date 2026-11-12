---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.14 CallIn1Code"]
file_pages: [619]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.14 CallIn1Code

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 619 to 619.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 619

```text
CodeName Name Definition
SPLL Simple The yield of a bond assuming no
reinvestment of coupon payments.
(Act/360 day count).
TXQV TaxEquivalent The after tax yield grossed up by the
maximum federal tax rate of 39.6%. For
comparison to taxable yields.
TTDT ToTenderDate The yield on a Municipal bond to its
mandatory tender date.
TRYL True The yield calculated with coupon dates
moved from a weekend or holiday to the
next valid settlement date.
WRST ToWorstConvention The lowest yield to all possible
redemption date scenarios.
7.2.2.14  CallIn1Code
Definition: Specifies the type of pay-in call report.
Type: CodeSet
CodeName Name Definition
CFAV CallForAccountValue Pay-in call is for account value.
CFST CallForSettlement Pay-in call is for settlement.
CFCC CallForCurrencyClose Pay-in call is for currency close.
7.2.2.15  CashMarginOrder1Code
Definition: Identifies whether an order is a non-margin, an opening margin or a closing margin order.
Type: CodeSet
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
7.2.2.16  CashSettlementSystem2Code
Definition: Specifies the cash settlement system used.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 619 February 2025
```

