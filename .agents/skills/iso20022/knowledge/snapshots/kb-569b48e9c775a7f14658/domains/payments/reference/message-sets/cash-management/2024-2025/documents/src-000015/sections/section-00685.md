---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.42 PaymentType3Code"]
file_pages: [863, 864]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.42 PaymentType3Code

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 863 to 864.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 863

```text
CodeName Name Definition
the system, such as the liquidity
transfers ormanagement of standing
instructions for liquidity control.
LMMG LimitManager Party in a financial institution responsible
for the management of the limits. This
party is responsible for fixing, modifying,
or suspending limits as relevant for the
management of counterpart risk or
systemic risk containment.
PYMG PaymentManager Party in a financial institution responsible
for the management of payment
processing for the financial institution.
This includes authorising, recycling, and
modification of payment transactions.
REDR Reader Party in a financial institution entitled to
obtain information from the system, but
not act upon/alter this information.
BKMG BackupManager Party responsible for managing the
recovery functions related to a system.
STMG SettlementManager Party in a financial institution responsible
for the management of settlement
processing.
37.2.2.42  PaymentType3Code
Definition: Specifies the type, or nature, of the payment.
Type: CodeSet
CodeName Name Definition
CBS CrossBorderPayment Payment has an origin in one country, a
destination in another, and is made in
the currency of either the origin or
destination country.
BCK BackUp Payment is made under the recovery
procedure to move liquidity to/from the
settlement account of a member
according to the specifications of the
system.
BAL BalanceRetail Transaction is a payment offsetting the
net cash balance owed/due in a retail
payment system.
CLS CLSPayment Payment is linked to CLS activities.
CTR CentralBankOperation Payment is made to settle an operation
made with the central bank.
CBH CrossBorderHighValuePayment Transaction is a high value payment that
has an origin in one country and a
destination in another country and is
made in the currency of either the origin
or destination country.
CBP CrossBorderPriorityPayment Transaction is a priority payment that
has an origin in one country and a
destination in another and is made in the
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 863 February 2025
```

## File page 864

```text
CodeName Name Definition
currency of either the origin or
destination country.
DPG DVPGross Gross cash payment offsetting the
amount owed/due for a securities
transaction settlement.
DPN DVPNet Net payment offsetting the cash balance
due/owed for a series of securities
transactions settlement.
EXP ExpressPayment Transaction is a payment that is
processed whenever liquidity is available
on the settlement account of a member
of the RTGSPlus system.
TCH ThirdCurrencyHighValuePayment Transaction is a high value payment that
is made in a third currency to the origin
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
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 864 February 2025
```

