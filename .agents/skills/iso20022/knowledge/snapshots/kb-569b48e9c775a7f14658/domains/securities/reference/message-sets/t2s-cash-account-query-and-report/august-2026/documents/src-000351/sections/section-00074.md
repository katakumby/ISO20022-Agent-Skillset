---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.3 ContractDates <CtrctDts>", "3.4.4.2.3.1 TargetGoLiveDate <TrgtGoLiveDt>"]
file_pages: [88]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.3.1 TargetGoLiveDate <TrgtGoLiveDt>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 88 to 88.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 88

```text
Definition: Specifies target and actual dates.
ContractDates <CtrctDts> contains the following AccountContract3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TargetGoLiveDate <TrgtGoLiveDt> [0..1] Date 88
   TargetClosingDate <TrgtClsgDt> [0..1] Date 88
   GoLiveDate <GoLiveDt> [0..1] Date 88
   ClosingDate <ClsgDt> [0..1] Date 88
   UrgencyFlag <UrgcyFlg> [0..1] Indicator 88
   RemovalIndicator <RmvlInd> [0..1] Indicator 89
3.4.4.2.3.1  TargetGoLiveDate <TrgtGoLiveDt>
Presence: [0..1]
Definition: Date on which the account and related basic services are expected to be operational for the
account owner.
Datatype: "ISODate" on page 179
3.4.4.2.3.2  TargetClosingDate <TrgtClsgDt>
Presence: [0..1]
Definition: Date on which the account and related services are expected to cease to be operational for
the account owner.
Datatype: "ISODate" on page 179
3.4.4.2.3.3  GoLiveDate <GoLiveDt>
Presence: [0..1]
Definition: Date on which the account and related basic services are effectively operational for the
account owner.
Datatype: "ISODate" on page 179
3.4.4.2.3.4  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Date on which the account and related services cease effectively to be operational for the
account owner.
Datatype: "ISODate" on page 179
3.4.4.2.3.5  UrgencyFlag <UrgcyFlg>
Presence: [0..1]
Definition: Indicator that the account opening/maintenance/closing process needs to be treated
urgently, that is, sooner than the terms established by the service level agreed between the account
holder customer and the account servicing institution.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 181):
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 88 August 2026
```

