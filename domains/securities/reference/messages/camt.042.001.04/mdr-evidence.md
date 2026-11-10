---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.042.001.04"
message_family: "camt.042"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.042.001.04"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04", "file_pages": [116, 125]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# camt.042.001.04 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); file pp116–125; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04, Functionality, file p116.**

Scope
A report provider, such as a transfer agent, sends the FundDetailedEstimatedCashForecastReport
message to the report user, such as an investment manager or pricing agent, to report the estimated
cash incomings and outgoings, sorted by country, institution name or other criteria defined by the user
of one or more share classes of an investment fund on one or more trade dates.
The cash movements may result from, for example, redemption, subscription, switch transactions or
reinvestment of dividends.
Usage
The FundDetailedEstimatedCashForecastReport is used to provide estimated cash movements, that is,
it is sent prior to the cut-off time and/or the price valuation of the fund. The message contains incoming
and outgoing cash flows that are estimated, that is, the price has not been applied. If the price is
definitive, then the FundDetailedConfirmedCashForecastReport message must be used.
The message structure allows for the following uses:
- to provide cash in and cash out amounts for a fund/sub fund and one or more share classes (a
FundOrSubFundDetails sequence and one or more EstimatedFundCashForecastDetails sequences are
used),
- to provide cash in and cash out amounts for one or more share classes (one or more
EstimatedFundCashForecastDetails sequences are used).
If the report is to provide estimated cash in and cash out for a fund/sub fund only and not for one or
more share classes, then the FundEstimatedCashForecastReport message must be used.
The FundDetailedEstimatedCashForecastReport message is used to report cash movements in or out
of a fund, organised by party, such as fund management company, country, currency or by some other
criteria defined by the report provider. If the report is used to give the cash-in and cash-out for a party,
then additional criteria, such as currency and country, can be specified.
In addition, the underlying transaction type for the cash-in or cash-out movement can be specified, as
well as information about the cash movement's underlying orders, such as commission and charges.
Outline
The FundDetailedEstimatedCashForecastReportV04 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. MessageIdentification
Identifies the message.
B. PoolReference
Approved by the Securities SEG on 27 January 2026 camt.042.001.04
FundDetailedEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 116 May 2026

**src-000096, 9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04, Functionality, file p117.**

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
G. EstimatedFundCashForecastDetails
Information related to the estimated cash-in and cash-out flows for a specific trade date as a result
of transactions in shares in an investment fund, for example, subscriptions, redemptions or
switches. The information provided is sorted by pre-defined criteria such as country, institution,
currency or user defined criteria.
H. ConsolidatedNetCashForecast
Estimated net cash as a result of the cash-in and cash-out flows specified in the fund cash forecast
details.
I. Extension
Additional information that can not be captured in the structured fields and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00077.md) | 116–116 |
| [9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04 / 9.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00078.md) | 117–117 |
| [9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04 / 9.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00079.md) | 118–118 |
| [9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04 / 9.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00080.md) | 119–119 |
| [9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04 / 9.4 Message Building Blocks / 9.4.2 PoolReference &lt;PoolRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00081.md) | 120–120 |
| [9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04 / 9.4 Message Building Blocks / 9.4.5 MessagePagination &lt;MsgPgntn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00082.md) | 121–122 |
| [9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04 / 9.4 Message Building Blocks / 9.4.7 EstimatedFundCashForecastDetails &lt;EstmtdFndCshFcstDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00083.md) | 123–123 |
| [9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04 / 9.4 Message Building Blocks / 9.4.8 ConsolidatedNetCashForecast &lt;CnsltdNetCshFcst&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00084.md) | 124–125 |

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
