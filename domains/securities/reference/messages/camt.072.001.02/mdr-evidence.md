---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.072.001.02"
message_family: "camt.072"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.072.001.02"
source_ids: ["src-000233", "src-000360"]
source_locations: [{"source_id": "src-000233", "heading": "10 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "file_pages": [149, 172]}, {"source_id": "src-000360", "heading": "5 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "file_pages": [66, 89]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# camt.072.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 10 camt.072.001.02 IntraBalanceMovementModificationRequestV02

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp149–172; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 10 camt.072.001.02 IntraBalanceMovementModificationRequestV02, Functionality, file p149.**

The IntraBalanceMovementModificationRequest message is sent from an account owner/requestor to a
settlement infrastructure to request the modification of a processing indicator on a previously sent
IntraBalanceMovementInstruction message.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is
"CopyDuplicate").
Outline
The IntraBalanceMovementModificationRequestV02 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. CashAccount
Account to or from which an entry is made.
C. CashAccountOwner
Party that legally owns the cash account.
D. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
E. RequestDetails
Details of the request providing the changes and references of the instruction for which the
modification is requested.
F. UnderlyingIntraBalance
Original intra-balance movement transaction details.
G. SupplementaryData
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities 149 August 2026

**src-000233, 10 camt.072.001.02 IntraBalanceMovementModificationRequestV02, Functionality, file p150.**

Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities 150 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00108.md) | 149–150 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00109.md) | 151–152 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00110.md) | 153–153 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00111.md) | 154–154 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.1 Identification &lt;Id&gt; / 10.4.1.2 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00112.md) | 155–155 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.2 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00113.md) | 156–156 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.4 CashAccountServicer &lt;CshAcctSvcr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00114.md) | 157–158 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.5 RequestDetails &lt;ReqDtls&gt; / 10.4.5.1 Reference &lt;Ref&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00115.md) | 159–159 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.5 RequestDetails &lt;ReqDtls&gt; / 10.4.5.1 Reference &lt;Ref&gt; / 10.4.5.1.5 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00116.md) | 160–160 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.5 RequestDetails &lt;ReqDtls&gt; / 10.4.5.6 ClearingChannel &lt;ClrChanl&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00117.md) | 161–161 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.5 RequestDetails &lt;ReqDtls&gt; / 10.4.5.7 Linkages &lt;Lnkgs&gt; / 10.4.5.7.1 ProcessingPosition &lt;PrcgPos&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00118.md) | 162–162 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.5 RequestDetails &lt;ReqDtls&gt; / 10.4.5.7 Linkages &lt;Lnkgs&gt; / 10.4.5.7.3 Reference &lt;Ref&gt; / 10.4.5.7.3.1 SecuritiesSettlementTransactionIdentification &lt;SctiesSttlmTxId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00119.md) | 163–163 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.5 RequestDetails &lt;ReqDtls&gt; / 10.4.5.7 Linkages &lt;Lnkgs&gt; / 10.4.5.7.3 Reference &lt;Ref&gt; / 10.4.5.7.3.6 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00120.md) | 164–165 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 10.4.6.1 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00121.md) | 166–166 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 10.4.6.3 BalanceFrom &lt;BalFr&gt; / 10.4.6.3.1 Type &lt;Tp&gt; / 10.4.6.3.1.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00122.md) | 167–167 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 10.4.6.3 BalanceFrom &lt;BalFr&gt; / 10.4.6.3.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 10.4.6.3.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00123.md) | 168–168 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 10.4.6.4 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00124.md) | 169–169 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 10.4.6.4 BalanceTo &lt;BalTo&gt; / 10.4.6.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00125.md) | 170–170 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 10.4.6.4 BalanceTo &lt;BalTo&gt; / 10.4.6.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 10.4.6.4.2.3 LotQuantity &lt;LotQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00126.md) | 171–171 |
| [10 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 10.4 Message Building Blocks / 10.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 10.4.6.7 InstructionProcessingAdditionalDetails &lt;InstrPrcgAddtlDtls&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00127.md) | 172–172 |

## src-000360 — 5 camt.072.001.02 IntraBalanceMovementModificationRequestV02

