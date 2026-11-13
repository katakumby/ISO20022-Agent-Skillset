---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.35 Instruction1Code"]
file_pages: [859, 860]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.35 Instruction1Code

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 859 to 860.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 859

```text
37.2.2.35  Instruction1Code
Definition: Specifies further instructions concerning the processing of a payment instruction, provided by
the sending clearing agent to the next agent(s).
Type: CodeSet
CodeName Name Definition
PBEN PayTheBeneficiary (Ultimate) creditor to be paid only after
verification of identity.
TTIL TimeTill Payment instruction is valid and eligible
for execution until the date and time
stipulated. Otherwise, the payment
instruction will be rejected.
TFRO TimeFrom Payment instruction will be valid and
eligible for execution from the date and
time stipulated.
37.2.2.36  LimitStatus1Code
Definition: Specifies the current status of a limit.
Type: CodeSet
CodeName Name Definition
ENAB Enabled Limit is currently in effect.
DISA Disabled Limit is not currently in effect.
DELD Deleted Limit has been deleted or suspended.
REQD Requested Limit has been asked for and is not yet
enabled.
37.2.2.37  LimitType3Code
Definition: Specifies the type of risk management limit.
Type: CodeSet
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
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 859 February 2025
```

## File page 860

```text
CodeName Name Definition
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
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 860 February 2025
```

