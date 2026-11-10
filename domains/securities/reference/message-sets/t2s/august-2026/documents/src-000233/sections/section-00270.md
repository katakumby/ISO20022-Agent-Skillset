---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["16 camt.078.001.02 IntraBalanceMovementQueryV02", "16.4 Message Building Blocks", "16.4.2 QueryDefinition <QryDef>", "16.4.2.2 SearchCriteria <SchCrit>", "16.4.2.2.1 References <Refs>", "16.4.2.2.1.5 PoolIdentification <PoolId>"]
file_pages: [357]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 16.4.2.2.1.5 PoolIdentification <PoolId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 357 to 357.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 357

```text
Definition: Identification of the transaction as assigned by the processor.
Datatype: "Max35Text" on page 3328
16.4.2.2.1.5  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
16.4.2.2.1.6  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [1..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 3328
16.4.2.2.2  Status <Sts>
Presence: [0..1]
Definition: Provides the status of settlement of a transaction.
Status <Sts> contains the following IntraBalanceQueryStatus3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  358
     ProcessingStatus <PrcgSts> [0..*] ± 358
     SettlementStatus <SttlmSts> [0..*] ± 358
     Settled <Sttld> [0..1] ± C3 358
   DatePeriod <DtPrd> [0..1]  359
{Or     Date <Dt> [1..1]  359
{Or       FromDate <FrDt> [1..1] Date 359
Or       ToDate <ToDt> [1..1] Date 360
Or       FromToDate <FrToDt> [1..1] ± 360
Or       EqualDate <EQDt> [1..1] Date 360
Or}       NotEqualDate <NEQDt> [1..1] Date 360
Or}     DateTime <DtTm> [1..1]  360
{Or       FromDateTime <FrDtTm> [1..1] DateTime 360
Or       ToDateTime <ToDtTm> [1..1] DateTime 361
Or       FromToDateTime <FrToDtTm> [1..1] ± 361
Or       EqualDateTime <EQDtTm> [1..1] DateTime 361
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 361
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 357 August 2026
```

