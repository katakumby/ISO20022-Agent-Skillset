---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.118 InvestmentFundPlanType1Code"]
file_pages: [5318, 5319]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.118 InvestmentFundPlanType1Code

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5318 to 5319.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5318

```text
CodeName Name Definition
- 0 at maturity
Then maximum exit cost: 4%.
Typical cost : 0
OTES OneOffTypicalExitCostsStructured One-off typical exit cost linked to the
recommended holding period (RHP) for
a structured product. When used in
reference to MiFID, this is in the scope of
the European MiFID Template (EMT)
reference 07080 and may be specified
as an actual amount or a percentage of
the reference value, EMT reference
07150 or 07155.
OCAS OngoingCostsAccumulatedStructured Sum of daily recurring product costs
accumulated during the year until the ex
post reference date. This is typically
specified as an actual amount. When
used in reference to MiFID, this is in the
scope of the European MiFID Template
(EMT) reference 08040.
RPSS ReferencePrice Reference Price. When used in
reference to MiFID, this is in the scope of
the European MiFID Template (EMT)
reference 07150 and 08110 and is the
instrument price to which a unit
disclosed ex-post cost is based and to
which a percentage disclosed cost
should be multiplied in order to retrieve
the unit cost.
TRS1 TransactionCost Cost associated with the transaction.
When used in reference to MiFID, this is
in the scope of the European MiFID
Template (EMT) reference 07130 and
08070 and this is a percentage of the
NAV of the financial instrument
expressed in annualised terms (rate of
cost deduction to be applied).
66.2.2.118  InvestmentFundPlanType1Code
Definition: Specifies a type of investment fund plan.
Type: CodeSet
CodeName Name Definition
INVP SavingsInvestmentPlan Savings investment plan.
SWIP SwitchPlan Switch plan.
WTHP WithdrawalPlan Withdrawal plan.
66.2.2.119  InvestmentFundRole2Code
Definition: Specifies the role played by an actor in an investment fund transaction.
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5318 May 2026
```

## File page 5319

```text
CodeName Name Definition
FMCO FundManagementCompany Party that sets up a fund, decides upon
the investment strategy, appoints
agents, and is responsible for the
promotion and the marketing of the fund.
This party makes all the strategic
decisions related to a fund.
REGI Registrar Party responsible for keeping track of the
owners of securities. In the investment
fund business, this party keeps the
investor registry of the fund, and
administers investor accounts and
related records. It is appointed by the
fund management company.
TRAG TransferAgent Party appointed by the fund
management company. This party
updates records of investor accounts to
reflect the daily investor purchases,
redemptions, switches, transfers, and re-
registrations. It ensures the timely
settlement of transactions, and may
provide tax information to the investor
and/or to its intermediaries. It may
calculate, collect, and rebate
commissions. It prepares and distributes
confirmations reflecting transactions,
resulting in unit or cash account
movements to the investor or the
investor's intermediary. It responds to
inquiries concerning account status, and
processes the income distribution.
INTR Intermediary Party that provides services to investors
relating to financial products. These
services may include some, or all of,
provision of information and advice on
products, placement of investment
orders, transmission of payment,
custody of assets, and the administration
of rights and benefits. In the specific
framework of investment funds industry,
an intermediary may present information
about funds to potential investors, and
solicit orders for the fund. This
intermediary may facilitate the
transmission of the orders and
information from/to the investors and/or
other intermediaries. The intermediary
receives commission from the Fund
and/or fees from the investor.
DIST Distributor Party that act as an wholesaler of funds.
CONC Concentrator Party that acts as an aggregator of
funds, also called a funds hub.
UCL1 UnderlyingClient1 Underlying client of the intermediary.
UCL2 UnderlyingClient2 Underlying client of underlying client 1.
TRAN TransmittingAgent Party that transmits the instruction,
advice, notification or report.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5319 May 2026
```

