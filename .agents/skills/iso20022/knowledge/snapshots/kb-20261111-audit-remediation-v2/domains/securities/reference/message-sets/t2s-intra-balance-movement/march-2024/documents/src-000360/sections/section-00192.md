---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["11 camt.080.001.02 IntraBalanceMovementModificationQueryV02", "11.2 Structure"]
file_pages: [233]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.080.001.02"]
---

# 11.2 Structure

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 233 to 233.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 233

```text
11.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntModQry> [1..1]  
   Identification <Id> [0..1]  234
     Identification <Id> [1..1] Text 235
     CreationDateTime <CreDtTm> [0..1] ± 235
     CopyDuplicate <CpyDplct> [0..1] CodeSet 235
     MessageOriginator <MsgOrgtr> [0..1] ± 236
     MessageRecipient <MsgRcpt> [0..1] ± 236
   QueryDefinition <QryDef> [1..1]  236
     QueryType <QryTp> [1..1] CodeSet 237
     SearchCriteria <SchCrit> [1..1]  238
       ModificationRequestIdentification <ModReqId> [0..*] Text 238
       ProcessingStatus <PrcgSts> [0..*] ± 239
       CashAccount <CshAcct> [0..*]  239
{Or         Equal <EQ> [1..1] ± 239
Or         ContainText <CTTxt> [1..1] Text 239
Or}         NotContainText <NCTTxt> [1..1] Text 239
       CashAccountOwner <CshAcctOwnr> [0..*] ± 240
       CashAccountServicer <CshAcctSvcr> [0..1] ± 240
       MessageOriginator <MsgOrgtr> [0..*] ± 240
       CreationDateTime <CreDtTm> [0..1]  241
{Or         Date <Dt> [1..1]  241
{Or           FromDate <FrDt> [1..1] Date 242
Or           ToDate <ToDt> [1..1] Date 242
Or           FromToDate <FrToDt> [1..1] ± 242
Or           EqualDate <EQDt> [1..1] Date 242
Or}           NotEqualDate <NEQDt> [1..1] Date 242
Or}         DateTime <DtTm> [1..1]  242
{Or           FromDateTime <FrDtTm> [1..1] DateTime 243
Or           ToDateTime <ToDtTm> [1..1] DateTime 243
Or           FromToDateTime <FrToDtTm> [1..1] ± 243
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.080.001.02
IntraBalanceMovementModificationQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
233 March 2024
```

