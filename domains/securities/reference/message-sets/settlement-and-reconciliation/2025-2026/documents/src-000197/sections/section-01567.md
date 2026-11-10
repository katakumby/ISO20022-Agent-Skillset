---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.54 InvestmentFundRole2Code"]
file_pages: [2084, 2085]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.54 InvestmentFundRole2Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2084 to 2085.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2084

```text
CodeName Name Definition
A012 IC30E2360orEurobondbasismodel2 Method whereby interest is calculated
based on a 30-day month and a 360-day
year. Accrued interest to a value date on
the last day of a month shall be the
same as to the 30th calendar day of the
same month, except for the last day of
February whose day of the month value
shall be adapted to the value of the first
day of the interest period if the latter is
higher and if the period is one of a
regular schedule. This means that the
31st is assumed to be the 30th and 28
Feb of a non-leap year is assumed to be
equivalent to 29 Feb when the first day
of the interest period is the 29th, or to 30
Feb when the first day of the interest
period is the 30th or the 31st. The 29th
day of February in a leap year is
assumed to be equivalent to 30 Feb
when the first day of the interest period
is the 30th or the 31st. Similarly, if the
coupon period starts on the last day of
February, it is assumed to produce only
one day of interest in February as if it
was starting on 30 Feb when the end of
the period is the 30th or the 31st, or two
days of interest in February when the
end of the period is the 29th, or three
days of interest in February when it is 28
Feb of a non-leap year and the end of
the period is before the 29th.
A013 IC30E3360orEurobondbasismodel3 Method whereby interest is calculated
based on a 30-day month and a 360-day
year. Accrued interest to a value date on
the last day of a month shall be the
same as to the 30th calendar day of the
same month. This means that the 31st is
assumed to be the 30th and 28 Feb (or
29 Feb for a leap year) is assumed to be
equivalent to 30 Feb. It is a variation of
the 30E/360 (or Eurobond basis) method
where the last day of February is always
assumed to be the 30th, even if it is the
last day of the maturity coupon period.
A014 Actual365NL Method whereby interest is calculated
based on the actual number of accrued
days in the interest period, excluding any
leap day from the count, and a 365-day
year.
NARR Narrative Other method than A001-A020. See
Narrative.
35.2.2.54  InvestmentFundRole2Code
Definition: Specifies the role played by an actor in an investment fund transaction.
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2084 March 2026
```

## File page 2085

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
Settlement And Reconciliation - Maintenance 2025 - 2026 2085 March 2026
```

