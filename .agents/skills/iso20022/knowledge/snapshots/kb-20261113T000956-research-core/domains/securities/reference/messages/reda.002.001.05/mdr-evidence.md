---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.002.001.05"
message_family: "reda.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.002.001.05"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "14 reda.002.001.05 PriceReportCancellationV05", "file_pages": [222, 290]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# reda.002.001.05 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 14 reda.002.001.05 PriceReportCancellationV05

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); file pp222–290; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 14 reda.002.001.05 PriceReportCancellationV05, Functionality, file p222.**

SCOPE
A report provider, for example, a transfer agent, fund accountant or market data provider, sends the
PriceReportCancellation message to the report recipient, for example, a fund management company,
transfer agent, market data provider, regulator or any other interested party to cancel previously sent
prices.
USAGE
The PriceReportCancellation message is used to either:
- cancel an entire PriceReport that was previously sent (by quoting the business reference of the
original price report in the PriceReportIdentification element), or,
- cancel one or more individual prices from a previously sent price report (by using the
PriceDetailsToBeCancelled sequence).
Technically, it is possible to cancel all the prices individually by using the PriceDetailsToBeCancelled
sequence, but this is not recommended.
The cancellation should not contain the cancellation of prices for more than one NAV date.
Outline
The PriceReportCancellationV05 MessageDefinition is composed of 11 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies a message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. MessagePagination
Pagination of the message.
E. PriceReportIdentification
Unique and unambiguous identifier for the price report, as assigned by the reporting party.
F. CancellationIdentification
Unique and unambiguous identifier for the cancellation of the previous price report, as assigned by
the reporting party.
G. CancellationReason
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 222 May 2026

**src-000096, 14 reda.002.001.05 PriceReportCancellationV05, Functionality, file p223.**

