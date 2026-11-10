---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.001.001.05"
message_family: "reda.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.001.001.05"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "13 reda.001.001.05 PriceReportV05", "file_pages": [159, 221]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# reda.001.001.05 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 13 reda.001.001.05 PriceReportV05

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); file pp159–221; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 13 reda.001.001.05 PriceReportV05, Functionality, file p159.**

SCOPE
A report provider, for example, a transfer agent, fund accountant or market data provider, sends the
PriceReport message to the report recipient, for example, a fund management company, transfer agent,
market data provider, regulator or any other interested party to provide the net asset value and price
information for financial instruments on specific trade dates and, optionally, to quote price variation
information.
USAGE
The PriceReport message is sent by the report provider to the report recipient to:
- report prices for one or several different financial instruments for one or several different trade dates,
- report statistical information about the valuation of a financial instrument,
- inform another party that the quotation of a financial instrument is suspended,
- report prices that are used for other purposes than the execution of investment funds orders.
.
Outline
The PriceReportV05 MessageDefinition is composed of 10 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies a message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. MessagePagination
Pagination of the message.
F. PriceReportIdentification
Unique and unambiguous identifier for the price report, as assigned by the reporting party.
G. Function
Function of the price report, that is, whether the price report is a new price report or a replacement
of some kind.
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 159 May 2026

**src-000096, 13 reda.001.001.05 PriceReportV05, Functionality, file p160.**

