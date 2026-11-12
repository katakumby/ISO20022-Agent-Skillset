---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.074.001.02"
message_family: "camt.074"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.074.001.02"
source_ids: ["src-000233", "src-000360"]
source_locations: [{"source_id": "src-000233", "heading": "12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02", "file_pages": [198, 214]}, {"source_id": "src-000360", "heading": "7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02", "file_pages": [115, 131]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# camt.074.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp198–214; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02, Functionality, file p198.**

The IntraBalanceMovementCancellationRequest message is sent from an account owner/requestor to a
settlement infrastructure to request the cancellation of a previously sent
IntraBalanceMovementInstruction message.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is
"CopyDuplicate").
Outline
The IntraBalanceMovementCancellationRequestV02 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. TransactionIdentification
Unambiguous identification of a transaction as per the account owner (or the instructing party
managing the account).
C. CashAccount
Account to or from which an entry is made.
D. CashAccountOwner
Party that legally owns the cash account.
E. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
F. UnderlyingIntraBalance
Intra-balance movement transaction details.
G. SupplementaryData
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
Target2-Securities 198 August 2026

**src-000233, 12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02, Functionality, file p199.**

Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
Target2-Securities 199 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00149.md) | 198–199 |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 12.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00150.md) | 200–200 |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 12.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00151.md); [Constraints continuation C6–C12 (file p202)](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00152.md#file-page-202) | 201–201 |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 12.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00152.md) | 202–202 |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 12.4 Message Building Blocks / 12.4.1 Identification &lt;Id&gt; / 12.4.1.1 Identification &lt;Id&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00153.md) | 203–203 |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 12.4 Message Building Blocks / 12.4.1 Identification &lt;Id&gt; / 12.4.1.5 MessageRecipient &lt;MsgRcpt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00154.md) | 204–204 |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 12.4 Message Building Blocks / 12.4.2 TransactionIdentification &lt;TxId&gt; / 12.4.2.4 ProcessorTransactionIdentification &lt;PrcrTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00155.md) | 205–205 |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 12.4 Message Building Blocks / 12.4.5 CashAccountServicer &lt;CshAcctSvcr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00156.md) | 206–207 |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 12.4 Message Building Blocks / 12.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 12.4.6.1 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00157.md) | 208–208 |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 12.4 Message Building Blocks / 12.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 12.4.6.3 BalanceFrom &lt;BalFr&gt; / 12.4.6.3.1 Type &lt;Tp&gt; / 12.4.6.3.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00158.md) | 209–209 |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 12.4 Message Building Blocks / 12.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 12.4.6.3 BalanceFrom &lt;BalFr&gt; / 12.4.6.3.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 12.4.6.3.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00159.md) | 210–210 |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 12.4 Message Building Blocks / 12.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 12.4.6.4 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00160.md) | 211–211 |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 12.4 Message Building Blocks / 12.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 12.4.6.4 BalanceTo &lt;BalTo&gt; / 12.4.6.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00161.md) | 212–212 |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 12.4 Message Building Blocks / 12.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 12.4.6.4 BalanceTo &lt;BalTo&gt; / 12.4.6.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 12.4.6.4.2.3 LotQuantity &lt;LotQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00162.md) | 213–213 |
| [12 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 12.4 Message Building Blocks / 12.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 12.4.6.7 InstructionProcessingAdditionalDetails &lt;InstrPrcgAddtlDtls&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00163.md) | 214–214 |

## src-000360 — 7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02

[src-000360](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`; file pp115–131; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000360, 7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02, Functionality, file p115.**

The IntraBalanceMovementCancellationRequest message is sent from an account owner/requestor to a
settlement infrastructure to request the cancellation of a previously sent
IntraBalanceMovementInstruction message.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is
"CopyDuplicate").
Outline
The IntraBalanceMovementCancellationRequestV02 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. TransactionIdentification
Unambiguous identification of a transaction as per the account owner (or the instructing party
managing the account).
C. CashAccount
Account to or from which an entry is made.
D. CashAccountOwner
Party that legally owns the cash account.
E. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
F. UnderlyingIntraBalance
Intra-balance movement transaction details.
G. SupplementaryData
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
115 March 2024

**src-000360, 7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02, Functionality, file p116.**

Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
116 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00096.md) | 115–116 |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 7.2 Structure](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00097.md) | 117–117 |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 7.3 Constraints](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00098.md); [Constraints continuation C6–C12 (file p119)](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00099.md#file-page-119) | 118–118 |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 7.4 Message Building Blocks](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00099.md) | 119–119 |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 7.4 Message Building Blocks / 7.4.1 Identification &lt;Id&gt; / 7.4.1.1 Identification &lt;Id&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00100.md) | 120–120 |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 7.4 Message Building Blocks / 7.4.1 Identification &lt;Id&gt; / 7.4.1.5 MessageRecipient &lt;MsgRcpt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00101.md) | 121–121 |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 7.4 Message Building Blocks / 7.4.2 TransactionIdentification &lt;TxId&gt; / 7.4.2.4 ProcessorTransactionIdentification &lt;PrcrTxId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00102.md) | 122–122 |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 7.4 Message Building Blocks / 7.4.5 CashAccountServicer &lt;CshAcctSvcr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00103.md) | 123–124 |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 7.4 Message Building Blocks / 7.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 7.4.6.1 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00104.md) | 125–125 |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 7.4 Message Building Blocks / 7.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 7.4.6.3 BalanceFrom &lt;BalFr&gt; / 7.4.6.3.1 Type &lt;Tp&gt; / 7.4.6.3.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00105.md) | 126–126 |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 7.4 Message Building Blocks / 7.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 7.4.6.3 BalanceFrom &lt;BalFr&gt; / 7.4.6.3.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 7.4.6.3.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00106.md) | 127–127 |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 7.4 Message Building Blocks / 7.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 7.4.6.4 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00107.md) | 128–128 |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 7.4 Message Building Blocks / 7.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 7.4.6.4 BalanceTo &lt;BalTo&gt; / 7.4.6.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00108.md) | 129–129 |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 7.4 Message Building Blocks / 7.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 7.4.6.4 BalanceTo &lt;BalTo&gt; / 7.4.6.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 7.4.6.4.2.3 LotQuantity &lt;LotQty&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00109.md) | 130–130 |
| [7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02 / 7.4 Message Building Blocks / 7.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 7.4.6.7 InstructionProcessingAdditionalDetails &lt;InstrPrcgAddtlDtls&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00110.md) | 131–131 |

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
