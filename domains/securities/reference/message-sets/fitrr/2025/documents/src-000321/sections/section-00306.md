---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.11 Price", "22.1.11.6 SecuritiesTransactionPrice2Choice", "22.1.11.6.4 BasisPoints <BsisPts>"]
file_pages: [356, 357]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.11.6.4 BasisPoints <BsisPts>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 356 to 357.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 356

```text
22.1.11.6.4  BasisPoints <BsisPts>
Presence: [1..1]
Definition: Price expressed as basis points.
Datatype: "DecimalNumber" on page 451
22.1.12 Rate
22.1.12.1  BenchmarkCurveName6Choice
Definition: Choice of format for benchmark curve name.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 356
Or   Index <Indx> [1..1] CodeSet 356
Or}   Name <Nm> [1..1] Text 358
22.1.12.1.1  ISIN <ISIN>
Presence: [1..1]
Definition: International Securities Identification Number (ISIN) identifier of an index / benchmark.
Datatype: "ISINOct2015Identifier" on page 450
22.1.12.1.2  Index <Indx>
Presence: [1..1]
Definition: Name of the index / benchmark of a floating rate bond.
Datatype: "BenchmarkCurveName2Code" on page 432
CodeName Name Definition
WIBO WIBOR Warsaw Interbank Offered Rate.
TREA Treasury Treasury benchmark that comes in three
types: the yield curve, the par curve, and
the spot curve. All curves also have a
constituent time series.
TIBO TIBOR Tokyo Interbank Offered Rate.
TLBO TELBOR Tel Aviv Interbank Offered Rate.
SWAP SWAP In curve construction, Swap is the long
portion of the curve constituting about 3
years to 30 years term.
The exchange of one security, currency
or interest rate for another to change the
maturity (bonds), or quality of issues
(stocks or bonds), or because
investment objectives have changed.
STBO STIBOR Stockholm Interbank Offered Rate.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
356 July 2025
```

## File page 357

```text
CodeName Name Definition
PRBO PRIBOR Czech Fixing of Interest Rates on
Interbank Deposits.
PFAN Pfandbriefe Pfandbriefe security is a collateralised
bullet bond backed by either mortgage
loans or loans to the public sector.
Pfandbriefe differ from traditional asset-
backed securities in significant ways.
The most important difference is that
Pfandbriefe carry no pre-payment risk
since they remain on the balance sheet
of the issuing institution. Therefore, their
spreads over sovereign bonds are
attributable to liquidity and credit quality
alone. New indices have been created
and existing indices have been modified
in response to the growing importance of
the Pfandbriefe market. The Deutsche
Borse has three synthetic indices called
REX, JEX, and PEX. The Pfandbriefe
curve is used as a reference for credit as
well as mortgage market.
NIBO NIBOR Norwegian Interbank Offered Rate.
MAAA MuniAAA Benchmark curve used for municipals
based on the best credit rating for
municipal market debt.
MOSP MOSPRIM Moscow Prime Offered Rate.
LIBO LIBOR London Interbank Offered Rate, the
interest rate that major international
banks in London charge each other for
borrowing.
LIBI LIBID Rate at which major international banks
are willing to take deposits from one
another, is normally 1/8 percent below
LIBOR.
London InterBank Bid Rate, the rate bid
by banks on Eurocurrency deposits; the
international rate that banks lend to other
banks.
JIBA JIBAR Johannesburg Interbank Agreed Rate.
ISDA ISDAFIX Worldwide common reference rate value
for fixed interest rate swap rates, as
defined by the International Swaps and
Derivatives Association (ISDA).
GCFR GCFRepo GCF Repo Index, the Depository Trust &
Clearing Corporation (DTCC) general
collateral finance repurchase
agreements index.
FUSW FutureSWAP Portion of a synthetic curve that is
composed of Eurodollar or Treasury or
similar Futures and Swap rates. The
term usually begins at 3 months to 2
years for the futures strip component
with the Swaps filling in the points to 10
years and beyond.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
357 July 2025
```

