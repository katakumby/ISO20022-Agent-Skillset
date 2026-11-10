---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.17 Identification Information", "82.1.17.11 GenericIdentification13", "82.1.17.11.1 Identification <Id>"]
file_pages: [2969]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.17.11.1 Identification <Id>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2969 to 2969.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2969

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2969
   SchemeName <SchmeNm> [0..1] Text 2969
   Issuer <Issr> [1..1] Text 2969
82.1.17.11.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max4AlphaNumericText" on page 3328
82.1.17.11.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 3328
82.1.17.11.3  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 3328
82.1.18 Market
82.1.18.1  MarketIdentification89
Definition: Context, or geographic environment, in which trading parties may meet in order to negotiate
and execute trades among themselves.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 2969
   Type <Tp> [1..1]  2970
{Or     Code <Cd> [1..1] CodeSet 2970
Or}     Proprietary <Prtry> [1..1] ± 2970
82.1.18.1.1  Identification <Id>
Presence: [0..1]
Definition: Code allocated to places of trade (stock exchanges), to regulated markets (for example,
Electronic Trading Platforms - ECN), and to unregulated markets (for example, Automated Trading
Systems - ATS), as sources of prices and related information, in order to facilitate automated
processing.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2969 August 2026
```

