---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.6 TaxExemptionReason2Choice", "66.1.47.6.1 Code <Cd>"]
file_pages: [5251, 5252, 5253]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.6.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5251 to 5253.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5251

```text
66.1.47.6.1  Code <Cd>
Presence: [1..1]
Definition: Tax exemption reason expressed as a code.
Datatype: "TaxExemptReason3Code" on page 5370
CodeName Name Definition
NONE None Account is not tax exempt.
MASA MaxiISA Maxi Individual Savings Account (ISA).
Account is an ISA with a single ISA
manager that may contain cash, stocks
and shares, investment funds and life
assurance up to the prescribed annual
subscription limit (required for UK). The
Maxi ISA allows an investor to save all
three of the different elements of ISA
investments that are allowed, with one
savings institution in a single account.
MISA MiniCashISA Mini Cash Individual Savings Account
(ISA). Account is an ISA with a single
ISA manager that may contain cash,
stocks and shares, investment funds and
life assurance up to the prescribed
annual subscription limit (required for
UK). An investor can hold more than one
Mini ISA to utilise the overall Mini ISA
investment limit, and can invest with
more than one savings institution,
however only one of the three elements
of ISA investment is allowed in a single
account.
SISA MiniStocksAndSharesISA Mini Stocks and Shares Individual
Savings Account (ISA). Account is an
ISA with an ISA manager that may only
contain stocks, shares and collective
investments up to the prescribed annual
subscription limit (required for UK).
IISA MiniInsuranceISA Mini Insurance Individual Savings
Account (ISA). Account is an ISA with an
ISA manager that may only contain life
insurance investments up to the
prescribed annual subscription limit
(required for UK).
CUYP CurrentYearPayment Account is for current year payments into
an investment retirement account
(required for US).
PRYP PriorYearPayment Account is for a prior year payment into
an investment retirement account
(required for US).
ASTR AssetTransfer Account is for an asset transfer into an
investment retirement account (required
for US).
EMPY EmployeePriorYear Account is for employee - prior year
contributions into an investment
retirement account (required for US).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5251 May 2026
```

## File page 5252

```text
CodeName Name Definition
EMCY EmployeeCurrentYear Account is for employee - current year
contributions into an investment
retirement account (required for US).
EPRY EmployerPriorYear Account is for employer - prior year
contributions into an investment
retirement account (required for US).
ECYE EmployerCurrentYear Account is for employer - current year
contributions into an investment
retirement account (required for US).
NFPI NonFundPrototypeIRA Account is for non-fund prototype
Individual Retirement Account (IRA) into
an investment retirement account
(required for US).
NFQP NonFundQualifiedPlan Account is for non-fund qualified plan
into an investment retirement account
(required for US).
DECP DefinedContributionPlan Account is for a defined contribution plan
(required for US).
IRAC IndividualRetirementAccount Account is an Individual Retirement
Account (IRA) (required for US).
IRAR IndividualRetirementAccountRollover Account is for an Individual Retirement
Account (IRA) - Rollover (required for
US).
KEOG KEOGH KEOGH. Account is a tax-deferred
retirement plan designed to help self-
employed workers or individuals who
earn self-employed income establish a
retirement savings program (required for
US).
PFSP ProfitSharingPlan Account is a Profit Sharing Plan
(required for US).
401K FourHundredAndOneK 401k. Account is an optional retirement
plan supported by many companies, in
which income is invested before it is
taxed (required for US).
SIRA SelfDirectedIRA Self-Directed Individual Retirement
Account (IRA) (required for US).
403B FourHundredAndThreeB 403(b). Account is a tax-deferred
investment and savings program for
employees of hospitals, educational
institutions and other non-profit
organisations, to save and invest in their
own retirement. The name refers to the
relevant section in the US Internal
Revenue Code (required for US).
457X FourHundredFiftySeven 457. Account is a non-qualified deferred
compensation program that is available
to state and local governments and not-
for-profit employers (required for US).
RIRA RothIRAFundPrototype Roth Individual Retirement Account
(IRA) Fund Prototype. Account is a tax-
deferred retirement account based on
the reverse principle of a traditional IRA.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5252 May 2026
```

## File page 5253

```text
CodeName Name Definition
Retirement contributions are taxed
upfront, but withdrawals may be made
tax-free when a certain age is reached,
provided the Roth IRA has been set up
for a certain period of time (required for
US).
RIAN RothIRANonPrototype Roth Individual Retirement Account
(IRA) Non-Prototype. Account is a tax-
deferred retirement account based on
the reverse principle of a traditional IRA.
Retirement contributions are taxed
upfront, but withdrawals may be made
tax-free when a certain age is reached,
provided the Roth IRA has been set up
for a certain period of time (required for
US).
RCRF RothConversionIRAFundPrototype Roth Conversion Individual Retirement
Account (IRA) Fund Prototype. Account
is a retirement account established when
a party switches from a regular IRA
( required for US).
RCIP RothConversionIRANonPrototype Roth Conversion Individual Retirement
Account (IRA) Non-Prototype. Account is
a retirement account established when a
party switches from a Regular IRA
(required for US).
EIFP EducationIRAFundPrototype Education Individual Retirement Account
Fund Prototype (also known as an
Education Savings Account). Account is
a savings plan open to anyone under the
age of 18. When the account owner
withdraws money to pay for qualified
higher education expenses, the
withdrawals are generally tax-free
(required for US).
EIOP EducationIRANonPrototype Education Individual Retirement Account
Non-Prototype (also known as an
Education Savings Account). Account is
a savings plan open to anyone under the
age of 18. When the account owner
withdraws money to pay for qualified
higher education expenses, the
withdrawals are generally tax-free
(required in the US).
FORE Foreigner Account is for a foreigner for which a tax
exemption is permitted.
INCA Incapacity Exemption due to incapacitation.
MINO Minor Account is for a minor for which a tax
exemption is permitted.
ASSO Association Account is for an association, for
example, a sports club, for which a tax
exemption is permitted.
DIPL Diplomat Account is for a diplomat for which a tax
exemption is permitted.
DOME Domestic Account is for two account owners that
are both domestic.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5253 May 2026
```

