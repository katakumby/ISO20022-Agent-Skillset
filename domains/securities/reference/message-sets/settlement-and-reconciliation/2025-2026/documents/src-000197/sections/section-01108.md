---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.18 Role6Choice", "35.1.16.18.2 Proprietary <Prtry>"]
file_pages: [1550]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.18.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1550 to 1550.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1550

```text
CodeName Name Definition
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
35.1.16.18.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Role of the party in the activity expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.18.3  Text <Txt>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1550 March 2026
```

