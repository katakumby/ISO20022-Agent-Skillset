---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.10 CashSettlementDate <CshSttlmDt>"]
file_pages: [3067]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.10 CashSettlementDate <CshSttlmDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3067 to 3067.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3067

```text
50.4.4.9.10  CashSettlementDate <CshSttlmDt>
Presence: [0..1]
Definition: Date on which cash is available.
Datatype: "ISODate" on page 5388
50.4.4.9.11  SettlementMethod <SttlmMtd>
Presence: [0..1]
Definition: Method by which the transaction is settled.
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
50.4.4.9.12  ForeignExchangeDetails <FXDtls>
Presence: [0..1]
Definition: Information needed to process a currency exchange or conversion.
How the exchange rate is expressed determines which currency is the Unit Currency and Quoted
Currency. If the amounts concerned are EUR 1000 and USD 1300, the exchange rate may be
expressed as per either of the following examples:
EXAMPLE 1
UnitCurrency EUR
QuotedCurrency USD
ExchangeRate 1.300
EXAMPLE 2
UnitCurrency USD
QuotedCurrency EUR
ExchangeRate 0.769.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3067 May 2026
```

