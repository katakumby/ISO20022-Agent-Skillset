---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.040.001.01"
message_family: "semt.040"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.040.001.01"
source_ids: ["src-000233", "src-000375"]
source_locations: [{"source_id": "src-000233", "heading": "80 semt.040.001.01 SecuritiesAccountPositionResponseV01", "file_pages": [2748, 2760]}, {"source_id": "src-000375", "heading": "5 semt.040.001.01 SecuritiesAccountPositionResponseV01", "file_pages": [166, 178]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2026"]
---

# semt.040.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 80 semt.040.001.01 SecuritiesAccountPositionResponseV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2748–2760; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 80 semt.040.001.01 SecuritiesAccountPositionResponseV01, Functionality, file p2748.**

SCOPE
The SecuritiesAccountPositionResponse message is sent by a market infrastructure to an instructing
party to report the securities positions for the given date period as requested in the query, for all
securities across all accounts satisfying the query criteria.
USAGE
The message SecuritiesAccountPositionResponse will provide CSDs and T2S participants with a report
corresponding to the SecuritiesAccountPositionQuery returning balances held in the list of specified
securities accounts within the specified period satisfying the defined selection criteria. The Securities
Account Position Response will provide the following business attributes:
- CSD
- Account owner
- Securities Account Number
- Securities Identifier (e.g. ISIN)
- Date
- The total position
- The blocked position
- The free position
Unless otherwise specified by the sender in the Securities Balance Query, T2S will only return non-zero
securities positions in the accounts.
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate)
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy)
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate).
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities 2748 August 2026

**src-000233, 80 semt.040.001.01 SecuritiesAccountPositionResponseV01, Functionality, file p2749.**

Outline
The SecuritiesAccountPositionResponseV01 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. ReportGeneralDetails
Provides general information on the report.
C. AccountOwner
Party that legally owns the account.
D. AccountServicer
Central securities depository where the securities accounts are held.
E. Balances
Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
F. PartyBaseCurrencyTotalAmounts
Total valuation amounts provided in the base currency of the party.
G. OtherBusinessParties
Other business parties relevant to the transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities 2749 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [80 semt.040.001.01 SecuritiesAccountPositionResponseV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02020.md) | 2748–2749 |
| [80 semt.040.001.01 SecuritiesAccountPositionResponseV01 / 80.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02021.md) | 2750–2752 |
| [80 semt.040.001.01 SecuritiesAccountPositionResponseV01 / 80.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02022.md) | 2753–2753 |
| [80 semt.040.001.01 SecuritiesAccountPositionResponseV01 / 80.4 Message Building Blocks / 80.4.1 Pagination &lt;Pgntn&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02023.md) | 2754–2754 |
| [80 semt.040.001.01 SecuritiesAccountPositionResponseV01 / 80.4 Message Building Blocks / 80.4.4 AccountServicer &lt;AcctSvcr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02024.md) | 2755–2757 |
| [80 semt.040.001.01 SecuritiesAccountPositionResponseV01 / 80.4 Message Building Blocks / 80.4.6 PartyBaseCurrencyTotalAmounts &lt;PtyBaseCcyTtlAmts&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02025.md) | 2758–2758 |
| [80 semt.040.001.01 SecuritiesAccountPositionResponseV01 / 80.4 Message Building Blocks / 80.4.6 PartyBaseCurrencyTotalAmounts &lt;PtyBaseCcyTtlAmts&gt; / 80.4.6.3 TotalBookValueOfStatement &lt;TtlBookValOfStmt&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-02026.md) | 2759–2760 |

## src-000375 — 5 semt.040.001.01 SecuritiesAccountPositionResponseV01

