---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.7 Collateral"]
file_pages: [249]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.7 Collateral

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 249 to 249.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 249

```text
7.1.7 Collateral
7.1.7.1  CollateralType4Choice
Definition: Choice of format for the collateral type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 249
Or}   Proprietary <Prtry> [1..1] ± 249
7.1.7.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of collateral expressed as an ISO 20022 code.
Datatype: "CollateralType3Code" on page 621
CodeName Name Definition
CASH Cash Collateral type is cash.
SECU Securities Collateral type is securities.
PHYS PhysicalEntities Collateral type are physical entities, for
example, airplanes for debt issued by
the airline industry.
INSU Insurance Collateral type is an insurance contract.
STCF StockCertificate Collateral type is stock certificates.
BOND Bond Collateral type is bonds.
GBBK BankGuarantee Collateral type is a bank guarantee.
OTHR Other Other assets that could be used as
collateral.
7.1.7.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of collateral expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 249 February 2025
```