[src-000360](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`; file pp66–89; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000360, 5 camt.072.001.02 IntraBalanceMovementModificationRequestV02, Functionality, file p66.**

The IntraBalanceMovementModificationRequest message is sent from an account owner/requestor to a
settlement infrastructure to request the modification of a processing indicator on a previously sent
IntraBalanceMovementInstruction message.
Usage:
The message may be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is
"CopyDuplicate").
Outline
The IntraBalanceMovementModificationRequestV02 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. CashAccount
Account to or from which an entry is made.
C. CashAccountOwner
Party that legally owns the cash account.
D. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
E. RequestDetails
Details of the request providing the changes and references of the instruction for which the
modification is requested.
F. UnderlyingIntraBalance
Original intra-balance movement transaction details.
G. SupplementaryData
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
66 March 2024

**src-000360, 5 camt.072.001.02 IntraBalanceMovementModificationRequestV02, Functionality, file p67.**

Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.072.001.02
IntraBalanceMovementModificationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
67 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00055.md) | 66–67 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.2 Structure](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00056.md) | 68–69 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.3 Constraints](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00057.md) | 70–70 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00058.md) | 71–71 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.1 Identification &lt;Id&gt; / 5.4.1.2 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00059.md) | 72–72 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.2 CashAccount &lt;CshAcct&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00060.md) | 73–73 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.4 CashAccountServicer &lt;CshAcctSvcr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00061.md) | 74–75 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.5 RequestDetails &lt;ReqDtls&gt; / 5.4.5.1 Reference &lt;Ref&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00062.md) | 76–76 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.5 RequestDetails &lt;ReqDtls&gt; / 5.4.5.1 Reference &lt;Ref&gt; / 5.4.5.1.5 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00063.md) | 77–77 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.5 RequestDetails &lt;ReqDtls&gt; / 5.4.5.6 ClearingChannel &lt;ClrChanl&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00064.md) | 78–78 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.5 RequestDetails &lt;ReqDtls&gt; / 5.4.5.7 Linkages &lt;Lnkgs&gt; / 5.4.5.7.1 ProcessingPosition &lt;PrcgPos&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00065.md) | 79–79 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.5 RequestDetails &lt;ReqDtls&gt; / 5.4.5.7 Linkages &lt;Lnkgs&gt; / 5.4.5.7.3 Reference &lt;Ref&gt; / 5.4.5.7.3.1 SecuritiesSettlementTransactionIdentification &lt;SctiesSttlmTxId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00066.md) | 80–80 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.5 RequestDetails &lt;ReqDtls&gt; / 5.4.5.7 Linkages &lt;Lnkgs&gt; / 5.4.5.7.3 Reference &lt;Ref&gt; / 5.4.5.7.3.6 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00067.md) | 81–82 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 5.4.6.1 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00068.md) | 83–83 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 5.4.6.3 BalanceFrom &lt;BalFr&gt; / 5.4.6.3.1 Type &lt;Tp&gt; / 5.4.6.3.1.1 Code &lt;Cd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00069.md) | 84–84 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 5.4.6.3 BalanceFrom &lt;BalFr&gt; / 5.4.6.3.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 5.4.6.3.2.2 LotAmount &lt;LotAmt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00070.md) | 85–85 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 5.4.6.4 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00071.md) | 86–86 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 5.4.6.4 BalanceTo &lt;BalTo&gt; / 5.4.6.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00072.md) | 87–87 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 5.4.6.4 BalanceTo &lt;BalTo&gt; / 5.4.6.4.2 QuantityBreakdown &lt;QtyBrkdwn&gt; / 5.4.6.4.2.3 LotQuantity &lt;LotQty&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00073.md) | 88–88 |
| [5 camt.072.001.02 IntraBalanceMovementModificationRequestV02 / 5.4 Message Building Blocks / 5.4.6 UnderlyingIntraBalance &lt;UndrlygIntraBal&gt; / 5.4.6.7 InstructionProcessingAdditionalDetails &lt;InstrPrcgAddtlDtls&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00074.md) | 89–89 |

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
