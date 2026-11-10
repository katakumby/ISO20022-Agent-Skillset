---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.2 Agreement", "7.1.2.1 Agreement5", "7.1.2.1.6 DeliveryType <DlvryTp>"]
file_pages: [227]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.2.1.6 DeliveryType <DlvryTp>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 227 to 227.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 227

```text
7.1.2.1.6  DeliveryType <DlvryTp>
Presence: [0..1]
Definition: Identifies type of settlement.
Datatype: "DeliveryType2Code" on page 623
CodeName Name Definition
APMT AgainstPayment Indicates that the delivery is against
payment.
FREE Free Indicates the delivery is free of payment.
TRIP Triparty Indicates that a custodian bank or
international clearing organization acts
as an intermediary between the two
parties to the repo.
HOIC HoldInCustody Indicates that the collateral pledged by
the (cash) borrower is not actually
delivered to the cash lender. Rather, it is
placed in an internal account ("held in
custody") by the borrower, for the lender,
throughout the duration of the trade.
7.1.2.1.7  MarginRatio <MrgnRatio>
Presence: [0..1]
Definition: Fraction of the cash consideration that must be collateralized, expressed as a percent. A
margin ratio of 02% indicates that the value of the collateral (after deducting for "haircut") must exceed
the cash consideration by 2%.
Datatype: "PercentageRate" on page 667
7.1.3 Amount
7.1.3.1  AmountAndDirection5
Definition: Amount of money debited or credited on the books of an account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 227
   CreditDebit <CdtDbt> [0..1] CodeSet 228
7.1.3.1.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money that is debited or credited.
Impacted by: C1 "ActiveCurrency", C9 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 611
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 227 February 2025
```

