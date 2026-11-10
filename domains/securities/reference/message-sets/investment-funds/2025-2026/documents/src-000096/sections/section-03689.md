---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.11 PartyRole4Choice"]
file_pages: [4956, 4957]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.11 PartyRole4Choice

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4956 to 4957.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4956

```text
RegisteredShareholderName <RegdShrhldrNm> contains one of the following elements (see
"RegisteredShareholderName1Choice" on page 4917 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IndividualPerson <IndvPrsn> [1..1]  4918
     NamePrefix <NmPrfx> [0..1]  4918
{Or       Code <Cd> [1..1] CodeSet 4918
Or}       Proprietary <Prtry> [1..1] ± 4918
     GivenName <GvnNm> [0..1] Text 4919
     MiddleName <MddlNm> [0..1] Text 4919
     Name <Nm> [1..1] Text 4919
     PostalAddress <PstlAdr> [1..5] ± C23 4919
Or}   Organisation <Org> [1..1]  4920
     Name <Nm> [1..1] Text 4921
     ShortName <ShrtNm> [0..1] Text 4921
     PostalAddress <PstlAdr> [1..5] ± C23 4921
66.1.30.11  PartyRole4Choice
Definition: Choice of formats for the specification of the role.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4956
Or}   Proprietary <Prtry> [1..1] ± 4958
66.1.30.11.1  Code <Cd>
Presence: [1..1]
Definition: Role expressed as a code.
Datatype: "InvestmentFundRole7Code" on page 5322
CodeName Name Definition
CONC Concentrator Party that acts as an aggregator of
funds, also called a funds hub.
DIST Distributor Party that act as an wholesaler of funds.
FMCO FundManagementCompany Party that sets up a fund, decides upon
the investment strategy, appoints
agents, and is responsible for the
promotion and the marketing of the fund.
This party makes all the strategic
decisions related to a fund.
INTR Intermediary Party that provides services to investors
relating to financial products. These
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4956 May 2026
```

## File page 4957

```text
CodeName Name Definition
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
PAYI PayingAgent Agent that executes the payment. In the
context of the investment fund industry,
the paying agent is the local legal
representative of the fund. It may pay out
dividends, and collects money for the
purchase of funds when a client deals
directly with the fund and/or when a
client deals with bearer shares. It pays
out the redemption of the fund, may
distribute information about the fund, and
provides legal information about the
fund.
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
CUST Custodian Party that safekeeps and administers
assets on behalf of the owner.
CACO CashCorrespondent Financial institution that executes cash
transfers on behalf of its clients.
FACT FundAccountant Party that keeps accounting records of
the available assets and liabilities of the
fund. This party calculates deal prices,
the Net Asset Value (NAV) of the fund,
and may provide fund performance and
tax data.
INVE InvestmentManager Party that implements the investment
strategy, that is, selects portfolio
investments in accordance with the
objectives and strategy in the fund's
prospectus, and places orders to effect
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4957 May 2026
```

