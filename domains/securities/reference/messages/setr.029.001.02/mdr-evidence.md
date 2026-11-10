---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "setr.029.001.02"
message_family: "setr.029"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.029.001.02"
source_ids: ["src-000181"]
source_locations: [{"source_id": "src-000181", "heading": "4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02", "file_pages": [140, 147]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# setr.029.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000181 — 4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02

[src-000181](../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf); file pp140–147; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000181, 4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02, Functionality, file p140.**

Scope
Sent by an executing party to an instructing party directly or through Central Matching Utility (CMU) to
cancel the referenced SecuritiesTradeConfirmation message that was previously sent.
The instructing party is typically the investment manager or an intermediary system/vendor
communicating on behalf of the investment manager or of other categories of investors.
The executing party is typically the broker/dealer or an intermediary system/vendor communicating on
behalf of the broker/dealer.
It may also be used to cancel the trade confirmation previously sent from an executing party or an
instructing party to a custodian or an affirming party directly or through CMU.
The ISO 20022 Business Application Header must be used
Usage
Initiator: Both in local and central matching, the Initiator may be either the Executing Party or Instructing
Party.
Respondent: Instructing party, a custodian or an affirming party optionally responds with
SecuritiesTradeConfirmationResponse (accept or reject) message.
Outline
The SecuritiesTradeConfirmationCancellationV02 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. Identification
Information that unambiguously identifies an SecuritiesTradeConfirmationCancellation message as
known by the account owner (or the instructing party acting on its behalf).
B. References
Link to another transaction that must be processed after, before or at the same time.
C. OtherBusinessParties
Chain of parties involved in the settlement of a transaction, including receipts and deliveries, book
transfers, treasury deals, or other activities, resulting in the movement of a security or amount of
money from one account to another.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 13 February 2025 setr.029.001.02
SecuritiesTradeConfirmationCancellationV02
Post Trade Matching - Maintenance 2024 - 2025 140 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00107.md) | 140–140 |
| [4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02 / 4.2 Structure](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00108.md) | 141–141 |
| [4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02 / 4.4 Message Building Blocks](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00109.md) | 142–142 |
| [4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02 / 4.4 Message Building Blocks / 4.4.3 OtherBusinessParties &lt;OthrBizPties&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00110.md) | 143–143 |
| [4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02 / 4.4 Message Building Blocks / 4.4.3 OtherBusinessParties &lt;OthrBizPties&gt; / 4.4.3.2 StockExchange &lt;StockXchg&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00111.md) | 144–144 |
| [4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02 / 4.4 Message Building Blocks / 4.4.3 OtherBusinessParties &lt;OthrBizPties&gt; / 4.4.3.3 TradeRegulator &lt;TradRgltr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00112.md) | 145–145 |
| [4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02 / 4.4 Message Building Blocks / 4.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00113.md) | 146–147 |

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
