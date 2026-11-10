---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.8 AccountDetails <AcctDtls>", "30.4.9.9 RequestedSettlementDate <ReqdSttlmDt>"]
file_pages: [765]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.9.9 RequestedSettlementDate <ReqdSttlmDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 765 to 765.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 765

```text
Datatype: "ISODate" on page 5388
30.4.9.9  RequestedSettlementDate <ReqdSttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are to be exchanged at the International Central
Securities Depository (ICSD) or Central Securities Depository (CSD).
Datatype: "ISODate" on page 5388
30.4.9.10  EffectiveSettlementDate <FctvSttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities were exchanged at the International Central Securities
Depository (ICSD) or Central Securities Depository (CSD).
EffectiveSettlementDate <FctvSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
30.4.9.11  SettlementAmount <SttlmAmt>
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
30.4.9.12  StampDuty <StmpDty>
Presence: [0..1]
Definition: Specifies if the settlement amount includes the stamp duty amount.
Datatype: "StampDutyType2Code" on page 5364
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 765 May 2026
```

