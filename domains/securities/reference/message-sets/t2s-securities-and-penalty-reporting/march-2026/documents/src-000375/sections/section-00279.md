---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.17 Market", "7.1.17.2 MarketClientSide6Choice", "7.1.17.2.1 Code <Cd>"]
file_pages: [356]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.17.2.1 Code <Cd>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 356 to 356.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 356

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 356
Or}   Proprietary <Prtry> [1..1] ± 356
7.1.17.2.1  Code <Cd>
Presence: [1..1]
Definition: Market side or a client side information expressed as an ISO 20022 code.
Datatype: "MarketClientSide1Code" on page 514
CodeName Name Definition
CLNT ClientSide Instruction is for a client side transaction.
MAKT MarketSide Instruction is for a market side
transaction.
7.1.17.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Market side or a client side information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.17.3  MarketIdentification1Choice
Definition: Choice of market identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 356
Or}   Description <Desc> [1..1] Text 356
7.1.17.3.1  MarketIdentifierCode <MktIdrCd>
Presence: [1..1]
Definition: ISO 10383 Market Identification Code.
Datatype: "MICIdentifier" on page 553
7.1.17.3.2  Description <Desc>
Presence: [1..1]
Definition: Description of the market when no Market Identifier Code is available.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 356 March 2026
```

