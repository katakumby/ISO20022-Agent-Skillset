---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["8 camt.009.001.08 GetLimitV08", "8.4 Message Building Blocks", "8.4.2 LimitQueryDefinition <LmtQryDef>", "8.4.2.2 LimitCriteria <LmtCrit>", "8.4.2.2.2 NewCriteria <NewCrit>", "8.4.2.2.2.1 NewQueryName <NewQryNm>"]
file_pages: [374, 375]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.009.001.08"]
---

# 8.4.2.2.2.1 NewQueryName <NewQryNm>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 374 to 375.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 374

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     LimitAmount <LmtAmt> [0..1] ± 387
     LimitValidAsOfDate <LmtVldAsOfDt> [0..1]  387
{Or       Date <Dt> [1..1] Date 388
Or       Period <Prd> [1..1] ± 388
Or       FromDate <FrDt> [1..1] Date 388
Or}       ToDate <ToDt> [1..1] Date 388
   ReturnCriteria <RtrCrit> [0..1]  388
     StartDateTimeIndicator <StartDtTmInd> [0..1] Indicator 389
     StatusIndicator <StsInd> [0..1] Indicator 389
     UsedAmountIndicator <UsdAmtInd> [0..1] Indicator 389
     UsedPercentageIndicator <UsdPctgInd> [0..1] Indicator 389
Constraints
• LimitCriteriaGuideline
If a bilateral limit regarding specific members in the system is required, then the identification of the
bilateral counterpart should be given.
By default, if there is no identification of the bilateral counterpart and the current or default bilateral
limit is required, then all the bilateral limits with the relevant counterpart identifications are returned.
• ReturnCriteriaAndOrSearchCriteriaRule
If ReturnCriteria is not present, then at least one occurrence of SearchCriteria must be present. If
ReturnCriteria is present, then any occurrence of SearchCriteria is optional.
On Condition
    /ReturnCriteria is absent
Following Must be True
    /SearchCriteria[1] Must be present
8.4.2.2.2.1  NewQueryName <NewQryNm>
Presence: [0..1]
Definition: Name of the query defined by the search criteria and return criteria.
Datatype: "Max35Text" on page 889
8.4.2.2.2.2  SearchCriteria <SchCrit>
Presence: [0..*]
Definition: Defines the criteria to extract the limit information.
Impacted by: C3 "BilateralLimitCounterparty3Rule", C4 "BilateralLimitCounterparty4Rule"
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 374 February 2025
```

## File page 375

```text
SearchCriteria <SchCrit> contains the following LimitSearchCriteria7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [0..1] ± 376
   BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..*] ± 377
   DefaultLimitType <DfltLmtTp> [0..*]  377
{Or     Code <Cd> [1..1] CodeSet 377
Or}     Proprietary <Prtry> [1..1] Text 379
   CurrentLimitType <CurLmtTp> [0..*]  379
{Or     Code <Cd> [1..1] CodeSet 380
Or}     Proprietary <Prtry> [1..1] Text 382
   AccountOwner <AcctOwnr> [0..1] ± 382
   AccountIdentification <AcctId> [0..1] ± 382
   UsedAmount <UsdAmt> [0..1] ± 383
   UsedPercentage <UsdPctg> [0..1]  383
{Or     From <Fr> [1..1]  384
       BoundaryRate <BdryRate> [1..1] Rate 384
       Included <Incl> [1..1] Indicator 384
Or     To <To> [1..1]  385
       BoundaryRate <BdryRate> [1..1] Rate 385
       Included <Incl> [1..1] Indicator 385
Or     FromTo <FrTo> [1..1]  385
       From <Fr> [1..1]  385
         BoundaryRate <BdryRate> [1..1] Rate 386
         Included <Incl> [1..1] Indicator 386
       To <To> [1..1]  386
         BoundaryRate <BdryRate> [1..1] Rate 386
         Included <Incl> [1..1] Indicator 386
Or     Equal <EQ> [1..1] Rate 387
Or}     NotEqual <NEQ> [1..1] Rate 387
   LimitCurrency <LmtCcy> [0..1] CodeSet C1 387
   LimitAmount <LmtAmt> [0..1] ± 387
   LimitValidAsOfDate <LmtVldAsOfDt> [0..1]  387
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 375 February 2025
```

