---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.35 FutureOrOptionDetails3", "7.1.19.35.10 NearTermPositionLimit <NearTermPosLmt>"]
file_pages: [328]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.35.10 NearTermPositionLimit <NearTermPosLmt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 328 to 328.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 328

```text
Definition: Indicates the maximum number of listed option contracts on a single security which can be
held by an investor or group of investors acting jointly.
Datatype: "Number" on page 666
7.1.19.35.10  NearTermPositionLimit <NearTermPosLmt>
Presence: [0..1]
Definition: Position limit in the near-term contract for a given exchange-traded product.
Datatype: "Number" on page 666
7.1.19.35.11  MinimumTradingPricingIncrement <MinTradgPricgIncrmt>
Presence: [0..1]
Definition: Minimum price increase for a given exchange-traded Instrument.
Datatype: "Number" on page 666
7.1.19.35.12  Purpose <Purp>
Presence: [0..1]
Definition: Reason for which money is raised through the issuance of a security.
Datatype: "Max256Text" on page 668
7.1.19.35.13  ContractSettlementMonth <CtrctSttlmMnth>
Presence: [0..1]
Definition: Specifies when the contract (i.e. MBS/TBA) will settle.
Datatype: "ISOYearMonth" on page 670
7.1.19.35.14  FirstDealingDate <FrstDealgDt>
Presence: [0..1]
Definition: Date on which new securities begin trading.
FirstDealingDate <FrstDealgDt> contains one of the following elements (see
"DateAndDateTime1Choice" on page 263 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 263
Or}   DateTime <DtTm> [1..1] DateTime 263
7.1.19.35.15  Ratio <Ratio>
Presence: [0..*]
Definition: Ratio applied to convert the related security.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 328 February 2025
```

