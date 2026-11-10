---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.025.001.01"
message_family: "semt.025"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.025.001.01"
source_ids: ["src-000233", "src-000375"]
source_locations: [{"source_id": "src-000233", "heading": "70 semt.025.001.01 SecuritiesAccountPositionQueryV01", "file_pages": [2401, 2408]}, {"source_id": "src-000375", "heading": "2 semt.025.001.01 SecuritiesAccountPositionQueryV01", "file_pages": [5, 12]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "march-2026"]
---

# semt.025.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 70 semt.025.001.01 SecuritiesAccountPositionQueryV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); file pp2401–2408; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 70 semt.025.001.01 SecuritiesAccountPositionQueryV01, Functionality, file p2401.**

The SecuritiesAccountPositionQuery message is sent by an account owner to an account servicer or
servicing party to request an account view on the position at a particular point in time period, or during a
particular time period, where all positions are summarised in the account structure that is compatible
with the query.
Usage:
The message may also be used to:
-re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
-re-send to a third party a copy of a message for information (the sub-function of the message is
CopyDuplicate).
Outline
The SecuritiesAccountPositionQueryV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. Statement
Defines the criteria used to report on the securities account position.
B. SearchCriteria
Provides the criteria in the form of business attributes to extract the securities account position
result set.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities 2401 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [70 semt.025.001.01 SecuritiesAccountPositionQueryV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01750.md) | 2401–2401 |
| [70 semt.025.001.01 SecuritiesAccountPositionQueryV01 / 70.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01751.md) | 2402–2402 |
| [70 semt.025.001.01 SecuritiesAccountPositionQueryV01 / 70.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01752.md) | 2403–2403 |
| [70 semt.025.001.01 SecuritiesAccountPositionQueryV01 / 70.4 Message Building Blocks / 70.4.2 SearchCriteria &lt;SchCrit&gt; / 70.4.2.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01753.md) | 2404–2404 |
| [70 semt.025.001.01 SecuritiesAccountPositionQueryV01 / 70.4 Message Building Blocks / 70.4.2 SearchCriteria &lt;SchCrit&gt; / 70.4.2.4 FinancialInstrument &lt;FinInstrm&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01754.md) | 2405–2405 |
| [70 semt.025.001.01 SecuritiesAccountPositionQueryV01 / 70.4 Message Building Blocks / 70.4.2 SearchCriteria &lt;SchCrit&gt; / 70.4.2.5 CountryOfIssue &lt;CtryOfIsse&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01755.md) | 2406–2406 |
| [70 semt.025.001.01 SecuritiesAccountPositionQueryV01 / 70.4 Message Building Blocks / 70.4.2 SearchCriteria &lt;SchCrit&gt; / 70.4.2.8 OtherBusinessParties &lt;OthrBizPties&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01756.md) | 2407–2407 |
| [70 semt.025.001.01 SecuritiesAccountPositionQueryV01 / 70.4 Message Building Blocks / 70.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-01757.md) | 2408–2408 |

## src-000375 — 2 semt.025.001.01 SecuritiesAccountPositionQueryV01

[src-000375](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`; file pp5–12; publication march-2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000375, 2 semt.025.001.01 SecuritiesAccountPositionQueryV01, Functionality, file p5.**

The SecuritiesAccountPositionQuery message is sent by an account owner to an account servicer or
servicing party to request an account view on the position at a particular point in time period, or during a
particular time period, where all positions are summarised in the account structure that is compatible
with the query.
Usage:
The message may also be used to:
-re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
-re-send to a third party a copy of a message for information (the sub-function of the message is
CopyDuplicate).
Outline
The SecuritiesAccountPositionQueryV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. Statement
Defines the criteria used to report on the securities account position.
B. SearchCriteria
Provides the criteria in the form of business attributes to extract the securities account position
result set.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG 19 February 2026. semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities - Securities and Penalty Reporting 5 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 semt.025.001.01 SecuritiesAccountPositionQueryV01](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00004.md) | 5–5 |
| [2 semt.025.001.01 SecuritiesAccountPositionQueryV01 / 2.2 Structure](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00005.md) | 6–6 |
| [2 semt.025.001.01 SecuritiesAccountPositionQueryV01 / 2.4 Message Building Blocks](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00006.md) | 7–7 |
| [2 semt.025.001.01 SecuritiesAccountPositionQueryV01 / 2.4 Message Building Blocks / 2.4.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00007.md) | 8–8 |
| [2 semt.025.001.01 SecuritiesAccountPositionQueryV01 / 2.4 Message Building Blocks / 2.4.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.4 FinancialInstrument &lt;FinInstrm&gt;](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00008.md) | 9–9 |
| [2 semt.025.001.01 SecuritiesAccountPositionQueryV01 / 2.4 Message Building Blocks / 2.4.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.5 CountryOfIssue &lt;CtryOfIsse&gt;](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00009.md) | 10–10 |
| [2 semt.025.001.01 SecuritiesAccountPositionQueryV01 / 2.4 Message Building Blocks / 2.4.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.8 OtherBusinessParties &lt;OthrBizPties&gt;](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00010.md) | 11–11 |
| [2 semt.025.001.01 SecuritiesAccountPositionQueryV01 / 2.4 Message Building Blocks / 2.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00011.md) | 12–12 |

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
