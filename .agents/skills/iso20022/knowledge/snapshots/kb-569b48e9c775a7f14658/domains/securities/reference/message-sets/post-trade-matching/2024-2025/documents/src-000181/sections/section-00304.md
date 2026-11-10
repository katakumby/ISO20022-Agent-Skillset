---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.49 SecuritiesFinancing12", "7.1.19.49.19 TotalNumberOfCollateralInstructions <TtlNbOfCollInstrs>"]
file_pages: [365]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.49.19 TotalNumberOfCollateralInstructions <TtlNbOfCollInstrs>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 365 to 365.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 365

```text
ClosingAmountPerPiecesOfCollateral <ClsgAmtPerPcsOfColl> contains the following elements
(see "AmountAndDirection5" on page 227 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 227
   CreditDebit <CdtDbt> [0..1] CodeSet 228
7.1.19.49.19  TotalNumberOfCollateralInstructions <TtlNbOfCollInstrs>
Presence: [0..1]
Definition: Indicates the total Number of collateral instructions involved in the transaction.
Datatype: "Max3NumericText" on page 669
7.1.19.49.20  FinancingAgreement <FincgAgrmt>
Presence: [0..1]
Definition: Provides details for the securities financing transaction.
FinancingAgreement <FincgAgrmt> contains the following elements (see "Agreement5" on page 225
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Description <Desc> [0..1] Text 225
   Date <Dt> [0..1] DateTime 226
   Currency <Ccy> [0..1] CodeSet C1 226
   ClosingType <ClsgTp> [0..1] CodeSet 226
   StartDate <StartDt> [0..1] DateTime 226
   DeliveryType <DlvryTp> [0..1] CodeSet 227
   MarginRatio <MrgnRatio> [0..1] Rate 227
7.1.19.49.21  LendingTransactionMethod <LndgTxMtd>
Presence: [0..1]
Definition: Method applied to a lending transaction.
LendingTransactionMethod <LndgTxMtd> contains one of the following elements (see
"LendingTransactionMethod2Choice" on page 383 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 383
Or}   Proprietary <Prtry> [1..1] ± 383
7.1.19.49.22  LendingWithCollateral <LndgWthColl>
Presence: [0..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 365 February 2025
```

