---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.12 ForeignExchangeDetails <FXDtls>"]
file_pages: [1743]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.12 ForeignExchangeDetails <FXDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1743 to 1743.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1743

```text
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
41.4.4.8.12  ForeignExchangeDetails <FXDtls>
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
ForeignExchangeDetails <FXDtls> contains the following ForeignExchangeTerms44 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C3 1743
   QuotedCurrency <QtdCcy> [1..1] CodeSet C3 1744
   ExchangeRate <XchgRate> [1..1] Rate 1744
   QuotationDate <QtnDt> [0..1] DateTime 1744
   QuotingInstitution <QtgInstn> [0..1] ± 1745
41.4.4.8.12.1  UnitCurrency <UnitCcy>
Presence: [1..1]
Definition: Currency from which the quoted currency is converted in an exchange rate calculation.
1 x <UnitCcy> = <XchgRate> x <QtdCcy>.
Impacted by: C3 "ActiveCurrency"
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1743 May 2026
```

