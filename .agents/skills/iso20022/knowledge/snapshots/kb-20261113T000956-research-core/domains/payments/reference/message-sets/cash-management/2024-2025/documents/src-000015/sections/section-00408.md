---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["19 camt.020.001.04 GetGeneralBusinessInformationV04", "19.4 Message Building Blocks", "19.4.2 GeneralBusinessInformationQueryDefinition <GnlBizInfQryDef>", "19.4.2.1 QueryType <QryTp>"]
file_pages: [561]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.020.001.04"]
---

# 19.4.2.1 QueryType <QryTp>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 561 to 561.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 561

```text
GeneralBusinessInformationQueryDefinition <GnlBizInfQryDef> contains the following
BusinessInformationQueryDefinition3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryType <QryTp> [0..1] CodeSet 561
   GeneralBusinessInformationCriteria <GnlBizInfCrit> [0..1]  562
{Or     QueryName <QryNm> [1..1] Text 562
Or}     NewCriteria <NewCrit> [1..1]  C1 562
       NewQueryName <NewQryNm> [0..1] Text 563
       SearchCriteria <SchCrit> [0..*]  563
         Reference <Ref> [0..*] Text 564
         Subject <Sbjt> [0..*]  564
{Or           Equal <EQ> [1..1] Text 564
Or           NotEqual <NEQ> [1..1] Text 564
Or           Contain <CT> [1..1] Text 565
Or}           NotContain <NCT> [1..1] Text 565
         Qualifier <Qlfr> [0..*]  565
           IsFormatted <IsFrmtd> [0..1] Indicator 565
           Priority <Prty> [0..1] CodeSet 565
       ReturnCriteria <RtrCrit> [0..1]  565
         QualifierIndicator <QlfrInd> [0..1] Indicator 566
         SubjectIndicator <SbjtInd> [0..1] Indicator 566
         SubjectDetailsIndicator <SbjtDtlsInd> [0..1] Indicator 566
19.4.2.1  QueryType <QryTp>
Presence: [0..1]
Definition: Specifies the type of matching items to be returned in the response to the query.
Datatype: "QueryType2Code" on page 872
CodeName Name Definition
ALLL All Specifies that the query requests that all
matching items be returned.
CHNG Changed Specifies that the query requests that
only new matching items since the last
similar query be returned.
MODF Modified Specifies that the query requests that
only items that have changed since the
last query be returned.
Approved by the Payments SEG on 04 February 2025 camt.020.001.04
GetGeneralBusinessInformationV04
Cash Management - Maintenance 2024 - 2025 561 February 2025
```

