---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["19 camt.020.001.04 GetGeneralBusinessInformationV04", "19.4 Message Building Blocks", "19.4.2 GeneralBusinessInformationQueryDefinition <GnlBizInfQryDef>", "19.4.2.2 GeneralBusinessInformationCriteria <GnlBizInfCrit>"]
file_pages: [562]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.020.001.04"]
---

# 19.4.2.2 GeneralBusinessInformationCriteria <GnlBizInfCrit>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 562 to 562.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 562

```text
CodeName Name Definition
DELD Deleted Specifies that the query requests that
items that have been deleted since the
last query be returned.
19.4.2.2  GeneralBusinessInformationCriteria <GnlBizInfCrit>
Presence: [0..1]
Definition: Defines the general business information query criteria.
GeneralBusinessInformationCriteria <GnlBizInfCrit> contains one of the following
GeneralBusinessInformationCriteriaDefinition1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QueryName <QryNm> [1..1] Text 562
Or}   NewCriteria <NewCrit> [1..1]  C1 562
     NewQueryName <NewQryNm> [0..1] Text 563
     SearchCriteria <SchCrit> [0..*]  563
       Reference <Ref> [0..*] Text 564
       Subject <Sbjt> [0..*]  564
{Or         Equal <EQ> [1..1] Text 564
Or         NotEqual <NEQ> [1..1] Text 564
Or         Contain <CT> [1..1] Text 565
Or}         NotContain <NCT> [1..1] Text 565
       Qualifier <Qlfr> [0..*]  565
         IsFormatted <IsFrmtd> [0..1] Indicator 565
         Priority <Prty> [0..1] CodeSet 565
     ReturnCriteria <RtrCrit> [0..1]  565
       QualifierIndicator <QlfrInd> [0..1] Indicator 566
       SubjectIndicator <SbjtInd> [0..1] Indicator 566
       SubjectDetailsIndicator <SbjtDtlsInd> [0..1] Indicator 566
19.4.2.2.1  QueryName <QryNm>
Presence: [1..1]
Definition: Recalls the criteria (search and return criteria) defined in a preceding query.
Datatype: "Max35Text" on page 889
19.4.2.2.2  NewCriteria <NewCrit>
Presence: [1..1]
Definition: Defines the criteria based on which the information is extracted.
Approved by the Payments SEG on 04 February 2025 camt.020.001.04
GetGeneralBusinessInformationV04
Cash Management - Maintenance 2024 - 2025 562 February 2025
```

