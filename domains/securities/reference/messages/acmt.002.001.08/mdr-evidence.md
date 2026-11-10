---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "acmt.002.001.08"
message_family: "acmt.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "3 acmt.002.001.08 AccountDetailsConfirmationV08", "file_pages": [38, 56]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# acmt.002.001.08 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 3 acmt.002.001.08 AccountDetailsConfirmationV08

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); file pp38–56; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 3 acmt.002.001.08 AccountDetailsConfirmationV08, Functionality, file p38.**

Scope
The AccountDetailsConfirmation message is sent by an account servicer, for example, a registrar,
transfer agent, custodian bank or securities depository to the account owner, for example, an investor to
confirm the opening of an account, execution of an AccountModificationInstruction or to return
information requested in a GetAccountDetails message.
Usage
The AccountDetailsConfirmation message is used to confirm the opening of an account, modification of
an account or the provision of information requested in a previously sent GetAccountDetails message.
The message contains detailed information relevant to the opened account.
When the AccountDetailsConfirmation is used to confirm execution of an AccountModificationInstruction
message, it may:
- contain the modified subsets of account details that were specified in the
AccountModificationInstruction, and/or
- provide the status of the account.
When the AccountModificationInstruction message is used to instruct the closure of an account, the
AccountDetailsConfirmation message is used to confirm the account has been closed.
When the AccountDetailsConfirmation is used to reply to a GetAccountDetails message, it returns the
selected subsets of account details that were specified in the GetAccountDetails message.
Outline
The AccountDetailsConfirmationV08 MessageDefinition is composed of 16 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. OrderReference
Identifies a related order or settlement transaction.
C. RelatedReference
Reference to a linked message that was previously received.
D. ConfirmationDetails
Information about the request or instruction which triggered this confirmation.
E. InvestmentAccount
Confirmation of the information related to the investment account.
F. AccountParties
Approved by the Securities SEG on 27 January 2026 acmt.002.001.08 AccountDetailsConfirmationV08
Investment Funds - Maintenance 2025 - 2026 38 May 2026

**src-000096, 3 acmt.002.001.08 AccountDetailsConfirmationV08, Functionality, file p39.**

Confirmation of information related to parties that are related to the account, for example, primary
account owner.
G. Intermediaries
Confirmation of an intermediary or other party related to the management of the account.
H. Placement
Confirmation of referral information.
I. NewIssueAllocation
Confirmation of eligibility conditions applicable when there is an allocation of new issues for hedge
fund account opening.
J. SavingsInvestmentPlan
Confirmation of the information related to a savings plan that is related to the account.
K. WithdrawalInvestmentPlan
Confirmation of the information related to a withdrawal plan that is related to the account.
L. CashSettlement
Confirmation of a cash settlement standing instruction associated to transactions on the account.
M. ServiceLevelAgreement
Identifies documents to be provided for the account opening.
N. AdditionalInformation
Additional information such as remarks or notes that must be conveyed about the party and or
limitations and restrictions.
O. MarketPracticeVersion
Identifies the market practice to which the message conforms.
P. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 acmt.002.001.08 AccountDetailsConfirmationV08
Investment Funds - Maintenance 2025 - 2026 39 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00018.md) | 38–39 |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08 / 3.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00019.md) | 40–42 |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08 / 3.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00020.md) | 43–43 |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08 / 3.4 Message Building Blocks / 3.4.3 RelatedReference &lt;RltdRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00021.md) | 44–44 |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08 / 3.4 Message Building Blocks / 3.4.4 ConfirmationDetails &lt;ConfDtls&gt; / 3.4.4.2 AccountApplicationIdentification &lt;AcctApplId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00022.md) | 45–45 |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08 / 3.4 Message Building Blocks / 3.4.5 InvestmentAccount &lt;InvstmtAcct&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00023.md) | 46–47 |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08 / 3.4 Message Building Blocks / 3.4.6 AccountParties &lt;AcctPties&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00024.md) | 48–48 |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08 / 3.4 Message Building Blocks / 3.4.7 Intermediaries &lt;Intrmies&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00025.md) | 49–49 |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08 / 3.4 Message Building Blocks / 3.4.8 Placement &lt;Plcmnt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00026.md) | 50–50 |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08 / 3.4 Message Building Blocks / 3.4.10 SavingsInvestmentPlan &lt;SvgsInvstmtPlan&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00027.md) | 51–51 |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08 / 3.4 Message Building Blocks / 3.4.11 WithdrawalInvestmentPlan &lt;WdrwlInvstmtPlan&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00028.md) | 52–52 |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08 / 3.4 Message Building Blocks / 3.4.12 CashSettlement &lt;CshSttlm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00029.md) | 53–53 |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08 / 3.4 Message Building Blocks / 3.4.13 ServiceLevelAgreement &lt;SvcLvlAgrmt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00030.md) | 54–54 |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08 / 3.4 Message Building Blocks / 3.4.14 AdditionalInformation &lt;AddtlInf&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00031.md) | 55–55 |
| [3 acmt.002.001.08 AccountDetailsConfirmationV08 / 3.4 Message Building Blocks / 3.4.16 Extension &lt;Xtnsn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00032.md) | 56–56 |

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
