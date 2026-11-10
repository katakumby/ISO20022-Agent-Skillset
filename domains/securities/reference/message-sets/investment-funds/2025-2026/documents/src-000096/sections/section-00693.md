---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.21 DrawdownTranche <DrwdwnTrch>", "34.4.4.21.14 CappedLimits <CapdLmts>"]
file_pages: [935]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.21.14 CappedLimits <CapdLmts>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 935 to 935.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 935

```text
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
34.4.4.21.14  CappedLimits <CapdLmts>
Presence: [0..1]
Definition: Limits of the capped drawdown.
CappedLimits <CapdLmts> contains the following Capped1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StartDate <StartDt> [0..1] Date 935
   IncomeLimitCurrentPeriod <IncmLmtCurPrd> [0..1] Amount C1 935
   IncomeCurrentPeriod <IncmCurPrd> [0..1] Amount C1 935
   IncomeLimitNextPeriod <IncmLmtNxtPrd> [0..1] Amount C1 936
   AdditionalInformation <AddtlInf> [0..*] ± 936
34.4.4.21.14.1  StartDate <StartDt>
Presence: [0..1]
Definition: Start date of current reference period
Datatype: "ISODate" on page 5388
34.4.4.21.14.2  IncomeLimitCurrentPeriod <IncmLmtCurPrd>
Presence: [0..1]
Definition: Income limit for the current period.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
34.4.4.21.14.3  IncomeCurrentPeriod <IncmCurPrd>
Presence: [0..1]
Definition: Income taken in the current income year.
Impacted by: C1 "ActiveCurrency"
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 935 May 2026
```

