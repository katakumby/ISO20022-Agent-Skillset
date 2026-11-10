---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.082.001.02"
message_family: "camt.082"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.082.001.02"
source_ids: ["src-000233", "src-000360"]
source_locations: [{"source_id": "src-000233", "heading": "20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02", "file_pages": [477, 490]}, {"source_id": "src-000360", "heading": "13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02", "file_pages": [286, 299]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# camt.082.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp477–490; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02, Functionality, file p477.**

The IntraBalanceMovementCancellationQuery message is sent from an account owner/requestor to a
settlement infrastructure to query for the status of intra-balance movement cancellation instruction(s)
based on a set of search criteria or business attributes.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementCancellationQueryV02 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. QueryDefinition
Defines the intra-balance movement cancellation query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.082.001.02
IntraBalanceMovementCancellationQueryV02
Target2-Securities 477 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00370.md) | 477–477 |
| [20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 20.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00371.md) | 478–478 |
| [20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 20.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00372.md) | 479–479 |
| [20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 20.4 Message Building Blocks / 20.4.1 Identification &lt;Id&gt; / 20.4.1.1 Identification &lt;Id&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00373.md) | 480–480 |
| [20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 20.4 Message Building Blocks / 20.4.1 Identification &lt;Id&gt; / 20.4.1.4 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00374.md) | 481–481 |
| [20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 20.4 Message Building Blocks / 20.4.2 QueryDefinition &lt;QryDef&gt; / 20.4.2.1 QueryType &lt;QryTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00375.md) | 482–482 |
| [20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 20.4 Message Building Blocks / 20.4.2 QueryDefinition &lt;QryDef&gt; / 20.4.2.2 SearchCriteria &lt;SchCrit&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00376.md) | 483–483 |
| [20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 20.4 Message Building Blocks / 20.4.2 QueryDefinition &lt;QryDef&gt; / 20.4.2.2 SearchCriteria &lt;SchCrit&gt; / 20.4.2.2.1 CancellationRequestIdentification &lt;CxlReqId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00377.md) | 484–484 |
| [20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 20.4 Message Building Blocks / 20.4.2 QueryDefinition &lt;QryDef&gt; / 20.4.2.2 SearchCriteria &lt;SchCrit&gt; / 20.4.2.2.2 ProcessingStatus &lt;PrcgSts&gt; / 20.4.2.2.2.1 Code &lt;Cd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00378.md) | 485–485 |
| [20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 20.4 Message Building Blocks / 20.4.2 QueryDefinition &lt;QryDef&gt; / 20.4.2.2 SearchCriteria &lt;SchCrit&gt; / 20.4.2.2.3 CashAccount &lt;CshAcct&gt; / 20.4.2.2.3.1 Equal &lt;EQ&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00379.md) | 486–486 |
| [20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 20.4 Message Building Blocks / 20.4.2 QueryDefinition &lt;QryDef&gt; / 20.4.2.2 SearchCriteria &lt;SchCrit&gt; / 20.4.2.2.6 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00380.md) | 487–487 |
| [20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 20.4 Message Building Blocks / 20.4.2 QueryDefinition &lt;QryDef&gt; / 20.4.2.2 SearchCriteria &lt;SchCrit&gt; / 20.4.2.2.7 CreationDateTime &lt;CreDtTm&gt; / 20.4.2.2.7.1 Date &lt;Dt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00381.md) | 488–488 |
| [20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 20.4 Message Building Blocks / 20.4.2 QueryDefinition &lt;QryDef&gt; / 20.4.2.2 SearchCriteria &lt;SchCrit&gt; / 20.4.2.2.7 CreationDateTime &lt;CreDtTm&gt; / 20.4.2.2.7.1 Date &lt;Dt&gt; / 20.4.2.2.7.1.3 FromToDate &lt;FrToDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00382.md) | 489–489 |
| [20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 20.4 Message Building Blocks / 20.4.2 QueryDefinition &lt;QryDef&gt; / 20.4.2.2 SearchCriteria &lt;SchCrit&gt; / 20.4.2.2.7 CreationDateTime &lt;CreDtTm&gt; / 20.4.2.2.7.2 DateTime &lt;DtTm&gt; / 20.4.2.2.7.2.3 FromToDateTime &lt;FrToDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00383.md) | 490–490 |

## src-000360 — 13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02

[src-000360](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`; file pp286–299; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000360, 13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02, Functionality, file p286.**

The IntraBalanceMovementCancellationQuery message is sent from an account owner/requestor to a
settlement infrastructure to query for the status of intra-balance movement cancellation instruction(s)
based on a set of search criteria or business attributes.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementCancellationQueryV02 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. QueryDefinition
Defines the intra-balance movement cancellation query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.082.001.02
IntraBalanceMovementCancellationQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
286 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00235.md) | 286–286 |
| [13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 13.2 Structure](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00236.md) | 287–287 |
| [13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 13.3 Constraints](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00237.md) | 288–288 |
| [13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 13.4 Message Building Blocks / 13.4.1 Identification &lt;Id&gt; / 13.4.1.1 Identification &lt;Id&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00238.md) | 289–289 |
| [13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 13.4 Message Building Blocks / 13.4.1 Identification &lt;Id&gt; / 13.4.1.4 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00239.md) | 290–290 |
| [13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 13.4 Message Building Blocks / 13.4.2 QueryDefinition &lt;QryDef&gt; / 13.4.2.1 QueryType &lt;QryTp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00240.md) | 291–291 |
| [13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 13.4 Message Building Blocks / 13.4.2 QueryDefinition &lt;QryDef&gt; / 13.4.2.2 SearchCriteria &lt;SchCrit&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00241.md) | 292–292 |
| [13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 13.4 Message Building Blocks / 13.4.2 QueryDefinition &lt;QryDef&gt; / 13.4.2.2 SearchCriteria &lt;SchCrit&gt; / 13.4.2.2.1 CancellationRequestIdentification &lt;CxlReqId&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00242.md) | 293–293 |
| [13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 13.4 Message Building Blocks / 13.4.2 QueryDefinition &lt;QryDef&gt; / 13.4.2.2 SearchCriteria &lt;SchCrit&gt; / 13.4.2.2.2 ProcessingStatus &lt;PrcgSts&gt; / 13.4.2.2.2.1 Code &lt;Cd&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00243.md) | 294–294 |
| [13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 13.4 Message Building Blocks / 13.4.2 QueryDefinition &lt;QryDef&gt; / 13.4.2.2 SearchCriteria &lt;SchCrit&gt; / 13.4.2.2.3 CashAccount &lt;CshAcct&gt; / 13.4.2.2.3.1 Equal &lt;EQ&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00244.md) | 295–295 |
| [13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 13.4 Message Building Blocks / 13.4.2 QueryDefinition &lt;QryDef&gt; / 13.4.2.2 SearchCriteria &lt;SchCrit&gt; / 13.4.2.2.6 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00245.md) | 296–296 |
| [13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 13.4 Message Building Blocks / 13.4.2 QueryDefinition &lt;QryDef&gt; / 13.4.2.2 SearchCriteria &lt;SchCrit&gt; / 13.4.2.2.7 CreationDateTime &lt;CreDtTm&gt; / 13.4.2.2.7.1 Date &lt;Dt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00246.md) | 297–297 |
| [13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 13.4 Message Building Blocks / 13.4.2 QueryDefinition &lt;QryDef&gt; / 13.4.2.2 SearchCriteria &lt;SchCrit&gt; / 13.4.2.2.7 CreationDateTime &lt;CreDtTm&gt; / 13.4.2.2.7.1 Date &lt;Dt&gt; / 13.4.2.2.7.1.3 FromToDate &lt;FrToDt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00247.md) | 298–298 |
| [13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02 / 13.4 Message Building Blocks / 13.4.2 QueryDefinition &lt;QryDef&gt; / 13.4.2.2 SearchCriteria &lt;SchCrit&gt; / 13.4.2.2.7 CreationDateTime &lt;CreDtTm&gt; / 13.4.2.2.7.2 DateTime &lt;DtTm&gt; / 13.4.2.2.7.2.3 FromToDateTime &lt;FrToDtTm&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00248.md) | 299–299 |

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
