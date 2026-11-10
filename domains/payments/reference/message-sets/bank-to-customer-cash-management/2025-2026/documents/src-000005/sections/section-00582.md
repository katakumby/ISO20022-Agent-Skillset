---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.4 Amount Range", "6.1.4.3 AmountRangeBoundary1"]
file_pages: [815]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.4.3 AmountRangeBoundary1

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 815 to 815.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 815

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
6.1.4.3  AmountRangeBoundary1
Definition: Limit for an amount range.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 815
   Included <Incl> [1..1] Indicator 815
6.1.4.3.1  BoundaryAmount <BdryAmt>
Presence: [1..1]
Definition: Amount value of the range limit.
Datatype: "ImpliedCurrencyAndAmount" on page 886
6.1.4.3.2  Included <Incl>
Presence: [1..1]
Definition: Indicates whether the boundary amount is included in the range of amount values.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 911):
• Meaning When True: Yes
• Meaning When False: No
6.1.5 Balance
6.1.5.1  CreditLine3
Definition: Set of elements used to provide details of the credit line.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Included <Incl> [1..1] Indicator 815
   Type <Tp> [0..1]  816
{Or     Code <Cd> [1..1] CodeSet 816
Or}     Proprietary <Prtry> [1..1] Text 816
   Amount <Amt> [0..1] Amount C1, C5 816
   Date <Dt> [0..1] ± 816
6.1.5.1.1  Included <Incl>
Presence: [1..1]
Definition: Indicates whether or not the credit line is included in the balance.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 911):
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
815 March 2026
```