H. CancellationIdentification
Unique and unambiguous identifier for the cancellation of the previous price report, as assigned by
the reporting party.
I. PriceValuationDetails
Information related to the price valuation of a financial instrument.
J. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 160 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.1 MessageDefinition Functionality](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00109.md) | 159–160 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00110.md) | 161–165 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00111.md) | 166–167 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00112.md) | 168–175 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00113.md) | 176–177 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.4 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 13.4.9.4.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00114.md) | 178–178 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.4 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 13.4.9.4.1 Identification &lt;Id&gt; / 13.4.9.4.1.2 SEDOL &lt;SEDOL&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00115.md) | 179–179 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.4 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 13.4.9.4.1 Identification &lt;Id&gt; / 13.4.9.4.1.9 Wertpapier &lt;Wrtppr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00116.md) | 180–180 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.4 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 13.4.9.4.1 Identification &lt;Id&gt; / 13.4.9.4.1.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00117.md) | 181–181 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.4 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 13.4.9.4.5 DenominationCurrency &lt;DnmtnCcy&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00118.md) | 182–182 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.4 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 13.4.9.4.9 DualFundIndicator &lt;DualFndInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00119.md) | 183–183 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.5 FundManagementCompany &lt;FndMgmtCpny&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00120.md) | 184–184 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.8 NextValuationDateTime &lt;NxtValtnDtTm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00121.md) | 185–185 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.12 OfficialValuationIndicator &lt;OffclValtnInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00122.md) | 186–188 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.1 PriceType &lt;PricTp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00123.md) | 189–189 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.1 PriceType &lt;PricTp&gt; / 13.4.9.14.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00124.md) | 190–190 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.3 ValueInInvestmentCurrency &lt;ValInInvstmtCcy&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00125.md) | 191–191 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.8 EstimatedPriceIndicator &lt;EstmtdPricInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00126.md) | 192–192 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.11 TaxableIncomePerShareCalculated &lt;TaxblIncmPerShrClctd&gt; / 13.4.9.14.11.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00127.md) | 193–193 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.13 EUDividendStatus &lt;EUDvddSts&gt; / 13.4.9.14.13.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00128.md) | 194–194 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.14 ChargeDetails &lt;ChrgDtls&gt; / 13.4.9.14.14.1 Type &lt;Tp&gt; / 13.4.9.14.14.1.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00129.md) | 195–195 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.14 ChargeDetails &lt;ChrgDtls&gt; / 13.4.9.14.14.3 CalculationBasis &lt;ClctnBsis&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00130.md) | 196–196 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.15 TaxLiabilityDetails &lt;TaxLbltyDtls&gt; / 13.4.9.14.15.1 Type &lt;Tp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00131.md) | 197–197 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.15 TaxLiabilityDetails &lt;TaxLbltyDtls&gt; / 13.4.9.14.15.1 Type &lt;Tp&gt; / 13.4.9.14.15.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00132.md) | 198–198 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.15 TaxLiabilityDetails &lt;TaxLbltyDtls&gt; / 13.4.9.14.15.4 Country &lt;Ctry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00133.md) | 199–199 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.15 TaxLiabilityDetails &lt;TaxLbltyDtls&gt; / 13.4.9.14.15.5 TaxCalculationDetails &lt;TaxClctnDtls&gt; / 13.4.9.14.15.5.1 EUCapitalGain &lt;EUCptlGn&gt; / 13.4.9.14.15.5.1.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00134.md) | 200–200 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.15 TaxLiabilityDetails &lt;TaxLbltyDtls&gt; / 13.4.9.14.15.5 TaxCalculationDetails &lt;TaxClctnDtls&gt; / 13.4.9.14.15.5.5 EUDividendStatus &lt;EUDvddSts&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00135.md) | 201–201 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.16 TaxRefundDetails &lt;TaxRfndDtls&gt; / 13.4.9.14.16.1 Type &lt;Tp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00136.md) | 202–202 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.16 TaxRefundDetails &lt;TaxRfndDtls&gt; / 13.4.9.14.16.1 Type &lt;Tp&gt; / 13.4.9.14.16.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00137.md) | 203–203 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.16 TaxRefundDetails &lt;TaxRfndDtls&gt; / 13.4.9.14.16.4 Country &lt;Ctry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00138.md) | 204–204 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.16 TaxRefundDetails &lt;TaxRfndDtls&gt; / 13.4.9.14.16.5 TaxCalculationDetails &lt;TaxClctnDtls&gt; / 13.4.9.14.16.5.1 EUCapitalGain &lt;EUCptlGn&gt; / 13.4.9.14.16.5.1.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00139.md) | 205–205 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.14 PriceDetails &lt;PricDtls&gt; / 13.4.9.14.16 TaxRefundDetails &lt;TaxRfndDtls&gt; / 13.4.9.14.16.5 TaxCalculationDetails &lt;TaxClctnDtls&gt; / 13.4.9.14.16.5.5 EUDividendStatus &lt;EUDvddSts&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00140.md) | 206–207 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 13.4.9.15.1 Currency &lt;Ccy&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00141.md) | 208–208 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 13.4.9.15.2 PriceTypeChangeBasis &lt;PricTpChngBsis&gt; / 13.4.9.15.2.1 Structured &lt;Strd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00142.md) | 209–209 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 13.4.9.15.2 PriceTypeChangeBasis &lt;PricTpChngBsis&gt; / 13.4.9.15.2.2 AdditionalInformation &lt;AddtlInf&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00143.md) | 210–210 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 13.4.9.15.3 PriceChange &lt;PricChng&gt; / 13.4.9.15.3.1 Amount &lt;Amt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00144.md) | 211–211 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 13.4.9.15.5 ByPredefinedTimePeriods &lt;ByPrdfndTmPrds&gt; / 13.4.9.15.5.1 HighestPriceValue12Months &lt;HghstPricVal12Mnths&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00145.md) | 212–212 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 13.4.9.15.5 ByPredefinedTimePeriods &lt;ByPrdfndTmPrds&gt; / 13.4.9.15.5.2 LowestPriceValue12Months &lt;LwstPricVal12Mnths&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00146.md) | 213–213 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 13.4.9.15.5 ByPredefinedTimePeriods &lt;ByPrdfndTmPrds&gt; / 13.4.9.15.5.3 OneYearPriceChange &lt;OneYrPricChng&gt; / 13.4.9.15.5.3.1 Amount &lt;Amt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00147.md) | 214–214 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 13.4.9.15.5 ByPredefinedTimePeriods &lt;ByPrdfndTmPrds&gt; / 13.4.9.15.5.4 ThreeYearPriceChange &lt;ThreeYrPricChng&gt; / 13.4.9.15.5.4.1 Amount &lt;Amt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00148.md) | 215–215 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 13.4.9.15.5 ByPredefinedTimePeriods &lt;ByPrdfndTmPrds&gt; / 13.4.9.15.5.5 FiveYearPriceChange &lt;FiveYrPricChng&gt; / 13.4.9.15.5.5.1 Amount &lt;Amt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00149.md) | 216–216 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 13.4.9.15.6 ByUserDefinedTimePeriod &lt;ByUsrDfndTmPrd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00150.md) | 217–217 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 13.4.9.15.6 ByUserDefinedTimePeriod &lt;ByUsrDfndTmPrd&gt; / 13.4.9.15.6.1 Period &lt;Prd&gt; / 13.4.9.15.6.1.2 DateTime &lt;DtTm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00151.md) | 218–218 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 13.4.9.15.6 ByUserDefinedTimePeriod &lt;ByUsrDfndTmPrd&gt; / 13.4.9.15.6.4 PriceChange &lt;PricChng&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00152.md) | 219–219 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 13.4.9.15.6 ByUserDefinedTimePeriod &lt;ByUsrDfndTmPrd&gt; / 13.4.9.15.6.4 PriceChange &lt;PricChng&gt; / 13.4.9.15.6.4.2 AmountSign &lt;AmtSgn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00153.md) | 220–220 |
| [12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03 / 13.4 Message Building Blocks / 13.4.3 PreviousReference &lt;PrvsRef&gt; / 13.4.9.16 PerformanceDetails &lt;PrfrmncDtls&gt; / 13.4.9.16.2 CumulativeCorporateActionFactor &lt;CmltvCorpActnFctr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00154.md) | 221–221 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Beneficial Owner](../../../../../shared/reference/participants/participant-src-000095-beneficial-owner.md) | participant | src-000095 |
| [Concentrator](../../../../../shared/reference/participants/participant-src-000095-concentrator.md) | participant | src-000095 |
| [CSD / ICSD](../../../../../shared/reference/participants/participant-src-000095-csd-icsd.md) | participant | src-000095 |
| [CSD](../../../../../shared/reference/participants/participant-src-000095-csd.md) | participant | src-000095 |
| [Custodian](../../../../../shared/reference/participants/participant-src-000095-custodian.md) | participant | src-000095 |
| [Distributor](../../../../../shared/reference/participants/participant-src-000095-distributor.md) | participant | src-000095 |
| [Executing Party / Registering Party](../../../../../shared/reference/participants/participant-src-000095-executing-party-registering-party.md) | participant | src-000095 |
| [Executing Party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | participant | src-000095 |
| [Fund Accountant](../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md) | participant | src-000095 |
| [Fund Manager](../../../../../shared/reference/participants/participant-src-000095-fund-manager.md) | participant | src-000095 |
| [ICSD](../../../../../shared/reference/participants/participant-src-000095-icsd.md) | participant | src-000095 |
| [Institutional Investor](../../../../../shared/reference/participants/participant-src-000095-institutional-investor.md) | participant | src-000095 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | participant | src-000095 |
| [Intermediary](../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | participant | src-000095 |
| [Market Data Provider](../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md) | participant | src-000095 |
| [Paying Agent](../../../../../shared/reference/participants/participant-src-000095-paying-agent.md) | participant | src-000095 |
| [Receiving Party (all levels)](../../../../../shared/reference/participants/participant-src-000095-receiving-party-all-levels.md) | participant | src-000095 |
| [Reporting Party](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md) | participant | src-000095 |
| [Requesting Party](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md) | participant | src-000095 |
| [Transfer Agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | participant | src-000095 |
| [Transferee's Bank (Executing Party)](../../../../../shared/reference/participants/participant-src-000095-transferee-s-bank-executing-party.md) | participant | src-000095 |
| [Transferee's Bank (Instructing Party)](../../../../../shared/reference/participants/participant-src-000095-transferee-s-bank-instructing-party.md) | participant | src-000095 |
| [Transferee](../../../../../shared/reference/participants/participant-src-000095-transferee.md) | participant | src-000095 |
| [Transferor's Bank (Executing Party)](../../../../../shared/reference/participants/participant-src-000095-transferor-s-bank-executing-party.md) | participant | src-000095 |
| [Transferor's Bank (Instructing Party)](../../../../../shared/reference/participants/participant-src-000095-transferor-s-bank-instructing-party.md) | participant | src-000095 |
| [Transferor](../../../../../shared/reference/participants/participant-src-000095-transferor.md) | participant | src-000095 |
| [Account Administration](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p185-account-administration.md) | business-flow | src-000095 |
| [Order Processing](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p186-order-processing.md) | business-flow | src-000095 |
| [Order Execution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p187-order-execution.md) | business-flow | src-000095 |
| [Payment Execution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p188-payment-execution.md) | business-flow | src-000095 |
| [Payment Execution - Advance Pay In](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p189-payment-execution-advance-pay-in.md) | business-flow | src-000095 |
| [Payment Execution - Pay In Arrears](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p190-payment-execution-pay-in-arrears.md) | business-flow | src-000095 |
| [Payment Execution - Pay Out Arrears](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p191-payment-execution-pay-out-arrears.md) | business-flow | src-000095 |
| [Tax Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p192-tax-accounting.md) | business-flow | src-000095 |
| [Fund Valuation](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p193-fund-valuation.md) | business-flow | src-000095 |
| [Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p194-commission-accounting.md) | business-flow | src-000095 |
| [Commission Accounting / Transaction Based Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p195-commission-accounting-transaction-based-commission-accounting.md) | business-flow | src-000095 |
| [Commission Accounting / Trailer Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p196-commission-accounting-trailer-commission-accounting.md) | business-flow | src-000095 |
| [Reconciliation](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p197-reconciliation.md) | business-flow | src-000095 |
| [Distribution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p199-distribution.md) | business-flow | src-000095 |
| [Registration](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p200-registration.md) | business-flow | src-000095 |
| [Account Opening](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p205-account-opening.md) | business-flow | src-000095 |
| [Account Modification](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p207-account-modification.md) | business-flow | src-000095 |
| [Reporting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p209-reporting.md) | business-flow | src-000095 |
| [Order Processing](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p212-order-processing.md) | business-flow | src-000095 |
| [Custody and Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p216-custody-and-accounting.md) | business-flow | src-000095 |
| [Transparency of Holdings](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p218-transparency-of-holdings.md) | business-flow | src-000095 |
| [Stock Transfers (Single Leg Transfer)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p221-stock-transfers-single-leg-transfer.md) | business-flow | src-000095 |
| [Portfolio and Stock Transfers (Single Leg)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p226-portfolio-and-stock-transfers-single-leg.md) | business-flow | src-000095 |
| [Portfolio and Stock Transfers (Double/Matched Leg)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg.md) | business-flow | src-000095 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
