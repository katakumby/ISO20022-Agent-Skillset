---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.019.001.09"
message_family: "sese.019"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.019.001.09"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "39 sese.019.001.09 AccountHoldingInformationRequestV09", "file_pages": [1442, 1488]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# sese.019.001.09 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 39 sese.019.001.09 AccountHoldingInformationRequestV09

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); file pp1442–1488; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 39 sese.019.001.09 AccountHoldingInformationRequestV09, Functionality, file p1442.**

Scope
The AccountHoldingInformationRequest message is sent by an instructing party, for example, a (new)
plan manager (transferee), to the executing party, for example, a (old) plan manager (transferor), on
behalf of the initiating party, for example, an investor (client), to request information about financial
instruments held on behalf of the client.
Usage
The AccountHoldingInformationRequest message is used to request information about assets held on
behalf of the client for which it intends to instruct a portfolio transfer at a later time.
Outline
The AccountHoldingInformationRequestV09 MessageDefinition is composed of 17
MessageBuildingBlocks:
A. MessageReference
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. BusinessFlowDirectionType
Business flow direction (assets to be delivered or received).
F. PrimaryIndividualInvestor
Information identifying the primary individual investor, for example, name, address, social security
number and date of birth.
G. SecondaryIndividualInvestor
Information identifying the secondary individual investor, for example, name, address, social
security number and date of birth.
H. OtherIndividualInvestor
Information identifying the other individual investors, for example, name, address, social security
number and date of birth.
I. PrimaryCorporateInvestor
Information identifying the primary corporate investor, for example, name and address.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1442 May 2026

**src-000096, 39 sese.019.001.09 AccountHoldingInformationRequestV09, Functionality, file p1443.**

