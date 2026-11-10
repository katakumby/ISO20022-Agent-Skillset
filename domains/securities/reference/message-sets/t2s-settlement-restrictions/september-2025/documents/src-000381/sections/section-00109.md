---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01", "6.4 Message Building Blocks", "6.4.1 QueryDefinition <QryDef>", "6.4.1.2 SearchCriteria <SchCrit>"]
file_pages: [138]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.032.001.01"]
---

# 6.4.1.2 SearchCriteria <SchCrit>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 138 to 138.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 138

```text
CodeName Name Definition
STTS Status Response will include limited details
including the status on the movements
reported.
6.4.1.2  SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to extract the cancellation instructions for intra-position movements or
settlement instructions information.
SearchCriteria <SchCrit> contains the following SecuritiesCancellationQueryCriteria1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CancellationRequestIdentification <CxlReqId> [0..*] Text 138
   InstructionQueryType <InstrQryTp> [1..1] CodeSet 139
   ProcessingStatus <PrcgSts> [0..*]  139
{Or     Code <Cd> [1..1] CodeSet 139
Or}     Proprietary <Prtry> [1..1] ± 140
   SafekeepingAccount <SfkpgAcct> [0..*] ± 140
   AccountOwner <AcctOwnr> [0..*] ± 140
   MessageOriginator <MsgOrgtr> [0..*] ± 140
   CreationDateTime <CreDtTm> [0..1]  141
{Or     Date <Dt> [1..1]  141
{Or       FromDate <FrDt> [1..1] Date 142
Or       ToDate <ToDt> [1..1] Date 142
Or       FromToDate <FrToDt> [1..1] ± 142
Or       EqualDate <EQDt> [1..1] Date 142
Or}       NotEqualDate <NEQDt> [1..1] Date 142
Or}     DateTime <DtTm> [1..1]  142
{Or       FromDateTime <FrDtTm> [1..1] DateTime 143
Or       ToDateTime <ToDtTm> [1..1] DateTime 143
Or       FromToDateTime <FrToDtTm> [1..1] ± 143
Or       EqualDateTime <EQDtTm> [1..1] DateTime 143
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 143
6.4.1.2.1  CancellationRequestIdentification <CxlReqId>
Presence: [0..*]
Definition: Collective reference identifying a set of messages.
Approved by the Securities SEG on 21 August 2025 semt.032.001.01
SecuritiesTransactionCancellationRequestQueryV0
1
Target2-Securities - Settlement Restrictions 138 September 2025
```

