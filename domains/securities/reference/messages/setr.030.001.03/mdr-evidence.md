---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "setr.030.001.03"
message_family: "setr.030"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.030.001.03"
source_ids: ["src-000181"]
source_locations: [{"source_id": "src-000181", "heading": "5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03", "file_pages": [148, 161]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# setr.030.001.03 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000181 — 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03

[src-000181](../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf); file pp148–161; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000181, 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03, Functionality, file p148.**

Scope
Sent by an instructing party, a custodian or an affirming party to an executing party (local matching) or
to Central Matching Utility (CMU) to affirm (accept) or disaffirm (reject) (central matching) the
SecuritiesTradeConfirmation message. If accepting the SecuritiesTradeConfirmation message, then the
trade is ready for settlement processing. If rejecting the SecuritiesTradeConfirmation message, then the
trade is not ready for settlement.
The executing party is typically the broker/dealer or an intermediary system/vendor communicating on
behalf of the broker/dealer.
The instructing party is typically the investment manager or an intermediary system/vendor
communicating on behalf of the investment manager or of other categories of investors.
The custodian or an affirming party is typically the custodian, trustee, financial institution, intermediary
system/vendor communicating on behalf of them, or their agent.
The ISO 20022 Business Application Header must be used
Usage
Initiator: Both in local and central matching, the Initiator may be the Instructing Party, Custodian or
Affirming party.
Respondent: Executing party does not need to respond if an affirmation. Executing party may respond
with modification or cancellation of the rejected SecuritiesTradeConfirmation message.
Outline
The SecuritiesTradeConfirmationResponseV03 MessageDefinition is composed of 6
MessageBuildingBlocks:
A. Identification
Information that unambiguously identifies an SecuritiesTradeConfirmationResponse message as
known by the account owner (or the instructing party acting on its behalf).
B. References
Link to another transaction that must be processed after, before or at the same time.
C. Status
Provides details on the processing status of the trade.
D. ClearingDetails
Provides clearing member information.
E. ConfirmationParties
Parties involved in the confirmation of the details of a trade.
Approved by the Securities SEG on 13 February 2025 setr.030.001.03
SecuritiesTradeConfirmationResponseV03
Post Trade Matching - Maintenance 2024 - 2025 148 February 2025

**src-000181, 5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03, Functionality, file p149.**

F. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00114.md) | 148–148 |
| [5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03 / 5.2 Structure](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00115.md) | 149–149 |
| [5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03 / 5.4 Message Building Blocks](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00116.md) | 150–150 |
| [5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03 / 5.4 Message Building Blocks / 5.4.1 Identification &lt;Id&gt; / 5.4.1.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00117.md) | 151–151 |
| [5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03 / 5.4 Message Building Blocks / 5.4.3 Status &lt;Sts&gt; / 5.4.3.2 UnaffirmedReason &lt;UaffrmdRsn&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00118.md) | 152–152 |
| [5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03 / 5.4 Message Building Blocks / 5.4.4 ClearingDetails &lt;ClrDtls&gt; / 5.4.4.2 ClearingSegment &lt;ClrSgmt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00119.md) | 153–153 |
| [5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03 / 5.4 Message Building Blocks / 5.4.5 ConfirmationParties &lt;ConfPties&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00120.md) | 154–154 |
| [5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03 / 5.4 Message Building Blocks / 5.4.5 ConfirmationParties &lt;ConfPties&gt; / 5.4.5.2 Buyer &lt;Buyr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00121.md) | 155–155 |
| [5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03 / 5.4 Message Building Blocks / 5.4.5 ConfirmationParties &lt;ConfPties&gt; / 5.4.5.3 Borrower &lt;Brrwr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00122.md) | 156–156 |
| [5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03 / 5.4 Message Building Blocks / 5.4.5 ConfirmationParties &lt;ConfPties&gt; / 5.4.5.4 Seller &lt;Sellr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00123.md) | 157–157 |
| [5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03 / 5.4 Message Building Blocks / 5.4.5 ConfirmationParties &lt;ConfPties&gt; / 5.4.5.5 Lender &lt;Lndr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00124.md) | 158–158 |
| [5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03 / 5.4 Message Building Blocks / 5.4.5 ConfirmationParties &lt;ConfPties&gt; / 5.4.5.6 TradeBeneficiaryParty &lt;TradBnfcryPty&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00125.md) | 159–159 |
| [5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03 / 5.4 Message Building Blocks / 5.4.6 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00126.md) | 160–161 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Affirming Party](../../../../../shared/reference/participants/participant-src-000180-affirming-party.md) | participant | src-000180 |
| [Broker/Executing Broker](../../../../../shared/reference/participants/participant-src-000180-broker-executing-broker.md) | participant | src-000180 |
| [Broker/Underwriter](../../../../../shared/reference/participants/participant-src-000180-broker-underwriter.md) | participant | src-000180 |
| [Broker](../../../../../shared/reference/participants/participant-src-000180-broker.md) | participant | src-000180 |
| [Cash Settlement Agent](../../../../../shared/reference/participants/participant-src-000180-cash-settlement-agent.md) | participant | src-000180 |
| [Central Counterparty](../../../../../shared/reference/participants/participant-src-000180-central-counterparty.md) | participant | src-000180 |
| [Central Matching Utility (CMU)](../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-cmu.md) | participant | src-000180 |
| [Central Matching Utility (JASDEC)](../../../../../shared/reference/participants/participant-src-000180-central-matching-utility-jasdec.md) | participant | src-000180 |
| [Central Securities Depositories](../../../../../shared/reference/participants/participant-src-000180-central-securities-depositories.md) | participant | src-000180 |
| [Confirmation Party](../../../../../shared/reference/participants/participant-src-000180-confirmation-party.md) | participant | src-000180 |
| [Custodian](../../../../../shared/reference/participants/participant-src-000180-custodian.md) | participant | src-000180 |
| [Exchange](../../../../../shared/reference/participants/participant-src-000180-exchange.md) | participant | src-000180 |
| [Executing/Servicing Party](../../../../../shared/reference/participants/participant-src-000180-executing-servicing-party.md) | participant | src-000180 |
| [Institutional Investor/Issuer Agent](../../../../../shared/reference/participants/participant-src-000180-institutional-investor-issuer-agent.md) | participant | src-000180 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000180-instructing-party.md) | participant | src-000180 |
| [Investment Manager](../../../../../shared/reference/participants/participant-src-000180-investment-manager.md) | participant | src-000180 |
| [Order Giver](../../../../../shared/reference/participants/participant-src-000180-order-giver.md) | participant | src-000180 |
| [Prime Broker](../../../../../shared/reference/participants/participant-src-000180-prime-broker.md) | participant | src-000180 |
| [Transfer Agent](../../../../../shared/reference/participants/participant-src-000180-transfer-agent.md) | participant | src-000180 |
| [Trust Bank](../../../../../shared/reference/participants/participant-src-000180-trust-bank.md) | participant | src-000180 |
| [Underwriter](../../../../../shared/reference/participants/participant-src-000180-underwriter.md) | participant | src-000180 |
| [Through Type](../../message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p146-through-type.md) | business-flow | src-000180 |
| [Own Account Trade Type](../../message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p153-own-account-trade-type.md) | business-flow | src-000180 |
| [Duplex Type](../../message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p159-duplex-type.md) | business-flow | src-000180 |
| [End of Process Report for Listed Derivatives](../../message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p165-end-of-process-report-for-listed-derivatives.md) | business-flow | src-000180 |
| [Tripartite Central Matching Without Confirmation Distribution Service](../../message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service.md) | business-flow | src-000180 |
| [Tripartite Central Matching With Confirmation Distribution Service](../../message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service.md) | business-flow | src-000180 |
| [Bilateral Central Matching](../../message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p185-bilateral-central-matching.md) | business-flow | src-000180 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