J. SecondaryCorporateInvestor
Information identifying the secondary corporate investor, for example, name and address.
K. OtherCorporateInvestor
Information identifying the other corporate investors, for example, name and address.
L. TransferorAccount
Identification of the account owned by the investor at the old plan manager (account servicer).
M. NomineeAccount
Account held in the name of a party that is not the name of the beneficial owner of the shares.
N. Transferee
Identification of the institution to which the financial instrument is to be transferred. This may also
be known as the new plan manager.
O. ProductTransfer
Information about the portfolio and assets.
P. MarketPracticeVersion
Identifies the market practice to which the message conforms.
Q. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1443 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.1 MessageDefinition Functionality](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01048.md) | 1442–1443 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01049.md) | 1444–1446 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01050.md) | 1447–1449 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01051.md) | 1450–1450 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.4 RelatedReference &lt;RltdRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01052.md) | 1451–1451 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01053.md) | 1452–1458 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.1 MasterReference &lt;MstrRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01054.md) | 1459–1459 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.3 Portfolio &lt;Prtfl&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01055.md) | 1460–1460 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.3 Portfolio &lt;Prtfl&gt; / 39.4.15.3.2 GeneralInvestment &lt;GnlInvstmt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01056.md) | 1461–1461 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.3 Portfolio &lt;Prtfl&gt; / 39.4.15.3.3 Pension &lt;Pnsn&gt; / 39.4.15.3.3.1 Identification &lt;Id&gt; / 39.4.15.3.3.1.1 Identifier &lt;Idr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01057.md) | 1462–1462 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.3 Portfolio &lt;Prtfl&gt; / 39.4.15.3.3 Pension &lt;Pnsn&gt; / 39.4.15.3.3.2 Type &lt;Tp&gt; / 39.4.15.3.3.2.2 Proprietary &lt;Prtry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01058.md) | 1463–1463 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.3 Portfolio &lt;Prtfl&gt; / 39.4.15.3.3 Pension &lt;Pnsn&gt; / 39.4.15.3.3.3 TransferScope &lt;TrfScp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01059.md) | 1464–1464 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.3 Portfolio &lt;Prtfl&gt; / 39.4.15.3.3 Pension &lt;Pnsn&gt; / 39.4.15.3.3.7 AdditionalInformation &lt;AddtlInf&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01060.md) | 1465–1467 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.1 LineIdentification &lt;LineId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01061.md) | 1468–1468 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.2 Instrument &lt;Instrm&gt; / 39.4.15.4.2.1 Security &lt;Scty&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01062.md) | 1469–1469 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.2 Instrument &lt;Instrm&gt; / 39.4.15.4.2.1 Security &lt;Scty&gt; / 39.4.15.4.2.1.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01063.md) | 1470–1470 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.2 Instrument &lt;Instrm&gt; / 39.4.15.4.2.1 Security &lt;Scty&gt; / 39.4.15.4.2.1.1 Identification &lt;Id&gt; / 39.4.15.4.2.1.1.1 ISIN &lt;ISIN&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01064.md) | 1471–1471 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.2 Instrument &lt;Instrm&gt; / 39.4.15.4.2.1 Security &lt;Scty&gt; / 39.4.15.4.2.1.1 Identification &lt;Id&gt; / 39.4.15.4.2.1.1.3 CUSIP &lt;CUSIP&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01065.md) | 1472–1472 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.2 Instrument &lt;Instrm&gt; / 39.4.15.4.2.1 Security &lt;Scty&gt; / 39.4.15.4.2.1.1 Identification &lt;Id&gt; / 39.4.15.4.2.1.1.10 Dutch &lt;Dtch&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01066.md) | 1473–1473 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.2 Instrument &lt;Instrm&gt; / 39.4.15.4.2.1 Security &lt;Scty&gt; / 39.4.15.4.2.1.1 Identification &lt;Id&gt; / 39.4.15.4.2.1.1.16 OtherProprietaryIdentification &lt;OthrPrtryId&gt; / 39.4.15.4.2.1.1.16.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01067.md) | 1474–1474 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.2 Instrument &lt;Instrm&gt; / 39.4.15.4.2.3 OtherAsset &lt;OthrAsst&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01068.md) | 1475–1475 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.5 TransfereeAccount &lt;TrfeeAcct&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01069.md) | 1476–1476 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.5 TransfereeAccount &lt;TrfeeAcct&gt; / 39.4.15.4.5.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01070.md) | 1477–1477 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.5 TransfereeAccount &lt;TrfeeAcct&gt; / 39.4.15.4.5.7 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01071.md) | 1478–1478 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.6 Transferor &lt;Trfr&gt; / 39.4.15.4.6.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01072.md) | 1479–1479 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.6 Transferor &lt;Trfr&gt; / 39.4.15.4.6.6 SubAccountDetails &lt;SubAcctDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01073.md) | 1480–1480 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.7 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 39.4.15.4.7.1 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01074.md) | 1481–1481 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.7 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 39.4.15.4.7.2 TradeTransactionCondition &lt;TradTxCond&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01075.md) | 1482–1483 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.7 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 39.4.15.4.7.5 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 39.4.15.4.7.5.1 Depository &lt;Dpstry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01076.md) | 1484–1484 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.7 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 39.4.15.4.7.5 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 39.4.15.4.7.5.2 Party1 &lt;Pty1&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01077.md) | 1485–1485 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.7 SettlementPartiesDetails &lt;SttlmPtiesDtls&gt; / 39.4.15.4.7.5 ReceivingSideDetails &lt;RcvgSdDtls&gt; / 39.4.15.4.7.5.5 Party4 &lt;Pty4&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01078.md) | 1486–1486 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.7 SecondaryIndividualInvestor &lt;ScndryIndvInvstr&gt; / 39.4.15.4 FinancialInstrumentAssetForTransfer &lt;FinInstrmAsstForTrf&gt; / 39.4.15.4.8 AssetsHeldInOwnName &lt;AsstsHeldInOwnNm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01079.md) | 1487–1487 |
| [37 sese.014.001.09 PortfolioTransferCancellationRequestV09 / 39.4 Message Building Blocks / 39.4.16 MarketPracticeVersion &lt;MktPrctcVrsn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-01080.md) | 1488–1488 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Beneficial Owner](../../../../../shared/reference/participants/participant-src-000095-beneficial-owner.md) | participant | src-000095 |
| [Concentrator](../../../../../shared/reference/participants/participant-src-000095-concentrator.md) | participant | src-000095 |
| [CSD / ICSD](../../../../../shared/reference/participants/participant-src-000095-csd-icsd.md) | participant | src-000095 |
| [CSD](../../../../../shared/reference/participants/participant-src-000095-csd.md) | participant | src-000095 |
| [Custodian](../../../../../shared/reference/participants/participant-src-000095-custodian.md) | participant | src-000095 |
| [Distributor](../../../../../shared/reference/participants/participant-src-000095-distributor.md) | participant | src-000095 |
| [Executing Party / Registering Party](../../../../../shared/reference/participants/participant-src-000095-executing-party-registering-party.md) | participant | src-000095 |
| [Executing Party](../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | participant | src-000095 |
| [Fund Accountant](../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md) | participant | src-000095 |
| [Fund Manager](../../../../../shared/reference/participants/participant-src-000095-fund-manager.md) | participant | src-000095 |
| [ICSD](../../../../../shared/reference/participants/participant-src-000095-icsd.md) | participant | src-000095 |
| [Institutional Investor](../../../../../shared/reference/participants/participant-src-000095-institutional-investor.md) | participant | src-000095 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | participant | src-000095 |
| [Intermediary](../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | participant | src-000095 |
| [Market Data Provider](../../../../../shared/reference/participants/participant-src-000095-market-data-provider.md) | participant | src-000095 |
| [Paying Agent](../../../../../shared/reference/participants/participant-src-000095-paying-agent.md) | participant | src-000095 |
| [Receiving Party (all levels)](../../../../../shared/reference/participants/participant-src-000095-receiving-party-all-levels.md) | participant | src-000095 |
| [Reporting Party](../../../../../shared/reference/participants/participant-src-000095-reporting-party.md) | participant | src-000095 |
| [Requesting Party](../../../../../shared/reference/participants/participant-src-000095-requesting-party.md) | participant | src-000095 |
| [Transfer Agent](../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | participant | src-000095 |
| [Transferee's Bank (Executing Party)](../../../../../shared/reference/participants/participant-src-000095-transferee-s-bank-executing-party.md) | participant | src-000095 |
| [Transferee's Bank (Instructing Party)](../../../../../shared/reference/participants/participant-src-000095-transferee-s-bank-instructing-party.md) | participant | src-000095 |
| [Transferee](../../../../../shared/reference/participants/participant-src-000095-transferee.md) | participant | src-000095 |
| [Transferor's Bank (Executing Party)](../../../../../shared/reference/participants/participant-src-000095-transferor-s-bank-executing-party.md) | participant | src-000095 |
| [Transferor's Bank (Instructing Party)](../../../../../shared/reference/participants/participant-src-000095-transferor-s-bank-instructing-party.md) | participant | src-000095 |
| [Transferor](../../../../../shared/reference/participants/participant-src-000095-transferor.md) | participant | src-000095 |
| [Account Administration](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p185-account-administration.md) | business-flow | src-000095 |
| [Order Processing](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p186-order-processing.md) | business-flow | src-000095 |
| [Order Execution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p187-order-execution.md) | business-flow | src-000095 |
| [Payment Execution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p188-payment-execution.md) | business-flow | src-000095 |
| [Payment Execution - Advance Pay In](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p189-payment-execution-advance-pay-in.md) | business-flow | src-000095 |
| [Payment Execution - Pay In Arrears](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p190-payment-execution-pay-in-arrears.md) | business-flow | src-000095 |
| [Payment Execution - Pay Out Arrears](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p191-payment-execution-pay-out-arrears.md) | business-flow | src-000095 |
| [Tax Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p192-tax-accounting.md) | business-flow | src-000095 |
| [Fund Valuation](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p193-fund-valuation.md) | business-flow | src-000095 |
| [Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p194-commission-accounting.md) | business-flow | src-000095 |
| [Commission Accounting / Transaction Based Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p195-commission-accounting-transaction-based-commission-accounting.md) | business-flow | src-000095 |
| [Commission Accounting / Trailer Commission Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p196-commission-accounting-trailer-commission-accounting.md) | business-flow | src-000095 |
| [Reconciliation](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p197-reconciliation.md) | business-flow | src-000095 |
| [Distribution](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p199-distribution.md) | business-flow | src-000095 |
| [Registration](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p200-registration.md) | business-flow | src-000095 |
| [Account Opening](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p205-account-opening.md) | business-flow | src-000095 |
| [Account Modification](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p207-account-modification.md) | business-flow | src-000095 |
| [Reporting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p209-reporting.md) | business-flow | src-000095 |
| [Order Processing](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p212-order-processing.md) | business-flow | src-000095 |
| [Custody and Accounting](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p216-custody-and-accounting.md) | business-flow | src-000095 |
| [Transparency of Holdings](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p218-transparency-of-holdings.md) | business-flow | src-000095 |
| [Stock Transfers (Single Leg Transfer)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p221-stock-transfers-single-leg-transfer.md) | business-flow | src-000095 |
| [Portfolio and Stock Transfers (Single Leg)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p226-portfolio-and-stock-transfers-single-leg.md) | business-flow | src-000095 |
| [Portfolio and Stock Transfers (Double/Matched Leg)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p230-portfolio-and-stock-transfers-double-matched-leg.md) | business-flow | src-000095 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
