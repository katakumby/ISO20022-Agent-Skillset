---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.14 AverageAcquisitionPrice <AvrgAcqstnPric>"]
file_pages: [1638]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.14 AverageAcquisitionPrice <AvrgAcqstnPric>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1638 to 1638.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1638

```text
Datatype: "BusinessFlowType1Code" on page 5279
CodeName Name Definition
SLDP SingleLegDeliveringParty Single leg process initiated by the
delivering party.
SLRP SingleLegReceivingParty Single leg process initiated by the
receiving party.
DLPR DoubleLegProcess Double leg process.
40.4.15.11.14  AverageAcquisitionPrice <AvrgAcqstnPric>
Presence: [0..1]
Definition: Average cost per share of the security, including all fees.
Impacted by: C1 "ActiveCurrency", C18 "CurrencyAmount"
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
40.4.15.11.15  TransferCurrency <TrfCcy>
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
40.4.15.11.16  TotalBookValue <TtlBookVal>
Presence: [0..1]
Definition: Net asset on the balance sheet, the total portfolio value minus or plus the unrealised gain or
loss.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1638 May 2026
```

