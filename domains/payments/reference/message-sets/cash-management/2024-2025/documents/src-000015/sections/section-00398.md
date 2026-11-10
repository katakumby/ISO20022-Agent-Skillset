---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["18 camt.019.001.07 ReturnBusinessDayInformationV07", "18.4 Message Building Blocks", "18.4.2 ReportOrError <RptOrErr>", "18.4.2.1 BusinessReport <BizRpt>", "18.4.2.1.2 BusinessDayOrError <BizDayOrErr>", "18.4.2.1.2.1 BusinessDayInformation <BizDayInf>", "18.4.2.1.2.1.3 SystemInformationPerCurrency <SysInfPerCcy>", "18.4.2.1.2.1.3.1 SystemCurrency <SysCcy>"]
file_pages: [550]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.019.001.07"]
---

# 18.4.2.1.2.1.3.1 SystemCurrency <SysCcy>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 550 to 550.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 550

```text
SystemInformationPerCurrency <SysInfPerCcy> contains the following
SystemAvailabilityAndEvents3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemCurrency <SysCcy> [0..1] CodeSet C1 550
   SessionPeriod <SsnPrd> [0..1]  551
     FromTime <FrTm> [1..1] Time 551
     ToTime <ToTm> [1..1] Time 551
   Event <Evt> [0..*]  551
     Type <Tp> [1..1]  551
{Or       Code <Cd> [1..1] CodeSet 552
Or}       Proprietary <Prtry> [1..1] ± 552
     ScheduledTime <SchdldTm> [1..1] DateTime 552
     EffectiveTime <FctvTm> [0..1] DateTime 552
     StartTime <StartTm> [0..1] DateTime 552
     EndTime <EndTm> [0..1] DateTime 552
   ClosureInformation <ClsrInf> [0..*]  553
     Period <Prd> [0..1]  553
{Or       FromDateTime <FrDtTm> [1..1] DateTime 553
Or       ToDateTime <ToDtTm> [1..1] DateTime 553
Or}       DateTimeRange <DtTmRg> [1..1] ± 553
     Reason <Rsn> [1..1]  554
{Or       Code <Cd> [1..1] CodeSet 554
Or}       Proprietary <Prtry> [1..1] Text 554
18.4.2.1.2.1.3.1  SystemCurrency <SysCcy>
Presence: [0..1]
Definition: Currency which may be processed by the system. A system may process transactions in a
single currency or in multiple currencies.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 849
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 550 February 2025
```

