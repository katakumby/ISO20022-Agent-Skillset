---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.9 FinancialInstrument <FinInstrm>", "22.1.13.2.9.3 Other <Othr>", "22.1.13.2.9.3.3 DerivativeInstrumentAttributes <DerivInstrmAttrbts>", "22.1.13.2.9.3.3.3 UnderlyingInstrument <UndrlygInstrm>", "22.1.13.2.9.3.3.3.1 Swap <Swp>", "22.1.13.2.9.3.3.3.1.2 SwapOut <SwpOut>"]
file_pages: [385]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.9.3.3.3.1.2 SwapOut <SwpOut>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 385 to 385.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 385

```text
SwapIn <SwpIn> contains one of the following elements (see
"FinancialInstrumentIdentification7Choice" on page 331 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Single <Sngl> [1..1] ± 332
Or}   Basket <Bskt> [1..1]  332
     ISIN <ISIN> [0..*] IdentifierSet 332
     Index <Indx> [0..*] ± 332
22.1.13.2.9.3.3.3.1.2  SwapOut <SwpOut>
Presence: [0..1]
Definition: Instrument paid by the buyer.
SwapOut <SwpOut> contains one of the following elements (see
"FinancialInstrumentIdentification7Choice" on page 331 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Single <Sngl> [1..1] ± 332
Or}   Basket <Bskt> [1..1]  332
     ISIN <ISIN> [0..*] IdentifierSet 332
     Index <Indx> [0..*] ± 332
22.1.13.2.9.3.3.3.2  Other <Othr>
Presence: [1..1]
Definition: Underlying of any other type of transaction.
Other <Othr> contains one of the following elements (see "FinancialInstrumentIdentification7Choice"
on page 331 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Single <Sngl> [1..1] ± 332
Or}   Basket <Bskt> [1..1]  332
     ISIN <ISIN> [0..*] IdentifierSet 332
     Index <Indx> [0..*] ± 332
22.1.13.2.9.3.3.4  OptionType <OptnTp>
Presence: [0..1]
Definition: Specifies whether it is a call option (right to purchase a specific underlying asset) or a put
option (right to sell a specific underlying asset).
Datatype: "OptionType2Code" on page 442
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
385 July 2025
```

