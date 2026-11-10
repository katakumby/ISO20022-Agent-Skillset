---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-8cbba10ca914faa6cd02"
title: "SecuritiesQuantity"
business_component_name: "SecuritiesQuantity"
aliases: []
domain: "shared"
domains: ["securities", "shared"]
message_sets: ["t2s-administration", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-reference-data"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000345", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000379"]
source_editions: ["december-2019", "december-2024", "february-2025", "june-2021", "march-2024", "may-2025"]
source_locations: [{"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A1402:F1489"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A4258:F4345"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A1402:F1489"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A1402:F1489"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A4258:F4345"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A4258:F4345"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A1402:F1489"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A1402:F1489"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A1402:F1489"]}]
content_sha256: "8cbba10ca914faa6cd02b2c759c1841163c8bf06d9816ce775251606aec98212"
parent_names: []
related_component_names: ["Allocation", "BiddingConditions", "BuyIn", "CorporateActionDistribution", "CorporateActionElection", "CorporateActionEvent", "CorporateActionProtectProcess", "CorporateActionSecuritiesEntitlement", "CurrencyAndAmount", "Debt", "DecimalNumber", "FundsCashFlow", "InvestmentFundOrder", "InvestmentFundOrderExecution", "Issuance", "Liquidity", "LotBreakdown", "Lottery", "NetAssetValueCalculation", "Netting", "PairOff", "PercentageRate", "Position", "QuantityCode", "Quote", "SecuritiesAndCashDistribution", "SecuritiesBalance", "SecuritiesConversion", "SecuritiesDistribution", "SecuritiesEntry", "SecuritiesOrder", "SecuritiesOrderParameters", "SecuritiesOrderStatus", "SecuritiesProceedsDefinition", "SecuritiesSettlement", "SecuritiesTrade", "SecuritiesTradeExecution", "SecuritiesTransfer", "Security", "SidePocket", "TaxVoucher", "TradingMarket", "UKTaxGroupUnitCode", "UnderlyingRatio"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# SecuritiesQuantity

## Definition

Quantity of a security.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SecuritiesQuantity | ∅ | ∅ | Quantity of a security. | ∅ | ∅ |
| 2 | SecuritiesQuantity | Unit | ∅ | Quantity of a security. | DecimalNumber | ∅ |
| 3 | SecuritiesQuantity | SecuritiesTransfer | ∅ | Transfer of a specific quantity of securities. | SecuritiesTransfer | TransferredQuantity |
| 4 | SecuritiesQuantity | SecurityIdentification | ∅ | Identifies the security. | Security | SecuritiesQuantity |
| 5 | SecuritiesQuantity | Order | ∅ | Order for which a number of units is specified. | InvestmentFundOrder | UnitsNumber |
| 6 | SecuritiesQuantity | Group1Or2Units | ∅ | Tax group to which the purchased units belong. | UKTaxGroupUnitCode | ∅ |
| 7 | SecuritiesQuantity | RelatedOrderExecution | ∅ | Order execution process for which a number of units is specified. | InvestmentFundOrderExecution | UnitsNumber |
| 8 | SecuritiesQuantity | SecuritiesSettlement | ∅ | Settlement of a specific amount of securities. | SecuritiesSettlement | SettlementQuantity |
| 9 | SecuritiesQuantity | MinimumQuantityDebt | ∅ | Security for which a minimum quantity is specified. | Security | MinimumQuantity |
| 10 | SecuritiesQuantity | LotBreakdown | ∅ | Number of securities purchased or sold in one transaction. In terms of options, a lot represents the number of contracts contained in one derivative security. | LotBreakdown | SecuritiesQuantity |
| 11 | SecuritiesQuantity | MinimumExercisableQuantitySecuritiesConversion | ∅ | Securities conversion process for which a minimum exercisable quantity is specified. | SecuritiesConversion | MinimumExercisableQuantity |
| 12 | SecuritiesQuantity | MinimumExercisableMultipleQuantitySecuritiesConversion | ∅ | Securities conversion process for which a minimum exercisable multiple quantity is specified. | SecuritiesConversion | MinimumExercisableMultipleQuantity |
| 13 | SecuritiesQuantity | AggregateQuantityBalance | ∅ | Securities balance which contains the aggregate quantity. | SecuritiesBalance | AggregateQuantity |
| 14 | SecuritiesQuantity | SecuritiesProceedsDefinition | ∅ | Securities proceeds for which an amount of securities is posted. | SecuritiesProceedsDefinition | SecuritiesQuantity |
| 15 | SecuritiesQuantity | ConditionalQuantitySecuritiesProceeds | ∅ | Securities proceeds for which a conditional quantity has been defined. | SecuritiesProceedsDefinition | ConditionalQuantity |
| 16 | SecuritiesQuantity | OverAndAboveQuantitySecuritiesProceeds | ∅ | Securities proceeds for which an over and above normal endured quantity has been provided. | SecuritiesProceedsDefinition | OverAndAboveNormalEnsuredEntitlementQuantity |
| 17 | SecuritiesQuantity | Entry | ∅ | Entry in a securities account of a specific quantity of securities. | SecuritiesEntry | FinancialInstrumentQuantity |
| 18 | SecuritiesQuantity | Code | ∅ | Quantity expressed as a code. | QuantityCode | ∅ |
| 19 | SecuritiesQuantity | ExpectedQuantitySecuritiesProceeds | ∅ | Securities proceeds for which a quantity of securities to receive has been specified. | SecuritiesProceedsDefinition | QuantityToReceive |
| 20 | SecuritiesQuantity | StatusRelatedSecuritiesProceeds | ∅ | Securities proceeds related to securities with a specific status. | SecuritiesProceedsDefinition | StatusQuantity |
| 21 | SecuritiesQuantity | CorporateActionDistribution | ∅ | Corporate action distribution process for which a quantity of securities has been posted. | CorporateActionDistribution | PostingQuantity |
| 22 | SecuritiesQuantity | RelatedEventForFractionalQuantity | ∅ | Event for which the resulting fractional quantity will be paid with cash in lieu.  | CorporateActionEvent | FractionalQuantity |
| 23 | SecuritiesQuantity | MaximumExercisableQuantitySecuritiesConversion | ∅ | Securities conversion process for which a maximum exercisable quantity is specified. | SecuritiesConversion | MaximumExercisableQuantity |
| 24 | SecuritiesQuantity | BoardLotSecuritiesProceeds | ∅ | Securities proceeds related to a board lot. | SecuritiesProceedsDefinition | BoardLotSecuritiesQuantity |
| 25 | SecuritiesQuantity | NewDenominationSecuritiesProceeds | ∅ | Securities proceeds related to a quantity of redenominated securities. | SecuritiesProceedsDefinition | NewDenominationSecuritiesQuantity |
| 26 | SecuritiesQuantity | BackEndOddLotBiddingConditions | ∅ | BiddingConditions for which a back end odd lot is provided. | BiddingConditions | BackEndOddLotQuantity |
| 27 | SecuritiesQuantity | SecuritiesEntitlement | ∅ | Specifies the entitlement parameters relative to the securities entitlement. | CorporateActionSecuritiesEntitlement | EntitledSecuritiesQuantity |
| 28 | SecuritiesQuantity | CorporateActionEvent | ∅ | Corporate action for which a quantity of securities is specified. | CorporateActionEvent | SecuritiesQuantity |
| 29 | SecuritiesQuantity | BiddingConditions | ∅ | Bidding conditions related to the base denomination quantity. | BiddingConditions | BaseDenomination |
| 30 | SecuritiesQuantity | Lottery | ∅ | Lottery for which an incremental denomination is specified. | Lottery | IncrementalDenomination |
| 31 | SecuritiesQuantity | RelatedSubBalance | ∅ | Sub balance which contains a quantity of securities. | SecuritiesBalance | SubBalanceQuantity |
| 32 | SecuritiesQuantity | AvailableQuantityBalance | ∅ | Securities balance which contains the securities quantity. | SecuritiesBalance | AvailableQuantity |
| 33 | SecuritiesQuantity | Trade | ∅ | Trade for which a quantity is specified. | SecuritiesTrade | TradeQuantity |
| 34 | SecuritiesQuantity | RatioDenominatorSecuritiesConversion | ∅ | Securities conversion process for which a conversion ratio denominator quantity is specified. | SecuritiesConversion | ConversionRatioDenominator |
| 35 | SecuritiesQuantity | RatioNumeratorSecuritiesConversion | ∅ | Securities conversion process for which a conversion ratio denominator quantity is specified. | SecuritiesConversion | ConversionRatioNumerator |
| 36 | SecuritiesQuantity | MinimumTradedQuantityMarket | ∅ | Market for which a minimum traded quantity is specified. | TradingMarket | MinimumTradedNominalQuantity |
| 37 | SecuritiesQuantity | MinimumDenominationDebt | ∅ | Debt for which a minimum denomination is specified. | Debt | MinimumDenomination |
| 38 | SecuritiesQuantity | MinimumIncrementDebt | ∅ | Debt for which a minimum increment is specified. | Debt | MinimumIncrement |
| 39 | SecuritiesQuantity | RelatedOrder | ∅ | Order for which a specific quantity is requested. | SecuritiesOrder | OrderedQuantity |
| 40 | SecuritiesQuantity | Allocation | ∅ | Allocation process for which a quantity is specified. | Allocation | AllocatedQuantity |
| 41 | SecuritiesQuantity | Amount | ∅ | Quantity expressed as an amount, eg,  in the investment fund business, a quantity of a financial instrument may be expressed as an amount of money. | CurrencyAndAmount | ∅ |
| 42 | SecuritiesQuantity | DenominatorRatio | ∅ | Ratio for which a denominator is specified. | UnderlyingRatio | UnderlyingQuantityDenominator |
| 43 | SecuritiesQuantity | NumeratorRatio | ∅ | Ratio for which a numerator is specified. | UnderlyingRatio | UnderlyingQuantityNumerator |
| 44 | SecuritiesQuantity | SecuritiesTradeExecution | ∅ | Trade for which settlement takes place. | SecuritiesTradeExecution | ExecutedTradeQuantity |
| 45 | SecuritiesQuantity | RelatedCorporateActionEvent | ∅ | Corporate action for which the offeror/issuer has specified a quantity of securities to purchase or redeem under the terms of the event. | CorporateActionEvent | SecuritiesQuantitySought |
| 46 | SecuritiesQuantity | CorporateActionElection | ∅ | Election process which selected a quantity of securities. | CorporateActionElection | Quantity |
| 47 | SecuritiesQuantity | TaxVoucher | ∅ | Tax voucher for which the calculation of holdings at record date took place. | TaxVoucher | RecordDateHolding |
| 48 | SecuritiesQuantity | RelatedBuyIn | ∅ | Buy-in process for which a compensation amount of securities is specified. | BuyIn | SecuritiesCompensation |
| 49 | SecuritiesQuantity | PreviousDayOrder | ∅ | Securities order which uses information on a day order quantity. | SecuritiesOrder | DayOrderQuantity |
| 50 | SecuritiesQuantity | Liquidity | ∅ | Liquidity information related to a quantity of a financial instrument. | Liquidity | Quantity |
| 51 | SecuritiesQuantity | Rate | ∅ | Quantity expressed as a percentage rate, eg,  in the investment fund business, a quantity of a financial instrument may be expressed as percentage of the investor's total holding. | PercentageRate | ∅ |
| 52 | SecuritiesQuantity | MinimumQuantityOrderParameters | ∅ | Securities order for which a minimum quantity to execute is specified. | SecuritiesOrderParameters | MinimumQuantity |
| 53 | SecuritiesQuantity | MaximumQuantityRelatedQuote | ∅ | Quote process for which a maximum quantity of securities is specified. | Quote | MaximumQuantity |
| 54 | SecuritiesQuantity | UnavailableQuantityBalance | ∅ | Securities balance which contains the unavailable quantity. | SecuritiesBalance | UnavailableQuantity |
| 55 | SecuritiesQuantity | MatchIncrementOrderParameters | ∅ | Securities order parameters for which a match increment quantity is provided. | SecuritiesOrderParameters | MatchIncrement |
| 56 | SecuritiesQuantity | RelatedIssuance | ∅ | Issuance for which a minimum subscription quantity of securities is specified. | Issuance | Minimum |
| 57 | SecuritiesQuantity | Pairoff | ∅ | Pair off process for which a quantity has been specified. | PairOff | PairedOffQuantity |
| 58 | SecuritiesQuantity | Issuance | ∅ | Issuance for which the nominal amount is specified. | Issuance | IssueNominalAmount |
| 59 | SecuritiesQuantity | IntermediateToUnderlyingDenominatorDistributionInformation | ∅ | Cash and securities distribution information for which an intermediate to underlying denominator quantity is specified. | SecuritiesAndCashDistribution | IntermediateToUnderlyingDenominator |
| 60 | SecuritiesQuantity | MaximumHoldingDistributionInformation | ∅ | Cash and securities distribution information for which a maximum holding quantity is specified. | SecuritiesAndCashDistribution | MaximumHolding |
| 61 | SecuritiesQuantity | MaximumExercisableQuantityDistributionInformation | ∅ | Cash and securities distribution information for which a maximum exercisable quantity is specified. | SecuritiesAndCashDistribution | MaximumExercisableQuantity |
| 62 | SecuritiesQuantity | MinimumExercisableQuantityDistributionInformation | ∅ | Cash and securities distribution information for which a minimum exercisable quantity is specified. | SecuritiesAndCashDistribution | MinimumExercisableQuantity |
| 63 | SecuritiesQuantity | DistributedToUnderlyingDenominatorDistributionInformation | ∅ | Cash and securities distribution information for which a distributed to underlying denominator quantity is specified. | SecuritiesAndCashDistribution | DistributedToUnderlyingDenominator |
| 64 | SecuritiesQuantity | IntermediateToUnderlyingNumeratorDistributionInformation | ∅ | Cash and securities distribution information for which an intermediate to underlying numerator quantity is specified. | SecuritiesAndCashDistribution | IntermediateToUnderlyingNumerator |
| 65 | SecuritiesQuantity | MinimumHoldingDistributionInformation | ∅ | Cash and securities distribution information for which a minimum holding quantity is specified. | SecuritiesAndCashDistribution | MinimumHolding |
| 66 | SecuritiesQuantity | DistributedToUnderlyingNumeratorDistributionInformation | ∅ | Cash and securities distribution information for which a distributed to underlying numerator quantity is specified. | SecuritiesAndCashDistribution | DistributedToUnderlyingNumerator |
| 67 | SecuritiesQuantity | MaximumHoldingRelatedSecuritiesDistribution | ∅ | Securities distribution for which a maximum holding quantity is provided. | SecuritiesDistribution | MaximumHolding |
| 68 | SecuritiesQuantity | IntermediateToUnderlyingNumeratorRelatedSecuritiesDistribution | ∅ | Securities distribution for which an intermediate to underlying numerator quantity is provided. | SecuritiesDistribution | IntermediateToUnderlyingNumerator |
| 69 | SecuritiesQuantity | IntermediateToUnderlyingDenominatorRelatedSecuritiesDistribution | ∅ | Securities distribution for which an intermediate to underlying denominator quantity is provided. | SecuritiesDistribution | IntermediateToUnderlyingDenominator |
| 70 | SecuritiesQuantity | DistributedToUnderlyingDenominatorRelatedSecuritiesDistribution | ∅ | Securities distribution for which a distributed to underlying denominator quantity is provided. | SecuritiesDistribution | DistributedToUnderlyingDenominator |
| 71 | SecuritiesQuantity | DistributedToUnderlyingNumeratorRelatedSecuritiesDistribution | ∅ | Securities distribution for which a distributed to underlying numerator quantity is provided. | SecuritiesDistribution | DistributedToUnderlyingNumerator |
| 72 | SecuritiesQuantity | MinimumHoldingRelatedSecuritiesDistribution | ∅ | Securities distribution for which a minimum holding quantity is provided. | SecuritiesDistribution | MinimumHolding |
| 73 | SecuritiesQuantity | MaximumTradedQuantityMarket | ∅ | Market for which a maximum traded quantity is specified. | TradingMarket | MaximumTradedNominalQuantity |
| 74 | SecuritiesQuantity | QuantityRelatedQuote | ∅ | Quote process for which a quantity of securities is specified. | Quote | Quantity |
| 75 | SecuritiesQuantity | MinimumQuantityRelatedQuote | ∅ | Quote process for which a minimum quantity of securities is specified. | Quote | MinimumQuantity |
| 76 | SecuritiesQuantity | NetAssetValueCalculation | ∅ | Net asset value calculation parameters. | NetAssetValueCalculation | SecuritiesQuantity |
| 77 | SecuritiesQuantity | SidePocket | ∅ | Side pocket for which a quantity is specified. | SidePocket | SidePocketQuantity |
| 78 | SecuritiesQuantity | Netting | ∅ | Netting process for which a net quantity of securities has been calculated. | Netting | NetQuantity |
| 79 | SecuritiesQuantity | RelatedOrderStatus | ∅ | Order status for which a remaining quantity is specified. | SecuritiesOrderStatus | RemainingQuantity |
| 80 | SecuritiesQuantity | SecuritiesOrderStatus | ∅ | Order status for which a cumulative quantity is specified. | SecuritiesOrderStatus | CumulativeQuantity |
| 81 | SecuritiesQuantity | RelatedTurnaroundSettlement | ∅ | Securities settlement process for which a turned quantity is specified. | SecuritiesSettlement | TurnedQuantity |
| 82 | SecuritiesQuantity | RelatedCashFlow | ∅ | Cash flow for which quantities are specified. | FundsCashFlow | CashFlowQuantity |
| 83 | SecuritiesQuantity | Position | ∅ | Position which contains the net quantity. | Position | NetQuantity |
| 84 | SecuritiesQuantity | MaximumQuantityBiddingConditions | ∅ | Bidding conditions for which a maximum quantity is specified. | BiddingConditions | MaximumQuantity |
| 85 | SecuritiesQuantity | FrontEndOddLotBiddingConditions | ∅ | Bidding conditions for which a front end odd lot is specified. | BiddingConditions | FrontEndOddLotQuantity |
| 86 | SecuritiesQuantity | MinimumQuantityBiddingConditions | ∅ | Bidding conditions for which a minimum quantity is specified. | BiddingConditions | MinimumQuantitySought |
| 87 | SecuritiesQuantity | RelatedCorporateActionProtectProcess | ∅ | Protect process which selected a quantity of securities. | CorporateActionProtectProcess | UncoveredProtectQuantity |
| 88 | SecuritiesQuantity | DigitalTokenUnit | ∅ | Quantity of digital tokens expressed as a number, for example, a number of blockchain tokens. | DecimalNumber | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `8cbba10ca914faa6cd02b2c759c1841163c8bf06d9816ce775251606aec98212`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000345 | FullBusinessModel!A1402:F1489 | 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489 | [src-000345 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](<../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md>) |
| src-000355 | FullBusinessModel!A4258:F4345 | 4258, 4259, 4260, 4261, 4262, 4263, 4264, 4265, 4266, 4267, 4268, 4269, 4270, 4271, 4272, 4273, 4274, 4275, 4276, 4277, 4278, 4279, 4280, 4281, 4282, 4283, 4284, 4285, 4286, 4287, 4288, 4289, 4290, 4291, 4292, 4293, 4294, 4295, 4296, 4297, 4298, 4299, 4300, 4301, 4302, 4303, 4304, 4305, 4306, 4307, 4308, 4309, 4310, 4311, 4312, 4313, 4314, 4315, 4316, 4317, 4318, 4319, 4320, 4321, 4322, 4323, 4324, 4325, 4326, 4327, 4328, 4329, 4330, 4331, 4332, 4333, 4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4343, 4344, 4345 | [src-000355 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md>) |
| src-000358 | FullBusinessModel!A1402:F1489 | 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489 | [src-000358 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md>) |
| src-000361 | FullBusinessModel!A1402:F1489 | 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489 | [src-000361 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md>) |
| src-000364 | FullBusinessModel!A4258:F4345 | 4258, 4259, 4260, 4261, 4262, 4263, 4264, 4265, 4266, 4267, 4268, 4269, 4270, 4271, 4272, 4273, 4274, 4275, 4276, 4277, 4278, 4279, 4280, 4281, 4282, 4283, 4284, 4285, 4286, 4287, 4288, 4289, 4290, 4291, 4292, 4293, 4294, 4295, 4296, 4297, 4298, 4299, 4300, 4301, 4302, 4303, 4304, 4305, 4306, 4307, 4308, 4309, 4310, 4311, 4312, 4313, 4314, 4315, 4316, 4317, 4318, 4319, 4320, 4321, 4322, 4323, 4324, 4325, 4326, 4327, 4328, 4329, 4330, 4331, 4332, 4333, 4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4343, 4344, 4345 | [src-000364 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md>) |
| src-000367 | FullBusinessModel!A4258:F4345 | 4258, 4259, 4260, 4261, 4262, 4263, 4264, 4265, 4266, 4267, 4268, 4269, 4270, 4271, 4272, 4273, 4274, 4275, 4276, 4277, 4278, 4279, 4280, 4281, 4282, 4283, 4284, 4285, 4286, 4287, 4288, 4289, 4290, 4291, 4292, 4293, 4294, 4295, 4296, 4297, 4298, 4299, 4300, 4301, 4302, 4303, 4304, 4305, 4306, 4307, 4308, 4309, 4310, 4311, 4312, 4313, 4314, 4315, 4316, 4317, 4318, 4319, 4320, 4321, 4322, 4323, 4324, 4325, 4326, 4327, 4328, 4329, 4330, 4331, 4332, 4333, 4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4343, 4344, 4345 | [src-000367 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md>) |
| src-000370 | FullBusinessModel!A1402:F1489 | 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489 | [src-000370 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md>) |
| src-000373 | FullBusinessModel!A1402:F1489 | 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489 | [src-000373 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md>) |
| src-000379 | FullBusinessModel!A1402:F1489 | 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489 | [src-000379 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000345 | field-type | E1403 | DecimalNumber | Not a component record in this worksheet |
| src-000345 | field-type | E1404 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000345 | field-type | E1405 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000345 | field-type | E1406 | InvestmentFundOrder | [InvestmentFundOrder](<bc-6aec42483ef15d38c88f.md>) |
| src-000345 | field-type | E1407 | UKTaxGroupUnitCode | Not a component record in this worksheet |
| src-000345 | field-type | E1408 | InvestmentFundOrderExecution | [InvestmentFundOrderExecution](<bc-227f2d44136fb326f809.md>) |
| src-000345 | field-type | E1409 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000345 | field-type | E1410 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000345 | field-type | E1411 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000345 | field-type | E1412 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000345 | field-type | E1413 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000345 | field-type | E1414 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000345 | field-type | E1415 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000345 | field-type | E1416 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000345 | field-type | E1417 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000345 | field-type | E1418 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000345 | field-type | E1419 | QuantityCode | Not a component record in this worksheet |
| src-000345 | field-type | E1420 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000345 | field-type | E1421 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000345 | field-type | E1422 | CorporateActionDistribution | [CorporateActionDistribution](<bc-f371fbd458438de6240f.md>) |
| src-000345 | field-type | E1423 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000345 | field-type | E1424 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000345 | field-type | E1425 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000345 | field-type | E1426 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000345 | field-type | E1427 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000345 | field-type | E1428 | CorporateActionSecuritiesEntitlement | [CorporateActionSecuritiesEntitlement](<bc-5cff81ce6e7bbfabfbf5.md>) |
| src-000345 | field-type | E1429 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000345 | field-type | E1430 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000345 | field-type | E1431 | Lottery | [Lottery](<bc-8676962b006118d93678.md>) |
| src-000345 | field-type | E1432 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000345 | field-type | E1433 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000345 | field-type | E1434 | SecuritiesTrade | [SecuritiesTrade](<bc-cacdabc7b3d47e9b7b24.md>) |
| src-000345 | field-type | E1435 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000345 | field-type | E1436 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000345 | field-type | E1437 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000345 | field-type | E1438 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000345 | field-type | E1439 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000345 | field-type | E1440 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000345 | field-type | E1441 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000345 | field-type | E1442 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E1443 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000345 | field-type | E1444 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000345 | field-type | E1445 | SecuritiesTradeExecution | [SecuritiesTradeExecution](<bc-854b1f66f9a7836895cf.md>) |
| src-000345 | field-type | E1446 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000345 | field-type | E1447 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000345 | field-type | E1448 | TaxVoucher | [TaxVoucher](<bc-6ed358f7b4b5fd0e83a1.md>) |
| src-000345 | field-type | E1449 | BuyIn | [BuyIn](<bc-5b3c24df7aa8aca3f795.md>) |
| src-000345 | field-type | E1450 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000345 | field-type | E1451 | Liquidity | [Liquidity](<bc-e58491436c12d922bc5f.md>) |
| src-000345 | field-type | E1452 | PercentageRate | Not a component record in this worksheet |
| src-000345 | field-type | E1453 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000345 | field-type | E1454 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000345 | field-type | E1455 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000345 | field-type | E1456 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000345 | field-type | E1457 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000345 | field-type | E1458 | PairOff | [PairOff](<bc-8b5c2deb20538dd935f7.md>) |
| src-000345 | field-type | E1459 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000345 | field-type | E1460 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000345 | field-type | E1461 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000345 | field-type | E1462 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000345 | field-type | E1463 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000345 | field-type | E1464 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000345 | field-type | E1465 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000345 | field-type | E1466 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000345 | field-type | E1467 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000345 | field-type | E1468 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000345 | field-type | E1469 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000345 | field-type | E1470 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000345 | field-type | E1471 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000345 | field-type | E1472 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000345 | field-type | E1473 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000345 | field-type | E1474 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000345 | field-type | E1475 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000345 | field-type | E1476 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000345 | field-type | E1477 | NetAssetValueCalculation | [NetAssetValueCalculation](<bc-b0ebfc4418fb9fb1bce3.md>) |
| src-000345 | field-type | E1478 | SidePocket | [SidePocket](<bc-19b0c48c5a47daa2e3bd.md>) |
| src-000345 | field-type | E1479 | Netting | [Netting](<bc-7d7a630fba8f626545ab.md>) |
| src-000345 | field-type | E1480 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000345 | field-type | E1481 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000345 | field-type | E1482 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000345 | field-type | E1483 | FundsCashFlow | [FundsCashFlow](<bc-04400270b3df0ca87f1e.md>) |
| src-000345 | field-type | E1484 | Position | [Position](<bc-48d203cb80c73aaee87b.md>) |
| src-000345 | field-type | E1485 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000345 | field-type | E1486 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000345 | field-type | E1487 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000345 | field-type | E1488 | CorporateActionProtectProcess | [CorporateActionProtectProcess](<bc-8e4e963671c2ec477553.md>) |
| src-000345 | field-type | E1489 | DecimalNumber | Not a component record in this worksheet |
| src-000355 | field-type | E4259 | DecimalNumber | Not a component record in this worksheet |
| src-000355 | field-type | E4260 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000355 | field-type | E4261 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000355 | field-type | E4262 | InvestmentFundOrder | [InvestmentFundOrder](<bc-6aec42483ef15d38c88f.md>) |
| src-000355 | field-type | E4263 | UKTaxGroupUnitCode | Not a component record in this worksheet |
| src-000355 | field-type | E4264 | InvestmentFundOrderExecution | [InvestmentFundOrderExecution](<bc-227f2d44136fb326f809.md>) |
| src-000355 | field-type | E4265 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000355 | field-type | E4266 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000355 | field-type | E4267 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000355 | field-type | E4268 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000355 | field-type | E4269 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000355 | field-type | E4270 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000355 | field-type | E4271 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000355 | field-type | E4272 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000355 | field-type | E4273 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000355 | field-type | E4274 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000355 | field-type | E4275 | QuantityCode | Not a component record in this worksheet |
| src-000355 | field-type | E4276 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000355 | field-type | E4277 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000355 | field-type | E4278 | CorporateActionDistribution | [CorporateActionDistribution](<bc-f371fbd458438de6240f.md>) |
| src-000355 | field-type | E4279 | CorporateActionEvent | [CorporateActionEvent](<bc-9a03dfa9ef86b81a3985.md>) |
| src-000355 | field-type | E4280 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000355 | field-type | E4281 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000355 | field-type | E4282 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000355 | field-type | E4283 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000355 | field-type | E4284 | CorporateActionSecuritiesEntitlement | [CorporateActionSecuritiesEntitlement](<bc-5cff81ce6e7bbfabfbf5.md>) |
| src-000355 | field-type | E4285 | CorporateActionEvent | [CorporateActionEvent](<bc-9a03dfa9ef86b81a3985.md>) |
| src-000355 | field-type | E4286 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000355 | field-type | E4287 | Lottery | [Lottery](<bc-8676962b006118d93678.md>) |
| src-000355 | field-type | E4288 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000355 | field-type | E4289 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000355 | field-type | E4290 | SecuritiesTrade | [SecuritiesTrade](<bc-cacdabc7b3d47e9b7b24.md>) |
| src-000355 | field-type | E4291 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000355 | field-type | E4292 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000355 | field-type | E4293 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000355 | field-type | E4294 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000355 | field-type | E4295 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000355 | field-type | E4296 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000355 | field-type | E4297 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000355 | field-type | E4298 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E4299 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000355 | field-type | E4300 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000355 | field-type | E4301 | SecuritiesTradeExecution | [SecuritiesTradeExecution](<bc-854b1f66f9a7836895cf.md>) |
| src-000355 | field-type | E4302 | CorporateActionEvent | [CorporateActionEvent](<bc-9a03dfa9ef86b81a3985.md>) |
| src-000355 | field-type | E4303 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000355 | field-type | E4304 | TaxVoucher | [TaxVoucher](<bc-6ed358f7b4b5fd0e83a1.md>) |
| src-000355 | field-type | E4305 | BuyIn | [BuyIn](<bc-5b3c24df7aa8aca3f795.md>) |
| src-000355 | field-type | E4306 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000355 | field-type | E4307 | Liquidity | [Liquidity](<bc-e58491436c12d922bc5f.md>) |
| src-000355 | field-type | E4308 | PercentageRate | Not a component record in this worksheet |
| src-000355 | field-type | E4309 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000355 | field-type | E4310 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000355 | field-type | E4311 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000355 | field-type | E4312 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000355 | field-type | E4313 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000355 | field-type | E4314 | PairOff | [PairOff](<bc-8b5c2deb20538dd935f7.md>) |
| src-000355 | field-type | E4315 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000355 | field-type | E4316 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000355 | field-type | E4317 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000355 | field-type | E4318 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000355 | field-type | E4319 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000355 | field-type | E4320 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000355 | field-type | E4321 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000355 | field-type | E4322 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000355 | field-type | E4323 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000355 | field-type | E4324 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000355 | field-type | E4325 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000355 | field-type | E4326 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000355 | field-type | E4327 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000355 | field-type | E4328 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000355 | field-type | E4329 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000355 | field-type | E4330 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000355 | field-type | E4331 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000355 | field-type | E4332 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000355 | field-type | E4333 | NetAssetValueCalculation | [NetAssetValueCalculation](<bc-b0ebfc4418fb9fb1bce3.md>) |
| src-000355 | field-type | E4334 | SidePocket | [SidePocket](<bc-19b0c48c5a47daa2e3bd.md>) |
| src-000355 | field-type | E4335 | Netting | [Netting](<bc-7d7a630fba8f626545ab.md>) |
| src-000355 | field-type | E4336 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000355 | field-type | E4337 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000355 | field-type | E4338 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000355 | field-type | E4339 | FundsCashFlow | [FundsCashFlow](<bc-04400270b3df0ca87f1e.md>) |
| src-000355 | field-type | E4340 | Position | [Position](<bc-48d203cb80c73aaee87b.md>) |
| src-000355 | field-type | E4341 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000355 | field-type | E4342 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000355 | field-type | E4343 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000355 | field-type | E4344 | CorporateActionProtectProcess | [CorporateActionProtectProcess](<bc-8e4e963671c2ec477553.md>) |
| src-000355 | field-type | E4345 | DecimalNumber | Not a component record in this worksheet |
| src-000358 | field-type | E1403 | DecimalNumber | Not a component record in this worksheet |
| src-000358 | field-type | E1404 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000358 | field-type | E1405 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000358 | field-type | E1406 | InvestmentFundOrder | [InvestmentFundOrder](<bc-6aec42483ef15d38c88f.md>) |
| src-000358 | field-type | E1407 | UKTaxGroupUnitCode | Not a component record in this worksheet |
| src-000358 | field-type | E1408 | InvestmentFundOrderExecution | [InvestmentFundOrderExecution](<bc-227f2d44136fb326f809.md>) |
| src-000358 | field-type | E1409 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000358 | field-type | E1410 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000358 | field-type | E1411 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000358 | field-type | E1412 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000358 | field-type | E1413 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000358 | field-type | E1414 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000358 | field-type | E1415 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000358 | field-type | E1416 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000358 | field-type | E1417 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000358 | field-type | E1418 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000358 | field-type | E1419 | QuantityCode | Not a component record in this worksheet |
| src-000358 | field-type | E1420 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000358 | field-type | E1421 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000358 | field-type | E1422 | CorporateActionDistribution | [CorporateActionDistribution](<bc-f371fbd458438de6240f.md>) |
| src-000358 | field-type | E1423 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000358 | field-type | E1424 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000358 | field-type | E1425 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000358 | field-type | E1426 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000358 | field-type | E1427 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000358 | field-type | E1428 | CorporateActionSecuritiesEntitlement | [CorporateActionSecuritiesEntitlement](<bc-5cff81ce6e7bbfabfbf5.md>) |
| src-000358 | field-type | E1429 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000358 | field-type | E1430 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000358 | field-type | E1431 | Lottery | [Lottery](<bc-8676962b006118d93678.md>) |
| src-000358 | field-type | E1432 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000358 | field-type | E1433 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000358 | field-type | E1434 | SecuritiesTrade | [SecuritiesTrade](<bc-cacdabc7b3d47e9b7b24.md>) |
| src-000358 | field-type | E1435 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000358 | field-type | E1436 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000358 | field-type | E1437 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000358 | field-type | E1438 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000358 | field-type | E1439 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000358 | field-type | E1440 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000358 | field-type | E1441 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000358 | field-type | E1442 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E1443 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000358 | field-type | E1444 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000358 | field-type | E1445 | SecuritiesTradeExecution | [SecuritiesTradeExecution](<bc-854b1f66f9a7836895cf.md>) |
| src-000358 | field-type | E1446 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000358 | field-type | E1447 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000358 | field-type | E1448 | TaxVoucher | [TaxVoucher](<bc-6ed358f7b4b5fd0e83a1.md>) |
| src-000358 | field-type | E1449 | BuyIn | [BuyIn](<bc-5b3c24df7aa8aca3f795.md>) |
| src-000358 | field-type | E1450 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000358 | field-type | E1451 | Liquidity | [Liquidity](<bc-e58491436c12d922bc5f.md>) |
| src-000358 | field-type | E1452 | PercentageRate | Not a component record in this worksheet |
| src-000358 | field-type | E1453 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000358 | field-type | E1454 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000358 | field-type | E1455 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000358 | field-type | E1456 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000358 | field-type | E1457 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000358 | field-type | E1458 | PairOff | [PairOff](<bc-8b5c2deb20538dd935f7.md>) |
| src-000358 | field-type | E1459 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000358 | field-type | E1460 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000358 | field-type | E1461 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000358 | field-type | E1462 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000358 | field-type | E1463 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000358 | field-type | E1464 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000358 | field-type | E1465 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000358 | field-type | E1466 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000358 | field-type | E1467 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000358 | field-type | E1468 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000358 | field-type | E1469 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000358 | field-type | E1470 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000358 | field-type | E1471 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000358 | field-type | E1472 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000358 | field-type | E1473 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000358 | field-type | E1474 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000358 | field-type | E1475 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000358 | field-type | E1476 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000358 | field-type | E1477 | NetAssetValueCalculation | [NetAssetValueCalculation](<bc-b0ebfc4418fb9fb1bce3.md>) |
| src-000358 | field-type | E1478 | SidePocket | [SidePocket](<bc-19b0c48c5a47daa2e3bd.md>) |
| src-000358 | field-type | E1479 | Netting | [Netting](<bc-7d7a630fba8f626545ab.md>) |
| src-000358 | field-type | E1480 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000358 | field-type | E1481 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000358 | field-type | E1482 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000358 | field-type | E1483 | FundsCashFlow | [FundsCashFlow](<bc-04400270b3df0ca87f1e.md>) |
| src-000358 | field-type | E1484 | Position | [Position](<bc-48d203cb80c73aaee87b.md>) |
| src-000358 | field-type | E1485 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000358 | field-type | E1486 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000358 | field-type | E1487 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000358 | field-type | E1488 | CorporateActionProtectProcess | [CorporateActionProtectProcess](<bc-8e4e963671c2ec477553.md>) |
| src-000358 | field-type | E1489 | DecimalNumber | Not a component record in this worksheet |
| src-000361 | field-type | E1403 | DecimalNumber | Not a component record in this worksheet |
| src-000361 | field-type | E1404 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000361 | field-type | E1405 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000361 | field-type | E1406 | InvestmentFundOrder | [InvestmentFundOrder](<bc-6aec42483ef15d38c88f.md>) |
| src-000361 | field-type | E1407 | UKTaxGroupUnitCode | Not a component record in this worksheet |
| src-000361 | field-type | E1408 | InvestmentFundOrderExecution | [InvestmentFundOrderExecution](<bc-227f2d44136fb326f809.md>) |
| src-000361 | field-type | E1409 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000361 | field-type | E1410 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000361 | field-type | E1411 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000361 | field-type | E1412 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000361 | field-type | E1413 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000361 | field-type | E1414 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000361 | field-type | E1415 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000361 | field-type | E1416 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000361 | field-type | E1417 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000361 | field-type | E1418 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000361 | field-type | E1419 | QuantityCode | Not a component record in this worksheet |
| src-000361 | field-type | E1420 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000361 | field-type | E1421 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000361 | field-type | E1422 | CorporateActionDistribution | [CorporateActionDistribution](<bc-f371fbd458438de6240f.md>) |
| src-000361 | field-type | E1423 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000361 | field-type | E1424 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000361 | field-type | E1425 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000361 | field-type | E1426 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000361 | field-type | E1427 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000361 | field-type | E1428 | CorporateActionSecuritiesEntitlement | [CorporateActionSecuritiesEntitlement](<bc-5cff81ce6e7bbfabfbf5.md>) |
| src-000361 | field-type | E1429 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000361 | field-type | E1430 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000361 | field-type | E1431 | Lottery | [Lottery](<bc-8676962b006118d93678.md>) |
| src-000361 | field-type | E1432 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000361 | field-type | E1433 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000361 | field-type | E1434 | SecuritiesTrade | [SecuritiesTrade](<bc-cacdabc7b3d47e9b7b24.md>) |
| src-000361 | field-type | E1435 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000361 | field-type | E1436 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000361 | field-type | E1437 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000361 | field-type | E1438 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000361 | field-type | E1439 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000361 | field-type | E1440 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000361 | field-type | E1441 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000361 | field-type | E1442 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E1443 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000361 | field-type | E1444 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000361 | field-type | E1445 | SecuritiesTradeExecution | [SecuritiesTradeExecution](<bc-854b1f66f9a7836895cf.md>) |
| src-000361 | field-type | E1446 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000361 | field-type | E1447 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000361 | field-type | E1448 | TaxVoucher | [TaxVoucher](<bc-6ed358f7b4b5fd0e83a1.md>) |
| src-000361 | field-type | E1449 | BuyIn | [BuyIn](<bc-5b3c24df7aa8aca3f795.md>) |
| src-000361 | field-type | E1450 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000361 | field-type | E1451 | Liquidity | [Liquidity](<bc-e58491436c12d922bc5f.md>) |
| src-000361 | field-type | E1452 | PercentageRate | Not a component record in this worksheet |
| src-000361 | field-type | E1453 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000361 | field-type | E1454 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000361 | field-type | E1455 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000361 | field-type | E1456 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000361 | field-type | E1457 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000361 | field-type | E1458 | PairOff | [PairOff](<bc-8b5c2deb20538dd935f7.md>) |
| src-000361 | field-type | E1459 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000361 | field-type | E1460 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000361 | field-type | E1461 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000361 | field-type | E1462 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000361 | field-type | E1463 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000361 | field-type | E1464 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000361 | field-type | E1465 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000361 | field-type | E1466 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000361 | field-type | E1467 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000361 | field-type | E1468 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000361 | field-type | E1469 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000361 | field-type | E1470 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000361 | field-type | E1471 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000361 | field-type | E1472 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000361 | field-type | E1473 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000361 | field-type | E1474 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000361 | field-type | E1475 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000361 | field-type | E1476 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000361 | field-type | E1477 | NetAssetValueCalculation | [NetAssetValueCalculation](<bc-b0ebfc4418fb9fb1bce3.md>) |
| src-000361 | field-type | E1478 | SidePocket | [SidePocket](<bc-19b0c48c5a47daa2e3bd.md>) |
| src-000361 | field-type | E1479 | Netting | [Netting](<bc-7d7a630fba8f626545ab.md>) |
| src-000361 | field-type | E1480 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000361 | field-type | E1481 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000361 | field-type | E1482 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000361 | field-type | E1483 | FundsCashFlow | [FundsCashFlow](<bc-04400270b3df0ca87f1e.md>) |
| src-000361 | field-type | E1484 | Position | [Position](<bc-48d203cb80c73aaee87b.md>) |
| src-000361 | field-type | E1485 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000361 | field-type | E1486 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000361 | field-type | E1487 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000361 | field-type | E1488 | CorporateActionProtectProcess | [CorporateActionProtectProcess](<bc-8e4e963671c2ec477553.md>) |
| src-000361 | field-type | E1489 | DecimalNumber | Not a component record in this worksheet |
| src-000364 | field-type | E4259 | DecimalNumber | Not a component record in this worksheet |
| src-000364 | field-type | E4260 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000364 | field-type | E4261 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000364 | field-type | E4262 | InvestmentFundOrder | [InvestmentFundOrder](<bc-6aec42483ef15d38c88f.md>) |
| src-000364 | field-type | E4263 | UKTaxGroupUnitCode | Not a component record in this worksheet |
| src-000364 | field-type | E4264 | InvestmentFundOrderExecution | [InvestmentFundOrderExecution](<bc-227f2d44136fb326f809.md>) |
| src-000364 | field-type | E4265 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000364 | field-type | E4266 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000364 | field-type | E4267 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000364 | field-type | E4268 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000364 | field-type | E4269 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000364 | field-type | E4270 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000364 | field-type | E4271 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000364 | field-type | E4272 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000364 | field-type | E4273 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000364 | field-type | E4274 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000364 | field-type | E4275 | QuantityCode | Not a component record in this worksheet |
| src-000364 | field-type | E4276 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000364 | field-type | E4277 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000364 | field-type | E4278 | CorporateActionDistribution | [CorporateActionDistribution](<bc-f371fbd458438de6240f.md>) |
| src-000364 | field-type | E4279 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000364 | field-type | E4280 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000364 | field-type | E4281 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000364 | field-type | E4282 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000364 | field-type | E4283 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000364 | field-type | E4284 | CorporateActionSecuritiesEntitlement | [CorporateActionSecuritiesEntitlement](<bc-5cff81ce6e7bbfabfbf5.md>) |
| src-000364 | field-type | E4285 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000364 | field-type | E4286 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000364 | field-type | E4287 | Lottery | [Lottery](<bc-8676962b006118d93678.md>) |
| src-000364 | field-type | E4288 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000364 | field-type | E4289 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000364 | field-type | E4290 | SecuritiesTrade | [SecuritiesTrade](<bc-cacdabc7b3d47e9b7b24.md>) |
| src-000364 | field-type | E4291 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000364 | field-type | E4292 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000364 | field-type | E4293 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000364 | field-type | E4294 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000364 | field-type | E4295 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000364 | field-type | E4296 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000364 | field-type | E4297 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000364 | field-type | E4298 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E4299 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000364 | field-type | E4300 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000364 | field-type | E4301 | SecuritiesTradeExecution | [SecuritiesTradeExecution](<bc-854b1f66f9a7836895cf.md>) |
| src-000364 | field-type | E4302 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000364 | field-type | E4303 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000364 | field-type | E4304 | TaxVoucher | [TaxVoucher](<bc-6ed358f7b4b5fd0e83a1.md>) |
| src-000364 | field-type | E4305 | BuyIn | [BuyIn](<bc-5b3c24df7aa8aca3f795.md>) |
| src-000364 | field-type | E4306 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000364 | field-type | E4307 | Liquidity | [Liquidity](<bc-e58491436c12d922bc5f.md>) |
| src-000364 | field-type | E4308 | PercentageRate | Not a component record in this worksheet |
| src-000364 | field-type | E4309 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000364 | field-type | E4310 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000364 | field-type | E4311 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000364 | field-type | E4312 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000364 | field-type | E4313 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000364 | field-type | E4314 | PairOff | [PairOff](<bc-8b5c2deb20538dd935f7.md>) |
| src-000364 | field-type | E4315 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000364 | field-type | E4316 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000364 | field-type | E4317 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000364 | field-type | E4318 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000364 | field-type | E4319 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000364 | field-type | E4320 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000364 | field-type | E4321 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000364 | field-type | E4322 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000364 | field-type | E4323 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000364 | field-type | E4324 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000364 | field-type | E4325 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000364 | field-type | E4326 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000364 | field-type | E4327 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000364 | field-type | E4328 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000364 | field-type | E4329 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000364 | field-type | E4330 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000364 | field-type | E4331 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000364 | field-type | E4332 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000364 | field-type | E4333 | NetAssetValueCalculation | [NetAssetValueCalculation](<bc-b0ebfc4418fb9fb1bce3.md>) |
| src-000364 | field-type | E4334 | SidePocket | [SidePocket](<bc-19b0c48c5a47daa2e3bd.md>) |
| src-000364 | field-type | E4335 | Netting | [Netting](<bc-7d7a630fba8f626545ab.md>) |
| src-000364 | field-type | E4336 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000364 | field-type | E4337 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000364 | field-type | E4338 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000364 | field-type | E4339 | FundsCashFlow | [FundsCashFlow](<bc-04400270b3df0ca87f1e.md>) |
| src-000364 | field-type | E4340 | Position | [Position](<bc-48d203cb80c73aaee87b.md>) |
| src-000364 | field-type | E4341 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000364 | field-type | E4342 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000364 | field-type | E4343 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000364 | field-type | E4344 | CorporateActionProtectProcess | [CorporateActionProtectProcess](<bc-8e4e963671c2ec477553.md>) |
| src-000364 | field-type | E4345 | DecimalNumber | Not a component record in this worksheet |
| src-000367 | field-type | E4259 | DecimalNumber | Not a component record in this worksheet |
| src-000367 | field-type | E4260 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000367 | field-type | E4261 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000367 | field-type | E4262 | InvestmentFundOrder | [InvestmentFundOrder](<bc-6aec42483ef15d38c88f.md>) |
| src-000367 | field-type | E4263 | UKTaxGroupUnitCode | Not a component record in this worksheet |
| src-000367 | field-type | E4264 | InvestmentFundOrderExecution | [InvestmentFundOrderExecution](<bc-227f2d44136fb326f809.md>) |
| src-000367 | field-type | E4265 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000367 | field-type | E4266 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000367 | field-type | E4267 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000367 | field-type | E4268 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000367 | field-type | E4269 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000367 | field-type | E4270 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000367 | field-type | E4271 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000367 | field-type | E4272 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000367 | field-type | E4273 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000367 | field-type | E4274 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000367 | field-type | E4275 | QuantityCode | Not a component record in this worksheet |
| src-000367 | field-type | E4276 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000367 | field-type | E4277 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000367 | field-type | E4278 | CorporateActionDistribution | [CorporateActionDistribution](<bc-f371fbd458438de6240f.md>) |
| src-000367 | field-type | E4279 | CorporateActionEvent | [CorporateActionEvent](<bc-9a03dfa9ef86b81a3985.md>) |
| src-000367 | field-type | E4280 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000367 | field-type | E4281 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000367 | field-type | E4282 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000367 | field-type | E4283 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000367 | field-type | E4284 | CorporateActionSecuritiesEntitlement | [CorporateActionSecuritiesEntitlement](<bc-5cff81ce6e7bbfabfbf5.md>) |
| src-000367 | field-type | E4285 | CorporateActionEvent | [CorporateActionEvent](<bc-9a03dfa9ef86b81a3985.md>) |
| src-000367 | field-type | E4286 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000367 | field-type | E4287 | Lottery | [Lottery](<bc-8676962b006118d93678.md>) |
| src-000367 | field-type | E4288 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000367 | field-type | E4289 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000367 | field-type | E4290 | SecuritiesTrade | [SecuritiesTrade](<bc-cacdabc7b3d47e9b7b24.md>) |
| src-000367 | field-type | E4291 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000367 | field-type | E4292 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000367 | field-type | E4293 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000367 | field-type | E4294 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000367 | field-type | E4295 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000367 | field-type | E4296 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000367 | field-type | E4297 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000367 | field-type | E4298 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E4299 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000367 | field-type | E4300 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000367 | field-type | E4301 | SecuritiesTradeExecution | [SecuritiesTradeExecution](<bc-854b1f66f9a7836895cf.md>) |
| src-000367 | field-type | E4302 | CorporateActionEvent | [CorporateActionEvent](<bc-9a03dfa9ef86b81a3985.md>) |
| src-000367 | field-type | E4303 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000367 | field-type | E4304 | TaxVoucher | [TaxVoucher](<bc-6ed358f7b4b5fd0e83a1.md>) |
| src-000367 | field-type | E4305 | BuyIn | [BuyIn](<bc-5b3c24df7aa8aca3f795.md>) |
| src-000367 | field-type | E4306 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000367 | field-type | E4307 | Liquidity | [Liquidity](<bc-e58491436c12d922bc5f.md>) |
| src-000367 | field-type | E4308 | PercentageRate | Not a component record in this worksheet |
| src-000367 | field-type | E4309 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000367 | field-type | E4310 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000367 | field-type | E4311 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000367 | field-type | E4312 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000367 | field-type | E4313 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000367 | field-type | E4314 | PairOff | [PairOff](<bc-8b5c2deb20538dd935f7.md>) |
| src-000367 | field-type | E4315 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000367 | field-type | E4316 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000367 | field-type | E4317 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000367 | field-type | E4318 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000367 | field-type | E4319 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000367 | field-type | E4320 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000367 | field-type | E4321 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000367 | field-type | E4322 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000367 | field-type | E4323 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000367 | field-type | E4324 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000367 | field-type | E4325 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000367 | field-type | E4326 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000367 | field-type | E4327 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000367 | field-type | E4328 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000367 | field-type | E4329 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000367 | field-type | E4330 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000367 | field-type | E4331 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000367 | field-type | E4332 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000367 | field-type | E4333 | NetAssetValueCalculation | [NetAssetValueCalculation](<bc-b0ebfc4418fb9fb1bce3.md>) |
| src-000367 | field-type | E4334 | SidePocket | [SidePocket](<bc-19b0c48c5a47daa2e3bd.md>) |
| src-000367 | field-type | E4335 | Netting | [Netting](<bc-7d7a630fba8f626545ab.md>) |
| src-000367 | field-type | E4336 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000367 | field-type | E4337 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000367 | field-type | E4338 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000367 | field-type | E4339 | FundsCashFlow | [FundsCashFlow](<bc-04400270b3df0ca87f1e.md>) |
| src-000367 | field-type | E4340 | Position | [Position](<bc-48d203cb80c73aaee87b.md>) |
| src-000367 | field-type | E4341 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000367 | field-type | E4342 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000367 | field-type | E4343 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000367 | field-type | E4344 | CorporateActionProtectProcess | [CorporateActionProtectProcess](<bc-8e4e963671c2ec477553.md>) |
| src-000367 | field-type | E4345 | DecimalNumber | Not a component record in this worksheet |
| src-000370 | field-type | E1403 | DecimalNumber | Not a component record in this worksheet |
| src-000370 | field-type | E1404 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000370 | field-type | E1405 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000370 | field-type | E1406 | InvestmentFundOrder | [InvestmentFundOrder](<bc-6aec42483ef15d38c88f.md>) |
| src-000370 | field-type | E1407 | UKTaxGroupUnitCode | Not a component record in this worksheet |
| src-000370 | field-type | E1408 | InvestmentFundOrderExecution | [InvestmentFundOrderExecution](<bc-227f2d44136fb326f809.md>) |
| src-000370 | field-type | E1409 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000370 | field-type | E1410 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000370 | field-type | E1411 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000370 | field-type | E1412 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000370 | field-type | E1413 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000370 | field-type | E1414 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000370 | field-type | E1415 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000370 | field-type | E1416 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000370 | field-type | E1417 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000370 | field-type | E1418 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000370 | field-type | E1419 | QuantityCode | Not a component record in this worksheet |
| src-000370 | field-type | E1420 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000370 | field-type | E1421 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000370 | field-type | E1422 | CorporateActionDistribution | [CorporateActionDistribution](<bc-f371fbd458438de6240f.md>) |
| src-000370 | field-type | E1423 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000370 | field-type | E1424 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000370 | field-type | E1425 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000370 | field-type | E1426 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000370 | field-type | E1427 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000370 | field-type | E1428 | CorporateActionSecuritiesEntitlement | [CorporateActionSecuritiesEntitlement](<bc-5cff81ce6e7bbfabfbf5.md>) |
| src-000370 | field-type | E1429 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000370 | field-type | E1430 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000370 | field-type | E1431 | Lottery | [Lottery](<bc-8676962b006118d93678.md>) |
| src-000370 | field-type | E1432 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000370 | field-type | E1433 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000370 | field-type | E1434 | SecuritiesTrade | [SecuritiesTrade](<bc-cacdabc7b3d47e9b7b24.md>) |
| src-000370 | field-type | E1435 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000370 | field-type | E1436 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000370 | field-type | E1437 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000370 | field-type | E1438 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000370 | field-type | E1439 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000370 | field-type | E1440 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000370 | field-type | E1441 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000370 | field-type | E1442 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E1443 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000370 | field-type | E1444 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000370 | field-type | E1445 | SecuritiesTradeExecution | [SecuritiesTradeExecution](<bc-854b1f66f9a7836895cf.md>) |
| src-000370 | field-type | E1446 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000370 | field-type | E1447 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000370 | field-type | E1448 | TaxVoucher | [TaxVoucher](<bc-6ed358f7b4b5fd0e83a1.md>) |
| src-000370 | field-type | E1449 | BuyIn | [BuyIn](<bc-5b3c24df7aa8aca3f795.md>) |
| src-000370 | field-type | E1450 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000370 | field-type | E1451 | Liquidity | [Liquidity](<bc-e58491436c12d922bc5f.md>) |
| src-000370 | field-type | E1452 | PercentageRate | Not a component record in this worksheet |
| src-000370 | field-type | E1453 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000370 | field-type | E1454 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000370 | field-type | E1455 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000370 | field-type | E1456 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000370 | field-type | E1457 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000370 | field-type | E1458 | PairOff | [PairOff](<bc-8b5c2deb20538dd935f7.md>) |
| src-000370 | field-type | E1459 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000370 | field-type | E1460 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000370 | field-type | E1461 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000370 | field-type | E1462 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000370 | field-type | E1463 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000370 | field-type | E1464 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000370 | field-type | E1465 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000370 | field-type | E1466 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000370 | field-type | E1467 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000370 | field-type | E1468 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000370 | field-type | E1469 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000370 | field-type | E1470 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000370 | field-type | E1471 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000370 | field-type | E1472 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000370 | field-type | E1473 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000370 | field-type | E1474 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000370 | field-type | E1475 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000370 | field-type | E1476 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000370 | field-type | E1477 | NetAssetValueCalculation | [NetAssetValueCalculation](<bc-b0ebfc4418fb9fb1bce3.md>) |
| src-000370 | field-type | E1478 | SidePocket | [SidePocket](<bc-19b0c48c5a47daa2e3bd.md>) |
| src-000370 | field-type | E1479 | Netting | [Netting](<bc-7d7a630fba8f626545ab.md>) |
| src-000370 | field-type | E1480 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000370 | field-type | E1481 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000370 | field-type | E1482 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000370 | field-type | E1483 | FundsCashFlow | [FundsCashFlow](<bc-04400270b3df0ca87f1e.md>) |
| src-000370 | field-type | E1484 | Position | [Position](<bc-48d203cb80c73aaee87b.md>) |
| src-000370 | field-type | E1485 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000370 | field-type | E1486 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000370 | field-type | E1487 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000370 | field-type | E1488 | CorporateActionProtectProcess | [CorporateActionProtectProcess](<bc-8e4e963671c2ec477553.md>) |
| src-000370 | field-type | E1489 | DecimalNumber | Not a component record in this worksheet |
| src-000373 | field-type | E1403 | DecimalNumber | Not a component record in this worksheet |
| src-000373 | field-type | E1404 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000373 | field-type | E1405 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000373 | field-type | E1406 | InvestmentFundOrder | [InvestmentFundOrder](<bc-6aec42483ef15d38c88f.md>) |
| src-000373 | field-type | E1407 | UKTaxGroupUnitCode | Not a component record in this worksheet |
| src-000373 | field-type | E1408 | InvestmentFundOrderExecution | [InvestmentFundOrderExecution](<bc-227f2d44136fb326f809.md>) |
| src-000373 | field-type | E1409 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000373 | field-type | E1410 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000373 | field-type | E1411 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000373 | field-type | E1412 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000373 | field-type | E1413 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000373 | field-type | E1414 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000373 | field-type | E1415 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000373 | field-type | E1416 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000373 | field-type | E1417 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000373 | field-type | E1418 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000373 | field-type | E1419 | QuantityCode | Not a component record in this worksheet |
| src-000373 | field-type | E1420 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000373 | field-type | E1421 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000373 | field-type | E1422 | CorporateActionDistribution | [CorporateActionDistribution](<bc-f371fbd458438de6240f.md>) |
| src-000373 | field-type | E1423 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000373 | field-type | E1424 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000373 | field-type | E1425 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000373 | field-type | E1426 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000373 | field-type | E1427 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000373 | field-type | E1428 | CorporateActionSecuritiesEntitlement | [CorporateActionSecuritiesEntitlement](<bc-5cff81ce6e7bbfabfbf5.md>) |
| src-000373 | field-type | E1429 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000373 | field-type | E1430 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000373 | field-type | E1431 | Lottery | [Lottery](<bc-8676962b006118d93678.md>) |
| src-000373 | field-type | E1432 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000373 | field-type | E1433 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000373 | field-type | E1434 | SecuritiesTrade | [SecuritiesTrade](<bc-cacdabc7b3d47e9b7b24.md>) |
| src-000373 | field-type | E1435 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000373 | field-type | E1436 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000373 | field-type | E1437 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000373 | field-type | E1438 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000373 | field-type | E1439 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000373 | field-type | E1440 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000373 | field-type | E1441 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000373 | field-type | E1442 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E1443 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000373 | field-type | E1444 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000373 | field-type | E1445 | SecuritiesTradeExecution | [SecuritiesTradeExecution](<bc-854b1f66f9a7836895cf.md>) |
| src-000373 | field-type | E1446 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000373 | field-type | E1447 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000373 | field-type | E1448 | TaxVoucher | [TaxVoucher](<bc-6ed358f7b4b5fd0e83a1.md>) |
| src-000373 | field-type | E1449 | BuyIn | [BuyIn](<bc-5b3c24df7aa8aca3f795.md>) |
| src-000373 | field-type | E1450 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000373 | field-type | E1451 | Liquidity | [Liquidity](<bc-e58491436c12d922bc5f.md>) |
| src-000373 | field-type | E1452 | PercentageRate | Not a component record in this worksheet |
| src-000373 | field-type | E1453 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000373 | field-type | E1454 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000373 | field-type | E1455 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000373 | field-type | E1456 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000373 | field-type | E1457 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000373 | field-type | E1458 | PairOff | [PairOff](<bc-8b5c2deb20538dd935f7.md>) |
| src-000373 | field-type | E1459 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000373 | field-type | E1460 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000373 | field-type | E1461 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000373 | field-type | E1462 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000373 | field-type | E1463 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000373 | field-type | E1464 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000373 | field-type | E1465 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000373 | field-type | E1466 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000373 | field-type | E1467 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000373 | field-type | E1468 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000373 | field-type | E1469 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000373 | field-type | E1470 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000373 | field-type | E1471 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000373 | field-type | E1472 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000373 | field-type | E1473 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000373 | field-type | E1474 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000373 | field-type | E1475 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000373 | field-type | E1476 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000373 | field-type | E1477 | NetAssetValueCalculation | [NetAssetValueCalculation](<bc-b0ebfc4418fb9fb1bce3.md>) |
| src-000373 | field-type | E1478 | SidePocket | [SidePocket](<bc-19b0c48c5a47daa2e3bd.md>) |
| src-000373 | field-type | E1479 | Netting | [Netting](<bc-7d7a630fba8f626545ab.md>) |
| src-000373 | field-type | E1480 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000373 | field-type | E1481 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000373 | field-type | E1482 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000373 | field-type | E1483 | FundsCashFlow | [FundsCashFlow](<bc-04400270b3df0ca87f1e.md>) |
| src-000373 | field-type | E1484 | Position | [Position](<bc-48d203cb80c73aaee87b.md>) |
| src-000373 | field-type | E1485 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000373 | field-type | E1486 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000373 | field-type | E1487 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000373 | field-type | E1488 | CorporateActionProtectProcess | [CorporateActionProtectProcess](<bc-8e4e963671c2ec477553.md>) |
| src-000373 | field-type | E1489 | DecimalNumber | Not a component record in this worksheet |
| src-000379 | field-type | E1403 | DecimalNumber | Not a component record in this worksheet |
| src-000379 | field-type | E1404 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000379 | field-type | E1405 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000379 | field-type | E1406 | InvestmentFundOrder | [InvestmentFundOrder](<bc-6aec42483ef15d38c88f.md>) |
| src-000379 | field-type | E1407 | UKTaxGroupUnitCode | Not a component record in this worksheet |
| src-000379 | field-type | E1408 | InvestmentFundOrderExecution | [InvestmentFundOrderExecution](<bc-227f2d44136fb326f809.md>) |
| src-000379 | field-type | E1409 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000379 | field-type | E1410 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000379 | field-type | E1411 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000379 | field-type | E1412 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000379 | field-type | E1413 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000379 | field-type | E1414 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000379 | field-type | E1415 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000379 | field-type | E1416 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000379 | field-type | E1417 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000379 | field-type | E1418 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000379 | field-type | E1419 | QuantityCode | Not a component record in this worksheet |
| src-000379 | field-type | E1420 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000379 | field-type | E1421 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000379 | field-type | E1422 | CorporateActionDistribution | [CorporateActionDistribution](<bc-f371fbd458438de6240f.md>) |
| src-000379 | field-type | E1423 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000379 | field-type | E1424 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000379 | field-type | E1425 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000379 | field-type | E1426 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000379 | field-type | E1427 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000379 | field-type | E1428 | CorporateActionSecuritiesEntitlement | [CorporateActionSecuritiesEntitlement](<bc-5cff81ce6e7bbfabfbf5.md>) |
| src-000379 | field-type | E1429 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000379 | field-type | E1430 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000379 | field-type | E1431 | Lottery | [Lottery](<bc-8676962b006118d93678.md>) |
| src-000379 | field-type | E1432 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000379 | field-type | E1433 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000379 | field-type | E1434 | SecuritiesTrade | [SecuritiesTrade](<bc-cacdabc7b3d47e9b7b24.md>) |
| src-000379 | field-type | E1435 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000379 | field-type | E1436 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000379 | field-type | E1437 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000379 | field-type | E1438 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000379 | field-type | E1439 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000379 | field-type | E1440 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000379 | field-type | E1441 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000379 | field-type | E1442 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E1443 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000379 | field-type | E1444 | UnderlyingRatio | [UnderlyingRatio](<bc-52f946b89a1688a96084.md>) |
| src-000379 | field-type | E1445 | SecuritiesTradeExecution | [SecuritiesTradeExecution](<bc-854b1f66f9a7836895cf.md>) |
| src-000379 | field-type | E1446 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000379 | field-type | E1447 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000379 | field-type | E1448 | TaxVoucher | [TaxVoucher](<bc-6ed358f7b4b5fd0e83a1.md>) |
| src-000379 | field-type | E1449 | BuyIn | [BuyIn](<bc-5b3c24df7aa8aca3f795.md>) |
| src-000379 | field-type | E1450 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000379 | field-type | E1451 | Liquidity | [Liquidity](<bc-e58491436c12d922bc5f.md>) |
| src-000379 | field-type | E1452 | PercentageRate | Not a component record in this worksheet |
| src-000379 | field-type | E1453 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000379 | field-type | E1454 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000379 | field-type | E1455 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000379 | field-type | E1456 | SecuritiesOrderParameters | [SecuritiesOrderParameters](<bc-7cf834a09e2cb2ff529a.md>) |
| src-000379 | field-type | E1457 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000379 | field-type | E1458 | PairOff | [PairOff](<bc-8b5c2deb20538dd935f7.md>) |
| src-000379 | field-type | E1459 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000379 | field-type | E1460 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000379 | field-type | E1461 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000379 | field-type | E1462 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000379 | field-type | E1463 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000379 | field-type | E1464 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000379 | field-type | E1465 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000379 | field-type | E1466 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000379 | field-type | E1467 | SecuritiesAndCashDistribution | [SecuritiesAndCashDistribution](<bc-e0960d1a2a1b18789677.md>) |
| src-000379 | field-type | E1468 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000379 | field-type | E1469 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000379 | field-type | E1470 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000379 | field-type | E1471 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000379 | field-type | E1472 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000379 | field-type | E1473 | SecuritiesDistribution | [SecuritiesDistribution](<bc-270b79f8f5e5f98b1586.md>) |
| src-000379 | field-type | E1474 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000379 | field-type | E1475 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000379 | field-type | E1476 | Quote | [Quote](<bc-c4bc9dc9555692bda396.md>) |
| src-000379 | field-type | E1477 | NetAssetValueCalculation | [NetAssetValueCalculation](<bc-b0ebfc4418fb9fb1bce3.md>) |
| src-000379 | field-type | E1478 | SidePocket | [SidePocket](<bc-19b0c48c5a47daa2e3bd.md>) |
| src-000379 | field-type | E1479 | Netting | [Netting](<bc-7d7a630fba8f626545ab.md>) |
| src-000379 | field-type | E1480 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000379 | field-type | E1481 | SecuritiesOrderStatus | [SecuritiesOrderStatus](<bc-da07523d8f20b93df9a5.md>) |
| src-000379 | field-type | E1482 | SecuritiesSettlement | [SecuritiesSettlement](<bc-18ee94584decdbdc6961.md>) |
| src-000379 | field-type | E1483 | FundsCashFlow | [FundsCashFlow](<bc-04400270b3df0ca87f1e.md>) |
| src-000379 | field-type | E1484 | Position | [Position](<bc-48d203cb80c73aaee87b.md>) |
| src-000379 | field-type | E1485 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000379 | field-type | E1486 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000379 | field-type | E1487 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000379 | field-type | E1488 | CorporateActionProtectProcess | [CorporateActionProtectProcess](<bc-8e4e963671c2ec477553.md>) |
| src-000379 | field-type | E1489 | DecimalNumber | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
