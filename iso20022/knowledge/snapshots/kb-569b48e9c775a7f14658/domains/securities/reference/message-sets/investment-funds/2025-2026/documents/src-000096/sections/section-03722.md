---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.23 Intermediary48", "66.1.30.23.2 Account <Acct>", "66.1.30.23.2.5 RegistrationAddress <RegnAdr>"]
file_pages: [5007, 5008]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.23.2.5 RegistrationAddress <RegnAdr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5007 to 5008.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5007

```text
66.1.30.23.2.5  RegistrationAddress <RegnAdr>
Presence: [0..1]
Definition: Address of the nominee company that holds the assets at the transfer agent or International
Central Securities Depository or Central Securities Depository on behalf of the party.
RegistrationAddress <RegnAdr> contains the following elements (see "PostalAddress1" on
page 5098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 5098
   AddressLine <AdrLine> [0..5] Text 5099
   StreetName <StrtNm> [0..1] Text 5099
   BuildingNumber <BldgNb> [0..1] Text 5099
   PostCode <PstCd> [0..1] Text 5099
   TownName <TwnNm> [0..1] Text 5099
   CountrySubDivision <CtrySubDvsn> [0..1] Text 5099
   Country <Ctry> [1..1] CodeSet C12 5100
66.1.30.23.3  Role <Role>
Presence: [0..1]
Definition: Function performed by the intermediary or related party.
Role <Role> contains one of the following Role8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5007
Or}   Proprietary <Prtry> [1..1] ± 5009
66.1.30.23.3.1  Code <Cd>
Presence: [1..1]
Definition: Role of the party in the activity expressed as a code.
Datatype: "InvestmentFundRole8Code" on page 5323
CodeName Name Definition
CUST Custodian Party that safekeeps and administers
assets on behalf of the owner.
DIST Distributor Party that act as an wholesaler of funds.
FMCO FundManagementCompany Party that sets up a fund, decides upon
the investment strategy, appoints
agents, and is responsible for the
promotion and the marketing of the fund.
This party makes all the strategic
decisions related to a fund.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5007 May 2026
```

## File page 5008

```text
CodeName Name Definition
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
INVE InvestmentManager Party that implements the investment
strategy, that is, selects portfolio
investments in accordance with the
objectives and strategy in the fund's
prospectus, and places orders to effect
or liquidate selected investments in
accordance with net flow of capital into
or out of the fund.
INVS Investor Party, either an individual or
organisation, whose assets are being
invested.
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
TRAN TransmittingAgent Party that transmits the instruction,
advice, notification or report.
UCL1 UnderlyingClient1 Underlying client of the intermediary.
UCL2 UnderlyingClient2 Underlying client of underlying client 1.
REGI Registrar Party responsible for keeping track of the
owners of securities. In the investment
fund business, this party keeps the
investor registry of the fund, and
administers investor accounts and
related records. It is appointed by the
fund management company.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5008 May 2026
```