Reason for the cancellation.
H. ExpectedPriceCorrectionDate
Date or date and time the price will be corrected.
I. CompletePriceCancellation
Indicates whether or not all the prices of the referenced price report are cancelled.
J. CancelledPriceValuationDetails
Details of prices to be cancelled.
K. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 223 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [14 reda.002.001.05 PriceReportCancellationV05](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00155.md) | 222–223 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00156.md) | 224–228 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00157.md); [Constraints continuation C18–C21 (file p231)](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00158.md#file-page-231) | 229–230 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00158.md) | 231–231 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.6 CancellationIdentification &lt;CxlId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00159.md) | 232–232 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.8 ExpectedPriceCorrectionDate &lt;XpctdPricCrrctnDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00160.md) | 233–237 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00161.md) | 238–244 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00162.md) | 245–246 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.4 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 14.4.10.1.4.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00163.md) | 247–247 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.4 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 14.4.10.1.4.1 Identification &lt;Id&gt; / 14.4.10.1.4.1.2 SEDOL &lt;SEDOL&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00164.md) | 248–248 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.4 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 14.4.10.1.4.1 Identification &lt;Id&gt; / 14.4.10.1.4.1.9 Wertpapier &lt;Wrtppr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00165.md) | 249–249 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.4 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 14.4.10.1.4.1 Identification &lt;Id&gt; / 14.4.10.1.4.1.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00166.md) | 250–250 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.4 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 14.4.10.1.4.5 DenominationCurrency &lt;DnmtnCcy&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00167.md) | 251–251 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.4 FinancialInstrumentDetails &lt;FinInstrmDtls&gt; / 14.4.10.1.4.9 DualFundIndicator &lt;DualFndInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00168.md) | 252–252 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.5 FundManagementCompany &lt;FndMgmtCpny&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00169.md) | 253–253 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.8 NextValuationDateTime &lt;NxtValtnDtTm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00170.md) | 254–254 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.12 OfficialValuationIndicator &lt;OffclValtnInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00171.md) | 255–257 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.1 PriceType &lt;PricTp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00172.md) | 258–258 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.1 PriceType &lt;PricTp&gt; / 14.4.10.1.14.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00173.md) | 259–259 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.3 ValueInInvestmentCurrency &lt;ValInInvstmtCcy&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00174.md) | 260–260 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.8 EstimatedPriceIndicator &lt;EstmtdPricInd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00175.md) | 261–261 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.11 TaxableIncomePerShareCalculated &lt;TaxblIncmPerShrClctd&gt; / 14.4.10.1.14.11.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00176.md) | 262–262 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.13 EUDividendStatus &lt;EUDvddSts&gt; / 14.4.10.1.14.13.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00177.md) | 263–263 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.14 ChargeDetails &lt;ChrgDtls&gt; / 14.4.10.1.14.14.1 Type &lt;Tp&gt; / 14.4.10.1.14.14.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00178.md) | 264–264 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.14 ChargeDetails &lt;ChrgDtls&gt; / 14.4.10.1.14.14.3 CalculationBasis &lt;ClctnBsis&gt; / 14.4.10.1.14.14.3.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00179.md) | 265–265 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.15 TaxLiabilityDetails &lt;TaxLbltyDtls&gt; / 14.4.10.1.14.15.1 Type &lt;Tp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00180.md) | 266–266 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.15 TaxLiabilityDetails &lt;TaxLbltyDtls&gt; / 14.4.10.1.14.15.1 Type &lt;Tp&gt; / 14.4.10.1.14.15.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00181.md) | 267–267 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.15 TaxLiabilityDetails &lt;TaxLbltyDtls&gt; / 14.4.10.1.14.15.4 Country &lt;Ctry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00182.md) | 268–268 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.15 TaxLiabilityDetails &lt;TaxLbltyDtls&gt; / 14.4.10.1.14.15.5 TaxCalculationDetails &lt;TaxClctnDtls&gt; / 14.4.10.1.14.15.5.1 EUCapitalGain &lt;EUCptlGn&gt; / 14.4.10.1.14.15.5.1.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00183.md) | 269–269 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.15 TaxLiabilityDetails &lt;TaxLbltyDtls&gt; / 14.4.10.1.14.15.5 TaxCalculationDetails &lt;TaxClctnDtls&gt; / 14.4.10.1.14.15.5.5 EUDividendStatus &lt;EUDvddSts&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00184.md) | 270–270 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.16 TaxRefundDetails &lt;TaxRfndDtls&gt; / 14.4.10.1.14.16.1 Type &lt;Tp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00185.md) | 271–271 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.16 TaxRefundDetails &lt;TaxRfndDtls&gt; / 14.4.10.1.14.16.1 Type &lt;Tp&gt; / 14.4.10.1.14.16.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00186.md) | 272–272 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.16 TaxRefundDetails &lt;TaxRfndDtls&gt; / 14.4.10.1.14.16.4 Country &lt;Ctry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00187.md) | 273–273 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.16 TaxRefundDetails &lt;TaxRfndDtls&gt; / 14.4.10.1.14.16.5 TaxCalculationDetails &lt;TaxClctnDtls&gt; / 14.4.10.1.14.16.5.1 EUCapitalGain &lt;EUCptlGn&gt; / 14.4.10.1.14.16.5.1.1 Code &lt;Cd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00188.md) | 274–274 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.14 PriceDetails &lt;PricDtls&gt; / 14.4.10.1.14.16 TaxRefundDetails &lt;TaxRfndDtls&gt; / 14.4.10.1.14.16.5 TaxCalculationDetails &lt;TaxClctnDtls&gt; / 14.4.10.1.14.16.5.5 EUDividendStatus &lt;EUDvddSts&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00189.md) | 275–276 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 14.4.10.1.15.1 Currency &lt;Ccy&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00190.md) | 277–277 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 14.4.10.1.15.2 PriceTypeChangeBasis &lt;PricTpChngBsis&gt; / 14.4.10.1.15.2.1 Structured &lt;Strd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00191.md) | 278–278 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 14.4.10.1.15.2 PriceTypeChangeBasis &lt;PricTpChngBsis&gt; / 14.4.10.1.15.2.2 AdditionalInformation &lt;AddtlInf&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00192.md) | 279–279 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 14.4.10.1.15.3 PriceChange &lt;PricChng&gt; / 14.4.10.1.15.3.1 Amount &lt;Amt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00193.md) | 280–280 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 14.4.10.1.15.5 ByPredefinedTimePeriods &lt;ByPrdfndTmPrds&gt; / 14.4.10.1.15.5.1 HighestPriceValue12Months &lt;HghstPricVal12Mnths&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00194.md) | 281–281 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 14.4.10.1.15.5 ByPredefinedTimePeriods &lt;ByPrdfndTmPrds&gt; / 14.4.10.1.15.5.2 LowestPriceValue12Months &lt;LwstPricVal12Mnths&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00195.md) | 282–282 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 14.4.10.1.15.5 ByPredefinedTimePeriods &lt;ByPrdfndTmPrds&gt; / 14.4.10.1.15.5.3 OneYearPriceChange &lt;OneYrPricChng&gt; / 14.4.10.1.15.5.3.1 Amount &lt;Amt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00196.md) | 283–283 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 14.4.10.1.15.5 ByPredefinedTimePeriods &lt;ByPrdfndTmPrds&gt; / 14.4.10.1.15.5.4 ThreeYearPriceChange &lt;ThreeYrPricChng&gt; / 14.4.10.1.15.5.4.1 Amount &lt;Amt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00197.md) | 284–284 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 14.4.10.1.15.5 ByPredefinedTimePeriods &lt;ByPrdfndTmPrds&gt; / 14.4.10.1.15.5.5 FiveYearPriceChange &lt;FiveYrPricChng&gt; / 14.4.10.1.15.5.5.1 Amount &lt;Amt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00198.md) | 285–285 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 14.4.10.1.15.6 ByUserDefinedTimePeriod &lt;ByUsrDfndTmPrd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00199.md) | 286–286 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 14.4.10.1.15.6 ByUserDefinedTimePeriod &lt;ByUsrDfndTmPrd&gt; / 14.4.10.1.15.6.1 Period &lt;Prd&gt; / 14.4.10.1.15.6.1.2 DateTime &lt;DtTm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00200.md) | 287–287 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 14.4.10.1.15.6 ByUserDefinedTimePeriod &lt;ByUsrDfndTmPrd&gt; / 14.4.10.1.15.6.4 PriceChange &lt;PricChng&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00201.md) | 288–288 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.15 ValuationStatistics &lt;ValtnSttstcs&gt; / 14.4.10.1.15.6 ByUserDefinedTimePeriod &lt;ByUsrDfndTmPrd&gt; / 14.4.10.1.15.6.4 PriceChange &lt;PricChng&gt; / 14.4.10.1.15.6.4.2 AmountSign &lt;AmtSgn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00202.md) | 289–289 |
| [14 reda.002.001.05 PriceReportCancellationV05 / 14.4 Message Building Blocks / 14.4.10 CancelledPriceValuationDetails &lt;CancPricValtnDtls&gt; / 14.4.10.1 PriceValuationDetails &lt;PricValtnDtls&gt; / 14.4.10.1.16 PerformanceDetails &lt;PrfrmncDtls&gt; / 14.4.10.1.16.2 CumulativeCorporateActionFactor &lt;CmltvCorpActnFctr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00203.md) | 290–290 |

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
