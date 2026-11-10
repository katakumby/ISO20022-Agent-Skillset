---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "acmt.003.001.08"
message_family: "acmt.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "4 acmt.003.001.08 AccountModificationInstructionV08", "file_pages": [57, 76]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# acmt.003.001.08 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 4 acmt.003.001.08 AccountModificationInstructionV08

[src-000096](../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md); file pp57–76; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 4 acmt.003.001.08 AccountModificationInstructionV08, Functionality, file p57.**

Scope
The AccountModificationInstruction message is sent by an account owner, for example, an investor or
its designated agent to the account servicer, for example, a registrar, transfer agent, custodian bank or
securities depository to modify, that is, create, update or delete specific details of an existing account.
Usage
The AccountModificationInstruction message is used to modify the details of an existing account.
The AccountModificationInstruction message can be used to:
- maintain/update any of the existing account details, for example, to update the address of the
beneficiary or modify the preference to income from distribution to capitalisation, or,
- add/create specific details to the existing account when these details were not yet recorded at the time
of account creation, for example, to add a second address or to establish new cash settlement standing
instructions, or,
- delete specific account details, for example, delete cash standing instructions, or,
- instruct a change to the status of the account, for example, instruct the closure of the account.
The usage of this message may be subject to service level agreement (SLA) between the
counterparties.
Execution of the AccountModificationInstruction is confirmed via an AccountDetailsConfirmation
message.
Outline
The AccountModificationInstructionV08 MessageDefinition is composed of 16 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PreviousReference
Reference to a linked message that was previously sent.
C. InstructionDetails
Information about the modification instruction.
D. InvestmentAccountSelection
Identifies the account for which the information is modified.
E. ModifiedInvestmentAccount
Information related to general characteristics of the account to be inserted, updated or deleted.
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 57 May 2026

**src-000096, 4 acmt.003.001.08 AccountModificationInstructionV08, Functionality, file p58.**

F. ModifiedAccountParties
Information related to an account party to be inserted, updated or deleted.
G. ModifiedIntermediaries
Information related to intermediaries to be inserted, updated or deleted.
H. ModifiedPlacement
Information related to referral information to be inserted, updated or deleted.
I. ModifiedIssueAllocation
Eligibility conditions related to allocation of new issues to be inserted, updated or deleted.
J. ModifiedSavingsInvestmentPlan
Information related to a savings plan to be inserted, updated or deleted.
K. ModifiedWithdrawalInvestmentPlan
Information related to a withdrawal plan to be inserted, updated or deleted.
L. ModifiedCashSettlement
Cash settlement standing instruction to be either inserted or deleted.
M. ModifiedServiceLevelAgreement
Information related to documents to be added, deleted or updated.
N. ModifiedAdditionalInformation
Information related to additional information to be added, deleted or updated.
O. MarketPracticeVersion
Identifies the market practice to which the message conforms.
P. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 58 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 acmt.003.001.08 AccountModificationInstructionV08](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00033.md) | 57–58 |
| [4 acmt.003.001.08 AccountModificationInstructionV08 / 4.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00034.md) | 59–62 |
| [4 acmt.003.001.08 AccountModificationInstructionV08 / 4.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00035.md) | 63–63 |
| [4 acmt.003.001.08 AccountModificationInstructionV08 / 4.4 Message Building Blocks / 4.4.3 InstructionDetails &lt;InstrDtls&gt; / 4.4.3.1 ModificationReason &lt;ModRsn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00036.md) | 64–64 |
| [4 acmt.003.001.08 AccountModificationInstructionV08 / 4.4 Message Building Blocks / 4.4.3 InstructionDetails &lt;InstrDtls&gt; / 4.4.3.5 ExistingAccountIdentification &lt;ExstgAcctId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00037.md) | 65–65 |
| [4 acmt.003.001.08 AccountModificationInstructionV08 / 4.4 Message Building Blocks / 4.4.5 ModifiedInvestmentAccount &lt;ModfdInvstmtAcct&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00038.md) | 66–68 |
| [4 acmt.003.001.08 AccountModificationInstructionV08 / 4.4 Message Building Blocks / 4.4.6 ModifiedAccountParties &lt;ModfdAcctPties&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00039.md) | 69–69 |
| [4 acmt.003.001.08 AccountModificationInstructionV08 / 4.4 Message Building Blocks / 4.4.7 ModifiedIntermediaries &lt;ModfdIntrmies&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00040.md) | 70–70 |
| [4 acmt.003.001.08 AccountModificationInstructionV08 / 4.4 Message Building Blocks / 4.4.9 ModifiedIssueAllocation &lt;ModfdIsseAllcn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00041.md) | 71–71 |
| [4 acmt.003.001.08 AccountModificationInstructionV08 / 4.4 Message Building Blocks / 4.4.11 ModifiedWithdrawalInvestmentPlan &lt;ModfdWdrwlInvstmtPlan&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00042.md) | 72–72 |
| [4 acmt.003.001.08 AccountModificationInstructionV08 / 4.4 Message Building Blocks / 4.4.12 ModifiedCashSettlement &lt;ModfdCshSttlm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00043.md) | 73–73 |
| [4 acmt.003.001.08 AccountModificationInstructionV08 / 4.4 Message Building Blocks / 4.4.13 ModifiedServiceLevelAgreement &lt;ModfdSvcLvlAgrmt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00044.md) | 74–74 |
| [4 acmt.003.001.08 AccountModificationInstructionV08 / 4.4 Message Building Blocks / 4.4.14 ModifiedAdditionalInformation &lt;ModfdAddtlInf&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00045.md) | 75–76 |

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
