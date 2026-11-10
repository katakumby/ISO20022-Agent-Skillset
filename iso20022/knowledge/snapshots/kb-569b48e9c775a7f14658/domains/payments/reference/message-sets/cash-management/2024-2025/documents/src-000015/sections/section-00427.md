---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["21 camt.023.001.07 BackupPaymentV07", "21.4 Message Building Blocks", "21.4.3 InstructionInformation <InstrInf>", "21.4.3.2 PaymentType <PmtTp>", "21.4.3.2.2 Proprietary <Prtry>"]
file_pages: [583]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.023.001.07"]
---

# 21.4.3.2.2 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 583 to 583.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 583

```text
CodeName Name Definition
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
21.4.3.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Payment type that is not included in a predefined list.
Datatype: "Max35Text" on page 889
21.4.4 TransferredAmount <TrfdAmt>
Presence: [1..1]
Definition: Quantity of cash that the transaction administrator transfers from one account to another.
TransferredAmount <TrfdAmt> contains one of the following elements (see "Amount2Choice" on
page 788 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
Approved by the Payments SEG on 04 February 2025 camt.023.001.07 BackupPaymentV07
Cash Management - Maintenance 2024 - 2025 583 February 2025
```

