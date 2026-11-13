---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["17 camt.018.001.05 GetBusinessDayInformationV05", "17.4 Message Building Blocks", "17.4.2 BusinessDayInformationQueryDefinition <BizDayInfQryDef>", "17.4.2.2 Criteria <Crit>", "17.4.2.2.2 NewCriteria <NewCrit>", "17.4.2.2.2.1 NewQueryName <NewQryNm>"]
file_pages: [528]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.018.001.05"]
---

# 17.4.2.2.2.1 NewQueryName <NewQryNm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 528 to 528.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 528

```text
NewCriteria <NewCrit> contains the following BusinessDayCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NewQueryName <NewQryNm> [0..1] Text 528
   SearchCriteria <SchCrit> [0..*]  529
     SystemDate <SysDt> [0..1] Date 529
     SystemIdentification <SysId> [0..*] ± 529
     SystemCurrency <SysCcy> [0..*] CodeSet C1 529
     EventType <EvtTp> [0..1]  530
{Or       Code <Cd> [1..1] CodeSet 530
Or}       Proprietary <Prtry> [1..1] ± 531
     ClosurePeriod <ClsrPrd> [0..1]  531
{Or       FromDateTime <FrDtTm> [1..1] DateTime 532
Or       ToDateTime <ToDtTm> [1..1] DateTime 532
Or}       DateTimeRange <DtTmRg> [1..1] ± 532
   ReturnCriteria <RtrCrit> [0..1]  532
     SystemDateIndicator <SysDtInd> [0..1] Indicator 533
     SystemStatusIndicator <SysStsInd> [0..1] Indicator 533
     SystemCurrencyIndicator <SysCcyInd> [0..1] Indicator 533
     ClosurePeriodIndicator <ClsrPrdInd> [0..1] Indicator 533
     EventIndicator <EvtInd> [0..1] Indicator 534
     SessionPeriodIndicator <SsnPrdInd> [0..1] Indicator 534
     EventTypeIndicator <EvtTpInd> [0..1] Indicator 534
Constraints
• ReturnCriteriaAndOrSearchCriteriaRule
If ReturnCriteria is not present, then at least one occurrence of SearchCriteria must be present. If
ReturnCriteria is present, then any occurrence of SearchCriteria is optional.
On Condition
    /ReturnCriteria is absent
Following Must be True
    /SearchCriteria[1] Must be present
17.4.2.2.2.1  NewQueryName <NewQryNm>
Presence: [0..1]
Definition: Name of the query defined by the search criteria and return criteria.
Datatype: "Max35Text" on page 889
Approved by the Payments SEG on 04 February 2025 camt.018.001.05 GetBusinessDayInformationV05
Cash Management - Maintenance 2024 - 2025 528 February 2025
```

