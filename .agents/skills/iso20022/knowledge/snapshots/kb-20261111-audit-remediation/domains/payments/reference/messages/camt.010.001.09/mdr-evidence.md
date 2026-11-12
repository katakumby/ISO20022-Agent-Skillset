---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.010.001.09"
message_family: "camt.010"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.010.001.09"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "9 camt.010.001.09 ReturnLimitV09", "file_pages": [391, 421]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.010.001.09 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 9 camt.010.001.09 ReturnLimitV09

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp391–421; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 9 camt.010.001.09 ReturnLimitV09, Functionality, file p391.**

Scope
The ReturnLimit message is sent by the transaction administrator to a member of the system.
It is used to provide information on the details of one or more limits set by the member (or on behalf of
the member) and managed by the transaction administrator.
The ReturnLimit message can be sent as a response to a related GetLimit message (pull mode) or
initiated by the transaction administrator (push mode). The push of information can take place either at
prearranged times or as a warning or alarm when a problem has occurred.
Usage
At any time during the operating hours of the system, the member can query the transaction
administrator to get information about the limit(s) that the transaction administrator manages for the
member.
The transaction administrator may also send a ReturnLimit message with pre-defined information at
times previously agreed with the member or to warn the member about a particular problem that may
have arisen and which needs attention.
The message from the transaction administrator can contain information on the following elements:
- type of risk and/or liquidity limit
- value of the limit(s) (default and/or current limit(s) for risk and/or liquidity management)
- identification of the system
- status of the limit(s) (default and/or current limit(s) for risk and/or liquidity management)
- point in time when the limit becomes effective
- identification of the counterparty
Additional information on the generic design of the Get/Return messages can be found in the section
How to Use the Cash Management Messages.
Outline
The ReturnLimitV09 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Reports on limits.
C. SupplementaryData
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 391 February 2025

**src-000015, 9 camt.010.001.09 ReturnLimitV09, Functionality, file p392.**

Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 392 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [9 camt.010.001.09 ReturnLimitV09](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00266.md) | 391–392 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00267.md) | 393–394 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00268.md) | 395–395 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00269.md) | 396–397 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00270.md) | 398–399 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.1 CurrentLimit &lt;CurLmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00271.md) | 400–400 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.1 CurrentLimit &lt;CurLmt&gt; / 9.4.2.1.1.1 LimitIdentification &lt;LmtId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00272.md) | 401–401 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.1 CurrentLimit &lt;CurLmt&gt; / 9.4.2.1.1.1 LimitIdentification &lt;LmtId&gt; / 9.4.2.1.1.1.1 SystemIdentification &lt;SysId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00273.md) | 402–402 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.1 CurrentLimit &lt;CurLmt&gt; / 9.4.2.1.1.1 LimitIdentification &lt;LmtId&gt; / 9.4.2.1.1.1.3 Type &lt;Tp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00274.md) | 403–404 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.1 CurrentLimit &lt;CurLmt&gt; / 9.4.2.1.1.1 LimitIdentification &lt;LmtId&gt; / 9.4.2.1.1.1.3 Type &lt;Tp&gt; / 9.4.2.1.1.1.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00275.md) | 405–405 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.1 CurrentLimit &lt;CurLmt&gt; / 9.4.2.1.1.1 LimitIdentification &lt;LmtId&gt; / 9.4.2.1.1.1.5 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00276.md) | 406–406 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.1 CurrentLimit &lt;CurLmt&gt; / 9.4.2.1.1.2 LimitOrError &lt;LmtOrErr&gt; / 9.4.2.1.1.2.1 Limit &lt;Lmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00277.md) | 407–407 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.1 CurrentLimit &lt;CurLmt&gt; / 9.4.2.1.1.2 LimitOrError &lt;LmtOrErr&gt; / 9.4.2.1.1.2.1 Limit &lt;Lmt&gt; / 9.4.2.1.1.2.1.2 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00278.md) | 408–408 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.1 CurrentLimit &lt;CurLmt&gt; / 9.4.2.1.1.2 LimitOrError &lt;LmtOrErr&gt; / 9.4.2.1.1.2.1 Limit &lt;Lmt&gt; / 9.4.2.1.1.2.1.6 UsedAmountCreditDebitIndicator &lt;UsdAmtCdtDbtInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00279.md) | 409–409 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.1 CurrentLimit &lt;CurLmt&gt; / 9.4.2.1.1.2 LimitOrError &lt;LmtOrErr&gt; / 9.4.2.1.1.2.2 BusinessError &lt;BizErr&gt; / 9.4.2.1.1.2.2.1 Error &lt;Err&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00280.md) | 410–410 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.2 DefaultLimit &lt;DfltLmt&gt; / 9.4.2.1.2.1 LimitIdentification &lt;LmtId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00281.md) | 411–411 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.2 DefaultLimit &lt;DfltLmt&gt; / 9.4.2.1.2.1 LimitIdentification &lt;LmtId&gt; / 9.4.2.1.2.1.1 SystemIdentification &lt;SysId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00282.md) | 412–412 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.2 DefaultLimit &lt;DfltLmt&gt; / 9.4.2.1.2.1 LimitIdentification &lt;LmtId&gt; / 9.4.2.1.2.1.3 Type &lt;Tp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00283.md) | 413–414 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.2 DefaultLimit &lt;DfltLmt&gt; / 9.4.2.1.2.1 LimitIdentification &lt;LmtId&gt; / 9.4.2.1.2.1.3 Type &lt;Tp&gt; / 9.4.2.1.2.1.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00284.md) | 415–415 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.2 DefaultLimit &lt;DfltLmt&gt; / 9.4.2.1.2.1 LimitIdentification &lt;LmtId&gt; / 9.4.2.1.2.1.5 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00285.md) | 416–416 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.2 DefaultLimit &lt;DfltLmt&gt; / 9.4.2.1.2.2 LimitOrError &lt;LmtOrErr&gt; / 9.4.2.1.2.2.1 Limit &lt;Lmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00286.md) | 417–417 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.2 DefaultLimit &lt;DfltLmt&gt; / 9.4.2.1.2.2 LimitOrError &lt;LmtOrErr&gt; / 9.4.2.1.2.2.1 Limit &lt;Lmt&gt; / 9.4.2.1.2.2.1.2 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00287.md) | 418–418 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.2 DefaultLimit &lt;DfltLmt&gt; / 9.4.2.1.2.2 LimitOrError &lt;LmtOrErr&gt; / 9.4.2.1.2.2.1 Limit &lt;Lmt&gt; / 9.4.2.1.2.2.1.6 UsedAmountCreditDebitIndicator &lt;UsdAmtCdtDbtInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00288.md) | 419–419 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.1 BusinessReport &lt;BizRpt&gt; / 9.4.2.1.2 DefaultLimit &lt;DfltLmt&gt; / 9.4.2.1.2.2 LimitOrError &lt;LmtOrErr&gt; / 9.4.2.1.2.2.2 BusinessError &lt;BizErr&gt; / 9.4.2.1.2.2.2.1 Error &lt;Err&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00289.md) | 420–420 |
| [9 camt.010.001.09 ReturnLimitV09 / 9.4 Message Building Blocks / 9.4.2 ReportOrError &lt;RptOrErr&gt; / 9.4.2.2 OperationalError &lt;OprlErr&gt; / 9.4.2.2.1 Error &lt;Err&gt; / 9.4.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00290.md) | 421–421 |

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

- [Get/Return Limit](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p207-get-return-limit.md)
- [Get/Return Limit Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p212-get-return-limit-receipt.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
