---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.21 DrawdownTranche <DrwdwnTrch>", "34.4.4.21.7 AdditionalFundsDesignated <AddtlFndsDsgntd>"]
file_pages: [932]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.21.7 AdditionalFundsDesignated <AddtlFndsDsgntd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 932 to 932.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 932

```text
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
34.4.4.21.7  AdditionalFundsDesignated <AddtlFndsDsgntd>
Presence: [0..1]
Definition: Indicates whether any additional funds have been designated since the original arrangement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
34.4.4.21.8  PensionCommencementLumpSumRemaining <PnsnCmcmntLumpSumRmng>
Presence: [0..1]
Definition: Amount of the pension commencement lump sum (PCLS) remaining.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
34.4.4.21.9  PensionCommencementLumpSumDate <PnsnCmcmntLumpSumDt>
Presence: [0..1]
Definition: Date by which the pension commencement lump sum (PCLS) must be used.
Datatype: "ISODate" on page 5388
34.4.4.21.10  MultiplePensionCommencementLumpSums <MltplPnsnCmcmntLumpSums>
Presence: [0..1]
Definition: Indicates there have been multiple pension commencement lump sum (PCLS) payments.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 932 May 2026
```

