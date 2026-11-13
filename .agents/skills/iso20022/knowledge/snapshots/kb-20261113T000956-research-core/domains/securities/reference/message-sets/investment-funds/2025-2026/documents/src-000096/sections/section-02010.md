---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.18 PartiallyExecutedIndicator <PrtlyExctdInd>"]
file_pages: [2832]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.18 PartiallyExecutedIndicator <PrtlyExctdInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2832 to 2832.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2832

```text
Datatype: "DeliveryReceiptType2Code" on page 5294
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
49.4.5.9.18  PartiallyExecutedIndicator <PrtlyExctdInd>
Presence: [1..1]
Definition: Indicates whether the order has been partially executed, that is, the confirmed quantity does
not match the ordered quantity for a given financial instrument.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
49.4.5.9.19  BestExecution <BestExctn>
Presence: [0..1]
Definition: Specifies that the execution was subject to best execution rules as defined by MiFID.
Datatype: "BestExecution1Code" on page 5278
CodeName Name Definition
BTEX Best Best execution rules were followed.
49.4.5.9.20  CumDividendIndicator <CumDvddInd>
Presence: [1..1]
Definition: Indicates whether the dividend is included, that is, cum-dividend, in the executed price. When
the dividend is not included, the price will be ex-dividend.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
49.4.5.9.21  InterimProfitAmount <IntrmPrftAmt>
Presence: [0..1]
Definition: Part of the price deemed as accrued income or profit rather than capital. The interim profit
amount is used for tax purposes.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2832 May 2026
```

