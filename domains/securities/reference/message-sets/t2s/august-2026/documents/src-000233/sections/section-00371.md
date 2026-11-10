---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02", "20.2 Structure"]
file_pages: [478]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.082.001.02"]
---

# 20.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 478 to 478.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 478

```text
20.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntCxlQry> [1..1]  
   Identification <Id> [0..1]  479
     Identification <Id> [1..1] Text 480
     CreationDateTime <CreDtTm> [0..1] ± 480
     CopyDuplicate <CpyDplct> [0..1] CodeSet 480
     MessageOriginator <MsgOrgtr> [0..1] ± 481
     MessageRecipient <MsgRcpt> [0..1] ± 481
   QueryDefinition <QryDef> [1..1]  481
     QueryType <QryTp> [1..1] CodeSet 482
     SearchCriteria <SchCrit> [1..1]  483
       CancellationRequestIdentification <CxlReqId> [0..*] Text 484
       ProcessingStatus <PrcgSts> [0..*]  484
{Or         Code <Cd> [1..1] CodeSet 485
Or}         Proprietary <Prtry> [1..1] ± 485
       CashAccount <CshAcct> [0..*]  485
{Or         Equal <EQ> [1..1] ± 486
Or         ContainText <CTTxt> [1..1] Text 486
Or}         NotContainText <NCTTxt> [1..1] Text 486
       CashAccountOwner <CshAcctOwnr> [0..*] ± 486
       CashAccountServicer <CshAcctSvcr> [0..1] ± 486
       MessageOriginator <MsgOrgtr> [0..*] ± 487
       CreationDateTime <CreDtTm> [0..1]  487
{Or         Date <Dt> [1..1]  488
{Or           FromDate <FrDt> [1..1] Date 488
Or           ToDate <ToDt> [1..1] Date 488
Or           FromToDate <FrToDt> [1..1] ± 489
Or           EqualDate <EQDt> [1..1] Date 489
Or}           NotEqualDate <NEQDt> [1..1] Date 489
Or}         DateTime <DtTm> [1..1]  489
{Or           FromDateTime <FrDtTm> [1..1] DateTime 489
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.082.001.02
IntraBalanceMovementCancellationQueryV02
Target2-Securities 478 August 2026
```

