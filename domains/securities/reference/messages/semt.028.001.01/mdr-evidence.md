---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.028.001.01"
message_family: "semt.028"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.028.001.01"
source_ids: ["src-000233", "src-000381"]
source_locations: [{"source_id": "src-000233", "heading": "73 semt.028.001.01 IntraPositionMovementQueryV01", "file_pages": [2562, 2611]}, {"source_id": "src-000381", "heading": "2 semt.028.001.01 IntraPositionMovementQueryV01", "file_pages": [7, 56]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "september-2025"]
---

# semt.028.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 73 semt.028.001.01 IntraPositionMovementQueryV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2562–2611; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 73 semt.028.001.01 IntraPositionMovementQueryV01, Functionality, file p2562.**

The IntraPositionMovementQuery message is sent from an account owner/requestor to a settlement
infrastructure to query intra-position movement instructions, along with their current status, based on a
set of search criteria.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraPositionMovementQueryV01 MessageDefinition is composed of 2 MessageBuildingBlocks:
A. QueryDefinition
Defines the intra-position movement instruction query criteria.
B. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2562 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [73 semt.028.001.01 IntraPositionMovementQueryV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01868.md) | 2562–2562 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01869.md) | 2563–2566 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.3 Constraints](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01870.md) | 2567–2567 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01871.md) | 2568–2572 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.1 QueryType &lt;QryTp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01872.md) | 2573–2577 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.1 References &lt;Refs&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01873.md) | 2578–2578 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.1 References &lt;Refs&gt; / 73.4.1.2.1.6 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01874.md) | 2579–2579 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.2 Status &lt;Sts&gt; / 73.4.1.2.2.1 Type &lt;Tp&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01875.md) | 2580–2580 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.2 Status &lt;Sts&gt; / 73.4.1.2.2.2 DatePeriod &lt;DtPrd&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01876.md) | 2581–2581 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.2 Status &lt;Sts&gt; / 73.4.1.2.2.2 DatePeriod &lt;DtPrd&gt; / 73.4.1.2.2.2.1 Date &lt;Dt&gt; / 73.4.1.2.2.2.1.2 ToDate &lt;ToDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01877.md) | 2582–2582 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.2 Status &lt;Sts&gt; / 73.4.1.2.2.2 DatePeriod &lt;DtPrd&gt; / 73.4.1.2.2.2.2 DateTime &lt;DtTm&gt; / 73.4.1.2.2.2.2.2 ToDateTime &lt;ToDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01878.md) | 2583–2583 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.4 SafekeepingAccountOwner &lt;SfkpgAcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01879.md) | 2584–2584 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.5 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01880.md) | 2585–2585 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.6 BalanceType &lt;BalTp&gt; / 73.4.1.2.6.2 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01881.md) | 2586–2586 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 73.4.1.2.8.1 Quantity &lt;Qty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01882.md) | 2587–2587 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 73.4.1.2.8.1 Quantity &lt;Qty&gt; / 73.4.1.2.8.1.1 Unit &lt;Unit&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01883.md) | 2588–2588 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 73.4.1.2.8.1 Quantity &lt;Qty&gt; / 73.4.1.2.8.1.1 Unit &lt;Unit&gt; / 73.4.1.2.8.1.1.1 FromQuantity &lt;FrQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01884.md) | 2589–2589 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 73.4.1.2.8.1 Quantity &lt;Qty&gt; / 73.4.1.2.8.1.1 Unit &lt;Unit&gt; / 73.4.1.2.8.1.1.2 ToQuantity &lt;ToQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01885.md) | 2590–2590 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 73.4.1.2.8.1 Quantity &lt;Qty&gt; / 73.4.1.2.8.1.1 Unit &lt;Unit&gt; / 73.4.1.2.8.1.1.3 FromToQuantity &lt;FrToQty&gt; / 73.4.1.2.8.1.1.3.1 FromQuantity &lt;FrQty&gt; / 73.4.1.2.8.1.1.3.1.1 Boundary &lt;Bdry&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01886.md) | 2591–2591 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 73.4.1.2.8.1 Quantity &lt;Qty&gt; / 73.4.1.2.8.1.1 Unit &lt;Unit&gt; / 73.4.1.2.8.1.1.4 EqualQuantity &lt;EQQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01887.md) | 2592–2592 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 73.4.1.2.8.2 OriginalAndCurrentFace &lt;OrgnlAndCurFace&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01888.md) | 2593–2593 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 73.4.1.2.8.2 OriginalAndCurrentFace &lt;OrgnlAndCurFace&gt; / 73.4.1.2.8.2.2 AmortisedValue &lt;AmtsdVal&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01889.md) | 2594–2594 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 73.4.1.2.9.1 Quantity &lt;Qty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01890.md) | 2595–2595 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 73.4.1.2.9.1 Quantity &lt;Qty&gt; / 73.4.1.2.9.1.1 Unit &lt;Unit&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01891.md) | 2596–2596 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 73.4.1.2.9.1 Quantity &lt;Qty&gt; / 73.4.1.2.9.1.1 Unit &lt;Unit&gt; / 73.4.1.2.9.1.1.1 FromQuantity &lt;FrQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01892.md) | 2597–2597 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 73.4.1.2.9.1 Quantity &lt;Qty&gt; / 73.4.1.2.9.1.1 Unit &lt;Unit&gt; / 73.4.1.2.9.1.1.2 ToQuantity &lt;ToQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01893.md) | 2598–2598 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 73.4.1.2.9.1 Quantity &lt;Qty&gt; / 73.4.1.2.9.1.1 Unit &lt;Unit&gt; / 73.4.1.2.9.1.1.3 FromToQuantity &lt;FrToQty&gt; / 73.4.1.2.9.1.1.3.1 FromQuantity &lt;FrQty&gt; / 73.4.1.2.9.1.1.3.1.1 Boundary &lt;Bdry&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01894.md) | 2599–2599 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 73.4.1.2.9.1 Quantity &lt;Qty&gt; / 73.4.1.2.9.1.1 Unit &lt;Unit&gt; / 73.4.1.2.9.1.1.4 EqualQuantity &lt;EQQty&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01895.md) | 2600–2600 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 73.4.1.2.9.2 OriginalAndCurrentFace &lt;OrgnlAndCurFace&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01896.md) | 2601–2601 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 73.4.1.2.9.2 OriginalAndCurrentFace &lt;OrgnlAndCurFace&gt; / 73.4.1.2.9.2.2 AmortisedValue &lt;AmtsdVal&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01897.md) | 2602–2602 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.10 IntendedSettlementDate &lt;IntnddSttlmDt&gt; / 73.4.1.2.10.1 Date &lt;Dt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01898.md) | 2603–2603 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.10 IntendedSettlementDate &lt;IntnddSttlmDt&gt; / 73.4.1.2.10.2 DateTime &lt;DtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01899.md) | 2604–2604 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.11 EffectiveSettlementDate &lt;FctvSttlmDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01900.md) | 2605–2605 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.11 EffectiveSettlementDate &lt;FctvSttlmDt&gt; / 73.4.1.2.11.1 Date &lt;Dt&gt; / 73.4.1.2.11.1.2 ToDate &lt;ToDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01901.md) | 2606–2606 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.11 EffectiveSettlementDate &lt;FctvSttlmDt&gt; / 73.4.1.2.11.2 DateTime &lt;DtTm&gt; / 73.4.1.2.11.2.2 ToDateTime &lt;ToDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01902.md) | 2607–2607 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.14 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01903.md) | 2608–2608 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.15 CreationDateTime &lt;CreDtTm&gt; / 73.4.1.2.15.1 Date &lt;Dt&gt; / 73.4.1.2.15.1.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01904.md) | 2609–2609 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.1 QueryDefinition &lt;QryDef&gt; / 73.4.1.2 SearchCriteria &lt;SchCrit&gt; / 73.4.1.2.15 CreationDateTime &lt;CreDtTm&gt; / 73.4.1.2.15.2 DateTime &lt;DtTm&gt; / 73.4.1.2.15.2.1 FromDateTime &lt;FrDtTm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01905.md) | 2610–2610 |
| [73 semt.028.001.01 IntraPositionMovementQueryV01 / 73.4 Message Building Blocks / 73.4.2 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01906.md) | 2611–2611 |

