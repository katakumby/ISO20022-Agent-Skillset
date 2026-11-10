---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["17 camt.018.001.05 GetBusinessDayInformationV05", "17.4 Message Building Blocks", "17.4.2 BusinessDayInformationQueryDefinition <BizDayInfQryDef>", "17.4.2.2 Criteria <Crit>", "17.4.2.2.1 QueryName <QryNm>"]
file_pages: [527]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.018.001.05"]
---

# 17.4.2.2.1 QueryName <QryNm>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 527 to 527.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 527

```text
Criteria <Crit> contains one of the following BusinessDayCriteria3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QueryName <QryNm> [1..1] Text 527
Or}   NewCriteria <NewCrit> [1..1]  C3 527
     NewQueryName <NewQryNm> [0..1] Text 528
     SearchCriteria <SchCrit> [0..*]  529
       SystemDate <SysDt> [0..1] Date 529
       SystemIdentification <SysId> [0..*] ± 529
       SystemCurrency <SysCcy> [0..*] CodeSet C1 529
       EventType <EvtTp> [0..1]  530
{Or         Code <Cd> [1..1] CodeSet 530
Or}         Proprietary <Prtry> [1..1] ± 531
       ClosurePeriod <ClsrPrd> [0..1]  531
{Or         FromDateTime <FrDtTm> [1..1] DateTime 532
Or         ToDateTime <ToDtTm> [1..1] DateTime 532
Or}         DateTimeRange <DtTmRg> [1..1] ± 532
     ReturnCriteria <RtrCrit> [0..1]  532
       SystemDateIndicator <SysDtInd> [0..1] Indicator 533
       SystemStatusIndicator <SysStsInd> [0..1] Indicator 533
       SystemCurrencyIndicator <SysCcyInd> [0..1] Indicator 533
       ClosurePeriodIndicator <ClsrPrdInd> [0..1] Indicator 533
       EventIndicator <EvtInd> [0..1] Indicator 534
       SessionPeriodIndicator <SsnPrdInd> [0..1] Indicator 534
       EventTypeIndicator <EvtTpInd> [0..1] Indicator 534
17.4.2.2.1  QueryName <QryNm>
Presence: [1..1]
Definition: Recalls the criteria (search and return criteria) defined in a preceding query.
Datatype: "Max35Text" on page 889
17.4.2.2.2  NewCriteria <NewCrit>
Presence: [1..1]
Definition: Explicitly defines the query criteria.
Impacted by: C3 "ReturnCriteriaAndOrSearchCriteriaRule"
Approved by the Payments SEG on 04 February 2025 camt.018.001.05 GetBusinessDayInformationV05
Cash Management - Maintenance 2024 - 2025 527 February 2025
```

