---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.9 SubAccountDetails <SubAcctDtls>", "3.4.9.5 BalanceForSubAccount <BalForSubAcct>", "3.4.9.5.19 SupplementaryData <SplmtryData>"]
file_pages: [132]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.9.5.19 SupplementaryData <SplmtryData>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 132 to 132.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 132

```text
Datatype: "Max350Text" on page 2192
3.4.9.5.19  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C40 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1565
   Envelope <Envlp> [1..1] (External Schema) 1565
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
3.4.10 AccountBaseCurrencyTotalAmounts
<AcctBaseCcyTtlAmts>
Presence: [0..1]
Definition: Total valuation amounts provided in the base currency of the account.
AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts> contains the following
TotalValueInPageAndStatement2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] ± 132
   TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] ± 133
   TotalBookValueOfStatement <TtlBookValOfStmt> [0..1] ± 133
3.4.10.1  TotalHoldingsValueOfPage <TtlHldgsValOfPg>
Presence: [0..1]
Definition: Total value of positions reported in this message.
TotalHoldingsValueOfPage <TtlHldgsValOfPg> contains the following elements (see
"AmountAndDirection6" on page 1361 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1362
   Sign <Sgn> [1..1] Indicator 1362
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 132 March 2026
```

