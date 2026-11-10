---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.003.001.02"
message_family: "semt.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.003.001.02"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "19 semt.003.001.02 AccountingStatementOfHoldingsV02", "file_pages": [387, 397]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# semt.003.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 19 semt.003.001.02 AccountingStatementOfHoldingsV02

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); file pp387–397; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 19 semt.003.001.02 AccountingStatementOfHoldingsV02, Functionality, file p387.**

Scope
An account servicer, for example, a transfer agent sends the AccountStatementOfHoldings message to
the account owner, for example, a fund manager or an account owner's designated agent to provide
detailed holdings of the portfolio at a specified moment in time.
The message provides, at a moment in time, valuations of the portfolio together with details of each
financial instrument holding.
The message can be sent either audited or un-audited and may be provided on a trade date or
settlement date basis.
Usage
The AccountingStatementOfHoldings message is used to provide valuation detail for each financial
instrument held in a portfolio. The message should be sent at a frequency agreed bi-laterally between
the account servicer and the account owner.
This message can only be used to list the holdings of a single (master) account. However, it is possible
to break down these holdings into one or several sub-accounts. Therefore, the message can be used to
either specify holdings at
- the main account level, or,
- the sub-account level.
This message can be used to report where the financial instruments are safe-kept, physically or
notionally. If a security is held in more than one safekeeping place, this can also be indicated.
The AccountingStatementOfHoldings message should not be used for trading purposes.
Outline
The AccountingStatementOfHoldingsV02 MessageDefinition is composed of 10
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies a message from a business application standpoint.
B. PreviousReference
Reference to a linked message that was previously sent.
C. RelatedReference
Reference to a linked message that was previously received.
D. MessagePagination
Pagination of the message.
Approved by the Securities SEG on 27 January 2026 semt.003.001.02
AccountingStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 387 May 2026

**src-000096, 19 semt.003.001.02 AccountingStatementOfHoldingsV02, Functionality, file p388.**

E. StatementGeneralDetails
General information related to the accounting statement of holdings.
F. AccountDetails
The safekeeping or investment account.
G. BalanceForAccount
Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
H. SubAccountDetails
The sub-account of the safekeeping or investment account.
I. TotalValues
Value of total holdings reported.
J. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 semt.003.001.02
AccountingStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 388 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [19 semt.003.001.02 AccountingStatementOfHoldingsV02](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00276.md) | 387–388 |
| [19 semt.003.001.02 AccountingStatementOfHoldingsV02 / 19.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00277.md) | 389–390 |
| [19 semt.003.001.02 AccountingStatementOfHoldingsV02 / 19.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00278.md) | 391–391 |
| [19 semt.003.001.02 AccountingStatementOfHoldingsV02 / 19.4 Message Building Blocks / 19.4.4 MessagePagination &lt;MsgPgntn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00279.md) | 392–392 |
| [19 semt.003.001.02 AccountingStatementOfHoldingsV02 / 19.4 Message Building Blocks / 19.4.5 StatementGeneralDetails &lt;StmtGnlDtls&gt; / 19.4.5.3 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00280.md) | 393–393 |
| [19 semt.003.001.02 AccountingStatementOfHoldingsV02 / 19.4 Message Building Blocks / 19.4.5 StatementGeneralDetails &lt;StmtGnlDtls&gt; / 19.4.5.7 StatementBasis &lt;StmtBsis&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00281.md) | 394–394 |
| [19 semt.003.001.02 AccountingStatementOfHoldingsV02 / 19.4 Message Building Blocks / 19.4.7 BalanceForAccount &lt;BalForAcct&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00282.md) | 395–395 |
| [19 semt.003.001.02 AccountingStatementOfHoldingsV02 / 19.4 Message Building Blocks / 19.4.8 SubAccountDetails &lt;SubAcctDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00283.md) | 396–397 |

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
