---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["9 camt.078.001.02 IntraBalanceMovementQueryV02", "9.4 Message Building Blocks", "9.4.2 QueryDefinition <QryDef>", "9.4.2.2 SearchCriteria <SchCrit>", "9.4.2.2.1 References <Refs>", "9.4.2.2.1.5 PoolIdentification <PoolId>"]
file_pages: [166]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 9.4.2.2.1.5 PoolIdentification <PoolId>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 166 to 166.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 166

```text
Definition: Identification of the transaction as assigned by the processor.
Datatype: "Max35Text" on page 497
9.4.2.2.1.5  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 497
9.4.2.2.1.6  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [1..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 497
9.4.2.2.2  Status <Sts>
Presence: [0..1]
Definition: Provides the status of settlement of a transaction.
Status <Sts> contains the following IntraBalanceQueryStatus3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  167
     ProcessingStatus <PrcgSts> [0..*] ± 167
     SettlementStatus <SttlmSts> [0..*] ± 167
     Settled <Sttld> [0..1] ± C3 167
   DatePeriod <DtPrd> [0..1]  168
{Or     Date <Dt> [1..1]  168
{Or       FromDate <FrDt> [1..1] Date 168
Or       ToDate <ToDt> [1..1] Date 169
Or       FromToDate <FrToDt> [1..1] ± 169
Or       EqualDate <EQDt> [1..1] Date 169
Or}       NotEqualDate <NEQDt> [1..1] Date 169
Or}     DateTime <DtTm> [1..1]  169
{Or       FromDateTime <FrDtTm> [1..1] DateTime 169
Or       ToDateTime <ToDtTm> [1..1] DateTime 170
Or       FromToDateTime <FrToDtTm> [1..1] ± 170
Or       EqualDateTime <EQDtTm> [1..1] DateTime 170
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 170
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
166 March 2024
```

