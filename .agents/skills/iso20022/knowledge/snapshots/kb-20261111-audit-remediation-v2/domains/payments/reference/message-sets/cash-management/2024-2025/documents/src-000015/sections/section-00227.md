---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 camt.007.001.10 ModifyTransactionV10", "6.4 Message Building Blocks", "6.4.2 Modification <Mod>", "6.4.2.2 NewPaymentValueSet <NewPmtValSet>", "6.4.2.2.2 Type <Tp>", "6.4.2.2.2.2 Proprietary <Prtry>"]
file_pages: [344]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.007.001.10"]
---

# 6.4.2.2.2.2 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 344 to 344.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 344

```text
CodeName Name Definition
and destination countries. The origin and
destination countries may be one and
the same country.
LMT LimitPayment Transaction is a payment that is
processed when the pool of liquidity
exceeds the minimum value reserved for
an express payment in the RTGSPlus
system.
LIQ LiquidityTransfer Payment is made to transfer liquidity to/
from the settlement account of a
member, to/from the current account
held at the central institution or any other
institution.
DPP DomesticPriorityPayment Transaction is a priority payment that
has an origin and a destination in the
same country and is made in the
currency of that country.
DPH DomesticHighValuePayment Transaction is a high value payment that
has an origin and a destination in the
same country and is made in the
currency of that country.
DPS DomesticPayment Payment has an origin and a destination
in the same country, and is made in the
currency of that country.
STF StandingFacilities Payment is linked to overnight deposits
and the marginal lending facility.
TRP TreasuryStatePayment Payment is linked to the Treasury State.
TCS ThirdCurrencyPayment Transaction is a payment that is made in
a third currency to the origin and
destination countries. The origin and
destination countries may be one and
the same country.
LOA Loan Transaction is the payment of a specific
amount of money lent by a creditor/
lender.
LOR LoanRepayment Transaction is an amount of money
transferred in repayment of loan.
TCP ThirdCurrencyPriorityPayment Payment is made in a third currency to
the origin and destination countries. The
origin and destination countries may be
the same country.
OND OvernightDeposit Transaction is linked to an overnight
deposit.
MGL MarginalLending Transaction is linked to the marginal
lending facility.
6.4.2.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Payment type that is not included in a predefined list.
Datatype: "Max35Text" on page 889
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 344 February 2025
```

