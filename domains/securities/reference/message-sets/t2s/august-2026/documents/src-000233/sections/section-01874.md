---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["73 semt.028.001.01 IntraPositionMovementQueryV01", "73.4 Message Building Blocks", "73.4.1 QueryDefinition <QryDef>", "73.4.1.2 SearchCriteria <SchCrit>", "73.4.1.2.1 References <Refs>", "73.4.1.2.1.6 PoolIdentification <PoolId>"]
file_pages: [2579]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 73.4.1.2.1.6 PoolIdentification <PoolId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2579 to 2579.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2579

```text
Definition: Identification of the transaction as assigned by the processor.
Datatype: "Max35Text" on page 3328
73.4.1.2.1.6  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
73.4.1.2.1.7  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [1..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 3328
73.4.1.2.2  Status <Sts>
Presence: [0..1]
Definition: Provides the status of settlement of a transaction.
Status <Sts> contains the following IntraPositionQueryStatus3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  2580
     ProcessingStatus <PrcgSts> [0..*] ± 2580
     SettlementStatus <SttlmSts> [0..*] ± 2580
     Settled <Sttld> [0..1] ± C1 2580
   DatePeriod <DtPrd> [0..1]  2581
{Or     Date <Dt> [1..1]  2581
{Or       FromDate <FrDt> [1..1] Date 2581
Or       ToDate <ToDt> [1..1] Date 2582
Or       FromToDate <FrToDt> [1..1] ± 2582
Or       EqualDate <EQDt> [1..1] Date 2582
Or}       NotEqualDate <NEQDt> [1..1] Date 2582
Or}     DateTime <DtTm> [1..1]  2582
{Or       FromDateTime <FrDtTm> [1..1] DateTime 2582
Or       ToDateTime <ToDtTm> [1..1] DateTime 2583
Or       FromToDateTime <FrToDtTm> [1..1] ± 2583
Or       EqualDateTime <EQDtTm> [1..1] DateTime 2583
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 2583
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2579 August 2026
```

