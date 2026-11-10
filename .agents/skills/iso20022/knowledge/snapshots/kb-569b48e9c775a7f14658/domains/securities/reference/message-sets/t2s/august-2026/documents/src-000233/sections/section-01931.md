---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01", "75.2 Structure"]
file_pages: [2643]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.030.001.01"]
---

# 75.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2643 to 2643.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2643

```text
75.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmCondsModReqQry> [1..1]  
   QueryDefinition <QryDef> [1..1]  2644
     QueryType <QryTp> [1..1] CodeSet 2645
     SearchCriteria <SchCrit> [1..1]  2646
       ModificationRequestIdentification <ModReqId> [0..*] Text 2646
       InstructionQueryType <InstrQryTp> [1..1] CodeSet 2646
       ProcessingStatus <PrcgSts> [0..*] ± 2647
       SafekeepingAccount <SfkpgAcct> [0..*] ± 2647
       AccountOwner <AcctOwnr> [0..*] ± 2647
       MessageOriginator <MsgOrgtr> [0..*] ± 2648
       CreationDateTime <CreDtTm> [0..1]  2648
{Or         Date <Dt> [1..1]  2648
{Or           FromDate <FrDt> [1..1] Date 2649
Or           ToDate <ToDt> [1..1] Date 2649
Or           FromToDate <FrToDt> [1..1] ± 2649
Or           EqualDate <EQDt> [1..1] Date 2649
Or}           NotEqualDate <NEQDt> [1..1] Date 2649
Or}         DateTime <DtTm> [1..1]  2649
{Or           FromDateTime <FrDtTm> [1..1] DateTime 2650
Or           ToDateTime <ToDtTm> [1..1] DateTime 2650
Or           FromToDateTime <FrToDtTm> [1..1] ± 2650
Or           EqualDateTime <EQDtTm> [1..1] DateTime 2650
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 2650
   SupplementaryData <SplmtryData> [0..*] ± C3 2651
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.030.001.01
SecuritiesSettlementConditionsModificationRequest
QueryV01
Target2-Securities 2643 August 2026
```

