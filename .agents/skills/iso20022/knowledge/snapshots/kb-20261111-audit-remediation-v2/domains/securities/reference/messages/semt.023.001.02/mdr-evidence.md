---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.023.001.02"
message_family: "semt.023"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.023.001.02"
source_ids: ["src-000181"]
source_locations: [{"source_id": "src-000181", "heading": "2 semt.023.001.02 SecuritiesEndOfProcessReportV02", "file_pages": [6, 27]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# semt.023.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000181 — 2 semt.023.001.02 SecuritiesEndOfProcessReportV02

[src-000181](../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md); file pp6–27; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000181, 2 semt.023.001.02 SecuritiesEndOfProcessReportV02, Functionality, file p6.**

Scope
Sent by an executing party or an instructing party to the custodian or an affirming party to notify that all
the necessary SecuritiesTradeConfirmation message or any other notification of the process have been
sent.
It may also be sent through Central Matching Utility (CMU).
The instructing party is typically the investment manager or an intermediary system/vendor
communicating on behalf of the investment manager.
The executing party is typically the broker/dealer or an intermediary system/vendor communicating on
behalf of the broker/dealer.
The custodian or an affirming party is typically the custodian, trustee, financial institution, intermediary
system/vendor communicating on behalf of them, or their agent.
The ISO 20022 Business Application Header must be used
Usage
Initiator: Executing Party, CMU or Instructing Party
Respondent: Custodian or an affirming party does not need to respond.
Outline
The SecuritiesEndOfProcessReportV02 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. Pagination
Number used to sequence pages when it is not possible for data to be conveyed in a single
message and the data has to be split across several pages (messages).
B. ReportGeneralDetails
Notifies the type of report transmitted.
C. ConfirmationParties
Parties involved in the confirmation of the details of a trade.
D. Investor
Party that identifies the underlying investor.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 13 February 2025 semt.023.001.02
SecuritiesEndOfProcessReportV02
Post Trade Matching - Maintenance 2024 - 2025 6 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00004.md) | 6–6 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.2 Structure](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00005.md) | 7–7 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.3 Constraints](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00006.md) | 8–8 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00007.md) | 9–9 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.2 ReportGeneralDetails &lt;RptGnlDtls&gt; / 2.4.2.5 Frequency &lt;Frqcy&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00008.md) | 10–10 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.3 ConfirmationParties &lt;ConfPties&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00009.md) | 11–11 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.3 ConfirmationParties &lt;ConfPties&gt; / 2.4.3.2 Borrower &lt;Brrwr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00010.md) | 12–12 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.3 ConfirmationParties &lt;ConfPties&gt; / 2.4.3.3 Seller &lt;Sellr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00011.md) | 13–13 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.3 ConfirmationParties &lt;ConfPties&gt; / 2.4.3.4 Lender &lt;Lndr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00012.md) | 14–14 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.3 ConfirmationParties &lt;ConfPties&gt; / 2.4.3.5 BrokerOfCredit &lt;BrkrOfCdt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00013.md) | 15–15 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.3 ConfirmationParties &lt;ConfPties&gt; / 2.4.3.6 IntroducingFirm &lt;IntrdcgFirm&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00014.md) | 16–16 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.3 ConfirmationParties &lt;ConfPties&gt; / 2.4.3.7 StepInFirm &lt;StepInFirm&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00015.md) | 17–17 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.3 ConfirmationParties &lt;ConfPties&gt; / 2.4.3.8 StepOutFirm &lt;StepOutFirm&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00016.md) | 18–18 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.3 ConfirmationParties &lt;ConfPties&gt; / 2.4.3.9 ClearingFirm &lt;ClrFirm&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00017.md) | 19–19 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.3 ConfirmationParties &lt;ConfPties&gt; / 2.4.3.10 ExecutingBroker &lt;ExctgBrkr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00018.md) | 20–20 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.3 ConfirmationParties &lt;ConfPties&gt; / 2.4.3.11 CMUParty &lt;CMUPty&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00019.md) | 21–21 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.3 ConfirmationParties &lt;ConfPties&gt; / 2.4.3.12 CMUCounterparty &lt;CMUCtrPty&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00020.md) | 22–22 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.3 ConfirmationParties &lt;ConfPties&gt; / 2.4.3.13 AffirmingParty &lt;AffrmgPty&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00021.md) | 23–23 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.3 ConfirmationParties &lt;ConfPties&gt; / 2.4.3.14 TradeBeneficiaryParty &lt;TradBnfcryPty&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00022.md) | 24–24 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.4 Investor &lt;Invstr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00023.md) | 25–25 |
| [2 semt.023.001.02 SecuritiesEndOfProcessReportV02 / 2.4 Message Building Blocks / 2.4.5 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00024.md) | 26–27 |

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
