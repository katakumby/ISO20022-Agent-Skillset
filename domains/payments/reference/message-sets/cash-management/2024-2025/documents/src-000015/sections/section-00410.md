---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["19 camt.020.001.04 GetGeneralBusinessInformationV04", "19.4 Message Building Blocks", "19.4.2 GeneralBusinessInformationQueryDefinition <GnlBizInfQryDef>", "19.4.2.2 GeneralBusinessInformationCriteria <GnlBizInfCrit>", "19.4.2.2.2 NewCriteria <NewCrit>", "19.4.2.2.2.1 NewQueryName <NewQryNm>"]
file_pages: [563]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.020.001.04"]
---

# 19.4.2.2.2.1 NewQueryName <NewQryNm>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 563 to 563.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 563

```text
Impacted by: C1 "ReturnCriteriaAndOrSearchCriteriaRule"
NewCriteria <NewCrit> contains the following BusinessInformationCriteria1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NewQueryName <NewQryNm> [0..1] Text 563
   SearchCriteria <SchCrit> [0..*]  563
     Reference <Ref> [0..*] Text 564
     Subject <Sbjt> [0..*]  564
{Or       Equal <EQ> [1..1] Text 564
Or       NotEqual <NEQ> [1..1] Text 564
Or       Contain <CT> [1..1] Text 565
Or}       NotContain <NCT> [1..1] Text 565
     Qualifier <Qlfr> [0..*]  565
       IsFormatted <IsFrmtd> [0..1] Indicator 565
       Priority <Prty> [0..1] CodeSet 565
   ReturnCriteria <RtrCrit> [0..1]  565
     QualifierIndicator <QlfrInd> [0..1] Indicator 566
     SubjectIndicator <SbjtInd> [0..1] Indicator 566
     SubjectDetailsIndicator <SbjtDtlsInd> [0..1] Indicator 566
Constraints
• ReturnCriteriaAndOrSearchCriteriaRule
If ReturnCriteria is not present, then at least one occurrence of SearchCriteria must be present. If
ReturnCriteria is present, then any occurrence of SearchCriteria is optional.
19.4.2.2.2.1  NewQueryName <NewQryNm>
Presence: [0..1]
Definition: Name of the query defined by the search criteria and return criteria.
Datatype: "Max35Text" on page 889
19.4.2.2.2.2  SearchCriteria <SchCrit>
Presence: [0..*]
Definition: Defines the criteria based on which the information is extracted.
Approved by the Payments SEG on 04 February 2025 camt.020.001.04
GetGeneralBusinessInformationV04
Cash Management - Maintenance 2024 - 2025 563 February 2025
```

