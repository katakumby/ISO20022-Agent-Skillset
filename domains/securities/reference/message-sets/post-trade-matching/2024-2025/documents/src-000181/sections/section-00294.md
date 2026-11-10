---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.44 Reporting6Choice", "7.1.19.44.2 Proprietary <Prtry>"]
file_pages: [354]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.44.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 354 to 354.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 354

```text
CodeName Name Definition
STEX StockExchange Trade details are to be reported to a
stock exchange.
REGU RegulatoryOrganisation Trade details are to be reported to a
regulatory organisation.
DEFR DeferredReport Report is deferred, for example, because
the order was executed in partial fills.
7.1.19.44.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Third party reporting information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.45  SettlingCapacity9Choice
Definition: Choice of format for the settlement capacity information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 354
Or}   Proprietary <Prtry> [1..1] ± 354
7.1.19.45.1  Code <Cd>
Presence: [1..1]
Definition: Settlement capacity expressed as an ISO 20022 code.
Datatype: "SettlingCapacity1Code" on page 650
CodeName Name Definition
CUST SettlingCustodian Settlement party is a custodian. It
receives/delivers the securities and
carries out custodial duties.
SAGE SettlingAgent Settlement party is trading and settling
transactions in financial instruments on
behalf of its client(s).
SPRI SettlingPrincipal Settlement party is settling its own
trades.
7.1.19.45.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 354 February 2025
```

