---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.28 Intermediary11", "66.1.30.28.3 Role <Role>"]
file_pages: [5015]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.28.3 Role <Role>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5015 to 5015.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5015

```text
Account <Acct> contains the following elements (see "Account7" on page 4337 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4337
   AccountServicer <AcctSvcr> [0..1] ± 4337
66.1.30.28.3  Role <Role>
Presence: [0..1]
Warning   Either Role or ExtendedRole may be present, but not both.
Definition: Function performed by the intermediary.
Datatype: "InvestmentFundRole2Code" on page 5318
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5015 May 2026
```

