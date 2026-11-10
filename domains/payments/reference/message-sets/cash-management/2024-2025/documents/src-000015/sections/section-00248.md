---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["8 camt.009.001.08 GetLimitV08", "8.3 Constraints"]
file_pages: [366]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.009.001.08"]
---

# 8.3 Constraints

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 366 to 366.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 366

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
                 Included <Incl> [1..1] Indicator 386
               To <To> [1..1]  386
                 BoundaryRate <BdryRate> [1..1] Rate 386
                 Included <Incl> [1..1] Indicator 386
Or             Equal <EQ> [1..1] Rate 387
Or}             NotEqual <NEQ> [1..1] Rate 387
           LimitCurrency <LmtCcy> [0..1] CodeSet C1 387
           LimitAmount <LmtAmt> [0..1] ± 387
           LimitValidAsOfDate <LmtVldAsOfDt> [0..1]  387
{Or             Date <Dt> [1..1] Date 388
Or             Period <Prd> [1..1] ± 388
Or             FromDate <FrDt> [1..1] Date 388
Or}             ToDate <ToDt> [1..1] Date 388
         ReturnCriteria <RtrCrit> [0..1]  388
           StartDateTimeIndicator <StartDtTmInd> [0..1] Indicator 389
           StatusIndicator <StsInd> [0..1] Indicator 389
           UsedAmountIndicator <UsdAmtInd> [0..1] Indicator 389
           UsedPercentageIndicator <UsdPctgInd> [0..1] Indicator 389
   SupplementaryData <SplmtryData> [0..*] ± C9 389
8.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C3 BilateralLimitCounterparty3Rule
If at least one occurrence of CurrentLimitType is present and is MULT, then no occurrence of
BilateralLimitCounterpartyIdentification is allowed.
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 366 February 2025
```

