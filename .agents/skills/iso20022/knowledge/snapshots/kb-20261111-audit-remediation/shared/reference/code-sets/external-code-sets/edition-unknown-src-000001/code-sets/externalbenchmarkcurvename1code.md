---
template: false
review_status: "needs-review"
document_kind: "external-code-set"
domain: "shared"
source_ids: ["src-000001"]
source_locations: ["#/definitions/ExternalBenchmarkCurveName1Code"]
code_set: "ExternalBenchmarkCurveName1Code"
source_edition: null
limitations: ["Publication label is supplied by filename only.", "Applicability to a specific message version is not established by a matching type name."]
source_editions: []
---

# ExternalBenchmarkCurveName1Code

Source: src-000001, JSON Pointer `#/definitions/ExternalBenchmarkCurveName1Code`. [2Q2026_externalcodesets_v3.json](../../../../../../raw-input/ExternalCodeSets/2Q2026_externalcodesets_v3.json).

## Definition and source notes

Specifies the external benchmark curve name code in the format of character string with a maximum length of 4 characters.
The list of valid codes is an external code list published separately.
External code sets can be downloaded from www.iso20022.org.
*`MAAA`-Benchmark curve used for municipals based on the best credit rating for municipal market debt.
*`FUSW`-Portion of a synthetic curve that is composed of Eurodollar or Treasury or similar Futures and Swap rates. The term usually begins at 3 months to 2 years for the futures strip component with the Swaps filling in the points to 10 years and beyond.
*`LIBI`-Rate at which major international banks are willing to take deposits from one another, is normally 1/8 percent below LIBOR.

London InterBank Bid Rate, the rate bid by banks on Eurocurrency deposits; the international rate that banks lend to other banks.
*`LIBO`-London Interbank Offered Rate, the interest rate that major international banks in London charge each other for borrowing.
*`SWAP`-In curve construction, Swap is the long portion of the curve constituting about 3 years to 30 years term.

