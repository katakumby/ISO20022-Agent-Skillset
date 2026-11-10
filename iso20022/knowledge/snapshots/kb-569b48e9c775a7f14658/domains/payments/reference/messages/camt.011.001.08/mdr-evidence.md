---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.011.001.08"
message_family: "camt.011"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.011.001.08"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "10 camt.011.001.08 ModifyLimitV08", "file_pages": [422, 449]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.011.001.08 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 10 camt.011.001.08 ModifyLimitV08

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp422–449; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 10 camt.011.001.08 ModifyLimitV08, Functionality, file p422.**

Scope
The ModifyLimit message is sent by a member to the transaction administrator.
It is used to request modifications in the details of one particular, several or all limits set by the member
and managed by the transaction administrator.
Each ModifyLimit message can alter only one type of limit (current or default).
Usage
At any time during the operating hours of the system, the member can request modifications in the
limits it has set. For example, the reason may be to unlock the payments queue regarding a particular
member, or following a risk management decision issued after an exceptional event has occurred.
The member will submit a message requesting modifications in one or more of the following criteria:
- type of limit (current/default)
- identification of the system
- identification of the counterparty
- value of the limit(s) (default and/or current limit(s))
- point in time when the limit becomes effective
Based on the criteria received within the ModifyLimit message, the transaction administrator will
execute or reject the requested modification. The transaction administrator may send a Receipt
message as a reply to the ModifyLimit request. To verify the outcome of the request, the member may
submit a GetLimit message with the appropriate search criteria.
Outline
The ModifyLimitV08 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. LimitDetails
Identifies one particular limit set by the member and managed by the transaction administrator.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.011.001.08 ModifyLimitV08
Cash Management - Maintenance 2024 - 2025 422 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [10 camt.011.001.08 ModifyLimitV08](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00291.md) | 422–422 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00292.md) | 423–423 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00293.md) | 424–424 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00294.md) | 425–426 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00295.md) | 427–428 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt; / 10.4.2.1.1 Current &lt;Cur&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00296.md) | 429–429 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt; / 10.4.2.1.1 Current &lt;Cur&gt; / 10.4.2.1.1.2 BilateralLimitCounterpartyIdentification &lt;BilLmtCtrPtyId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00297.md) | 430–431 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt; / 10.4.2.1.1 Current &lt;Cur&gt; / 10.4.2.1.1.3 Type &lt;Tp&gt; / 10.4.2.1.1.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00298.md) | 432–432 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt; / 10.4.2.1.1 Current &lt;Cur&gt; / 10.4.2.1.1.5 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00299.md) | 433–433 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt; / 10.4.2.1.2 Default &lt;Dflt&gt; / 10.4.2.1.2.1 SystemIdentification &lt;SysId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00300.md) | 434–434 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt; / 10.4.2.1.2 Default &lt;Dflt&gt; / 10.4.2.1.2.3 Type &lt;Tp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00301.md) | 435–436 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt; / 10.4.2.1.2 Default &lt;Dflt&gt; / 10.4.2.1.2.3 Type &lt;Tp&gt; / 10.4.2.1.2.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00302.md) | 437–437 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt; / 10.4.2.1.2 Default &lt;Dflt&gt; / 10.4.2.1.2.5 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00303.md) | 438–438 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt; / 10.4.2.1.3 AllCurrent &lt;AllCur&gt; / 10.4.2.1.3.1 SystemIdentification &lt;SysId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00304.md) | 439–440 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt; / 10.4.2.1.3 AllCurrent &lt;AllCur&gt; / 10.4.2.1.3.2 Type &lt;Tp&gt; / 10.4.2.1.3.2.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00305.md) | 441–441 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt; / 10.4.2.1.3 AllCurrent &lt;AllCur&gt; / 10.4.2.1.3.4 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00306.md) | 442–442 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt; / 10.4.2.1.4 AllDefault &lt;AllDflt&gt; / 10.4.2.1.4.1 SystemIdentification &lt;SysId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00307.md) | 443–444 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt; / 10.4.2.1.4 AllDefault &lt;AllDflt&gt; / 10.4.2.1.4.2 Type &lt;Tp&gt; / 10.4.2.1.4.2.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00308.md) | 445–445 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.1 LimitIdentification &lt;LmtId&gt; / 10.4.2.1.4 AllDefault &lt;AllDflt&gt; / 10.4.2.1.4.4 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00309.md) | 446–446 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.2 NewLimitValueSet &lt;NewLmtValSet&gt; / 10.4.2.2.1 StartDateTime &lt;StartDtTm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00310.md) | 447–447 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.2 LimitDetails &lt;LmtDtls&gt; / 10.4.2.3 OldLimitValueSet &lt;OdLmtValSet&gt; / 10.4.2.3.2 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00311.md) | 448–448 |
| [10 camt.011.001.08 ModifyLimitV08 / 10.4 Message Building Blocks / 10.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00312.md) | 449–449 |

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

- [Modify Limit Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p225-modify-limit-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
