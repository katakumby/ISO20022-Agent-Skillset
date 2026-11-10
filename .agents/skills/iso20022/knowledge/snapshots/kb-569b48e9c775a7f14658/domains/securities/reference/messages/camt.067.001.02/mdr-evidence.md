---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.067.001.02"
message_family: "camt.067"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.067.001.02"
source_ids: ["src-000233", "src-000360"]
source_locations: [{"source_id": "src-000233", "heading": "8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02", "file_pages": [114, 132]}, {"source_id": "src-000360", "heading": "3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02", "file_pages": [31, 49]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# camt.067.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp114–132; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02, Functionality, file p114.**

The IntraBalanceMovementStatusAdvice message is sent from a settlement infrastructure to an
account owner/requestor to advise the status of an intra-balance movement instruction previously sent
by the account owner/requestor.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is
"CopyDuplicate").
Outline
The IntraBalanceMovementStatusAdviceV02 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
B. TransactionIdentification
Unambiguous identification of a transaction as per the account owner (or the instructing party
managing the account).
C. ProcessingStatus
Provides details on the processing status of the transaction.
D. SettlementStatus
Provides the settlement status of a transaction.
E. CashAccount
Account to or from which an entry is made.
F. CashAccountOwner
Party that legally owns the cash account.
G. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
H. UnderlyingIntraBalance
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities 114 August 2026

**src-000233, 8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02, Functionality, file p115.**

Intra-balance movement transaction details.
I. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities 115 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00075.md) | 114–115 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00076.md) | 116–116 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00077.md) | 117–117 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00078.md) | 118–118 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.4 Message Building Blocks / 8.4.1 Identification &lt;Id&gt; / 8.4.1.1 Identification &lt;Id&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00079.md) | 119–119 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.4 Message Building Blocks / 8.4.1 Identification &lt;Id&gt; / 8.4.1.4 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00080.md) | 120–120 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.4 Message Building Blocks / 8.4.2 TransactionIdentification &lt;TxId&gt; / 8.4.2.1 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00081.md) | 121–121 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.4 Message Building Blocks / 8.4.4 SettlementStatus &lt;SttlmSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00082.md) | 122–122 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.4 Message Building Blocks / 8.4.6 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00083.md) | 123–123 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.4 Message Building Blocks / 8.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00084.md) | 124–125 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.4 Message Building Blocks / 8.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 8.4.8.1 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00085.md) | 126–126 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.4 Message Building Blocks / 8.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 8.4.8.3 BalanceFrom &lt;BalFr&gt; / 8.4.8.3.1 Type &lt;Tp&gt; / 8.4.8.3.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00086.md) | 127–127 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.4 Message Building Blocks / 8.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 8.4.8.3 BalanceFrom &lt;BalFr&gt; / 8.4.8.3.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 8.4.8.3.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00087.md) | 128–128 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.4 Message Building Blocks / 8.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 8.4.8.4 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00088.md) | 129–129 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.4 Message Building Blocks / 8.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 8.4.8.4 BalanceTo &lt;BalTo&gt; / 8.4.8.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00089.md) | 130–130 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.4 Message Building Blocks / 8.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 8.4.8.4 BalanceTo &lt;BalTo&gt; / 8.4.8.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 8.4.8.4.2.3 LotQuantity &lt;LotQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00090.md) | 131–131 |
| [8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 8.4 Message Building Blocks / 8.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 8.4.8.7 InstructionProcessingAdditionalDetails &lt;InstrPrcgAddtlDtls&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00091.md) | 132–132 |

## src-000360 — 3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02

[src-000360](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`; file pp31–49; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000360, 3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02, Functionality, file p31.**

The IntraBalanceMovementStatusAdvice message is sent from a settlement infrastructure to an
account owner/requestor to advise the status of an intra-balance movement instruction previously sent
by the account owner/requestor.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is
"CopyDuplicate").
Outline
The IntraBalanceMovementStatusAdviceV02 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
B. TransactionIdentification
Unambiguous identification of a transaction as per the account owner (or the instructing party
managing the account).
C. ProcessingStatus
Provides details on the processing status of the transaction.
D. SettlementStatus
Provides the settlement status of a transaction.
E. CashAccount
Account to or from which an entry is made.
F. CashAccountOwner
Party that legally owns the cash account.
G. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
H. UnderlyingIntraBalance
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
31 March 2024

**src-000360, 3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02, Functionality, file p32.**

Intra-balance movement transaction details.
I. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
32 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00022.md) | 31–32 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.2 Structure](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00023.md) | 33–33 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.3 Constraints](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00024.md) | 34–34 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.4 Message Building Blocks](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00025.md) | 35–35 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.4 Message Building Blocks / 3.4.1 Identification &lt;Id&gt; / 3.4.1.1 Identification &lt;Id&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00026.md) | 36–36 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.4 Message Building Blocks / 3.4.1 Identification &lt;Id&gt; / 3.4.1.4 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00027.md) | 37–37 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.4 Message Building Blocks / 3.4.2 TransactionIdentification &lt;TxId&gt; / 3.4.2.1 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00028.md) | 38–38 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.4 Message Building Blocks / 3.4.4 SettlementStatus &lt;SttlmSts&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00029.md) | 39–39 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.4 Message Building Blocks / 3.4.6 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00030.md) | 40–40 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.4 Message Building Blocks / 3.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00031.md) | 41–42 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.4 Message Building Blocks / 3.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 3.4.8.1 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00032.md) | 43–43 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.4 Message Building Blocks / 3.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 3.4.8.3 BalanceFrom &lt;BalFr&gt; / 3.4.8.3.1 Type &lt;Tp&gt; / 3.4.8.3.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00033.md) | 44–44 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.4 Message Building Blocks / 3.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 3.4.8.3 BalanceFrom &lt;BalFr&gt; / 3.4.8.3.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 3.4.8.3.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00034.md) | 45–45 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.4 Message Building Blocks / 3.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 3.4.8.4 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00035.md) | 46–46 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.4 Message Building Blocks / 3.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 3.4.8.4 BalanceTo &lt;BalTo&gt; / 3.4.8.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00036.md) | 47–47 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.4 Message Building Blocks / 3.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 3.4.8.4 BalanceTo &lt;BalTo&gt; / 3.4.8.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 3.4.8.4.2.3 LotQuantity &lt;LotQty&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00037.md) | 48–48 |
| [3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02 / 3.4 Message Building Blocks / 3.4.8 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 3.4.8.7 InstructionProcessingAdditionalDetails &lt;InstrPrcgAddtlDtls&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00038.md) | 49–49 |

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