The exchange of one security, currency or interest rate for another to change the maturity (bonds), or quality of issues (stocks or bonds), or because investment objectives have changed.
*`TREA`-Treasury benchmark that comes in three types: the yield curve, the par curve, and the spot curve. All curves also have a constituent time series.
*`EURI`-Euro Interbank Offer Rate is the rate at which Euro inter-bank term deposits within the Euro zone are offered by one prime bank to another prime bank.
*`PFAN`-Pfandbriefe security is a collateralised bullet bond backed by either mortgage loans or loans to the public sector. Pfandbriefe differ from traditional asset-backed securities in significant ways. The most important difference is that Pfandbriefe carry no pre-payment risk since they remain on the balance sheet of the issuing institution. Therefore, their spreads over sovereign bonds are attributable to liquidity and credit quality alone. New indices have been created and existing indices have been modified in response to the growing importance of the Pfandbriefe market. The Deutsche Borse has three synthetic indices called REX, JEX, and PEX. The Pfandbriefe curve is used as a reference for credit as well as mortgage market.
*`EONA`-Euro OverNight Index Average rate.
*`EONS`-Euro OverNight Index Average swap rate.
*`EUUS`-Rate for the eurodollars, time deposits denominated in U.S. dollars at banks outside the United States, and thus are not under the jurisdiction of the Federal Reserve.
*`EUCH`-Swiss Franc LIBOR rate.
*`TIBO`-Tokyo Interbank Offered Rate.
*`ISDA`-Worldwide common reference rate value for fixed interest rate swap rates, as defined by the International Swaps and Derivatives Association (ISDA).
*`GCFR`-GCF Repo Index, the Depository Trust & Clearing Corporation (DTCC) general collateral finance repurchase agreements index.
*`STBO`-Stockholm Interbank Offered Rate.
*`BBSW`-Australian Financial Markets Association (AFMA) Bank-Bill Reference Rate (BBSW).
*`JIBA`-Johannesburg Interbank Agreed Rate.
*`BUBO`-Budapest Interbank Offered Rate.
*`CDOR`-Canadian Dollar Offered Rate.
*`CIBO`-Copenhagen Interbank Offered Rate.
*`MOSP`-Moscow Prime Offered Rate.
*`NIBO`-Norwegian Interbank Offered Rate.
*`PRBO`-Czech Fixing of Interest Rates on Interbank Deposits.
*`TLBO`-Tel Aviv Interbank Offered Rate.
*`WIBO`-Warsaw Interbank Offered Rate.
*`ESTR`-Euro Short Term Rate
*`SOFR`-Secured Overnight Financing Rate.
*`SONA`-Sterling Over Night Index Average.
*`RCTR`-RBA Cash Rate Target  (RBATCTR).
*`CORA`-Canadian Overnight Repo Rate Average (CAONREPO).
*`BCOL`-Bank of Canada Overnight Lending Rate (CABROVER).
*`HKIO`-Hong Kong Interbank Offered Rate (HIHD01M).
*`BJUO`-Bank of Japan Uncollateralized Overnight Call Rate (MUTSCALM).
*`ETIO`-Euroyen Tokyo Interbank Offered Rate (EUYN03M).
*`EFFR`-Effective Federal Funds Rate (FEDL01).
*`OBFR`-Overnight Bank Funding Rate (OBFR01).
*`CZNA`-Czech National Bank Reference Interest Rate
*`TONA`-Tokyo Overnight Average Rate:
Interest rate benchmark - also known as a reference rate or a benchmark rate. It is a measure of the cost of borrowing in the Japanese yen unsecured overnight money market and is the near risk-free rate (RFR) for Japanese yen markets, administered and published by the Bank of Japan. It is sometimes referred to as “TONAR”. Bloomberg ticker is MUTKCALM, and ISDA ISDA FpML Floating rate index code is JPY-TONA.
*`TORF`-Tokyo Term Risk Free Rate:
Interest rate Benchmark based on the uncollateralized overnight call rate which involves almost no credit risk of financial institutions, based on the Japanese Yen "Risk-Free-Rate" (RFR), administered and published by QUICK Benchmarks, Inc.
*`SIBO`-Singapore Interbank Offered Rate.

*`SSOR`-Singapore Dollar Swap Offer Rate.
*`SORA`-Singapore Overnight Rate Average

## Source constraints

```json
{
  "type": "string",
  "minLength": 1,
  "maxLength": 4
}
```

## Complete enumeration

| Position | Exact code |
| --- | --- |
| 1 | MAAA |
| 2 | FUSW |
| 3 | LIBI |
| 4 | LIBO |
| 5 | SWAP |
| 6 | TREA |
| 7 | EURI |
| 8 | PFAN |
| 9 | EONA |
| 10 | EONS |
| 11 | EUUS |
| 12 | EUCH |
| 13 | TIBO |
| 14 | ISDA |
| 15 | GCFR |
| 16 | STBO |
| 17 | BBSW |
| 18 | JIBA |
| 19 | BUBO |
| 20 | CDOR |
| 21 | CIBO |
| 22 | MOSP |
| 23 | NIBO |
| 24 | PRBO |
| 25 | TLBO |
| 26 | WIBO |
| 27 | ESTR |
| 28 | SOFR |
| 29 | SONA |
| 30 | RCTR |
| 31 | CORA |
| 32 | BCOL |
| 33 | HKIO |
| 34 | BJUO |
| 35 | ETIO |
| 36 | EFFR |
| 37 | OBFR |
| 38 | CZNA |
| 39 | TONA |
| 40 | TORF |
| 41 | SIBO |
| 42 | SSOR |
| 43 | SORA |

## Review evidence

JSON structure parsed and all declared values preserved on 2026-11-08. Values and complete description are copied from this source publication. Edition applicability and code-description interpretation remain needs-review.

[Publication index](../index.md).

Publication identity and unenumerated-value limitations are tracked in [issue-000001](../../../../../../tracking/issues.md#issue-000001).
