---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.21 DrawdownTranche <DrwdwnTrch>", "34.4.4.21.14 CappedLimits <CapdLmts>", "34.4.4.21.14.4 IncomeLimitNextPeriod <IncmLmtNxtPrd>"]
file_pages: [936]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.21.14.4 IncomeLimitNextPeriod <IncmLmtNxtPrd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 936 to 936.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 936

```text
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
34.4.4.21.14.4  IncomeLimitNextPeriod <IncmLmtNxtPrd>
Presence: [0..1]
Definition: Income limit for the next income year.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
34.4.4.21.14.5  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the cap.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
34.4.4.21.15  FlexibleDrawdownTriggeredDate <FlxblDrwdwnTrggrdDt>
Presence: [0..1]
Definition: Date on which the drawdown was triggered when the drawdown type is flexible.
Datatype: "ISODate" on page 5388
34.4.4.21.16  TrancheDate <TrchDt>
Presence: [0..1]
Definition: Date on which the tranche is actioned
Datatype: "ISODate" on page 5388
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 936 May 2026
```

