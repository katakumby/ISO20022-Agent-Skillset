---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.28 Intermediary11", "66.1.30.28.4 ExtendedRole <XtndedRole>"]
file_pages: [5016]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.28.4 ExtendedRole <XtndedRole>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5016 to 5016.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5016

```text
CodeName Name Definition
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
66.1.30.28.4  ExtendedRole <XtndedRole>
Presence: [0..1]
Warning   Either Role or ExtendedRole may be present, but not both.
Definition: Function performed by the intermediary.
Datatype: "Extended350Code" on page 5402
66.1.30.29  Role4Choice
Definition: Choice of format for a party role.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5016
Or}   Proprietary <Prtry> [1..1] ± 5017
66.1.30.29.1  Code <Cd>
Presence: [1..1]
Definition: Role of the party in the activity expressed as a code.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5016 May 2026
```

