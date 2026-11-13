---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 camt.007.001.10 ModifyTransactionV10", "6.4 Message Building Blocks", "6.4.2 Modification <Mod>", "6.4.2.2 NewPaymentValueSet <NewPmtValSet>", "6.4.2.2.2 Type <Tp>", "6.4.2.2.2.1 Code <Cd>"]
file_pages: [343]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.007.001.10"]
---

# 6.4.2.2.2.1 Code <Cd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 343 to 343.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 343

```text
Type <Tp> contains one of the following PaymentType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 343
Or}   Proprietary <Prtry> [1..1] Text 344
6.4.2.2.2.1  Code <Cd>
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
EXP ExpressPayment Transaction is a payment that is
processed whenever liquidity is available
on the settlement account of a member
of the RTGSPlus system.
TCH ThirdCurrencyHighValuePayment Transaction is a high value payment that
is made in a third currency to the origin
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 343 February 2025
```

