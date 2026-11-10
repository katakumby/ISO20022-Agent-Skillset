---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.11 PaymentType <PmtTp>"]
file_pages: [163, 164]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.11 PaymentType <PmtTp>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 163 to 164.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 163

```text
4.4.2.2.2.2.3.11  PaymentType <PmtTp>
Presence: [0..*]
Definition: Instruction to pay an amount of money to an ultimate beneficiary, on behalf of an originator.
This instruction may have to be forwarded several times to complete the settlement chain.
PaymentType <PmtTp> contains one of the following PaymentType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 163
Or}   Proprietary <Prtry> [1..1] Text 165
4.4.2.2.2.2.3.11.1  Code <Cd>
Presence: [1..1]
Definition: Type, or nature, of the payment, such as express payment.
.
Datatype: "PaymentType3Code" on page 863
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
currency of either the origin or
destination country.
DPG DVPGross Gross cash payment offsetting the
amount owed/due for a securities
transaction settlement.
DPN DVPNet Net payment offsetting the cash balance
due/owed for a series of securities
transactions settlement.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 163 February 2025
```

## File page 164

```text
CodeName Name Definition
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
origin and destination countries may be
the same country.
OND OvernightDeposit Transaction is linked to an overnight
deposit.
MGL MarginalLending Transaction is linked to the marginal
lending facility.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 164 February 2025
```

