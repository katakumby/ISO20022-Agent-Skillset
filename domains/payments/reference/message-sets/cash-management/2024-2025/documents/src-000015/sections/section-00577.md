---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["33 camt.101.001.02 CreateLimitV02", "33.4 Message Building Blocks", "33.4.2 LimitData <LmtData>", "33.4.2.1 LimitIdentification <LmtId>", "33.4.2.1.3 Type <Tp>"]
file_pages: [750, 751]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.101.001.02"]
---

# 33.4.2.1.3 Type <Tp>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 750 to 751.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 750

```text
33.4.2.1.3  Type <Tp>
Presence: [1..1]
Definition: Nature of the risk management limit.
Type <Tp> contains one of the following LimitType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 750
Or}   Proprietary <Prtry> [1..1] Text 752
33.4.2.1.3.1  Code <Cd>
Presence: [1..1]
Definition: Type of the limit, in a coded form.
Datatype: "LimitType3Code" on page 859
CodeName Name Definition
MULT Multilateral Limit is a maximum amount value
applied to, or by, a participant to a set of
counterparties. The multilateral limit is
taken into account by the transaction
administrator to contain the risk in the
system. With the help of the multilateral
limit, the direct participant restricts the
use of liquidity when clearing payments
with all other direct participants for which
no bilateral limit is set.
BILI Bilateral Limit is applied by one party to a specific
counterparty, and corresponds to the
maximum amount of traffic party setting
the limit can send to that counterparty.
The limit can be expressed as a debit or
a credit limit. With the help of a bilateral
limit, the direct participant restricts the
use of liquidity when clearing payments
with another direct participant.
MAND MandatoryBilateral Mandatory part of the bilateral limit
applied by one party to a specific
counterparty, and corresponds to the
maximum amount of traffic party setting
the limit can send to that counterparty.
The limit can be expressed as a debit or
a credit limit. With the help of a bilateral
limit, the direct participant restricts the
use of liquidity when clearing payments
with another direct participant.
DISC DiscretionaryBilateral Discretionary part of the bilateral limit
applied by one party to a specific
counterparty, and corresponds to the
maximum amount of traffic party setting
the limit can send to that counterparty.
The limit can be expressed as a debit or
a credit limit. With the help of a bilateral
limit, the direct participant restricts the
use of liquidity when clearing payments
with another direct participant.
Approved by the Payments SEG on 04 February 2025 camt.101.001.02 CreateLimitV02
Cash Management - Maintenance 2024 - 2025 750 February 2025
```

## File page 751

```text
CodeName Name Definition
NELI NetBilateral Limit is applied by one party to a specific
counterparty, and corresponds to the
maximum net balance acceptable by the
party that is setting the limit. The limit is
calculated as an arithmetic sum in value
of the bilateral flows exchanged between
the two parties. The net bilateral limit can
be expressed as a debit or a credit
balance.
INBI IndirectBilateral Limit is a maximum value set by a direct
participant with respect to its indirect
participant. The limit represents the
maximum amount the indirect participant
can use to settle its operations.
GLBL Global Maximum value set by either the
transaction administrator or by a
member for the participation of a
member in the system. The global limit
may be expressed as a credit or debit
maximum value and is taken into
account by the transaction administrator
when processing transaction inside the
system. With the help of the global limit,
the direct participant may limit the use of
liquidity when clearing specific type of
payments.
DIDB DirectDebit Limit not to be exceeded for direct debit
operations.
SPLC SingleCustomerDirectDebit Single direct debit payment limit not to
be exceeded by any single direct debit
transaction by a customer.
SPLF SingleFinancialInstitutionDirectDebit Single direct debit payment limit not to
be exceeded by any single direct debit
transaction initiated by a financial
institution.
TDLC TotalDailyCustomerDirectDebit Total daily payments limit for customer
direct debits not to be exceeded by the
total of all direct debit transactions
initiated by customers.
TDLF TotalDailyFinancialInstitutionDirectDebit Total daily payments limit for financial
institutions direct debits not to be
exceeded by the total of all direct debit
transactions initiated by financial
institutions.
UCDT UnsecuredCredit Limit is related to a cap amount granted
by a national central bank or a
settlement bank, but generally
unsecured outside of the market
infrastructure.
ACOL AutoCollateralisation Limit is related to a credit operation that
is or can be triggered when a buyer does
not have a sufficient amount of money to
settle a securities transaction in order to
improve its cash position for the next
settlement cycle. The credit provided can
be secured using securities already held
by the buyer ("collateral stocks") or the
Approved by the Payments SEG on 04 February 2025 camt.101.001.02 CreateLimitV02
Cash Management - Maintenance 2024 - 2025 751 February 2025
```

