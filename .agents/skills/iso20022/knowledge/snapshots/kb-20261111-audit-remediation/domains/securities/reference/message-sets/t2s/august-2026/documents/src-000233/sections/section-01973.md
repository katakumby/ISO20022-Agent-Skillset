---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01", "77.4 Message Building Blocks", "77.4.1 QueryDefinition <QryDef>", "77.4.1.2 SearchCriteria <SchCrit>"]
file_pages: [2693]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.032.001.01"]
---

# 77.4.1.2 SearchCriteria <SchCrit>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2693 to 2693.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2693

```text
CodeName Name Definition
STTS Status Response will include limited details
including the status on the movements
reported.
77.4.1.2  SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to extract the cancellation instructions for intra-position movements or
settlement instructions information.
SearchCriteria <SchCrit> contains the following SecuritiesCancellationQueryCriteria1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CancellationRequestIdentification <CxlReqId> [0..*] Text 2693
   InstructionQueryType <InstrQryTp> [1..1] CodeSet 2694
   ProcessingStatus <PrcgSts> [0..*]  2694
{Or     Code <Cd> [1..1] CodeSet 2694
Or}     Proprietary <Prtry> [1..1] ± 2695
   SafekeepingAccount <SfkpgAcct> [0..*] ± 2695
   AccountOwner <AcctOwnr> [0..*] ± 2695
   MessageOriginator <MsgOrgtr> [0..*] ± 2695
   CreationDateTime <CreDtTm> [0..1]  2696
{Or     Date <Dt> [1..1]  2696
{Or       FromDate <FrDt> [1..1] Date 2697
Or       ToDate <ToDt> [1..1] Date 2697
Or       FromToDate <FrToDt> [1..1] ± 2697
Or       EqualDate <EQDt> [1..1] Date 2697
Or}       NotEqualDate <NEQDt> [1..1] Date 2697
Or}     DateTime <DtTm> [1..1]  2697
{Or       FromDateTime <FrDtTm> [1..1] DateTime 2698
Or       ToDateTime <ToDtTm> [1..1] DateTime 2698
Or       FromToDateTime <FrToDtTm> [1..1] ± 2698
Or       EqualDateTime <EQDtTm> [1..1] DateTime 2698
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 2698
77.4.1.2.1  CancellationRequestIdentification <CxlReqId>
Presence: [0..*]
Definition: Collective reference identifying a set of messages.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.032.001.01
SecuritiesTransactionCancellationRequestQueryV0
1
Target2-Securities 2693 August 2026
```