[src-000375](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`; file pp166–178; publication march-2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000375, 5 semt.040.001.01 SecuritiesAccountPositionResponseV01, Functionality, file p166.**

SCOPE
The SecuritiesAccountPositionResponse message is sent by a market infrastructure to an instructing
party to report the securities positions for the given date period as requested in the query, for all
securities across all accounts satisfying the query criteria.
USAGE
The message SecuritiesAccountPositionResponse will provide CSDs and T2S participants with a report
corresponding to the SecuritiesAccountPositionQuery returning balances held in the list of specified
securities accounts within the specified period satisfying the defined selection criteria. The Securities
Account Position Response will provide the following business attributes:
- CSD
- Account owner
- Securities Account Number
- Securities Identifier (e.g. ISIN)
- Date
- The total position
- The blocked position
- The free position
Unless otherwise specified by the sender in the Securities Balance Query, T2S will only return non-zero
securities positions in the accounts.
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate)
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy)
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate).
Approved by the Securities SEG 19 February 2026. semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities - Securities and Penalty Reporting 166 March 2026

**src-000375, 5 semt.040.001.01 SecuritiesAccountPositionResponseV01, Functionality, file p167.**

Outline
The SecuritiesAccountPositionResponseV01 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. ReportGeneralDetails
Provides general information on the report.
C. AccountOwner
Party that legally owns the account.
D. AccountServicer
Central securities depository where the securities accounts are held.
E. Balances
Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
F. PartyBaseCurrencyTotalAmounts
Total valuation amounts provided in the base currency of the party.
G. OtherBusinessParties
Other business parties relevant to the transaction.
Approved by the Securities SEG 19 February 2026. semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities - Securities and Penalty Reporting 167 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [5 semt.040.001.01 SecuritiesAccountPositionResponseV01](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00122.md) | 166–167 |
| [5 semt.040.001.01 SecuritiesAccountPositionResponseV01 / 5.2 Structure](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00123.md) | 168–170 |
| [5 semt.040.001.01 SecuritiesAccountPositionResponseV01 / 5.4 Message Building Blocks](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00124.md) | 171–171 |
| [5 semt.040.001.01 SecuritiesAccountPositionResponseV01 / 5.4 Message Building Blocks / 5.4.1 Pagination &lt;Pgntn&gt;](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00125.md) | 172–172 |
| [5 semt.040.001.01 SecuritiesAccountPositionResponseV01 / 5.4 Message Building Blocks / 5.4.4 AccountServicer &lt;AcctSvcr&gt;](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00126.md) | 173–175 |
| [5 semt.040.001.01 SecuritiesAccountPositionResponseV01 / 5.4 Message Building Blocks / 5.4.6 PartyBaseCurrencyTotalAmounts &lt;PtyBaseCcyTtlAmts&gt;](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00127.md) | 176–176 |
| [5 semt.040.001.01 SecuritiesAccountPositionResponseV01 / 5.4 Message Building Blocks / 5.4.6 PartyBaseCurrencyTotalAmounts &lt;PtyBaseCcyTtlAmts&gt; / 5.4.6.3 TotalBookValueOfStatement &lt;TtlBookValOfStmt&gt;](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00128.md) | 177–178 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Central Counterparty](../../../../../shared/reference/participants/participant-src-000374-central-counterparty.md) | participant | src-000374 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000374-central-securities-depositories-csd.md) | participant | src-000374 |
| [Direct Connected Participant (DCP)](../../../../../shared/reference/participants/participant-src-000374-direct-connected-participant-dcp.md) | participant | src-000374 |
| [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md) | participant | src-000374 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000374-instructing-party.md) | participant | src-000374 |
| [Servicing Party](../../../../../shared/reference/participants/participant-src-000374-servicing-party.md) | participant | src-000374 |
| [Settlement Infrastructure](../../../../../shared/reference/participants/participant-src-000374-settlement-infrastructure.md) | participant | src-000374 |
| [T2S Operator](../../../../../shared/reference/participants/participant-src-000374-t2s-operator.md) | participant | src-000374 |
| [Query Report Process](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p224-query-report-process.md) | business-flow | src-000374 |
| [Securities Account Position Query and Securities Account Position Response](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md) | business-flow | src-000374 |
| [Securities Settlement Transaction Query and Securities Settlement Transaction Query Response](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p239-securities-settlement-transaction-query-and-securities-settlement-tran.md) | business-flow | src-000374 |
| [Securities Transaction Penalties Report](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p243-securities-transaction-penalties-report.md) | business-flow | src-000374 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
