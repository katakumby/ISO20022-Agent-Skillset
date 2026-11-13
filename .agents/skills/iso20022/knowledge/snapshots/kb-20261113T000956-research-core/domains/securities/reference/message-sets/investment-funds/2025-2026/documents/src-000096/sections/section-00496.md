---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.9.9 RequestedSettlementDate <ReqdSttlmDt>"]
file_pages: [677]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.9.9 RequestedSettlementDate <ReqdSttlmDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 677 to 677.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 677

```text
Datatype: "ISODate" on page 5388
28.4.9.9  RequestedSettlementDate <ReqdSttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be exchanged at the International Central
Securities Depository (ICSD) or Central Securities Depository (CSD).
Datatype: "ISODate" on page 5388
28.4.9.10  SettlementAmount <SttlmAmt>
Presence: [0..1]
Definition: Total amount of money paid/to be paid or received in exchange for the financial instrument.
Impacted by: C1 "ActiveCurrency", C10 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
28.4.9.11  StampDuty <StmpDty>
Presence: [0..1]
Definition: Specifies if the settlement amount includes the stamp duty amount.
Datatype: "StampDutyType2Code" on page 5364
CodeName Name Definition
ASTD Applicable Stamps duty is applicable.
SDRN NotApplicable Stamp duty not applicable.
28.4.9.12  NetAmount <NetAmt>
Presence: [0..1]
Definition: Deal amount.
Impacted by: C1 "ActiveCurrency", C10 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 677 May 2026
```

