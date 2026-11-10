---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.080.001.02"
message_family: "camt.080"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.080.001.02"
source_ids: ["src-000233", "src-000360"]
source_locations: [{"source_id": "src-000233", "heading": "18 camt.080.001.02 IntraBalanceMovementModificationQueryV02", "file_pages": [423, 435]}, {"source_id": "src-000360", "heading": "11 camt.080.001.02 IntraBalanceMovementModificationQueryV02", "file_pages": [232, 244]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2024"]
---

# camt.080.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 18 camt.080.001.02 IntraBalanceMovementModificationQueryV02

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp423–435; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 18 camt.080.001.02 IntraBalanceMovementModificationQueryV02, Functionality, file p423.**

The IntraBalanceMovementModificationQuery message is sent from an account owner/requestor to a
settlement infrastructure to query for the status of intra-balance movement modification instruction(s)
based on a set of search criteria or business attributes.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementModificationQueryV02 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. QueryDefinition
Defines the intra-balance movement modification query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.080.001.02
IntraBalanceMovementModificationQueryV02
Target2-Securities 423 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [18 camt.080.001.02 IntraBalanceMovementModificationQueryV02](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00326.md) | 423–423 |
| [18 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 18.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00327.md) | 424–424 |
| [18 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 18.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00328.md) | 425–425 |
| [18 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 18.4 Message Building Blocks / 18.4.1 Identification &lt;Id&gt; / 18.4.1.1 Identification &lt;Id&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00329.md) | 426–426 |
| [18 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 18.4 Message Building Blocks / 18.4.1 Identification &lt;Id&gt; / 18.4.1.4 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00330.md) | 427–427 |
| [18 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 18.4 Message Building Blocks / 18.4.2 QueryDefinition &lt;QryDef&gt; / 18.4.2.1 QueryType &lt;QryTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00331.md) | 428–428 |
| [18 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 18.4 Message Building Blocks / 18.4.2 QueryDefinition &lt;QryDef&gt; / 18.4.2.2 SearchCriteria &lt;SchCrit&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00332.md) | 429–429 |
| [18 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 18.4 Message Building Blocks / 18.4.2 QueryDefinition &lt;QryDef&gt; / 18.4.2.2 SearchCriteria &lt;SchCrit&gt; / 18.4.2.2.2 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00333.md) | 430–430 |
| [18 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 18.4 Message Building Blocks / 18.4.2 QueryDefinition &lt;QryDef&gt; / 18.4.2.2 SearchCriteria &lt;SchCrit&gt; / 18.4.2.2.4 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00334.md) | 431–431 |
| [18 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 18.4 Message Building Blocks / 18.4.2 QueryDefinition &lt;QryDef&gt; / 18.4.2.2 SearchCriteria &lt;SchCrit&gt; / 18.4.2.2.7 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00335.md) | 432–432 |
| [18 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 18.4 Message Building Blocks / 18.4.2 QueryDefinition &lt;QryDef&gt; / 18.4.2.2 SearchCriteria &lt;SchCrit&gt; / 18.4.2.2.7 CreationDateTime &lt;CreDtTm&gt; / 18.4.2.2.7.1 Date &lt;Dt&gt; / 18.4.2.2.7.1.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00336.md) | 433–433 |
| [18 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 18.4 Message Building Blocks / 18.4.2 QueryDefinition &lt;QryDef&gt; / 18.4.2.2 SearchCriteria &lt;SchCrit&gt; / 18.4.2.2.7 CreationDateTime &lt;CreDtTm&gt; / 18.4.2.2.7.2 DateTime &lt;DtTm&gt; / 18.4.2.2.7.2.1 FromDateTime &lt;FrDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00337.md) | 434–434 |
| [18 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 18.4 Message Building Blocks / 18.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00338.md) | 435–435 |

## src-000360 — 11 camt.080.001.02 IntraBalanceMovementModificationQueryV02

[src-000360](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`; file pp232–244; publication march-2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000360, 11 camt.080.001.02 IntraBalanceMovementModificationQueryV02, Functionality, file p232.**

The IntraBalanceMovementModificationQuery message is sent from an account owner/requestor to a
settlement infrastructure to query for the status of intra-balance movement modification instruction(s)
based on a set of search criteria or business attributes.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementModificationQueryV02 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. QueryDefinition
Defines the intra-balance movement modification query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.080.001.02
IntraBalanceMovementModificationQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
232 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [11 camt.080.001.02 IntraBalanceMovementModificationQueryV02](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00191.md) | 232–232 |
| [11 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 11.2 Structure](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00192.md) | 233–233 |
| [11 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 11.3 Constraints](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00193.md) | 234–234 |
| [11 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 11.4 Message Building Blocks / 11.4.1 Identification &lt;Id&gt; / 11.4.1.1 Identification &lt;Id&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00194.md) | 235–235 |
| [11 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 11.4 Message Building Blocks / 11.4.1 Identification &lt;Id&gt; / 11.4.1.4 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00195.md) | 236–236 |
| [11 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 11.4 Message Building Blocks / 11.4.2 QueryDefinition &lt;QryDef&gt; / 11.4.2.1 QueryType &lt;QryTp&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00196.md) | 237–237 |
| [11 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 11.4 Message Building Blocks / 11.4.2 QueryDefinition &lt;QryDef&gt; / 11.4.2.2 SearchCriteria &lt;SchCrit&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00197.md) | 238–238 |
| [11 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 11.4 Message Building Blocks / 11.4.2 QueryDefinition &lt;QryDef&gt; / 11.4.2.2 SearchCriteria &lt;SchCrit&gt; / 11.4.2.2.2 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00198.md) | 239–239 |
| [11 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 11.4 Message Building Blocks / 11.4.2 QueryDefinition &lt;QryDef&gt; / 11.4.2.2 SearchCriteria &lt;SchCrit&gt; / 11.4.2.2.4 CashAccountOwner &lt;CshAcctOwnr&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00199.md) | 240–240 |
| [11 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 11.4 Message Building Blocks / 11.4.2 QueryDefinition &lt;QryDef&gt; / 11.4.2.2 SearchCriteria &lt;SchCrit&gt; / 11.4.2.2.7 CreationDateTime &lt;CreDtTm&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00200.md) | 241–241 |
| [11 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 11.4 Message Building Blocks / 11.4.2 QueryDefinition &lt;QryDef&gt; / 11.4.2.2 SearchCriteria &lt;SchCrit&gt; / 11.4.2.2.7 CreationDateTime &lt;CreDtTm&gt; / 11.4.2.2.7.1 Date &lt;Dt&gt; / 11.4.2.2.7.1.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00201.md) | 242–242 |
| [11 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 11.4 Message Building Blocks / 11.4.2 QueryDefinition &lt;QryDef&gt; / 11.4.2.2 SearchCriteria &lt;SchCrit&gt; / 11.4.2.2.7 CreationDateTime &lt;CreDtTm&gt; / 11.4.2.2.7.2 DateTime &lt;DtTm&gt; / 11.4.2.2.7.2.1 FromDateTime &lt;FrDtTm&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00202.md) | 243–243 |
| [11 camt.080.001.02 IntraBalanceMovementModificationQueryV02 / 11.4 Message Building Blocks / 11.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00203.md) | 244–244 |

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
