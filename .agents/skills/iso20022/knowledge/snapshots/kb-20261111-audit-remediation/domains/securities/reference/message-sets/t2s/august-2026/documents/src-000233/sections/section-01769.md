---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.2 Status <Sts>", "71.4.1.2.2.1 Type <Tp>", "71.4.1.2.2.1.5 Settled <Sttld>"]
file_pages: [2432]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.2.1.5 Settled <Sttld>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2432 to 2432.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2432

```text
71.4.1.2.2.1.5  Settled <Sttld>
Presence: [0..1]
Definition: Defines that the transaction has been settled.
Impacted by: C3 "AdditionalReasonInforrmationRule"
Settled <Sttld> contains the following elements (see "ProprietaryReason4" on page 3139 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 3140
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3140
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
71.4.1.2.2.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Specified date period of the status.
DatePeriod <DtPrd> contains one of the following DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  2432
{Or     FromDate <FrDt> [1..1] Date 2433
Or     ToDate <ToDt> [1..1] Date 2433
Or     FromToDate <FrToDt> [1..1] ± 2433
Or     EqualDate <EQDt> [1..1] Date 2433
Or}     NotEqualDate <NEQDt> [1..1] Date 2433
Or}   DateTime <DtTm> [1..1]  2433
{Or     FromDateTime <FrDtTm> [1..1] DateTime 2434
Or     ToDateTime <ToDtTm> [1..1] DateTime 2434
Or     FromToDateTime <FrToDtTm> [1..1] ± 2434
Or     EqualDateTime <EQDtTm> [1..1] DateTime 2434
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 2434
71.4.1.2.2.2.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2432 August 2026
```

