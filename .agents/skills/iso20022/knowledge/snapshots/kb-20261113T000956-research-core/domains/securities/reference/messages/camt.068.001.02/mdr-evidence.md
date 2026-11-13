---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.068.001.02"
message_family: "camt.068"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.068.001.02"
source_ids: ["src-000233", "src-000360"]
source_locations: [{"source_id": "src-000233", "heading": "9 camt.068.001.02 IntraBalanceMovementConfirmationV02", "file_pages": [133, 148]}, {"source_id": "src-000360", "heading": "4 camt.068.001.02 IntraBalanceMovementConfirmationV02", "file_pages": [50, 65]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# camt.068.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 9 camt.068.001.02 IntraBalanceMovementConfirmationV02

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp133–148; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 9 camt.068.001.02 IntraBalanceMovementConfirmationV02, Functionality, file p133.**

The IntraBalanceMovementConfirmation message is sent from a settlement infrastructure to an account
owner/requestor to confirm the movement of an amount of money within its holdings from one sub-
balance to another.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is
"CopyDuplicate").
Outline
The IntraBalanceMovementConfirmationV02 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
B. AdditionalParameters
Additional parameters to the transaction.
C. CashAccount
Account to or from which an entry is made.
D. CashAccountOwner
Party that legally owns the cash account.
E. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
F. IntraBalance
Intra-balance movement transaction details.
G. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.068.001.02
IntraBalanceMovementConfirmationV02
Target2-Securities 133 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00092.md) | 133–133 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00093.md) | 134–134 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00094.md); [Constraints continuation C8–C10 (file p136)](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00095.md#file-page-136) | 135–135 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00095.md) | 136–136 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.4 Message Building Blocks / 9.4.1 Identification &lt;Id&gt; / 9.4.1.3 CopyDuplicate &lt;CpyDplct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00096.md) | 137–137 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.4 Message Building Blocks / 9.4.2 AdditionalParameters &lt;AddtlParams&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00097.md) | 138–138 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.4 Message Building Blocks / 9.4.4 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00098.md) | 139–139 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.4 Message Building Blocks / 9.4.6 IntraBalance &lt;IntraBal&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00099.md) | 140–140 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.4 Message Building Blocks / 9.4.6 IntraBalance &lt;IntraBal&gt; / 9.4.6.1 SettledAmount &lt;SttldAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00100.md) | 141–141 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.4 Message Building Blocks / 9.4.6 IntraBalance &lt;IntraBal&gt; / 9.4.6.2 PreviouslySettledAmount &lt;PrevslySttldAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00101.md) | 142–142 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.4 Message Building Blocks / 9.4.6 IntraBalance &lt;IntraBal&gt; / 9.4.6.5 BalanceFrom &lt;BalFr&gt; / 9.4.6.5.1 Type &lt;Tp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00102.md) | 143–143 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.4 Message Building Blocks / 9.4.6 IntraBalance &lt;IntraBal&gt; / 9.4.6.5 BalanceFrom &lt;BalFr&gt; / 9.4.6.5.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00103.md) | 144–144 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.4 Message Building Blocks / 9.4.6 IntraBalance &lt;IntraBal&gt; / 9.4.6.5 BalanceFrom &lt;BalFr&gt; / 9.4.6.5.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 9.4.6.5.2.4 CashSubBalanceType &lt;CshSubBalTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00104.md) | 145–145 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.4 Message Building Blocks / 9.4.6 IntraBalance &lt;IntraBal&gt; / 9.4.6.6 BalanceTo &lt;BalTo&gt; / 9.4.6.6.1 Type &lt;Tp&gt; / 9.4.6.6.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00105.md) | 146–146 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.4 Message Building Blocks / 9.4.6 IntraBalance &lt;IntraBal&gt; / 9.4.6.6 BalanceTo &lt;BalTo&gt; / 9.4.6.6.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 9.4.6.6.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00106.md) | 147–147 |
| [9 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 9.4 Message Building Blocks / 9.4.6 IntraBalance &lt;IntraBal&gt; / 9.4.6.7 CashSubBalanceIdentification &lt;CshSubBalId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00107.md) | 148–148 |

## src-000360 — 4 camt.068.001.02 IntraBalanceMovementConfirmationV02

[src-000360](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`; file pp50–65; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000360, 4 camt.068.001.02 IntraBalanceMovementConfirmationV02, Functionality, file p50.**

The IntraBalanceMovementConfirmation message is sent from a settlement infrastructure to an account
owner/requestor to confirm the movement of an amount of money within its holdings from one sub-
balance to another.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is
"CopyDuplicate").
Outline
The IntraBalanceMovementConfirmationV02 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
B. AdditionalParameters
Additional parameters to the transaction.
C. CashAccount
Account to or from which an entry is made.
D. CashAccountOwner
Party that legally owns the cash account.
E. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
F. IntraBalance
Intra-balance movement transaction details.
G. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.068.001.02
IntraBalanceMovementConfirmationV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
50 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00039.md) | 50–50 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.2 Structure](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00040.md) | 51–51 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.3 Constraints](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00041.md); [Constraints continuation C8–C10 (file p53)](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00042.md#file-page-53) | 52–52 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.4 Message Building Blocks](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00042.md) | 53–53 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.4 Message Building Blocks / 4.4.1 Identification &lt;Id&gt; / 4.4.1.3 CopyDuplicate &lt;CpyDplct&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00043.md) | 54–54 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.4 Message Building Blocks / 4.4.2 AdditionalParameters &lt;AddtlParams&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00044.md) | 55–55 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.4 Message Building Blocks / 4.4.4 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00045.md) | 56–56 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.4 Message Building Blocks / 4.4.6 IntraBalance &lt;IntraBal&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00046.md) | 57–57 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.4 Message Building Blocks / 4.4.6 IntraBalance &lt;IntraBal&gt; / 4.4.6.1 SettledAmount &lt;SttldAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00047.md) | 58–58 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.4 Message Building Blocks / 4.4.6 IntraBalance &lt;IntraBal&gt; / 4.4.6.2 PreviouslySettledAmount &lt;PrevslySttldAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00048.md) | 59–59 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.4 Message Building Blocks / 4.4.6 IntraBalance &lt;IntraBal&gt; / 4.4.6.5 BalanceFrom &lt;BalFr&gt; / 4.4.6.5.1 Type &lt;Tp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00049.md) | 60–60 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.4 Message Building Blocks / 4.4.6 IntraBalance &lt;IntraBal&gt; / 4.4.6.5 BalanceFrom &lt;BalFr&gt; / 4.4.6.5.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00050.md) | 61–61 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.4 Message Building Blocks / 4.4.6 IntraBalance &lt;IntraBal&gt; / 4.4.6.5 BalanceFrom &lt;BalFr&gt; / 4.4.6.5.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 4.4.6.5.2.4 CashSubBalanceType &lt;CshSubBalTp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00051.md) | 62–62 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.4 Message Building Blocks / 4.4.6 IntraBalance &lt;IntraBal&gt; / 4.4.6.6 BalanceTo &lt;BalTo&gt; / 4.4.6.6.1 Type &lt;Tp&gt; / 4.4.6.6.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00052.md) | 63–63 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.4 Message Building Blocks / 4.4.6 IntraBalance &lt;IntraBal&gt; / 4.4.6.6 BalanceTo &lt;BalTo&gt; / 4.4.6.6.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 4.4.6.6.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00053.md) | 64–64 |
| [4 camt.068.001.02 IntraBalanceMovementConfirmationV02 / 4.4 Message Building Blocks / 4.4.6 IntraBalance &lt;IntraBal&gt; / 4.4.6.7 CashSubBalanceIdentification &lt;CshSubBalId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00054.md) | 65–65 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Central Counterparty](../../../../../shared/reference/participants/participant-src-000359-central-counterparty.md) | participant | src-000359 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000359-central-securities-depositories-csd.md) | participant | src-000359 |
| [Central Securities Depositories](../../../../../shared/reference/participants/participant-src-000359-central-securities-depositories.md) | participant | src-000359 |
| [Central Securities Depository](../../../../../shared/reference/participants/participant-src-000359-central-securities-depository.md) | participant | src-000359 |
| [Executing/Servicing Party](../../../../../shared/reference/participants/participant-src-000359-executing-servicing-party.md) | participant | src-000359 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | participant | src-000359 |
| [National Central Bank (NCB)](../../../../../shared/reference/participants/participant-src-000359-national-central-bank-ncb.md) | participant | src-000359 |
| [National Central Bank](../../../../../shared/reference/participants/participant-src-000359-national-central-bank.md) | participant | src-000359 |
| [Payment Bank](../../../../../shared/reference/participants/participant-src-000359-payment-bank.md) | participant | src-000359 |
| [Servicing/Executing Party Instructing Party](../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party-instructing-party.md) | participant | src-000359 |
| [Servicing/Executing Party](../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party.md) | participant | src-000359 |
| [Settlement Infrastructure Direct Participant](../../../../../shared/reference/participants/participant-src-000359-settlement-infrastructure-direct-participant.md) | participant | src-000359 |
| [Settlement Infrastructure](../../../../../shared/reference/participants/participant-src-000359-settlement-infrastructure.md) | participant | src-000359 |
| [Stock Exchange](../../../../../shared/reference/participants/participant-src-000359-stock-exchange.md) | participant | src-000359 |
| [System Member](../../../../../shared/reference/participants/participant-src-000359-system-member.md) | participant | src-000359 |
| [System Transaction Administrator](../../../../../shared/reference/participants/participant-src-000359-system-transaction-administrator.md) | participant | src-000359 |
| [T2S operator](../../../../../shared/reference/participants/participant-src-000359-t2s-operator.md) | participant | src-000359 |
| [Third Party](../../../../../shared/reference/participants/participant-src-000359-third-party.md) | participant | src-000359 |
| [Movement Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p158-movement-process.md) | business-flow | src-000359 |
| [Status Advice Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p159-status-advice-process.md) | business-flow | src-000359 |
| [Confirmation Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p160-confirmation-process.md) | business-flow | src-000359 |
| [Modification Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p161-modification-process.md) | business-flow | src-000359 |
| [Cancellation Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p162-cancellation-process.md) | business-flow | src-000359 |
| [Modification/Cancellation Status Advice Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p164-modification-cancellation-status-advice-process.md) | business-flow | src-000359 |
| [Movement Querying Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p165-movement-querying-process.md) | business-flow | src-000359 |
| [Movement Reporting Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p166-movement-reporting-process.md) | business-flow | src-000359 |
| [Modification/Cancellation Query and Report Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p169-modification-cancellation-query-and-report-process.md) | business-flow | src-000359 |
| [Pending Reporting Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p170-pending-reporting-process.md) | business-flow | src-000359 |
| [Posting Reporting Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p171-posting-reporting-process.md) | business-flow | src-000359 |
| [External Scenario](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p189-external-scenario.md) | business-flow | src-000359 |
| [Internal Scenario](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p193-internal-scenario.md) | business-flow | src-000359 |
| [Intra-Balance Movement Modification/Cancellation Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p197-intra-balance-movement-modification-cancellation-process.md) | business-flow | src-000359 |
| [Push Mode](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p200-push-mode.md) | business-flow | src-000359 |
| [Pull Mode](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p204-pull-mode.md) | business-flow | src-000359 |
| [Intra-Balance Movement Pending/Posting Report Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p208-intra-balance-movement-pending-posting-report-process.md) | business-flow | src-000359 |
| [Intra-Balance Movement Query/Response Process](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p211-intra-balance-movement-query-response-process.md) | business-flow | src-000359 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
