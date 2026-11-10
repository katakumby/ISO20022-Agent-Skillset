---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.069.001.05"
message_family: "camt.069"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.069.001.05"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "30 camt.069.001.05 GetStandingOrderV05", "file_pages": [686, 706]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.069.001.05 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 30 camt.069.001.05 GetStandingOrderV05

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp686–706; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 30 camt.069.001.05 GetStandingOrderV05, Functionality, file p686.**

Scope
The GetStandingOrder message is sent by a member to the transaction administrator.
It is used to request information on the details of one or more standing orders, based on specific
request criteria, especially to query the amount of the overall liquidity available. It will allow to query
both reserved liquidity and liquidity available for normal operations.
Usage
The member can request information based on the following elements:
- individual standing orders (predefined or standing liquidity transfer orders)
- amount
- account to be credited
- account to be debited
- account owner (for on behalf scenario)
- frequency of payment
- daytime or overnight processing
- dates when the standing order begins and ceases to be effective
This message will be answered by a ReturnStandingOrder message.
Outline
The GetStandingOrderV05 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. StandingOrderQueryDefinition
Defines the account query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 686 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [30 camt.069.001.05 GetStandingOrderV05](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00524.md) | 686–686 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00525.md) | 687–687 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00526.md) | 688–688 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00527.md) | 689–690 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.4 Message Building Blocks / 30.4.2 StandingOrderQueryDefinition &lt;StgOrdrQryDef&gt; / 30.4.2.1 QueryType &lt;QryTp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00528.md) | 691–692 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.4 Message Building Blocks / 30.4.2 StandingOrderQueryDefinition &lt;StgOrdrQryDef&gt; / 30.4.2.2 StandingOrderCriteria &lt;StgOrdrCrit&gt; / 30.4.2.2.1 QueryName &lt;QryNm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00529.md) | 693–694 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.4 Message Building Blocks / 30.4.2 StandingOrderQueryDefinition &lt;StgOrdrQryDef&gt; / 30.4.2.2 StandingOrderCriteria &lt;StgOrdrCrit&gt; / 30.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 30.4.2.2.2.1 NewQueryName &lt;NewQryNm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00530.md) | 695–695 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.4 Message Building Blocks / 30.4.2 StandingOrderQueryDefinition &lt;StgOrdrQryDef&gt; / 30.4.2.2 StandingOrderCriteria &lt;StgOrdrCrit&gt; / 30.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 30.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 30.4.2.2.2.2.1 KeyAttributesIndicator &lt;KeyAttrbtsInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00531.md) | 696–696 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.4 Message Building Blocks / 30.4.2 StandingOrderQueryDefinition &lt;StgOrdrQryDef&gt; / 30.4.2.2 StandingOrderCriteria &lt;StgOrdrCrit&gt; / 30.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 30.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 30.4.2.2.2.2.3 Type &lt;Tp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00532.md) | 697–697 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.4 Message Building Blocks / 30.4.2 StandingOrderQueryDefinition &lt;StgOrdrQryDef&gt; / 30.4.2.2 StandingOrderCriteria &lt;StgOrdrCrit&gt; / 30.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 30.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 30.4.2.2.2.2.5 Currency &lt;Ccy&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00533.md) | 698–698 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.4 Message Building Blocks / 30.4.2 StandingOrderQueryDefinition &lt;StgOrdrQryDef&gt; / 30.4.2.2 StandingOrderCriteria &lt;StgOrdrCrit&gt; / 30.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 30.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 30.4.2.2.2.2.6 ValidityPeriod &lt;VldtyPrd&gt; / 30.4.2.2.2.2.6.1 FromDate &lt;FrDt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00534.md) | 699–699 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.4 Message Building Blocks / 30.4.2 StandingOrderQueryDefinition &lt;StgOrdrQryDef&gt; / 30.4.2.2 StandingOrderCriteria &lt;StgOrdrCrit&gt; / 30.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 30.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 30.4.2.2.2.2.8 ResponsibleParty &lt;RspnsblPty&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00535.md) | 700–700 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.4 Message Building Blocks / 30.4.2 StandingOrderQueryDefinition &lt;StgOrdrQryDef&gt; / 30.4.2.2 StandingOrderCriteria &lt;StgOrdrCrit&gt; / 30.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 30.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 30.4.2.2.2.2.9 AssociatedPoolAccount &lt;AssoctdPoolAcct&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00536.md) | 701–701 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.4 Message Building Blocks / 30.4.2 StandingOrderQueryDefinition &lt;StgOrdrQryDef&gt; / 30.4.2.2 StandingOrderCriteria &lt;StgOrdrCrit&gt; / 30.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 30.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 30.4.2.2.2.3.1 StandingOrderIdentificationIndicator &lt;StgOrdrIdInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00537.md) | 702–702 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.4 Message Building Blocks / 30.4.2 StandingOrderQueryDefinition &lt;StgOrdrQryDef&gt; / 30.4.2.2 StandingOrderCriteria &lt;StgOrdrCrit&gt; / 30.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 30.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 30.4.2.2.2.3.4 ResponsiblePartyIndicator &lt;RspnsblPtyInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00538.md) | 703–703 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.4 Message Building Blocks / 30.4.2 StandingOrderQueryDefinition &lt;StgOrdrQryDef&gt; / 30.4.2.2 StandingOrderCriteria &lt;StgOrdrCrit&gt; / 30.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 30.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 30.4.2.2.2.3.9 FrequencyIndicator &lt;FrqcyInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00539.md) | 704–704 |
| [30 camt.069.001.05 GetStandingOrderV05 / 30.4 Message Building Blocks / 30.4.2 StandingOrderQueryDefinition &lt;StgOrdrQryDef&gt; / 30.4.2.2 StandingOrderCriteria &lt;StgOrdrCrit&gt; / 30.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 30.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 30.4.2.2.2.3.15 LinkSetOrderSequenceIndicator &lt;LkSetOrdrSeqInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00540.md) | 705–706 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [ACH](../../../../../shared/reference/participants/participant-src-000014-ach.md) | participant | src-000014 |
| [Automated Clearing House (ACH)](../../../../../shared/reference/participants/participant-src-000014-automated-clearing-house-ach.md) | participant | src-000014 |
| [Cash Provider](../../../../../shared/reference/participants/participant-src-000014-cash-provider.md) | participant | src-000014 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000014-central-securities-depositories-csd.md) | participant | src-000014 |
| [Corporate](../../../../../shared/reference/participants/participant-src-000014-corporate.md) | participant | src-000014 |
| [CSD](../../../../../shared/reference/participants/participant-src-000014-csd.md) | participant | src-000014 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000014-market-infrastructure.md) | participant | src-000014 |
| [Real Time Gross Settlement System (RTGS)](../../../../../shared/reference/participants/participant-src-000014-real-time-gross-settlement-system-rtgs.md) | participant | src-000014 |
| [RTGS](../../../../../shared/reference/participants/participant-src-000014-rtgs.md) | participant | src-000014 |
| [Settlement Agent](../../../../../shared/reference/participants/participant-src-000014-settlement-agent.md) | participant | src-000014 |
| [System Member](../../../../../shared/reference/participants/participant-src-000014-system-member.md) | participant | src-000014 |
| [System / Transaction Administrator](../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | participant | src-000014 |
| [Transaction Administrator/System](../../../../../shared/reference/participants/participant-src-000014-transaction-administrator-system.md) | participant | src-000014 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)

<!-- CASH-FLOWS -->
## Operational Cash Management flows

- [Get/Return Standing Order Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p341-get-return-standing-order-scenario.md)
- [Get/Return Standing Order Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p346-get-return-standing-order-receipt.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
