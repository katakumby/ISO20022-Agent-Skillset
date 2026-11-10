---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["11 camt.080.001.02 IntraBalanceMovementModificationQueryV02", "11.4 Message Building Blocks", "11.4.2 QueryDefinition <QryDef>", "11.4.2.1 QueryType <QryTp>"]
file_pages: [237]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.080.001.02"]
---

# 11.4.2.1 QueryType <QryTp>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 237 to 237.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 237

```text
QueryDefinition <QryDef> contains the following IntraBalanceQueryDefinition12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryType <QryTp> [1..1] CodeSet 237
   SearchCriteria <SchCrit> [1..1]  238
     ModificationRequestIdentification <ModReqId> [0..*] Text 238
     ProcessingStatus <PrcgSts> [0..*] ± 239
     CashAccount <CshAcct> [0..*]  239
{Or       Equal <EQ> [1..1] ± 239
Or       ContainText <CTTxt> [1..1] Text 239
Or}       NotContainText <NCTTxt> [1..1] Text 239
     CashAccountOwner <CshAcctOwnr> [0..*] ± 240
     CashAccountServicer <CshAcctSvcr> [0..1] ± 240
     MessageOriginator <MsgOrgtr> [0..*] ± 240
     CreationDateTime <CreDtTm> [0..1]  241
{Or       Date <Dt> [1..1]  241
{Or         FromDate <FrDt> [1..1] Date 242
Or         ToDate <ToDt> [1..1] Date 242
Or         FromToDate <FrToDt> [1..1] ± 242
Or         EqualDate <EQDt> [1..1] Date 242
Or}         NotEqualDate <NEQDt> [1..1] Date 242
Or}       DateTime <DtTm> [1..1]  242
{Or         FromDateTime <FrDtTm> [1..1] DateTime 243
Or         ToDateTime <ToDtTm> [1..1] DateTime 243
Or         FromToDateTime <FrToDtTm> [1..1] ± 243
Or         EqualDateTime <EQDtTm> [1..1] DateTime 243
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 243
11.4.2.1  QueryType <QryTp>
Presence: [1..1]
Definition: Defines the type of query.
Datatype: "MovementResponseType1Code" on page 485
CodeName Name Definition
FULL Full Response will include full details on the
movements reported.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.080.001.02
IntraBalanceMovementModificationQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
237 March 2024
```

