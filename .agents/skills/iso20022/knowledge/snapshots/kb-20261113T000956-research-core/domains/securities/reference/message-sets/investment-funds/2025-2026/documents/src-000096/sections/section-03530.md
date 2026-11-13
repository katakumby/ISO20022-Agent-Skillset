---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.24 InvestmentFundRole2Choice", "66.1.26.24.2 Proprietary <Prtry>"]
file_pages: [4780]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.24.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4780 to 4780.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4780

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
DIST Distributor Party that act as an wholesaler of funds.
CONC Concentrator Party that acts as an aggregator of
funds, also called a funds hub.
UCL1 UnderlyingClient1 Underlying client of the intermediary.
UCL2 UnderlyingClient2 Underlying client of underlying client 1.
TRAN TransmittingAgent Party that transmits the instruction,
advice, notification or report.
66.1.26.24.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Role expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.26.25  LumpSumType1Choice
Definition: Choice of formats for a type of lump sum.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4780
Or}   Proprietary <Prtry> [1..1] ± 4781
66.1.26.25.1  Code <Cd>
Presence: [1..1]
Definition: Type of lump sum expressed as a code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4780 May 2026
```

