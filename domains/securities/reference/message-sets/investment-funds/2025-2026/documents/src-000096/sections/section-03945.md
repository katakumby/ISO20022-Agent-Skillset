---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.4 Tax38", "66.1.47.4.1 Type <Tp>", "66.1.47.4.1.1 Code <Cd>"]
file_pages: [5238]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.4.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5238 to 5238.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5238

```text
Type <Tp> contains one of the following TaxType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5238
Or}   Proprietary <Prtry> [1..1] ± 5238
66.1.47.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of tax expressed as a code.
Datatype: "TaxType16Code" on page 5374
CodeName Name Definition
COAX ConsumptionTax Tax that is levied on goods and services
purchased by customers, and is added
to the retail price.
CTAX TaxCredit Direct reduction of an individual's tax
liability.
EUTR EUTaxRetention Tax withheld at source in the framework
of the European Directive on taxation of
savings in the form of interest payments.
LEVY PaymentLevyTax Tax levied on a payment.
LOCL LocalTax Tax that is charged by a local settlement
system or local jurisdiction.
NATI NationalTax Tax is a national tax.
PROV Provincial Tax is a provincial tax.
STAM StampDuty Tax is on certain documents and
transactions.
STAT StateTax Tax is a state tax.
STEX StockExchangeTax Tax collected by a stock exchange.
TRAN TransferTax Tax levied on a transfer.
TRAX TransactionTax Tax levied on a transaction.
VATA ValueAddedTax Tax is a value added tax.
WITH WithholdingTax Tax is on income deducted at source,
which the paying agent is legally obliged
to deduct from its payments of interest
on deposits and other proceeds of a
financial instrument.
NKAP CapitalLossCredit Tax recovery is due to capital loss.
KAPA CapitalGainTax Tax is on a capital gain (realised and
unrealised), that is, the profit that is
gained from the sale of a financial
instrument.
66.1.47.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5238 May 2026
```

