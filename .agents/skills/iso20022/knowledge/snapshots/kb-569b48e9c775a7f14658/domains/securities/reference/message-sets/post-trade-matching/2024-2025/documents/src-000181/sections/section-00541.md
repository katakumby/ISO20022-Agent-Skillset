---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.21 CollateralType3Code"]
file_pages: [621]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.21 CollateralType3Code

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 621 to 621.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 621

```text
Type: CodeSet
CodeName Name Definition
OVER Overnight Repo with a term of one day.
TERM Term Repo with a term of more than one day.
FLEX Flexible Identifies "a classic term repo with the
added feature that the cash is repaid to
the buyer in installments" (Definition from
"Mastering Repo Markets" by Bob
Steiner).
OPEN Open Repo which can be terminated by either
party at any time, and which has an
unspecified repurchase date.
7.2.2.21  CollateralType3Code
Definition: Specifies the type of collateral.
Type: CodeSet
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
7.2.2.22  CommissionType9Code
Definition: Type of service for which the commission is asked or paid.
Type: CodeSet
CodeName Name Definition
CLDI ClientDirected Commission is as per client agreement.
STEP StepOut Commission for a step-out trade,
charged by the step-out broker.
SOFT SoftDollar Commission designated by the broker
for third party services. The soft dollar
arrangement refers to an arrangement
wherean investment manager directs
transactions to a brokerand, in
exchange, the broker provides
brokerage and research services to the
investment manager. Soft dollar
arrangements include proprietary and
third party research arrangements, but
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 621 February 2025
```

