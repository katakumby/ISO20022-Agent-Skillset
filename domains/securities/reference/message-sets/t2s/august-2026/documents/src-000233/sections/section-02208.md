---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.18 Market", "82.1.18.2 MarketClientSide6Choice", "82.1.18.2.1 Code <Cd>"]
file_pages: [2971]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.18.2.1 Code <Cd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2971 to 2971.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2971

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2971
Or}   Proprietary <Prtry> [1..1] ± 2971
82.1.18.2.1  Code <Cd>
Presence: [1..1]
Definition: Market side or a client side information expressed as an ISO 20022 code.
Datatype: "MarketClientSide1Code" on page 3262
CodeName Name Definition
CLNT ClientSide Instruction is for a client side transaction.
MAKT MarketSide Instruction is for a market side
transaction.
82.1.18.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Market side or a client side information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.18.3  MarketIdentification1Choice
Definition: Choice of market identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 2971
Or}   Description <Desc> [1..1] Text 2971
82.1.18.3.1  MarketIdentifierCode <MktIdrCd>
Presence: [1..1]
Definition: ISO 10383 Market Identification Code.
Datatype: "MICIdentifier" on page 3322
82.1.18.3.2  Description <Desc>
Presence: [1..1]
Definition: Description of the market when no Market Identifier Code is available.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2971 August 2026
```

