---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.16 Identification Information", "7.1.16.10 GenericIdentification56", "7.1.16.10.1 Identification <Id>"]
file_pages: [354]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.16.10.1 Identification <Id>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 354 to 354.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 354

```text
7.1.16.10.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Exact4AlphaNumericText" on page 555
7.1.16.10.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 557
7.1.16.10.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 557
7.1.16.10.4  Balance <Bal>
Presence: [1..1]
Definition: Value of the balance.
Datatype: "DecimalNumber" on page 554
7.1.17 Market
7.1.17.1  MarketIdentification89
Definition: Context, or geographic environment, in which trading parties may meet in order to negotiate
and execute trades among themselves.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 354
   Type <Tp> [1..1]  355
{Or     Code <Cd> [1..1] CodeSet 355
Or}     Proprietary <Prtry> [1..1] ± 355
7.1.17.1.1  Identification <Id>
Presence: [0..1]
Definition: Code allocated to places of trade (stock exchanges), to regulated markets (for example,
Electronic Trading Platforms - ECN), and to unregulated markets (for example, Automated Trading
Systems - ATS), as sources of prices and related information, in order to facilitate automated
processing.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 354 March 2026
```

