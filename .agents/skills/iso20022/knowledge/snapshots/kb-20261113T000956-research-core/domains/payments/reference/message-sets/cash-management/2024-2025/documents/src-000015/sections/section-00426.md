---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["21 camt.023.001.07 BackupPaymentV07", "21.4 Message Building Blocks", "21.4.3 InstructionInformation <InstrInf>"]
file_pages: [581, 582]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.023.001.07"]
---

# 21.4.3 InstructionInformation <InstrInf>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 581 to 582.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 581

```text
OriginalMessageIdentification <OrgnlMsgId> contains the following elements (see
"MessageHeader1" on page 811 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 812
   CreationDateTime <CreDtTm> [0..1] DateTime 812
21.4.3 InstructionInformation <InstrInf>
Presence: [0..1]
Definition: Provides details on the execution and type of payment contained in the instruction.
InstructionInformation <InstrInf> contains the following PaymentInstruction13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RequestedExecutionDateTime <ReqdExctnDtTm> [0..1] DateTime 581
   PaymentType <PmtTp> [0..1]  581
{Or     Code <Cd> [1..1] CodeSet 581
Or}     Proprietary <Prtry> [1..1] Text 583
21.4.3.1  RequestedExecutionDateTime <ReqdExctnDtTm>
Presence: [0..1]
Definition: Date at which the initiating party requests that the payment instruction be processed.
.
Datatype: "ISODateTime" on page 883
21.4.3.2  PaymentType <PmtTp>
Presence: [0..1]
Definition: Type, or nature, of the payment, for example an express payment.
PaymentType <PmtTp> contains one of the following PaymentType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 581
Or}   Proprietary <Prtry> [1..1] Text 583
21.4.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Type, or nature, of the payment, such as express payment.
.
Datatype: "PaymentType3Code" on page 863
Approved by the Payments SEG on 04 February 2025 camt.023.001.07 BackupPaymentV07
Cash Management - Maintenance 2024 - 2025 581 February 2025
```

## File page 582

```text
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
Approved by the Payments SEG on 04 February 2025 camt.023.001.07 BackupPaymentV07
Cash Management - Maintenance 2024 - 2025 582 February 2025
```

