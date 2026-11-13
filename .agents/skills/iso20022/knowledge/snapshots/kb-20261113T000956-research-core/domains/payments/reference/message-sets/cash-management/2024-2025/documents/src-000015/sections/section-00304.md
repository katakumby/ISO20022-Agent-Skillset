---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["10 camt.011.001.08 ModifyLimitV08", "10.4 Message Building Blocks", "10.4.2 LimitDetails <LmtDtls>", "10.4.2.1 LimitIdentification <LmtId>", "10.4.2.1.3 AllCurrent <AllCur>", "10.4.2.1.3.1 SystemIdentification <SysId>"]
file_pages: [439, 440]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.011.001.08"]
---

# 10.4.2.1.3.1 SystemIdentification <SysId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 439 to 440.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 439

```text
AllCurrent <AllCur> contains the following LimitIdentification9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [0..1] ± 439
   Type <Tp> [1..1]  439
{Or     Code <Cd> [1..1] CodeSet 439
Or}     Proprietary <Prtry> [1..1] Text 441
   AccountOwner <AcctOwnr> [0..1] ± 441
   AccountIdentification <AcctId> [0..1] ± 442
10.4.2.1.3.1  SystemIdentification <SysId>
Presence: [0..1]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
10.4.2.1.3.2  Type <Tp>
Presence: [1..1]
Definition: Nature of the risk management limit.
Type <Tp> contains one of the following LimitType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 439
Or}   Proprietary <Prtry> [1..1] Text 441
10.4.2.1.3.2.1  Code <Cd>
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
Approved by the Payments SEG on 04 February 2025 camt.011.001.08 ModifyLimitV08
Cash Management - Maintenance 2024 - 2025 439 February 2025
```

## File page 440

```text
CodeName Name Definition
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
Approved by the Payments SEG on 04 February 2025 camt.011.001.08 ModifyLimitV08
Cash Management - Maintenance 2024 - 2025 440 February 2025
```

