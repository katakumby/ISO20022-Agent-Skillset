---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.041.001.04"
message_family: "camt.041"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.041.001.04"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "8 camt.041.001.04 FundConfirmedCashForecastReportV04", "file_pages": [105, 115]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# camt.041.001.04 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 8 camt.041.001.04 FundConfirmedCashForecastReportV04

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); file pp105–115; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 8 camt.041.001.04 FundConfirmedCashForecastReportV04, Functionality, file p105.**

Scope
A report provider, such as a transfer agent, sends the FundConfirmedCashForecastReport message to
the report user, such as an investment manager or pricing agent, to report the confirmed cash
incomings and outgoings of one or more share classes of an investment fund on one or more trade
dates.
The cash movements may result from, for example, redemption, subscription, switch transactions or
reinvestment of dividends.
Usage
The FundConfirmedCashForecastReport is used to report definitive cash movements, that is it is sent
after the cut-off time and/or the price valuation of the fund.
This message contains incoming and outgoing cash flows that are confirmed, that is, the price has been
applied. If the price is not yet definitive, then the FundEstimatedCashForecastReport message must be
used.
The message structure allows for the following uses:
- to provide cash in and cash out amounts for a fund/sub fund (a FundOrSubFundDetails sequence is
used),
- to provide cash in and cash out amounts for a fund/sub fund and one or more share classes
(FundOrSubFundDetails sequence and one or more FundCashForecastDetails sequences are used),
- to provide cash in and cash out amounts for one or more share classes (one or more
FundCashForecastDetails sequences are used).
- to provide cash in and cash out amounts for more than one fund/sub fund, and more than one share
classes (two or more FundOrSubFundDetails sequences and two or more FundCashForecastDetails
sequences and used); however, it should be noted that, in this usage, there is no way to determine
which share class belongs to which fund/sub fund from the message content itself, which may not be
desirable and the use of this kind of combination should be bilaterally agreed.
This message allows the report provider to report cash movements in or out of a fund, but does not
allow the Sender to categorise these movements, for example by country, or to give details of the
underlying orders, commission or charges.
If the report provider wishes to give detailed information related to cash movements, then the
FundDetailedConfirmedCashForecastReport message must be used.
Outline
The FundConfirmedCashForecastReportV04 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. MessageIdentification
Approved by the Securities SEG on 27 January 2026 camt.041.001.04
FundConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 105 May 2026

**src-000096, 8 camt.041.001.04 FundConfirmedCashForecastReportV04, Functionality, file p106.**

Identifies the message.
B. PoolReference
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
H. ConsolidatedNetCashForecast
Estimated net cash as a result of the cash-in and cash-out flows.
I. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 camt.041.001.04
FundConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 106 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [8 camt.041.001.04 FundConfirmedCashForecastReportV04](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00069.md) | 105–106 |
| [8 camt.041.001.04 FundConfirmedCashForecastReportV04 / 8.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00070.md) | 107–108 |
| [8 camt.041.001.04 FundConfirmedCashForecastReportV04 / 8.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00071.md) | 109–109 |
| [8 camt.041.001.04 FundConfirmedCashForecastReportV04 / 8.4 Message Building Blocks / 8.4.2 PoolReference &lt;PoolRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00072.md) | 110–110 |
| [8 camt.041.001.04 FundConfirmedCashForecastReportV04 / 8.4 Message Building Blocks / 8.4.5 MessagePagination &lt;MsgPgntn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00073.md) | 111–112 |
| [8 camt.041.001.04 FundConfirmedCashForecastReportV04 / 8.4 Message Building Blocks / 8.4.7 FundCashForecastDetails &lt;FndCshFcstDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00074.md) | 113–113 |
| [8 camt.041.001.04 FundConfirmedCashForecastReportV04 / 8.4 Message Building Blocks / 8.4.8 ConsolidatedNetCashForecast &lt;CnsltdNetCshFcst&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00075.md) | 114–114 |
| [8 camt.041.001.04 FundConfirmedCashForecastReportV04 / 8.4 Message Building Blocks / 8.4.9 Extension &lt;Xtnsn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00076.md) | 115–115 |

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
