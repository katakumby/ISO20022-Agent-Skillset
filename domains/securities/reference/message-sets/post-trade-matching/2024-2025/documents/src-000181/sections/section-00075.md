---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.8 Stipulations <Stiptns>", "3.4.8.14 LookBack <LookBck>"]
file_pages: [100]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.8.14 LookBack <LookBck>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 100 to 100.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 100

```text
3.4.8.14  LookBack <LookBck>
Presence: [0..1]
Definition: Indicates an instruction or attribute giving the number of days to be included in the look-back
period for the investment. E.g. some options allow exercise based on the underlying asset's optimal
value over the look-back period.
Datatype: "Number" on page 666
3.4.8.15  MaturityDate <MtrtyDt>
Presence: [0..1]
Definition: Indicates the maturity date.
Datatype: "ISOYearMonth" on page 670
3.4.8.16  IssueDate <IsseDt>
Presence: [0..1]
Definition: Indicates the issue date.
Datatype: "ISOYearMonth" on page 670
3.4.8.17  IssuerIdentification <IssrId>
Presence: [0..1]
Definition: Identification of the issuer.
Impacted by: C9 "BICNonFI"
Datatype: "BICNonFIDec2014Identifier" on page 663
Constraints
• BICNonFI
Valid BICs for non-financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
3.4.8.18  IssueSize <IsseSz>
Presence: [0..1]
Definition: Identifies the issue size range.
Datatype: "Number" on page 666
3.4.8.19  MinimumDenomination <MinDnmtn>
Presence: [0..1]
Definition: Indicates the minimum denomination of a security.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 100 February 2025
```

