---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.003.001.08"
message_family: "camt.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.003.001.08"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "2 camt.003.001.08 GetAccountV08", "file_pages": [13, 47]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.003.001.08 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 2 camt.003.001.08 GetAccountV08

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp13–47; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 2 camt.003.001.08 GetAccountV08, Functionality, file p13.**

Scope
The GetAccount message is sent by a member to the transaction administrator.
It is used to request information on the details of one or more accounts held at the transaction
administrator, including information on the balances.
Usage
At any time during the operating hours of the system, the member can query the transaction
administrator to get information about the account(s) that the transaction administrator maintains for the
member.
For example, this may be necessary in order to perform the appropriate liquidity management and the
funds transfers between accounts.
The member can request information about accounts through a series of criteria, corresponding to the
known information stored at the transaction administrator.
The query can concern one or more specific accounts, accounts of a particular identification, or a
particular type. The purpose of the query may be to obtain one or more types of balance.
The member can request information based on the following elements:
- account identification
- account type (this element can be used to refine the query when the account identification represents,
for example, a group of accounts)
- balance type (if not present, all balances are requested)
- type of counterparty: bilateral or multilateral (note that, by default, a balance is multilateral unless a
particular counterparty is specified)
- identification of the counterparty when a bilateral balance is requested
- balance value date (if not present in the GetAccount message, the ReturnAccount message will
contain the latest available balance)
This message will be answered by a ReturnAccount message.
Additional information on the generic design of the Get/Return messages can be found in the section
How to Use the Cash Management Messages.
Outline
The GetAccountV08 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 13 February 2025

**src-000015, 2 camt.003.001.08 GetAccountV08, Functionality, file p14.**

Common business identification for the message.
B. AccountQueryDefinition
Defines the account query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 14 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 camt.003.001.08 GetAccountV08](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00004.md) | 13–14 |
| [2 camt.003.001.08 GetAccountV08 / 2.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00005.md) | 15–16 |
| [2 camt.003.001.08 GetAccountV08 / 2.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00006.md); [Constraints continuation C7–C10 (file p18)](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00007.md#file-page-18) | 17–17 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00007.md) | 18–20 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.1 QueryType &lt;QryTp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00008.md) | 21–23 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.1 QueryName &lt;QryNm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00009.md) | 24–26 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.1 NewQueryName &lt;NewQryNm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00010.md) | 27–28 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.2.1 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00011.md) | 29–29 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.2.1 AccountIdentification &lt;AcctId&gt; / 2.4.2.2.2.2.1.2 ContainText &lt;CTTxt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00012.md) | 30–31 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.2.4 Balance &lt;Bal&gt; / 2.4.2.2.2.2.4.1 Type &lt;Tp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00013.md) | 32–32 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.2.4 Balance &lt;Bal&gt; / 2.4.2.2.2.2.4.3 CounterpartyIdentification &lt;CtrPtyId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00014.md) | 33–33 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.2.4 Balance &lt;Bal&gt; / 2.4.2.2.2.2.4.4 ValueDate &lt;ValDt&gt; / 2.4.2.2.2.2.4.4.1 DateTime &lt;DtTm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00015.md) | 34–34 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.2.4 Balance &lt;Bal&gt; / 2.4.2.2.2.2.4.4 ValueDate &lt;ValDt&gt; / 2.4.2.2.2.2.4.4.1 DateTime &lt;DtTm&gt; / 2.4.2.2.2.2.4.4.1.3 FromToDateTime &lt;FrToDtTm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00016.md) | 35–35 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.2.4 Balance &lt;Bal&gt; / 2.4.2.2.2.2.4.4 ValueDate &lt;ValDt&gt; / 2.4.2.2.2.2.4.4.2 Date &lt;Dt&gt; / 2.4.2.2.2.2.4.4.2.3 FromToDate &lt;FrToDt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00017.md) | 36–36 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.2.4 Balance &lt;Bal&gt; / 2.4.2.2.2.2.4.5 ProcessingDate &lt;PrcgDt&gt; / 2.4.2.2.2.2.4.5.1 DateTime &lt;DtTm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00018.md) | 37–37 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.2.4 Balance &lt;Bal&gt; / 2.4.2.2.2.2.4.5 ProcessingDate &lt;PrcgDt&gt; / 2.4.2.2.2.2.4.5.1 DateTime &lt;DtTm&gt; / 2.4.2.2.2.2.4.5.1.3 FromToDateTime &lt;FrToDtTm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00019.md) | 38–38 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.2.4 Balance &lt;Bal&gt; / 2.4.2.2.2.2.4.5 ProcessingDate &lt;PrcgDt&gt; / 2.4.2.2.2.2.4.5.2 Date &lt;Dt&gt; / 2.4.2.2.2.2.4.5.2.3 FromToDate &lt;FrToDt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00020.md) | 39–39 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2.2.2.6 AccountServicer &lt;AcctSvcr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00021.md) | 40–40 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00022.md) | 41–41 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 2.4.2.2.2.3.1 NameIndicator &lt;NmInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00023.md) | 42–42 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 2.4.2.2.2.3.3 TypeIndicator &lt;TpInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00024.md) | 43–43 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 2.4.2.2.2.3.5 MultilateralBalanceReturnCriteria &lt;MulBalRtrCrit&gt; / 2.4.2.2.2.3.5.3 ValueDateIndicator &lt;ValDtInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00025.md) | 44–44 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 2.4.2.2.2.3.7 BilateralBalanceReturnCriteria &lt;BilBalRtrCrit&gt; / 2.4.2.2.2.3.7.1 TypeIndicator &lt;TpInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00026.md) | 45–45 |
| [2 camt.003.001.08 GetAccountV08 / 2.4 Message Building Blocks / 2.4.2 AccountQueryDefinition &lt;AcctQryDef&gt; / 2.4.2.2 AccountCriteria &lt;AcctCrit&gt; / 2.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 2.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 2.4.2.2.2.3.7 BilateralBalanceReturnCriteria &lt;BilBalRtrCrit&gt; / 2.4.2.2.2.3.7.5 NumberOfPaymentsIndicator &lt;NbOfPmtsInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00027.md) | 46–47 |

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

- [Get/Return Account](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p261-get-return-account.md)
- [Get/Return Account Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p266-get-return-account-receipt.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
