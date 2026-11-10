---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.2 Status <Sts>", "71.4.1.2.2.1 Type <Tp>"]
file_pages: [2430]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.2.1 Type <Tp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2430 to 2430.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2430

```text
Status <Sts> contains the following SettlementInstructionQueryStatus3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  2430
     ProcessingStatus <PrcgSts> [0..*] ± 2431
     InferredMatchingStatus <IfrrdMtchgSts> [0..*] ± 2431
     MatchingStatus <MtchgSts> [0..*] ± 2431
     SettlementStatus <SttlmSts> [0..*] ± 2431
     Settled <Sttld> [0..1] ± C3 2432
   DatePeriod <DtPrd> [0..1]  2432
{Or     Date <Dt> [1..1]  2432
{Or       FromDate <FrDt> [1..1] Date 2433
Or       ToDate <ToDt> [1..1] Date 2433
Or       FromToDate <FrToDt> [1..1] ± 2433
Or       EqualDate <EQDt> [1..1] Date 2433
Or}       NotEqualDate <NEQDt> [1..1] Date 2433
Or}     DateTime <DtTm> [1..1]  2433
{Or       FromDateTime <FrDtTm> [1..1] DateTime 2434
Or       ToDateTime <ToDtTm> [1..1] DateTime 2434
Or       FromToDateTime <FrToDtTm> [1..1] ± 2434
Or       EqualDateTime <EQDtTm> [1..1] DateTime 2434
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 2434
71.4.1.2.2.1  Type <Tp>
Presence: [1..1]
Definition: Defines the status type of query criteria.
Type <Tp> contains the following SettlementTransactionStatusType2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingStatus <PrcgSts> [0..*] ± 2431
   InferredMatchingStatus <IfrrdMtchgSts> [0..*] ± 2431
   MatchingStatus <MtchgSts> [0..*] ± 2431
   SettlementStatus <SttlmSts> [0..*] ± 2431
   Settled <Sttld> [0..1] ± C3 2432
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2430 August 2026
```

