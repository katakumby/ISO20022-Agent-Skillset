---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["24 camt.046.001.08 GetReservationV08", "24.4 Message Building Blocks", "24.4.2 ReservationQueryDefinition <RsvatnQryDef>", "24.4.2.1 QueryType <QryTp>"]
file_pages: [627]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.046.001.08"]
---

# 24.4.2.1 QueryType <QryTp>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 627 to 627.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 627

```text
ReservationQueryDefinition <RsvatnQryDef> contains the following ReservationQuery6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryType <QryTp> [0..1] CodeSet 627
   ReservationCriteria <RsvatnCrit> [0..1]  628
{Or     QueryName <QryNm> [1..1] Text 629
Or}     NewCriteria <NewCrit> [1..1]  C4 629
       NewQueryName <NewQryNm> [0..1] Text 630
       SearchCriteria <SchCrit> [0..*]  631
         DateTime <DtTm> [0..1]  631
{Or           FromDateTime <FrDtTm> [1..1] DateTime 631
Or           ToDateTime <ToDtTm> [1..1] DateTime 632
Or           FromToDateTime <FrToDtTm> [1..1] ± 632
Or           EqualDateTime <EQDtTm> [1..1] DateTime 632
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 632
         SystemIdentification <SysId> [0..1] ± 632
         DefaultReservationType <DfltRsvatnTp> [0..*]  632
{Or           Code <Cd> [1..1] CodeSet 633
Or}           Proprietary <Prtry> [1..1] Text 633
         CurrentReservationType <CurRsvatnTp> [0..*]  633
{Or           Code <Cd> [1..1] CodeSet 633
Or}           Proprietary <Prtry> [1..1] Text 633
         AccountOwner <AcctOwnr> [0..1] ± 633
         AccountIdentification <AcctId> [0..1] ± 634
       ReturnCriteria <RtrCrit> [0..1]  634
         StartDateTimeIndicator <StartDtTmInd> [0..1] Indicator 634
         StatusIndicator <StsInd> [0..1] Indicator 635
24.4.2.1  QueryType <QryTp>
Presence: [0..1]
Definition: Specifies the type of matching items to be returned in the response to the query.
Datatype: "QueryType2Code" on page 872
CodeName Name Definition
ALLL All Specifies that the query requests that all
matching items be returned.
Approved by the Payments SEG on 04 February 2025 camt.046.001.08 GetReservationV08
Cash Management - Maintenance 2024 - 2025 627 February 2025
```

