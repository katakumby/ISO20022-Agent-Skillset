---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.43 Order23", "7.1.19.43.40 YieldType <YldTp>"]
file_pages: [352]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.43.40 YieldType <YldTp>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 352 to 352.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 352

```text
CodeName Name Definition
CFAV CallForAccountValue Pay-in call is for account value.
CFST CallForSettlement Pay-in call is for settlement.
CFCC CallForCurrencyClose Pay-in call is for currency close.
7.1.19.43.40  YieldType <YldTp>
Presence: [0..1]
Definition: Type of yield at which the transaction was effected.
YieldType <YldTp> contains the following elements (see "YieldCalculation7" on page 607 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] Rate 607
   CalculationType <ClctnTp> [1..1] CodeSet 607
   RedemptionPrice <RedPric> [0..1] ± 609
   ValueDate <ValDt> [0..1] Date 610
   ValuePeriod <ValPrd> [0..1]  610
{Or     FromDateTime <FrDtTm> [1..1] DateTime 610
Or     ToDateTime <ToDtTm> [1..1] DateTime 610
Or}     DateTimeRange <DtTmRg> [1..1] ± 610
   CalculationDate <ClctnDt> [0..1] Date 611
7.1.19.43.41  Reporting <Rptg>
Presence: [0..*]
Definition: Specifies that a trade is to be reported to a third party.
Reporting <Rptg> contains one of the following elements (see "Reporting6Choice" on page 353 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 353
Or}   Proprietary <Prtry> [1..1] ± 354
7.1.19.43.42  AdditionalPhysicalOrRegistrationDetails <AddtlPhysOrRegnDtls>
Presence: [0..1]
Definition: Provides information required for the registration or physical settlement.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 352 February 2025
```

