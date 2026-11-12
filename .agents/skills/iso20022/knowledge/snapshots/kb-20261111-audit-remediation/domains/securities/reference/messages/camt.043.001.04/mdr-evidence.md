---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.043.001.04"
message_family: "camt.043"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.043.001.04"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04", "file_pages": [126, 145]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# camt.043.001.04 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); file pp126–145; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04, Functionality, file p126.**

Scope
A report provider, such as a transfer agent, sends the FundDetailedConfirmedCashForecastReport
message to the report user, such as an investment manager or pricing agent, to report the confirmed
cash incomings and outgoings, sorted by country, institution name or other criteria defined by the user
of one or more share classes of an investment fund on one or more trade dates.
The cash movements may result from, for example, redemption, subscription, switch transactions or
reinvestment of dividends.
Usage
The FundDetailedConfirmedCashForecastReport is used to provide definitive cash movements, that is,
it is sent after the cut-off time and/or the price valuation of the fund.
If the price is not yet definitive, then the FundDetailedEstimatedCashForecastReport message must be
used.
The message structure allows for the following uses:
- to provide cash in and cash out amounts for a fund/sub fund and one or more share classes (a
FundOrSubFundDetails sequence and one or FundCashForecastDetails sequences are used),
- to provide cash in and cash out amounts for one or more share classes (one or more
FundCashForecastDetails sequences are used).
If the report is to provide cash in and cash out for a fund/sub fund only and not for one or more share
classes, then the FundConfirmedCashForecastReport message must be used.
The FundDetailedConfirmedCashForecastReport message is used to report cash movements in or out
of a fund, organised by party, such as fund management company, country, currency or by some other
criteria defined by the report provider. If the report is used to given the cash-in and cash-out for a party,
then additional criteria, such as currency and country, can be specified.
In addition, the underlying transaction type for the cash-in or cash-out movement can be specified, as
well as information about the cash movement's underlying orders, such as commission and charges.
Outline
The FundDetailedConfirmedCashForecastReportV04 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. MessageIdentification
Identifies the message.
B. PoolReference
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 126 May 2026

**src-000096, 10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04, Functionality, file p127.**

Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. MessagePagination
Pagination of the message.
F. FundOrSubFundDetails
Information about the fund/sub fund when the report either specifies cash flow for the fund/sub fund
or for a share class of the fund/sub fund.
G. FundCashForecastDetails
Information related to the cash-in and cash-out flows for a specific trade date as a result of
transactions in shares in an investment fund, for example, subscriptions, redemptions or switches.
The information provided is sorted by pre-defined criteria such as country, institution, currency or
user defined criteria.
H. ConsolidatedNetCashForecast
Net cash as a result of the cash-in and cash-out flows specified in the fund cash forecast details.
I. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 127 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00085.md) | 126–127 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00086.md) | 128–128 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00087.md) | 129–130 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00088.md) | 131–131 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.4 Message Building Blocks / 10.4.5 MessagePagination &lt;MsgPgntn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00089.md) | 132–133 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.4 Message Building Blocks / 10.4.7 FundCashForecastDetails &lt;FndCshFcstDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00090.md) | 134–134 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.4 Message Building Blocks / 10.4.7 FundCashForecastDetails &lt;FndCshFcstDtls&gt; / 10.4.7.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00091.md) | 135–135 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.4 Message Building Blocks / 10.4.7 FundCashForecastDetails &lt;FndCshFcstDtls&gt; / 10.4.7.5 TotalNAV &lt;TtlNAV&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00092.md) | 136–136 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.4 Message Building Blocks / 10.4.7 FundCashForecastDetails &lt;FndCshFcstDtls&gt; / 10.4.7.7 TotalUnitsNumber &lt;TtlUnitsNb&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00093.md) | 137–137 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.4 Message Building Blocks / 10.4.7 FundCashForecastDetails &lt;FndCshFcstDtls&gt; / 10.4.7.11 CurrencyStatus &lt;CcySts&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00094.md) | 138–138 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.4 Message Building Blocks / 10.4.7 FundCashForecastDetails &lt;FndCshFcstDtls&gt; / 10.4.7.14 ForeignExchangeRate &lt;FXRate&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00095.md) | 139–139 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.4 Message Building Blocks / 10.4.7 FundCashForecastDetails &lt;FndCshFcstDtls&gt; / 10.4.7.17 BreakdownByCountry &lt;BrkdwnByCtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00096.md) | 140–140 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.4 Message Building Blocks / 10.4.7 FundCashForecastDetails &lt;FndCshFcstDtls&gt; / 10.4.7.18 BreakdownByCurrency &lt;BrkdwnByCcy&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00097.md) | 141–141 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.4 Message Building Blocks / 10.4.7 FundCashForecastDetails &lt;FndCshFcstDtls&gt; / 10.4.7.19 BreakdownByUserDefinedParameter &lt;BrkdwnByUsrDfndParam&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00098.md) | 142–142 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.4 Message Building Blocks / 10.4.7 FundCashForecastDetails &lt;FndCshFcstDtls&gt; / 10.4.7.20 NetCashForecastDetails &lt;NetCshFcstDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00099.md) | 143–143 |
| [10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04 / 10.4 Message Building Blocks / 10.4.8 ConsolidatedNetCashForecast &lt;CnsltdNetCshFcst&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00100.md) | 144–145 |

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