## src-000381 — 2 semt.028.001.01 IntraPositionMovementQueryV01

[src-000381](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`; file pp7–56; publication september-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000381, 2 semt.028.001.01 IntraPositionMovementQueryV01, Functionality, file p7.**

The IntraPositionMovementQuery message is sent from an account owner/requestor to a settlement
infrastructure to query intra-position movement instructions, along with their current status, based on a
set of search criteria.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraPositionMovementQueryV01 MessageDefinition is composed of 2 MessageBuildingBlocks:
A. QueryDefinition
Defines the intra-position movement instruction query criteria.
B. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 7 September 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 semt.028.001.01 IntraPositionMovementQueryV01](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00004.md) | 7–7 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.2 Structure](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00005.md) | 8–11 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.3 Constraints](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00006.md) | 12–12 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00007.md) | 13–17 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.1 QueryType &lt;QryTp&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00008.md) | 18–22 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.1 References &lt;Refs&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00009.md) | 23–23 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.1 References &lt;Refs&gt; / 2.4.1.2.1.6 PoolIdentification &lt;PoolId&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00010.md) | 24–24 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.2 Status &lt;Sts&gt; / 2.4.1.2.2.1 Type &lt;Tp&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00011.md) | 25–25 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.2 Status &lt;Sts&gt; / 2.4.1.2.2.2 DatePeriod &lt;DtPrd&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00012.md) | 26–26 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.2 Status &lt;Sts&gt; / 2.4.1.2.2.2 DatePeriod &lt;DtPrd&gt; / 2.4.1.2.2.2.1 Date &lt;Dt&gt; / 2.4.1.2.2.2.1.2 ToDate &lt;ToDt&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00013.md) | 27–27 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.2 Status &lt;Sts&gt; / 2.4.1.2.2.2 DatePeriod &lt;DtPrd&gt; / 2.4.1.2.2.2.2 DateTime &lt;DtTm&gt; / 2.4.1.2.2.2.2.2 ToDateTime &lt;ToDtTm&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00014.md) | 28–28 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.4 SafekeepingAccountOwner &lt;SfkpgAcctOwnr&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00015.md) | 29–29 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.5 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00016.md) | 30–30 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.6 BalanceType &lt;BalTp&gt; / 2.4.1.2.6.2 BalanceTo &lt;BalTo&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00017.md) | 31–31 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 2.4.1.2.8.1 Quantity &lt;Qty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00018.md) | 32–32 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 2.4.1.2.8.1 Quantity &lt;Qty&gt; / 2.4.1.2.8.1.1 Unit &lt;Unit&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00019.md) | 33–33 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 2.4.1.2.8.1 Quantity &lt;Qty&gt; / 2.4.1.2.8.1.1 Unit &lt;Unit&gt; / 2.4.1.2.8.1.1.1 FromQuantity &lt;FrQty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00020.md) | 34–34 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 2.4.1.2.8.1 Quantity &lt;Qty&gt; / 2.4.1.2.8.1.1 Unit &lt;Unit&gt; / 2.4.1.2.8.1.1.2 ToQuantity &lt;ToQty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00021.md) | 35–35 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 2.4.1.2.8.1 Quantity &lt;Qty&gt; / 2.4.1.2.8.1.1 Unit &lt;Unit&gt; / 2.4.1.2.8.1.1.3 FromToQuantity &lt;FrToQty&gt; / 2.4.1.2.8.1.1.3.1 FromQuantity &lt;FrQty&gt; / 2.4.1.2.8.1.1.3.1.1 Boundary &lt;Bdry&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00022.md) | 36–36 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 2.4.1.2.8.1 Quantity &lt;Qty&gt; / 2.4.1.2.8.1.1 Unit &lt;Unit&gt; / 2.4.1.2.8.1.1.4 EqualQuantity &lt;EQQty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00023.md) | 37–37 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 2.4.1.2.8.2 OriginalAndCurrentFace &lt;OrgnlAndCurFace&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00024.md) | 38–38 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.8 SettlementQuantity &lt;SttlmQty&gt; / 2.4.1.2.8.2 OriginalAndCurrentFace &lt;OrgnlAndCurFace&gt; / 2.4.1.2.8.2.2 AmortisedValue &lt;AmtsdVal&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00025.md) | 39–39 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 2.4.1.2.9.1 Quantity &lt;Qty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00026.md) | 40–40 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 2.4.1.2.9.1 Quantity &lt;Qty&gt; / 2.4.1.2.9.1.1 Unit &lt;Unit&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00027.md) | 41–41 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 2.4.1.2.9.1 Quantity &lt;Qty&gt; / 2.4.1.2.9.1.1 Unit &lt;Unit&gt; / 2.4.1.2.9.1.1.1 FromQuantity &lt;FrQty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00028.md) | 42–42 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 2.4.1.2.9.1 Quantity &lt;Qty&gt; / 2.4.1.2.9.1.1 Unit &lt;Unit&gt; / 2.4.1.2.9.1.1.2 ToQuantity &lt;ToQty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00029.md) | 43–43 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 2.4.1.2.9.1 Quantity &lt;Qty&gt; / 2.4.1.2.9.1.1 Unit &lt;Unit&gt; / 2.4.1.2.9.1.1.3 FromToQuantity &lt;FrToQty&gt; / 2.4.1.2.9.1.1.3.1 FromQuantity &lt;FrQty&gt; / 2.4.1.2.9.1.1.3.1.1 Boundary &lt;Bdry&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00030.md) | 44–44 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 2.4.1.2.9.1 Quantity &lt;Qty&gt; / 2.4.1.2.9.1.1 Unit &lt;Unit&gt; / 2.4.1.2.9.1.1.4 EqualQuantity &lt;EQQty&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00031.md) | 45–45 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 2.4.1.2.9.2 OriginalAndCurrentFace &lt;OrgnlAndCurFace&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00032.md) | 46–46 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.9 SettledQuantity &lt;SttldQty&gt; / 2.4.1.2.9.2 OriginalAndCurrentFace &lt;OrgnlAndCurFace&gt; / 2.4.1.2.9.2.2 AmortisedValue &lt;AmtsdVal&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00033.md) | 47–47 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.10 IntendedSettlementDate &lt;IntnddSttlmDt&gt; / 2.4.1.2.10.1 Date &lt;Dt&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00034.md) | 48–48 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.10 IntendedSettlementDate &lt;IntnddSttlmDt&gt; / 2.4.1.2.10.2 DateTime &lt;DtTm&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00035.md) | 49–49 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.11 EffectiveSettlementDate &lt;FctvSttlmDt&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00036.md) | 50–50 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.11 EffectiveSettlementDate &lt;FctvSttlmDt&gt; / 2.4.1.2.11.1 Date &lt;Dt&gt; / 2.4.1.2.11.1.2 ToDate &lt;ToDt&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00037.md) | 51–51 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.11 EffectiveSettlementDate &lt;FctvSttlmDt&gt; / 2.4.1.2.11.2 DateTime &lt;DtTm&gt; / 2.4.1.2.11.2.2 ToDateTime &lt;ToDtTm&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00038.md) | 52–52 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.14 MessageOriginator &lt;MsgOrgtr&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00039.md) | 53–53 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.15 CreationDateTime &lt;CreDtTm&gt; / 2.4.1.2.15.1 Date &lt;Dt&gt; / 2.4.1.2.15.1.1 FromDate &lt;FrDt&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00040.md) | 54–54 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.1 QueryDefinition &lt;QryDef&gt; / 2.4.1.2 SearchCriteria &lt;SchCrit&gt; / 2.4.1.2.15 CreationDateTime &lt;CreDtTm&gt; / 2.4.1.2.15.2 DateTime &lt;DtTm&gt; / 2.4.1.2.15.2.1 FromDateTime &lt;FrDtTm&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00041.md) | 55–55 |
| [2 semt.028.001.01 IntraPositionMovementQueryV01 / 2.4 Message Building Blocks / 2.4.2 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-settlement-restrictions/september-2025/documents/src-000381/sections/section-00042.md) | 56–56 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Central Counterparty](../../../../../shared/reference/participants/participant-src-000380-central-counterparty.md) | participant | src-000380 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000380-central-securities-depositories-csd.md) | participant | src-000380 |
| [Direct Connected Participant (DCP)](../../../../../shared/reference/participants/participant-src-000380-direct-connected-participant-dcp.md) | participant | src-000380 |
| [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000380-executing-servicing-party.md) | participant | src-000380 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000380-instructing-party.md) | participant | src-000380 |
| [Settlement Infrastructure](../../../../../shared/reference/participants/participant-src-000380-settlement-infrastructure.md) | participant | src-000380 |
| [T2S Operator](../../../../../shared/reference/participants/participant-src-000380-t2s-operator.md) | participant | src-000380 |
| [Query Report Process](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p253-query-report-process.md) | business-flow | src-000380 |
| [Pull mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p259-pull-mode.md) | business-flow | src-000380 |
| [Push mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p263-push-mode.md) | business-flow | src-000380 |
| [Pull mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p268-pull-mode.md) | business-flow | src-000380 |
| [Push mode](../../message-sets/t2s-settlement-restrictions/september-2025/flows/flow-src-000380-p272-push-mode.md) | business-flow | src-000380 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
