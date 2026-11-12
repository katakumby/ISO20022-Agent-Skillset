---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["18 camt.080.001.02 IntraBalanceMovementModificationQueryV02", "18.4 Message Building Blocks", "18.4.2 QueryDefinition <QryDef>", "18.4.2.1 QueryType <QryTp>"]
file_pages: [428]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.080.001.02"]
---

# 18.4.2.1 QueryType <QryTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 428 to 428.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 428

```text
QueryDefinition <QryDef> contains the following IntraBalanceQueryDefinition12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryType <QryTp> [1..1] CodeSet 428
   SearchCriteria <SchCrit> [1..1]  429
     ModificationRequestIdentification <ModReqId> [0..*] Text 429
     ProcessingStatus <PrcgSts> [0..*] ± 430
     CashAccount <CshAcct> [0..*]  430
{Or       Equal <EQ> [1..1] ± 430
Or       ContainText <CTTxt> [1..1] Text 430
Or}       NotContainText <NCTTxt> [1..1] Text 430
     CashAccountOwner <CshAcctOwnr> [0..*] ± 431
     CashAccountServicer <CshAcctSvcr> [0..1] ± 431
     MessageOriginator <MsgOrgtr> [0..*] ± 431
     CreationDateTime <CreDtTm> [0..1]  432
{Or       Date <Dt> [1..1]  432
{Or         FromDate <FrDt> [1..1] Date 433
Or         ToDate <ToDt> [1..1] Date 433
Or         FromToDate <FrToDt> [1..1] ± 433
Or         EqualDate <EQDt> [1..1] Date 433
Or}         NotEqualDate <NEQDt> [1..1] Date 433
Or}       DateTime <DtTm> [1..1]  433
{Or         FromDateTime <FrDtTm> [1..1] DateTime 434
Or         ToDateTime <ToDtTm> [1..1] DateTime 434
Or         FromToDateTime <FrToDtTm> [1..1] ± 434
Or         EqualDateTime <EQDtTm> [1..1] DateTime 434
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 434
18.4.2.1  QueryType <QryTp>
Presence: [1..1]
Definition: Defines the type of query.
Datatype: "MovementResponseType1Code" on page 3264
CodeName Name Definition
FULL Full Response will include full details on the
movements reported.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.080.001.02
IntraBalanceMovementModificationQueryV02
Target2-Securities 428 August 2026
```

