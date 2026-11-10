---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.2 Status <Sts>", "3.4.1.2.2.1 Type <Tp>", "3.4.1.2.2.1.5 Settled <Sttld>"]
file_pages: [36]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.2.1.5 Settled <Sttld>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 36 to 36.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 36

```text
3.4.1.2.2.1.5  Settled <Sttld>
Presence: [0..1]
Definition: Defines that the transaction has been settled.
Impacted by: C3 "AdditionalReasonInforrmationRule"
Settled <Sttld> contains the following elements (see "ProprietaryReason4" on page 470 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 470
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 470
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
3.4.1.2.2.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Specified date period of the status.
DatePeriod <DtPrd> contains one of the following DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  36
{Or     FromDate <FrDt> [1..1] Date 37
Or     ToDate <ToDt> [1..1] Date 37
Or     FromToDate <FrToDt> [1..1] ± 37
Or     EqualDate <EQDt> [1..1] Date 37
Or}     NotEqualDate <NEQDt> [1..1] Date 37
Or}   DateTime <DtTm> [1..1]  37
{Or     FromDateTime <FrDtTm> [1..1] DateTime 38
Or     ToDateTime <ToDtTm> [1..1] DateTime 38
Or     FromToDateTime <FrToDtTm> [1..1] ± 38
Or     EqualDateTime <EQDtTm> [1..1] DateTime 38
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 38
3.4.1.2.2.2.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 36 March 2026
```

