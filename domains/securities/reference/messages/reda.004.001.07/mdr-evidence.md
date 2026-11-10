---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "reda.004.001.07"
message_family: "reda.004"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07"
source_ids: ["src-000096"]
source_locations: [{"source_id": "src-000096", "heading": "15 reda.004.001.07 FundReferenceDataReportV07", "file_pages": [291, 364]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["May 2026"]
---

# reda.004.001.07 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000096 — 15 reda.004.001.07 FundReferenceDataReportV07

[src-000096](../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf); file pp291–364; publication May 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000096, 15 reda.004.001.07 FundReferenceDataReportV07, Functionality, file p291.**

Scope
The FundReferenceDataReport message is sent by a report provider, for example, a fund promoter,
fund management company, transfer agent, or market data provider to the report recipient, for example,
a professional investor, investment fund distributor, market data provider, regulator or other interested
party, to provide the key reference data for financial instruments to facilitate trading. The message may
also include reporting data concerning product governance, such as target market data, and a
breakdown of the costs and fees.
Usage
A FundReferenceDataReport message should be prepared for each class of unit/share (for which an
individual ISIN should have been allocated), in respect of its "home" market. Each time the fund data
changes, the 'product provider' must provide the data to a product user, for example, the distributors, by
sending a new funds reference data report. A single message may contain more than one report. When
the FundReferenceDataReport message is sent to provide updated reference data, the message
overwrites the previously sent data.
The FundReferenceDataReport message may be used in various models or environments:
- in a standalone environment, for example, initiated by the Report Provider (fund promoter, fund
manager and / or reference data vendors) sent on a regular frequency, or when changes are needed.
- in a request / response environment, with the InvestmentFundReportRequest, for example, initiated by
report users (data vendors, professional investors, regulators or investment fund distributors) in
enabling the user to control the flow and updates of information.
- in a reference data vendor environment, for example, market infrastructure and reference data
providers may collate and store all fund reference data information centrally for access via database or
regular distribution information. A reference data vendor may assume the role of both report provider
and report user.
The FundReferenceDataReport message may be used to provide data concerning product governance,
such as target market data, and a breakdown of the costs and fees in the context of MiFID II, with
respect to the European MiFID Template (EMT).
Outline
The FundReferenceDataReportV07 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PreviousReference
Reference to a linked message that was previously sent.
C. RelatedReference
Reference to a linked message that was previously received.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 291 May 2026

**src-000096, 15 reda.004.001.07 FundReferenceDataReportV07, Functionality, file p292.**

D. FundReferenceDataReportIdentification
Unique and unambiguous identifier for the fund reference data report, as assigned by the issuer of
the report.
E. Report
Fund reference data.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 292 May 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/investment-funds/2025-2026/documents/src-000096/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [15 reda.004.001.07 FundReferenceDataReportV07](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00204.md) | 291–292 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.2 Structure](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00205.md) | 293–297 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.3 Constraints](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00206.md) | 298–299 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00207.md) | 300–300 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.2 PreviousReference &lt;PrvsRef&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00208.md) | 301–307 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00209.md) | 308–308 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.4 GeneralReferenceDate &lt;GnlRefDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00210.md) | 309–309 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.8 SecurityIdentification &lt;SctyId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00211.md) | 310–311 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.8 SecurityIdentification &lt;SctyId&gt; / 15.4.5.8.1 Identification &lt;Id&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00212.md) | 312–312 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.8 SecurityIdentification &lt;SctyId&gt; / 15.4.5.8.1 Identification &lt;Id&gt; / 15.4.5.8.1.1 OtherIdentification &lt;OthrId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00213.md) | 313–313 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.8 SecurityIdentification &lt;SctyId&gt; / 15.4.5.8.1 Identification &lt;Id&gt; / 15.4.5.8.1.2 Description &lt;Desc&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00214.md) | 314–314 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.8 SecurityIdentification &lt;SctyId&gt; / 15.4.5.8.7 ClassificationType &lt;ClssfctnTp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00215.md) | 315–315 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.8 SecurityIdentification &lt;SctyId&gt; / 15.4.5.8.11 ProductType &lt;PdctTp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00216.md) | 316–316 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.8 SecurityIdentification &lt;SctyId&gt; / 15.4.5.8.12 Issuer &lt;Issr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00217.md) | 317–317 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.8 SecurityIdentification &lt;SctyId&gt; / 15.4.5.8.15 ProductCategoryGermany &lt;PdctCtgyDE&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00218.md) | 318–318 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.8 SecurityIdentification &lt;SctyId&gt; / 15.4.5.8.17 QuotationType &lt;QtnTp&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00219.md) | 319–319 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.8 SecurityIdentification &lt;SctyId&gt; / 15.4.5.8.20 ExPostCostCalculationBasis &lt;ExPstCostClctnBsis&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00220.md) | 320–320 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.9 FundParties &lt;FndPties&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00221.md) | 321–321 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.12 FundDetails &lt;FndDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00222.md) | 322–323 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.13 ValuationDealingCharacteristics &lt;ValtnDealgChrtcs&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00223.md) | 324–324 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.15 SubscriptionProcessingCharacteristics &lt;SbcptPrcgChrtcs&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00224.md) | 325–326 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.16 RedemptionProcessingCharacteristics &lt;RedPrcgChrtcs&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00225.md) | 327–327 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.17 SwitchProcessingCharacteristics &lt;SwtchPrcgChrtcs&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00226.md) | 328–328 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.18 PlanCharacteristics &lt;PlanChrtcs&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00227.md) | 329–329 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.19 PaymentInstrument &lt;PmtInstrm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00228.md) | 330–330 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.20 CashSettlementDetails &lt;CshSttlmDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00229.md) | 331–331 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.20 CashSettlementDetails &lt;CshSttlmDtls&gt; / 15.4.5.20.2 PrimaryAccount &lt;PmryAcct&gt; / 15.4.5.20.2.1 AccountIdentification &lt;AcctId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00230.md) | 332–332 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.20 CashSettlementDetails &lt;CshSttlmDtls&gt; / 15.4.5.20.2 PrimaryAccount &lt;PmryAcct&gt; / 15.4.5.20.2.3 AccountTypeDescription &lt;AcctTpDesc&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00231.md) | 333–333 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.20 CashSettlementDetails &lt;CshSttlmDtls&gt; / 15.4.5.20.3 SecondaryAccount &lt;ScndryAcct&gt; / 15.4.5.20.3.1 AccountIdentification &lt;AcctId&gt; / 15.4.5.20.3.1.2 Name &lt;Nm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00232.md) | 334–334 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.21 LocalMarketAnnex &lt;LclMktAnx&gt; / 15.4.5.21.1 Country &lt;Ctry&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00233.md) | 335–335 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.21 LocalMarketAnnex &lt;LclMktAnx&gt; / 15.4.5.21.2 LocalOrderDesk &lt;LclOrdrDsk&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00234.md) | 336–337 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.21 LocalMarketAnnex &lt;LclMktAnx&gt; / 15.4.5.21.4 RedemptionProcessingCharacteristics &lt;RedPrcgChrtcs&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00235.md) | 338–338 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.21 LocalMarketAnnex &lt;LclMktAnx&gt; / 15.4.5.21.5 SwitchProcessingCharacteristics &lt;SwtchPrcgChrtcs&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00236.md) | 339–339 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.21 LocalMarketAnnex &lt;LclMktAnx&gt; / 15.4.5.21.6 CashSettlementDetails &lt;CshSttlmDtls&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00237.md) | 340–340 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.21 LocalMarketAnnex &lt;LclMktAnx&gt; / 15.4.5.21.6 CashSettlementDetails &lt;CshSttlmDtls&gt; / 15.4.5.21.6.1 Currency &lt;Ccy&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00238.md) | 341–341 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.21 LocalMarketAnnex &lt;LclMktAnx&gt; / 15.4.5.21.6 CashSettlementDetails &lt;CshSttlmDtls&gt; / 15.4.5.21.6.2 PrimaryAccount &lt;PmryAcct&gt; / 15.4.5.21.6.2.1 AccountIdentification &lt;AcctId&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00239.md) | 342–342 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.21 LocalMarketAnnex &lt;LclMktAnx&gt; / 15.4.5.21.6 CashSettlementDetails &lt;CshSttlmDtls&gt; / 15.4.5.21.6.2 PrimaryAccount &lt;PmryAcct&gt; / 15.4.5.21.6.2.3 AccountTypeDescription &lt;AcctTpDesc&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00240.md) | 343–343 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.21 LocalMarketAnnex &lt;LclMktAnx&gt; / 15.4.5.21.6 CashSettlementDetails &lt;CshSttlmDtls&gt; / 15.4.5.21.6.3 SecondaryAccount &lt;ScndryAcct&gt; / 15.4.5.21.6.3.1 AccountIdentification &lt;AcctId&gt; / 15.4.5.21.6.3.1.2 Name &lt;Nm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00241.md) | 344–344 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.22 TargetMarket &lt;TrgtMkt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00242.md) | 345–346 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.22 TargetMarket &lt;TrgtMkt&gt; / 15.4.5.22.1 ReferenceDate &lt;RefDt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00243.md) | 347–347 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.22 TargetMarket &lt;TrgtMkt&gt; / 15.4.5.22.2 InvestorType &lt;InvstrTp&gt; / 15.4.5.22.2.2 InvestorTypeProfessional &lt;InvstrTpPrfssnl&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00244.md) | 348–348 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.22 TargetMarket &lt;TrgtMkt&gt; / 15.4.5.22.3 KnowledgeAndOrExperience &lt;KnwldgAndOrExprnc&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00245.md) | 349–349 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.22 TargetMarket &lt;TrgtMkt&gt; / 15.4.5.22.3 KnowledgeAndOrExperience &lt;KnwldgAndOrExprnc&gt; / 15.4.5.22.3.3 AdvancedInvestor &lt;AdvncdInvstr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00246.md) | 350–350 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.22 TargetMarket &lt;TrgtMkt&gt; / 15.4.5.22.4 AbilityToBearLosses &lt;AbltyToBearLosses&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00247.md) | 351–351 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.22 TargetMarket &lt;TrgtMkt&gt; / 15.4.5.22.4 AbilityToBearLosses &lt;AbltyToBearLosses&gt; / 15.4.5.22.4.3 LimitedCapitalLossLevel &lt;LtdCptlLossLvl&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00248.md) | 352–352 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.22 TargetMarket &lt;TrgtMkt&gt; / 15.4.5.22.5 RiskTolerance &lt;RskTlrnce&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00249.md) | 353–353 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.22 TargetMarket &lt;TrgtMkt&gt; / 15.4.5.22.5 RiskTolerance &lt;RskTlrnce&gt; / 15.4.5.22.5.4 RiskToleranceForNonPRIIPSAndNonUCITSSpain &lt;RskTlrnceForNonPRIIPSAndNonUCITSES&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00250.md) | 354–354 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.22 TargetMarket &lt;TrgtMkt&gt; / 15.4.5.22.6 ClientObjectivesAndNeeds &lt;ClntObjctvsAndNeeds&gt; / 15.4.5.22.6.1 ReturnProfilePreservation &lt;RtrPrflPrsrvtn&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00251.md) | 355–355 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.22 TargetMarket &lt;TrgtMkt&gt; / 15.4.5.22.6 ClientObjectivesAndNeeds &lt;ClntObjctvsAndNeeds&gt; / 15.4.5.22.6.3 ReturnProfileIncome &lt;RtrPrflIncm&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00252.md) | 356–356 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.22 TargetMarket &lt;TrgtMkt&gt; / 15.4.5.22.6 ClientObjectivesAndNeeds &lt;ClntObjctvsAndNeeds&gt; / 15.4.5.22.6.7 MinimumHoldingPeriod &lt;MinHldgPrd&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00253.md) | 357–357 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.22 TargetMarket &lt;TrgtMkt&gt; / 15.4.5.22.6 ClientObjectivesAndNeeds &lt;ClntObjctvsAndNeeds&gt; / 15.4.5.22.6.10 Other &lt;Othr&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00254.md) | 358–358 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.25 AdditionalInformationUKMarket &lt;AddtlInfUKMkt&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00255.md) | 359–359 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.25 AdditionalInformationUKMarket &lt;AddtlInfUKMkt&gt; / 15.4.5.25.1 FinancialInstrumentTransactionCostsExAnteUK &lt;FinInstrmTxCostsExAnteUK&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00256.md) | 360–361 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.26 ValueForMoney &lt;ValForMny&gt; / 15.4.5.26.1 EMTDataReportingVFMUK &lt;EMTDataRptgVFMUK&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00257.md) | 362–362 |
| [15 reda.004.001.07 FundReferenceDataReportV07 / 15.4 Message Building Blocks / 15.4.5 Report &lt;Rpt&gt; / 15.4.5.26 ValueForMoney &lt;ValForMny&gt; / 15.4.5.26.5 OtherReviewRelatedToValueAndOrChargesUK &lt;OthrRvwRltdToValAndOrChrgsUK&gt;](../../message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00258.md) | 363–364 |

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
