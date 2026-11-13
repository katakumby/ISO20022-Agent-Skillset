---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.4 Payment <Pmt>", "5.4.2.1.3.2.1.4.11 Type <Tp>", "5.4.2.1.3.2.1.4.11.1 Code <Cd>"]
file_pages: [296]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.4.11.1 Code <Cd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 296 to 296.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 296

```text
.
Type <Tp> contains one of the following PaymentType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 296
Or}   Proprietary <Prtry> [1..1] Text 297
5.4.2.1.3.2.1.4.11.1  Code <Cd>
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
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 296 February 2025
```

