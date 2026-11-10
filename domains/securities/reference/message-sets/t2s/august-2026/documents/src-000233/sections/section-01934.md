---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01", "75.4 Message Building Blocks", "75.4.1 QueryDefinition <QryDef>", "75.4.1.2 SearchCriteria <SchCrit>"]
file_pages: [2646]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.030.001.01"]
---

# 75.4.1.2 SearchCriteria <SchCrit>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2646 to 2646.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2646

```text
75.4.1.2  SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to extract the intra-position movement instruction information.
SearchCriteria <SchCrit> contains the following SecuritiesModificationQueryCriteria1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationRequestIdentification <ModReqId> [0..*] Text 2646
   InstructionQueryType <InstrQryTp> [1..1] CodeSet 2646
   ProcessingStatus <PrcgSts> [0..*] ± 2647
   SafekeepingAccount <SfkpgAcct> [0..*] ± 2647
   AccountOwner <AcctOwnr> [0..*] ± 2647
   MessageOriginator <MsgOrgtr> [0..*] ± 2648
   CreationDateTime <CreDtTm> [0..1]  2648
{Or     Date <Dt> [1..1]  2648
{Or       FromDate <FrDt> [1..1] Date 2649
Or       ToDate <ToDt> [1..1] Date 2649
Or       FromToDate <FrToDt> [1..1] ± 2649
Or       EqualDate <EQDt> [1..1] Date 2649
Or}       NotEqualDate <NEQDt> [1..1] Date 2649
Or}     DateTime <DtTm> [1..1]  2649
{Or       FromDateTime <FrDtTm> [1..1] DateTime 2650
Or       ToDateTime <ToDtTm> [1..1] DateTime 2650
Or       FromToDateTime <FrToDtTm> [1..1] ± 2650
Or       EqualDateTime <EQDtTm> [1..1] DateTime 2650
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 2650
75.4.1.2.1  ModificationRequestIdentification <ModReqId>
Presence: [0..*]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
75.4.1.2.2  InstructionQueryType <InstrQryTp>
Presence: [1..1]
Definition: Type of underlying transaction to be modified, such as an settlement instruction or an intra-
position movement.
Datatype: "InstructionQueryType1Code" on page 3256
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.030.001.01
SecuritiesSettlementConditionsModificationRequest
QueryV01
Target2-Securities 2646 August 2026
```

