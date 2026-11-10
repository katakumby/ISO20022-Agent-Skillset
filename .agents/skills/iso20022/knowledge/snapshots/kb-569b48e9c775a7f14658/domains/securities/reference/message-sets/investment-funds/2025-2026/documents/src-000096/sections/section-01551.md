---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.15 TransactionOverhead <TxOvrhd>", "44.4.4.9.15.3 IndividualTax <IndvTax>", "44.4.4.9.15.3.2 Tax <Tax>", "44.4.4.9.15.3.2.2 Rate <Rate>"]
file_pages: [2176, 2177, 2178]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.15.3.2.2 Rate <Rate>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2176 to 2178.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2176

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
44.4.4.9.15.3.2.2  Rate <Rate>
Presence: [1..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 5401
44.4.4.9.15.3.3  Country <Ctry>
Presence: [0..1]
Definition: Country where the tax is due.
Impacted by: C8 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
44.4.4.9.15.3.4  ExemptionIndicator <XmptnInd>
Presence: [1..1]
Definition: Indicates whether a tax exemption applies.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
44.4.4.9.15.3.5  ExemptionReason <XmptnRsn>
Presence: [0..1]
Definition: Reason for the tax exemption.
ExemptionReason <XmptnRsn> contains one of the following ExemptionReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2176
Or}   Proprietary <Prtry> [1..1] ± 2179
44.4.4.9.15.3.5.1  Code <Cd>
Presence: [1..1]
Definition: Exemption reason expressed as a code.
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2176 May 2026
```

## File page 2177

```text
Datatype: "TaxExemptReason1Code" on page 5367
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
EMCY EmployeeCurrentYear Account is for employee - current year
contributions into an investment
retirement account (required for US).
EPRY EmployerPriorYear Account is for employer - prior year
contributions into an investment
retirement account (required for US).
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2177 May 2026
```

## File page 2178

```text
CodeName Name Definition
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
Retirement contributions are taxed
upfront, but withdrawals may be made
tax-free when a certain age is reached,
provided the Roth IRA has been set up
for a certain period of time (required for
US).
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2178 May 2026
```

