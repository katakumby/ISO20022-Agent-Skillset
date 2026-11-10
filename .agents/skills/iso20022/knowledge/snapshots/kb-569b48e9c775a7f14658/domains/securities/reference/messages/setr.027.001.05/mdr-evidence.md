---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "setr.027.001.05"
message_family: "setr.027"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.027.001.05"
source_ids: ["src-000181"]
source_locations: [{"source_id": "src-000181", "heading": "3 setr.027.001.05 SecuritiesTradeConfirmationV05", "file_pages": [28, 139]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# setr.027.001.05 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000181 — 3 setr.027.001.05 SecuritiesTradeConfirmationV05

[src-000181](../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md); file pp28–139; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000181, 3 setr.027.001.05 SecuritiesTradeConfirmationV05, Functionality, file p28.**

SCOPE
Sent by an executing party to an instructing party directly or through Central Matching Utility (CMU) to
provide trade confirmation on a per-account basis based on instructions provided by the instructing
party in the SecuritiesAllocationInstruction message.
It may also be used to provide trade confirmation on the trade level from an executing party or an
instructing party to the custodian or an affirming party directly or through CMU.
The instructing party is typically the investment manager or an intermediary system/vendor
communicating on behalf of the investment manager or of other categories of investors.
The executing party is typically the broker/dealer or an intermediary system/vendor communicating on
behalf of the broker/dealer.
The custodian or the affirming party is typically the custodian, trustee, financial institution, intermediary
system/vendor communicating on behalf of them, or their agent.
USAGE
Initiator: In local matching, the initiator of this message is always the executing party. In central
matching the initiator may be either the executing party or instructing party.
Respondent: instructing party, a custodian or an affirming party responds with
SecuritiesTradeConfirmationResponse (accept or reject) message.
Outline
The SecuritiesTradeConfirmationV05 MessageDefinition is composed of 22 MessageBuildingBlocks:
A. Identification
Information that unambiguously identifies an SecuritiesTradeConfirmation message as known by
the account owner (or the instructing party acting on its behalf).
B. NumberCount
Count of the number of transactions linked.
C. References
Reference to the transaction identifier issued by a business party and/or market infrastructure. It
may also be used to reference a previous transaction, for example, a block/allocation instruction, or
tie a set of messages together.
D. TradeDetails
Details of the trade.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 28 February 2025

**src-000181, 3 setr.027.001.05 SecuritiesTradeConfirmationV05, Functionality, file p29.**

E. FinancialInstrumentIdentification
Unique and unambiguous identifier of a financial instrument, assigned under a formal or proprietary
identification scheme.
F. FinancialInstrumentAttributes
Elements characterising a financial instrument.
G. UnderlyingFinancialInstrument
Underlying financial instrument to which an trade confirmation is related.
H. Stipulations
Additional restrictions on the financial instrument, related to the stipulation.
I. ConfirmationParties
Parties involved in the confirmation of the details of a trade.
J. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
K. StandingSettlementInstruction
Specifies what settlement standing instruction database is to be used to derive the settlement
parties involved in the transaction.
L. DeliveringSettlementParties
Specifies the chain of delivering settlement parties.
M. ReceivingSettlementParties
Specifies the chain of receiving settlement parties.
N. CashParties
Cash parties involved in the specific transaction.
O. ClearingDetails
Provides clearing member information.
P. SettlementAmount
Total amount of money to be paid or received in exchange for the securities. The amount includes
the principal with any commissions and fees or accrued interest.
Q. OtherAmounts
Other amounts than the settlement amount.
R. OtherPrices
Other prices than the deal price.
S. OtherBusinessParties
Other business parties relevant to the transaction.
T. TwoLegTransactionDetails
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 29 February 2025

**src-000181, 3 setr.027.001.05 SecuritiesTradeConfirmationV05, Functionality, file p30.**

Specifies a transaction that the trading parties are agreeing to repurchase, sell back or return the
same or similar securities at a later time.
The two leg transaction details defines the closing leg conditions of a two leg transaction. It is also
used to define the anticipated closing leg conditions at the time of opening the closed-end
transaction.
U. RegulatoryStipulations
Specifies regulatory stipulations that financial institutions must be compliant with in the country,
region, and/or area they conduct business.
V. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 30 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00025.md) | 28–30 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.2 Structure](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00026.md) | 31–38 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.3 Constraints](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00027.md) | 39–44 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00028.md) | 45–45 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.2 NumberCount &lt;NbCnt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00029.md) | 46–48 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.1 BusinessProcessType &lt;BizPrcTp&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00030.md) | 49–49 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.4 SecondaryClientOrderIdentification &lt;ScndryClntOrdrId&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00031.md) | 50–50 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.7 Payment &lt;Pmt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00032.md) | 51–51 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.8 TradeTransactionType &lt;TradTxTp&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00033.md) | 52–52 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.12 OrderBookingDate &lt;OrdrBookgDt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00034.md) | 53–53 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.15 ProcessingDate &lt;PrcgDt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00035.md) | 54–54 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.18 PartialFillDetails &lt;PrtlFillDtls&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00036.md) | 55–55 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.20 QuantityBreakdown &lt;QtyBrkdwn&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00037.md) | 56–56 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.23 TypeOfPrice &lt;TpOfPric&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00038.md) | 57–57 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.26 NumberOfDaysAccrued &lt;NbOfDaysAcrd&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00039.md) | 58–58 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.29 AccruedInterestAmount &lt;AcrdIntrstAmt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00040.md) | 59–59 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.33 OrderOriginatorEligibility &lt;OrdrOrgtrElgblty&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00041.md) | 60–60 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.36 ChargeTaxBasisType &lt;ChrgTaxBsisTp&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00042.md) | 61–61 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.40 YieldType &lt;YldTp&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00043.md) | 62–62 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.4 TradeDetails &lt;TradDtls&gt; / 3.4.4.43 AdditionalTradeInstructionProcessingInformation &lt;AddtlTradInstrPrcgInf&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00044.md) | 63–63 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.6 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00045.md) | 64–66 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.6 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 3.4.6.1 PlaceOfListing &lt;PlcOfListg&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00046.md) | 67–67 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.6 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 3.4.6.6 PaymentFrequency &lt;PmtFrqcy&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00047.md) | 68–68 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.6 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 3.4.6.10 OptionType &lt;OptnTp&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00048.md) | 69–69 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.6 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 3.4.6.14 FloatingRateFixingDate &lt;FltgRateFxgDt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00049.md) | 70–70 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.6 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 3.4.6.22 NextFactorDate &lt;NxtFctrDt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00050.md) | 71–71 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.6 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 3.4.6.29 IndexRateBasis &lt;IndxRateBsis&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00051.md) | 72–72 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.6 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 3.4.6.34 ConvertibleIndicator &lt;ConvtblInd&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00052.md) | 73–73 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.6 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 3.4.6.39 WarrantAttachedOnDelivery &lt;WarrtAttchdOnDlvry&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00053.md) | 74–74 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.6 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 3.4.6.43 ExercisePrice &lt;ExrcPric&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00054.md) | 75–75 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.6 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 3.4.6.47 MinimumNominalQuantity &lt;MinNmnlQty&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00055.md) | 76–76 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.6 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 3.4.6.50 FaceAmount &lt;FaceAmt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00056.md) | 77–78 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.7 UnderlyingFinancialInstrument &lt;UndrlygFinInstrm&gt; / 3.4.7.1 Identification &lt;Id&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00057.md) | 79–79 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.7 UnderlyingFinancialInstrument &lt;UndrlygFinInstrm&gt; / 3.4.7.2 Attributes &lt;Attrbts&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00058.md) | 80–82 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.7 UnderlyingFinancialInstrument &lt;UndrlygFinInstrm&gt; / 3.4.7.2 Attributes &lt;Attrbts&gt; / 3.4.7.2.1 PlaceOfListing &lt;PlcOfListg&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00059.md) | 83–83 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.7 UnderlyingFinancialInstrument &lt;UndrlygFinInstrm&gt; / 3.4.7.2 Attributes &lt;Attrbts&gt; / 3.4.7.2.2 Rating &lt;Ratg&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00060.md) | 84–84 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.7 UnderlyingFinancialInstrument &lt;UndrlygFinInstrm&gt; / 3.4.7.2 Attributes &lt;Attrbts&gt; / 3.4.7.2.6 PaymentFrequency &lt;PmtFrqcy&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00061.md) | 85–85 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.7 UnderlyingFinancialInstrument &lt;UndrlygFinInstrm&gt; / 3.4.7.2 Attributes &lt;Attrbts&gt; / 3.4.7.2.10 OptionType &lt;OptnTp&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00062.md) | 86–86 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.7 UnderlyingFinancialInstrument &lt;UndrlygFinInstrm&gt; / 3.4.7.2 Attributes &lt;Attrbts&gt; / 3.4.7.2.14 FloatingRateFixingDate &lt;FltgRateFxgDt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00063.md) | 87–87 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.7 UnderlyingFinancialInstrument &lt;UndrlygFinInstrm&gt; / 3.4.7.2 Attributes &lt;Attrbts&gt; / 3.4.7.2.22 NextFactorDate &lt;NxtFctrDt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00064.md) | 88–88 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.7 UnderlyingFinancialInstrument &lt;UndrlygFinInstrm&gt; / 3.4.7.2 Attributes &lt;Attrbts&gt; / 3.4.7.2.30 PercentageOfDebtClaims &lt;PctgOfDebtClms&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00065.md) | 89–89 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.7 UnderlyingFinancialInstrument &lt;UndrlygFinInstrm&gt; / 3.4.7.2 Attributes &lt;Attrbts&gt; / 3.4.7.2.34 ConvertibleIndicator &lt;ConvtblInd&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00066.md) | 90–90 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.7 UnderlyingFinancialInstrument &lt;UndrlygFinInstrm&gt; / 3.4.7.2 Attributes &lt;Attrbts&gt; / 3.4.7.2.40 OddCouponIndicator &lt;OddCpnInd&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00067.md) | 91–91 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.7 UnderlyingFinancialInstrument &lt;UndrlygFinInstrm&gt; / 3.4.7.2 Attributes &lt;Attrbts&gt; / 3.4.7.2.44 SubscriptionPrice &lt;SbcptPric&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00068.md) | 92–92 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.7 UnderlyingFinancialInstrument &lt;UndrlygFinInstrm&gt; / 3.4.7.2 Attributes &lt;Attrbts&gt; / 3.4.7.2.48 MinimumExercisableQuantity &lt;MinExrcblQty&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00069.md) | 93–93 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.7 UnderlyingFinancialInstrument &lt;UndrlygFinInstrm&gt; / 3.4.7.2 Attributes &lt;Attrbts&gt; / 3.4.7.2.52 FinancialInstrumentAttributeAdditionalDetails &lt;FinInstrmAttrAddtlDtls&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00070.md) | 94–95 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.8 Stipulations &lt;Stiptns&gt; / 3.4.8.1 Geographics &lt;Geogcs&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00071.md) | 96–96 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.8 Stipulations &lt;Stiptns&gt; / 3.4.8.4 CouponRange &lt;CpnRg&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00072.md) | 97–97 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.8 Stipulations &lt;Stiptns&gt; / 3.4.8.8 AutoReinvestment &lt;AutoRinvstmt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00073.md) | 98–98 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.8 Stipulations &lt;Stiptns&gt; / 3.4.8.10 Currency &lt;Ccy&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00074.md) | 99–99 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.8 Stipulations &lt;Stiptns&gt; / 3.4.8.14 LookBack &lt;LookBck&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00075.md) | 100–100 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.8 Stipulations &lt;Stiptns&gt; / 3.4.8.20 MaximumSubstitution &lt;MaxSbstitn&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00076.md) | 101–101 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.8 Stipulations &lt;Stiptns&gt; / 3.4.8.23 MinimumQuantity &lt;MinQty&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00077.md) | 102–102 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.8 Stipulations &lt;Stiptns&gt; / 3.4.8.27 Sector &lt;Sctr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00078.md) | 103–103 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.8 Stipulations &lt;Stiptns&gt; / 3.4.8.30 WholePoolIndicator &lt;WhlPoolInd&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00079.md) | 104–104 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.8 Stipulations &lt;Stiptns&gt; / 3.4.8.35 PriceRange &lt;PricRg&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00080.md) | 105–105 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.8 Stipulations &lt;Stiptns&gt; / 3.4.8.39 PreFundedIndicator &lt;PreFnddInd&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00081.md) | 106–106 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.9 ConfirmationParties &lt;ConfPties&gt; / 3.4.9.1 Buyer &lt;Buyr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00082.md) | 107–107 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.9 ConfirmationParties &lt;ConfPties&gt; / 3.4.9.3 Seller &lt;Sellr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00083.md) | 108–108 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.9 ConfirmationParties &lt;ConfPties&gt; / 3.4.9.5 BrokerOfCredit &lt;BrkrOfCdt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00084.md) | 109–109 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.9 ConfirmationParties &lt;ConfPties&gt; / 3.4.9.8 StepOutFirm &lt;StepOutFirm&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00085.md) | 110–110 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.9 ConfirmationParties &lt;ConfPties&gt; / 3.4.9.11 CMUParty &lt;CMUPty&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00086.md) | 111–111 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.9 ConfirmationParties &lt;ConfPties&gt; / 3.4.9.13 AffirmingParty &lt;AffrmgPty&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00087.md) | 112–114 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.11 StandingSettlementInstruction &lt;StgSttlmInstr&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00088.md) | 115–116 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.13 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00089.md) | 117–118 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.14 CashParties &lt;CshPties&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00090.md) | 119–120 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.15 ClearingDetails &lt;ClrDtls&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00091.md) | 121–121 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.15 ClearingDetails &lt;ClrDtls&gt; / 3.4.15.2 ClearingSegment &lt;ClrSgmt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00092.md) | 122–122 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.16 SettlementAmount &lt;SttlmAmt&gt; / 3.4.16.3 Amount &lt;Amt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00093.md) | 123–123 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.16 SettlementAmount &lt;SttlmAmt&gt; / 3.4.16.6 ForeignExchangeDetails &lt;FXDtls&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00094.md) | 124–125 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.18 OtherPrices &lt;OthrPrics&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00095.md) | 126–126 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.19 OtherBusinessParties &lt;OthrBizPties&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00096.md) | 127–127 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.19 OtherBusinessParties &lt;OthrBizPties&gt; / 3.4.19.2 StockExchange &lt;StockXchg&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00097.md) | 128–128 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.19 OtherBusinessParties &lt;OthrBizPties&gt; / 3.4.19.5 QualifiedForeignIntermediary &lt;QlfdFrgnIntrmy&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00098.md) | 129–129 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.20 TwoLegTransactionDetails &lt;TwoLegTxDtls&gt; / 3.4.20.1 TradeDate &lt;TradDt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00099.md) | 130–130 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.20 TwoLegTransactionDetails &lt;TwoLegTxDtls&gt; / 3.4.20.4 GrossTradeAmount &lt;GrssTradAmt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00100.md) | 131–132 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.20 TwoLegTransactionDetails &lt;TwoLegTxDtls&gt; / 3.4.20.6 SecondLegNarrative &lt;ScndLegNrrtv&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00101.md) | 133–133 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.20 TwoLegTransactionDetails &lt;TwoLegTxDtls&gt; / 3.4.20.9 ClosingSettlementAmount &lt;ClsgSttlmAmt&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00102.md) | 134–134 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.20 TwoLegTransactionDetails &lt;TwoLegTxDtls&gt; / 3.4.20.11 TwoLegTransactionType &lt;TwoLegTxTp&gt; / 3.4.20.11.1 FutureOrOptionDetails &lt;FutrOrOptnDtls&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00103.md) | 135–135 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.20 TwoLegTransactionDetails &lt;TwoLegTxDtls&gt; / 3.4.20.11 TwoLegTransactionType &lt;TwoLegTxTp&gt; / 3.4.20.11.2 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00104.md) | 136–137 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.21 RegulatoryStipulations &lt;RgltryStiptns&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00105.md) | 138–138 |
| [3 setr.027.001.05 SecuritiesTradeConfirmationV05 / 3.4 Message Building Blocks / 3.4.22 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00106.md) | 139–139 |

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
