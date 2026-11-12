---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.13 AverageAcquisitionPrice <AvrgAcqstnPric>"]
file_pages: [1060]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.13 AverageAcquisitionPrice <AvrgAcqstnPric>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1060 to 1060.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1060

```text
Datatype: "BusinessFlowType1Code" on page 5279
CodeName Name Definition
SLDP SingleLegDeliveringParty Single leg process initiated by the
delivering party.
SLRP SingleLegReceivingParty Single leg process initiated by the
receiving party.
DLPR DoubleLegProcess Double leg process.
35.4.14.10.13  AverageAcquisitionPrice <AvrgAcqstnPric>
Presence: [0..1]
Definition: Average cost per share of the security, including all fees.
Impacted by: C2 "ActiveOrHistoricCurrency", C17 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
35.4.14.10.14  TransferCurrency <TrfCcy>
Presence: [0..1]
Definition: Currency to be used to transfer the holdings. Some transfer agents register holdings grouped
by currency in addition to using the ISIN for multi-currency fund shares.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
35.4.14.10.15  TotalBookValue <TtlBookVal>
Presence: [0..1]
Definition: Net asset on the balance sheet, the total portfolio value minus or plus the unrealised gain or
loss.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1060 May 2026
```

