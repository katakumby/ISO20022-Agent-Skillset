---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01", "4.4 Message Building Blocks", "4.4.1 QueryDefinition <QryDef>", "4.4.1.1 QueryType <QryTp>"]
file_pages: [90]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.030.001.01"]
---

# 4.4.1.1 QueryType <QryTp>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 90 to 90.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 90

```text
QueryDefinition <QryDef> contains the following SecuritiesModificationQueryDefinition1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryType <QryTp> [1..1] CodeSet 90
   SearchCriteria <SchCrit> [1..1]  91
     ModificationRequestIdentification <ModReqId> [0..*] Text 91
     InstructionQueryType <InstrQryTp> [1..1] CodeSet 91
     ProcessingStatus <PrcgSts> [0..*] ± 92
     SafekeepingAccount <SfkpgAcct> [0..*] ± 92
     AccountOwner <AcctOwnr> [0..*] ± 92
     MessageOriginator <MsgOrgtr> [0..*] ± 93
     CreationDateTime <CreDtTm> [0..1]  93
{Or       Date <Dt> [1..1]  93
{Or         FromDate <FrDt> [1..1] Date 94
Or         ToDate <ToDt> [1..1] Date 94
Or         FromToDate <FrToDt> [1..1] ± 94
Or         EqualDate <EQDt> [1..1] Date 94
Or}         NotEqualDate <NEQDt> [1..1] Date 94
Or}       DateTime <DtTm> [1..1]  94
{Or         FromDateTime <FrDtTm> [1..1] DateTime 95
Or         ToDateTime <ToDtTm> [1..1] DateTime 95
Or         FromToDateTime <FrToDtTm> [1..1] ± 95
Or         EqualDateTime <EQDtTm> [1..1] DateTime 95
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 95
4.4.1.1  QueryType <QryTp>
Presence: [1..1]
Definition: Defines the type of query.
Datatype: "MovementResponseType1Code" on page 331
CodeName Name Definition
FULL Full Response will include full details on the
movements reported.
STTS Status Response will include limited details
including the status on the movements
reported.
Approved by the Securities SEG on 21 August 2025 semt.030.001.01
SecuritiesSettlementConditionsModificationRequest
QueryV01
Target2-Securities - Settlement Restrictions 90 September 2025
```

