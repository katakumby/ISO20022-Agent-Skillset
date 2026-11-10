---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "setr.044.001.04"
message_family: "setr.044"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04"
source_ids: ["src-000181"]
source_locations: [{"source_id": "src-000181", "heading": "6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "file_pages": [162, 221]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# setr.044.001.04 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000181 — 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04

[src-000181](../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf); file pp162–221; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000181, 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04, Functionality, file p162.**

Scope
This message is sent from Central Matching Utility (CMU) to an executing party or an instructing party
to advise the status of the SecuritiesTradeConfirmation message previously sent by the party. The
status may be a processing, pending processing, affirmed or disaffirmed, cancel or replacement by an
instructing party, a custodian or an affirming party, internal matching, and/or matching status.
The instructing party is typically the investment manager or an intermediary system/vendor
communicating on behalf of the investment manager or of other categories of investors. The executing
party is typically the broker/dealer or an intermediary system/vendor communicating on behalf of the
broker/dealer.
The ISO 20022 Business Application Header must be used
Usage
Initiator: In central matching the Initiator is the Central Matching Utility.
Respondent: no response is needed by the recipient of the message.
Outline
The SecuritiesTradeConfirmationStatusAdviceV04 MessageDefinition is composed of 13
MessageBuildingBlocks:
A. Identification
Information that unambiguously identifies an SecuritiesTradeConfirmationStatusAdvice message
as known by the account owner (or the instructing party acting on its behalf).
B. References
Link to another transaction that must be processed after, before or at the same time.
C. AffirmationStatus
Provides details on the affitrmation status of a trade.
D. ProcessingStatus
Provides the processing status of a trade.
E. MatchingStatus
Provides details on the matching status of a trade.
F. ReplacementProcessingStatus
Provides the replacement processing status of a trade.
G. CancellationProcessingStatus
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 162 February 2025

**src-000181, 6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04, Functionality, file p163.**

Provides details on the cancellation status of a trade.
H. PartyTradingDetails
Details of the trading party.
I. CounterpartyTradingDetails
Details of the trading counterparty.
J. ConfirmationParties
Parties used for acting parties that applies either to the whole message or to individual sides.
K. DeliveringSettlementParties
Identifies the chain of delivering settlement parties.
L. ReceivingSettlementParties
Identifies the chain of receiving settlement parties.
M. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 163 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00127.md) | 162–163 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.2 Structure](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00128.md) | 164–165 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.3 Constraints](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00129.md) | 166–169 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00130.md) | 170–170 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.1 Identification &lt;Id&gt; / 6.4.1.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00131.md) | 171–171 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.2 References &lt;Refs&gt; / 6.4.2.2 Reference &lt;Ref&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00132.md) | 172–172 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.3 AffirmationStatus &lt;AffirmSts&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00133.md) | 173–173 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.3 AffirmationStatus &lt;AffirmSts&gt; / 6.4.3.3 ProprietaryStatus &lt;PrtrySts&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00134.md) | 174–174 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.4 ProcessingStatus &lt;PrcgSts&gt; / 6.4.4.1 AcknowledgedAccepted &lt;AckdAccptd&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00135.md) | 175–175 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.4 ProcessingStatus &lt;PrcgSts&gt; / 6.4.4.4 Done &lt;Done&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00136.md) | 176–176 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.4 ProcessingStatus &lt;PrcgSts&gt; / 6.4.4.6 FullyExecutedConfirmationSent &lt;FullyExctdConfSnt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00137.md) | 177–177 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.4 ProcessingStatus &lt;PrcgSts&gt; / 6.4.4.9 InRepair &lt;InRpr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00138.md) | 178–178 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.4 ProcessingStatus &lt;PrcgSts&gt; / 6.4.4.11 OpenOrder &lt;OpnOrdr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00139.md) | 179–179 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.4 ProcessingStatus &lt;PrcgSts&gt; / 6.4.4.14 Rejected &lt;Rjctd&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00140.md) | 180–180 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.4 ProcessingStatus &lt;PrcgSts&gt; / 6.4.4.16 StandingInstruction &lt;StgInstr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00141.md) | 181–181 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.4 ProcessingStatus &lt;PrcgSts&gt; / 6.4.4.19 ProprietaryStatus &lt;PrtrySts&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00142.md) | 182–182 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.5 MatchingStatus &lt;MtchgSts&gt; / 6.4.5.2 MatchedWithTolerance &lt;MtchdWthTlrnce&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00143.md) | 183–183 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.5 MatchingStatus &lt;MtchgSts&gt; / 6.4.5.4 Unmatched &lt;Umtchd&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00144.md) | 184–184 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.6 ReplacementProcessingStatus &lt;RplcmntPrcgSts&gt; / 6.4.6.1 Accepted &lt;Accptd&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00145.md) | 185–185 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.6 ReplacementProcessingStatus &lt;RplcmntPrcgSts&gt; / 6.4.6.3 Denied &lt;Dnd&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00146.md) | 186–186 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.6 ReplacementProcessingStatus &lt;RplcmntPrcgSts&gt; / 6.4.6.5 PartialReplacementAccepted &lt;PrtlRplcmntAccptd&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00147.md) | 187–187 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.6 ReplacementProcessingStatus &lt;RplcmntPrcgSts&gt; / 6.4.6.8 ReceivedAtStockExchange &lt;RcvdAtStockXchg&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00148.md) | 188–188 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.6 ReplacementProcessingStatus &lt;RplcmntPrcgSts&gt; / 6.4.6.10 ModificationRequested &lt;ModReqd&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00149.md) | 189–189 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.7 CancellationProcessingStatus &lt;CxlPrcgSts&gt; / 6.4.7.1 CancellationPending &lt;CxlPdg&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00150.md) | 190–190 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.7 CancellationProcessingStatus &lt;CxlPrcgSts&gt; / 6.4.7.3 CancellationCompleted &lt;CxlCmpltd&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00151.md) | 191–193 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.9 CounterpartyTradingDetails &lt;CtrPtyTradgDtls&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00152.md) | 194–196 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.10 ConfirmationParties &lt;ConfPties&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00153.md) | 197–197 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.10 ConfirmationParties &lt;ConfPties&gt; / 6.4.10.1 Investor &lt;Invstr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00154.md) | 198–198 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.10 ConfirmationParties &lt;ConfPties&gt; / 6.4.10.2 Buyer &lt;Buyr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00155.md) | 199–199 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.10 ConfirmationParties &lt;ConfPties&gt; / 6.4.10.3 Borrower &lt;Brrwr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00156.md) | 200–200 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.10 ConfirmationParties &lt;ConfPties&gt; / 6.4.10.4 Seller &lt;Sellr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00157.md) | 201–201 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.10 ConfirmationParties &lt;ConfPties&gt; / 6.4.10.5 Lender &lt;Lndr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00158.md) | 202–202 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.10 ConfirmationParties &lt;ConfPties&gt; / 6.4.10.6 BrokerOfCredit &lt;BrkrOfCdt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00159.md) | 203–203 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.10 ConfirmationParties &lt;ConfPties&gt; / 6.4.10.7 IntroducingFirm &lt;IntrdcgFirm&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00160.md) | 204–204 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.10 ConfirmationParties &lt;ConfPties&gt; / 6.4.10.8 StepInFirm &lt;StepInFirm&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00161.md) | 205–205 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.10 ConfirmationParties &lt;ConfPties&gt; / 6.4.10.9 StepOutFirm &lt;StepOutFirm&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00162.md) | 206–206 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.10 ConfirmationParties &lt;ConfPties&gt; / 6.4.10.10 ClearingFirm &lt;ClrFirm&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00163.md) | 207–207 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.10 ConfirmationParties &lt;ConfPties&gt; / 6.4.10.11 ExecutingBroker &lt;ExctgBrkr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00164.md) | 208–208 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.10 ConfirmationParties &lt;ConfPties&gt; / 6.4.10.12 AffirmingParty &lt;AffrmgPty&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00165.md) | 209–209 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.10 ConfirmationParties &lt;ConfPties&gt; / 6.4.10.13 TradeBeneficiaryParty &lt;TradBnfcryPty&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00166.md) | 210–210 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.11 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00167.md) | 211–215 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.12 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00168.md) | 216–220 |
| [6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04 / 6.4 Message Building Blocks / 6.4.13 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00169.md) | 221–221 |

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
