---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-420f6b7b61cb1a61affe"
title: "DateTimePeriod"
business_component_name: "DateTimePeriod"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A1363:F1433"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A1346:F1416"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A1363:F1433"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A1363:F1433"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A1363:F1433"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A1363:F1433"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A1363:F1433"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A1346:F1416"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A1363:F1433"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A1359:F1429"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A693:F763"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A1359:F1429"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A1363:F1433"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A1335:F1405"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A693:F763"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A693:F763"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A1335:F1405"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A1335:F1405"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A693:F763"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A693:F763"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A1363:F1433"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A693:F763"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A1359:F1429"]}]
content_sha256: "420f6b7b61cb1a61affee081776ad939bd7d37c0d038040588d7d507ecdc798c"
parent_names: []
related_component_names: ["Account", "AccountLink", "AccountRestriction", "Adjustment", "Agreement", "AmountAndPeriod", "BankOperation", "BasicSecuritiesRegistration", "BiddingConditions", "ClassAction", "ComponentSecurity", "CorporateActionEvent", "CorporateActionOption", "Debt", "Distribution", "FinancialInstrumentSwap", "Guarantee", "ISODateTime", "InterestCalculation", "InvestmentPlan", "Invoice", "Issuance", "Limit", "Number", "PartyIdentificationInformation", "PaymentInstruction", "PaymentTerms", "PercentageAndPeriod", "PerformanceFactors", "PortfolioValuation", "PostalAddress", "ProductDelivery", "RedemptionSchedule", "RolePlayer", "Scheme", "SecuritiesConversion", "SecuritiesIdentification", "SecuritiesPricing", "SecuritiesProceedsDefinition", "StandingOrder", "StandingSettlementInstruction", "Status", "SuspensionPeriod", "System", "SystemAvailability", "TaxPeriod", "TradeCertificate", "TradingSession", "ValuationStatistics", "YieldCalculation"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# DateTimePeriod

## Definition

Time span defined by a start date and time, and an end date and time.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | DateTimePeriod | ∅ | ∅ | Time span defined by a start date and time, and an end date and time. | ∅ | ∅ |
| 2 | DateTimePeriod | FromDateTime | ∅ | Date and time at which the range starts. | ISODateTime | ∅ |
| 3 | DateTimePeriod | ToDateTime | ∅ | Date and time at which the range ends. | ISODateTime | ∅ |
| 4 | DateTimePeriod | RelatedStandingOrder | ∅ | Standing order for which a validity period is specified. | StandingOrder | ValidityPeriod |
| 5 | DateTimePeriod | PaymentInstruction | ∅ | Payment instruction for which a processing validity time is specified. | PaymentInstruction | ProcessingValidityTime |
| 6 | DateTimePeriod | NumberOfDays | ∅ | Period specified as a number of days. | Number | ∅ |
| 7 | DateTimePeriod | ValuationStatistics | ∅ | Valuation statistics for which a reference period is specified. | ValuationStatistics | Period |
| 8 | DateTimePeriod | PerformanceFactors | ∅ | Performance factors for which an accumulation period is specified. | PerformanceFactors | AccumulationPeriod |
| 9 | DateTimePeriod | Status | ∅ | Status for which a validity time is specified. | Status | ValidityTime |
| 10 | DateTimePeriod | PriceCalculationRelatedPricing | ∅ | Securities pricing for which a price calculation period is specified. | SecuritiesPricing | PriceCalculationPeriod |
| 11 | DateTimePeriod | CorporateActionOption | ∅ | Corporate action option for which an action period is defined. | CorporateActionOption | ActionPeriod |
| 12 | DateTimePeriod | ParallelTradingProceedsDefinition | ∅ | Securities proceeds for which a parallel trading period is specified. | SecuritiesProceedsDefinition | ParallelTradingPeriod |
| 13 | DateTimePeriod | PrivilegeSuspensionCorporateAction | ∅ | Corporate event for which a privilege suspension period has been defined. | SuspensionPeriod | PrivilegeSuspensionPeriod |
| 14 | DateTimePeriod | WithdrawalSuspensionRelatedEvent | ∅ | Corporate event for which a suspension period for withdrawals is specified. | SuspensionPeriod | DepositorySuspensionPeriodForWithdrawal |
| 15 | DateTimePeriod | RelatedInterestCalculation | ∅ | Interest calculation process for which an interest period is specified. | InterestCalculation | InterestPeriod |
| 16 | DateTimePeriod | BiddingConditions | ∅ | Bidding conditions for which a compulsory purchase period is specified. | BiddingConditions | CompulsoryPurchasePeriod |
| 17 | DateTimePeriod | ClassAction | ∅ | Class action for which a claim period is specified. | ClassAction | ClaimPeriod |
| 18 | DateTimePeriod | BookEntryTransferSuspensionRelatedEvent | ∅ | Corporate event for which a suspension period for book entry transfers is specified. | SuspensionPeriod | DepositorySuspensionPeriodForBookEntryTransfer |
| 19 | DateTimePeriod | DepositAtAgentSuspensionRelatedEvent | ∅ | Corporate event for which a suspension period for deposits at agent is specified. | SuspensionPeriod | DepositorySuspensionPeriodForDepositAtAgent |
| 20 | DateTimePeriod | DepositSuspensionRelatedEvent | ∅ | Corporate event for which a suspension period for deposits is specified. | SuspensionPeriod | DepositorySuspensionPeriodForDeposit |
| 21 | DateTimePeriod | PledgeSuspensionRelatedEvent | ∅ | Corporate event for which a suspension period for pledges is specified. | SuspensionPeriod | DepositorySuspensionPeriodForPledge |
| 22 | DateTimePeriod | SegregationPeriodRelatedEvent | ∅ | Corporate event for which a suspension period for segregation is specified. | SuspensionPeriod | DepositorySuspensionPeriodForSegregation |
| 23 | DateTimePeriod | WithdrawalAtAgentSuspensionRelatedEvent | ∅ | Corporate event for which a suspension period for withdrawals at agent is specified. | SuspensionPeriod | DepositorySuspensionPeriodForWithdrawalAtAgent |
| 24 | DateTimePeriod | WithdrawalInNomineeNameSuspensionRelatedEvent | ∅ | Corporate event for which a suspension period for withdrawals in nominee name is specified. | SuspensionPeriod | DepositorySuspensionPeriodForWithdrawalInNomineeName |
| 25 | DateTimePeriod | WithdrawalInStreetNameSuspensionRelatedEvent | ∅ | Corporate event for which a suspension period for withdrawals in street name is specified. | SuspensionPeriod | DepositorySuspensionPeriodForWithdrawalInStreetName |
| 26 | DateTimePeriod | BookClosureCorporateAction | ∅ | Corporate action for which a book closure period has been specified. | CorporateActionEvent | BookClosurePeriod |
| 27 | DateTimePeriod | CoDepositoriesSuspensionRelatedEvent | ∅ | Corporate event for which a suspension period for co-depositories is specified. | SuspensionPeriod | CoDepositoriesSuspensionPeriod |
| 28 | DateTimePeriod | ExtendiblePeriodDebt | ∅ | Debt for which an extendible period is specified. | Debt | ExtendiblePeriod |
| 29 | DateTimePeriod | SecuritiesConversion | ∅ | Securities conversion process for which a conversion period is specified. | SecuritiesConversion | ConversionPeriod |
| 30 | DateTimePeriod | YieldCalculation | ∅ | Yield calculation for which a value period is specified. | YieldCalculation | ValuePeriod |
| 31 | DateTimePeriod | CustomDateDebt | ∅ | Debt for which a custom date is specified. | Debt | CustomDate |
| 32 | DateTimePeriod | TaxPeriod | ∅ | Tax period for which a from/to date is specified. | TaxPeriod | FromToDate |
| 33 | DateTimePeriod | Account | ∅ | Account for which a reported period is specified. | Account | ReportedPeriod |
| 34 | DateTimePeriod | RelatedAgreement | ∅ | Agreement for which a validity period is specified. | Agreement | ValidityPeriod |
| 35 | DateTimePeriod | AssentedLinePeriodProceedsDefinition | ∅ | Securities proceeds for which an assented line period is specified. | SecuritiesProceedsDefinition | AssentedLinePeriod |
| 36 | DateTimePeriod | SellThruIssuerProceedsDefinition | ∅ | Securities proceeds for which a sell thru issuer period is specified. | SecuritiesProceedsDefinition | SellThruIssuerPeriod |
| 37 | DateTimePeriod | RelatedProductDelivery | ∅ | Trade delivery process for which a delivery period is specified. | ProductDelivery | DeliveryPeriod |
| 38 | DateTimePeriod | RelatedInvoice | ∅ | Invoice for which a period is specified. | Invoice | PeriodCovered |
| 39 | DateTimePeriod | TradeCertificate | ∅ | Trade certificate for which an inspection date is specified. | TradeCertificate | InspectionDate |
| 40 | DateTimePeriod | RelatedPortfolioValuation | ∅ | Portfolio valuation process for which a valuation period is specified. | PortfolioValuation | ValuationPeriod |
| 41 | DateTimePeriod | System | ∅ | System for which a validity period is specified. | System | VersionValidityPeriod |
| 42 | DateTimePeriod | AccountRestriction | ∅ | Account restriction for which a validity period is specified. | AccountRestriction | ValidityPeriod |
| 43 | DateTimePeriod | BankOperation | ∅ | Bank operation for which an applicable period is specified. | BankOperation | ApplicablePeriod |
| 44 | DateTimePeriod | RelatedCorporateAction | ∅ | Corporate action event for which a trading period is specified. | CorporateActionEvent | TradingPeriod |
| 45 | DateTimePeriod | RelatedLimit | ∅ | Limit for which a validity period is specified. | Limit | ValidityPeriod |
| 46 | DateTimePeriod | RelatedIdentification | ∅ | Party identification for which a validity period is specified. | PartyIdentificationInformation | ValidityPeriod |
| 47 | DateTimePeriod | AssessmentValidityScheme | ∅ | Scheme for which a validity period is specified. | Scheme | AssessmentValidityPeriod |
| 48 | DateTimePeriod | ExercisePeriodDistribution | ∅ | Cash and securities distribution information for which an exercise period is specified. | Distribution | ExercisePeriod |
| 49 | DateTimePeriod | OfferPeriodDistribution | ∅ | Cash and securities distribution information for which an offer period is specified. | Distribution | OfferPeriod |
| 50 | DateTimePeriod | TradingPeriodDistribution | ∅ | Cash and securities distribution information for which a trading period is specified. | Distribution | TradingPeriod |
| 51 | DateTimePeriod | BlockingPeriodDistribution | ∅ | Cash and securities distribution information for which a blocking period is specified. | Distribution | BlockingPeriod |
| 52 | DateTimePeriod | Guarantee | ∅ | Guarantee for which an effective period is specified. | Guarantee | EffectivePeriod |
| 53 | DateTimePeriod | PriceFactRelatedPricing | ∅ | Securities pricing for which a price fact period is specified. | SecuritiesPricing | PriceFactPeriod |
| 54 | DateTimePeriod | CashDistribution | ∅ | Cash distribution for which an interest period is specified. | Distribution | InterestPeriod |
| 55 | DateTimePeriod | ComponentSecurity | ∅ | Security component for which a separation period is specified. | ComponentSecurity | SeparationPeriod |
| 56 | DateTimePeriod | TradingSession | ∅ | Trading session for which a time bracket is specified. | TradingSession | TimeBracket |
| 57 | DateTimePeriod | FinancialInstrumentSwap | ∅ | Swap for which a maturity period is specified. | FinancialInstrumentSwap | Maturity |
| 58 | DateTimePeriod | RelatedPostalAddress | ∅ | Postal address for which a validity period is specified. | PostalAddress | ValidityPeriod |
| 59 | DateTimePeriod | RedemptionSchedule | ∅ | Redemption schedule for which a notice period is provided. | RedemptionSchedule | EffectivePeriod |
| 60 | DateTimePeriod | RelatedAccountLink | ∅ | Link between two accounts for which a validity period is specified. | AccountLink | ValidityPeriod |
| 61 | DateTimePeriod | RelatedAdjustment | ∅ | Adjustment for which a validity period is provided. | Adjustment | EffectivePeriod |
| 62 | DateTimePeriod | RelatedSecuritiesIdentification | ∅ | Securities identification for which a validity period is specified. | SecuritiesIdentification | ValidityPeriod |
| 63 | DateTimePeriod | RelatedStandingSettlementInstruction | ∅ | SSI for which a validity period is specified. | StandingSettlementInstruction | ValidityPeriod |
| 64 | DateTimePeriod | RelatedSecuritiesRegistration | ∅ | Securities registration process for which a split period is specified. | BasicSecuritiesRegistration | SplitPeriod |
| 65 | DateTimePeriod | Amount | ∅ | Relationship with an amount. | AmountAndPeriod | Period |
| 66 | DateTimePeriod | RelatedInvestmentPlan | ∅ | InvestmentPlan for which an investment period is specified. | InvestmentPlan | InvestmentPeriod |
| 67 | DateTimePeriod | Issuance | ∅ | Issuance for which subscription information is provided. | Issuance | SubscriptionPeriod |
| 68 | DateTimePeriod | RelatedPaymentTerms | ∅ | Payment terms for which a period is specified. | PaymentTerms | PaymentPeriod |
| 69 | DateTimePeriod | Percentage | ∅ | Relationship with a percentage. | PercentageAndPeriod | Period |
| 70 | DateTimePeriod | RelatedRolePlayer | ∅ | Role player for which a validity period is specified. | RolePlayer | ValidityPeriod |
| 71 | DateTimePeriod | RelatedSystemAvailability | ∅ | System availability for which the closure period is provided. | SystemAvailability | ClosurePeriod |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `420f6b7b61cb1a61affee081776ad939bd7d37c0d038040588d7d507ecdc798c`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A1363:F1433 | 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433 | [src-000006 original](<../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart3_BanktoCustomerCashManagement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md>) |
| src-000016 | FullBusinessModel!A1346:F1416 | 1346, 1347, 1348, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1357, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416 | [src-000016 original](<../../../raw-input/cash_management/ISO20022_MDRPart3_CashManagement_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md>) |
| src-000054 | FullBusinessModel!A1363:F1433 | 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433 | [src-000054 original](<../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart3_CentralCounterParty_SecuritiesClearing_Maintenance_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md>) |
| src-000081 | FullBusinessModel!A1363:F1433 | 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433 | [src-000081 original](<../../../raw-input/corporate_actions/ISO20022_MDRPart3_CorporateActions_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md>) |
| src-000097 | FullBusinessModel!A1363:F1433 | 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433 | [src-000097 original](<../../../raw-input/investment_funds/ISO20022_MDRPart3_Investment-Funds_2025_2026_v2.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md>) |
| src-000164 | FullBusinessModel!A1363:F1433 | 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433 | [src-000164 original](<../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart3_PaymentsClearingandSettlement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md>) |
| src-000175 | FullBusinessModel!A1363:F1433 | 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433 | [src-000175 original](<../../../raw-input/payments_initiation/ISO20022_MDRPart3_PaymentsInitiation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md>) |
| src-000182 | FullBusinessModel!A1346:F1416 | 1346, 1347, 1348, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1357, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416 | [src-000182 original](<../../../raw-input/post_trade_matching/ISO20022_MDRPart3_PostTradeMatching_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md>) |
| src-000198 | FullBusinessModel!A1363:F1433 | 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433 | [src-000198 original](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart3_SettlementAndReconciliation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md>) |
| src-000322 | FullBusinessModel!A1359:F1429 | 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429 | [src-000322 original](<../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart3_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md>) |
| src-000345 | FullBusinessModel!A693:F763 | 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763 | [src-000345 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](<../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md>) |
| src-000348 | FullBusinessModel!A1359:F1429 | 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429 | [src-000348 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md>) |
| src-000352 | FullBusinessModel!A1363:F1433 | 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433 | [src-000352 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md>) |
| src-000355 | FullBusinessModel!A1335:F1405 | 1335, 1336, 1337, 1338, 1339, 1340, 1341, 1342, 1343, 1344, 1345, 1346, 1347, 1348, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1357, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405 | [src-000355 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md>) |
| src-000358 | FullBusinessModel!A693:F763 | 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763 | [src-000358 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md>) |
| src-000361 | FullBusinessModel!A693:F763 | 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763 | [src-000361 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md>) |
| src-000364 | FullBusinessModel!A1335:F1405 | 1335, 1336, 1337, 1338, 1339, 1340, 1341, 1342, 1343, 1344, 1345, 1346, 1347, 1348, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1357, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405 | [src-000364 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md>) |
| src-000367 | FullBusinessModel!A1335:F1405 | 1335, 1336, 1337, 1338, 1339, 1340, 1341, 1342, 1343, 1344, 1345, 1346, 1347, 1348, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1357, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405 | [src-000367 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md>) |
| src-000370 | FullBusinessModel!A693:F763 | 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763 | [src-000370 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md>) |
| src-000373 | FullBusinessModel!A693:F763 | 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763 | [src-000373 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md>) |
| src-000376 | FullBusinessModel!A1363:F1433 | 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433 | [src-000376 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md>) |
| src-000379 | FullBusinessModel!A693:F763 | 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763 | [src-000379 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md>) |
| src-000382 | FullBusinessModel!A1359:F1429 | 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429 | [src-000382 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | field-type | E1364 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E1365 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E1366 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000006 | field-type | E1367 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000006 | field-type | E1368 | Number | Not a component record in this worksheet |
| src-000006 | field-type | E1369 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000006 | field-type | E1370 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000006 | field-type | E1371 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000006 | field-type | E1372 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000006 | field-type | E1373 | CorporateActionOption | [CorporateActionOption](<bc-8e1bf225c7608bf4fb65.md>) |
| src-000006 | field-type | E1374 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000006 | field-type | E1375 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000006 | field-type | E1376 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000006 | field-type | E1377 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000006 | field-type | E1378 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000006 | field-type | E1379 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000006 | field-type | E1380 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000006 | field-type | E1381 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000006 | field-type | E1382 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000006 | field-type | E1383 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000006 | field-type | E1384 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000006 | field-type | E1385 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000006 | field-type | E1386 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000006 | field-type | E1387 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000006 | field-type | E1388 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000006 | field-type | E1389 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000006 | field-type | E1390 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000006 | field-type | E1391 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000006 | field-type | E1392 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000006 | field-type | E1393 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000006 | field-type | E1394 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000006 | field-type | E1395 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000006 | field-type | E1396 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000006 | field-type | E1397 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000006 | field-type | E1398 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000006 | field-type | E1399 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000006 | field-type | E1400 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000006 | field-type | E1401 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000006 | field-type | E1402 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000006 | field-type | E1403 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000006 | field-type | E1404 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000006 | field-type | E1405 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000006 | field-type | E1406 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000006 | field-type | E1407 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000006 | field-type | E1408 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-388f466e73d406c114c3.md>) |
| src-000006 | field-type | E1409 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000006 | field-type | E1410 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000006 | field-type | E1411 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000006 | field-type | E1412 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000006 | field-type | E1413 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000006 | field-type | E1414 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000006 | field-type | E1415 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000006 | field-type | E1416 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000006 | field-type | E1417 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000006 | field-type | E1418 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000006 | field-type | E1419 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000006 | field-type | E1420 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000006 | field-type | E1421 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000006 | field-type | E1422 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000006 | field-type | E1423 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000006 | field-type | E1424 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000006 | field-type | E1425 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000006 | field-type | E1426 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000006 | field-type | E1427 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000006 | field-type | E1428 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000006 | field-type | E1429 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000006 | field-type | E1430 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000006 | field-type | E1431 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000006 | field-type | E1432 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000006 | field-type | E1433 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000016 | field-type | E1347 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E1348 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E1349 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000016 | field-type | E1350 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000016 | field-type | E1351 | Number | Not a component record in this worksheet |
| src-000016 | field-type | E1352 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000016 | field-type | E1353 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000016 | field-type | E1354 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000016 | field-type | E1355 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000016 | field-type | E1356 | CorporateActionOption | [CorporateActionOption](<bc-8e1bf225c7608bf4fb65.md>) |
| src-000016 | field-type | E1357 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000016 | field-type | E1358 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000016 | field-type | E1359 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000016 | field-type | E1360 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000016 | field-type | E1361 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000016 | field-type | E1362 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000016 | field-type | E1363 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000016 | field-type | E1364 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000016 | field-type | E1365 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000016 | field-type | E1366 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000016 | field-type | E1367 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000016 | field-type | E1368 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000016 | field-type | E1369 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000016 | field-type | E1370 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000016 | field-type | E1371 | CorporateActionEvent | [CorporateActionEvent](<bc-75065c4d72b4fc93dbd7.md>) |
| src-000016 | field-type | E1372 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000016 | field-type | E1373 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000016 | field-type | E1374 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000016 | field-type | E1375 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000016 | field-type | E1376 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000016 | field-type | E1377 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000016 | field-type | E1378 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000016 | field-type | E1379 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000016 | field-type | E1380 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000016 | field-type | E1381 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000016 | field-type | E1382 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000016 | field-type | E1383 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000016 | field-type | E1384 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000016 | field-type | E1385 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000016 | field-type | E1386 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000016 | field-type | E1387 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000016 | field-type | E1388 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000016 | field-type | E1389 | CorporateActionEvent | [CorporateActionEvent](<bc-75065c4d72b4fc93dbd7.md>) |
| src-000016 | field-type | E1390 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000016 | field-type | E1391 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-96b43f368fbd43460ca2.md>) |
| src-000016 | field-type | E1392 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000016 | field-type | E1393 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000016 | field-type | E1394 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000016 | field-type | E1395 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000016 | field-type | E1396 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000016 | field-type | E1397 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000016 | field-type | E1398 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000016 | field-type | E1399 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000016 | field-type | E1400 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000016 | field-type | E1401 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000016 | field-type | E1402 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000016 | field-type | E1403 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000016 | field-type | E1404 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000016 | field-type | E1405 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000016 | field-type | E1406 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000016 | field-type | E1407 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000016 | field-type | E1408 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000016 | field-type | E1409 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000016 | field-type | E1410 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000016 | field-type | E1411 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000016 | field-type | E1412 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000016 | field-type | E1413 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000016 | field-type | E1414 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000016 | field-type | E1415 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000016 | field-type | E1416 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000054 | field-type | E1364 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E1365 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E1366 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000054 | field-type | E1367 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000054 | field-type | E1368 | Number | Not a component record in this worksheet |
| src-000054 | field-type | E1369 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000054 | field-type | E1370 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000054 | field-type | E1371 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000054 | field-type | E1372 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000054 | field-type | E1373 | CorporateActionOption | [CorporateActionOption](<bc-8e1bf225c7608bf4fb65.md>) |
| src-000054 | field-type | E1374 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000054 | field-type | E1375 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000054 | field-type | E1376 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000054 | field-type | E1377 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000054 | field-type | E1378 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000054 | field-type | E1379 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000054 | field-type | E1380 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000054 | field-type | E1381 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000054 | field-type | E1382 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000054 | field-type | E1383 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000054 | field-type | E1384 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000054 | field-type | E1385 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000054 | field-type | E1386 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000054 | field-type | E1387 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000054 | field-type | E1388 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000054 | field-type | E1389 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000054 | field-type | E1390 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000054 | field-type | E1391 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000054 | field-type | E1392 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000054 | field-type | E1393 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000054 | field-type | E1394 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000054 | field-type | E1395 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000054 | field-type | E1396 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000054 | field-type | E1397 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000054 | field-type | E1398 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000054 | field-type | E1399 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000054 | field-type | E1400 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000054 | field-type | E1401 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000054 | field-type | E1402 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000054 | field-type | E1403 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000054 | field-type | E1404 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000054 | field-type | E1405 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000054 | field-type | E1406 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000054 | field-type | E1407 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000054 | field-type | E1408 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-388f466e73d406c114c3.md>) |
| src-000054 | field-type | E1409 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000054 | field-type | E1410 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000054 | field-type | E1411 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000054 | field-type | E1412 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000054 | field-type | E1413 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000054 | field-type | E1414 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000054 | field-type | E1415 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000054 | field-type | E1416 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000054 | field-type | E1417 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000054 | field-type | E1418 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000054 | field-type | E1419 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000054 | field-type | E1420 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000054 | field-type | E1421 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000054 | field-type | E1422 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000054 | field-type | E1423 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000054 | field-type | E1424 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000054 | field-type | E1425 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000054 | field-type | E1426 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000054 | field-type | E1427 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000054 | field-type | E1428 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000054 | field-type | E1429 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000054 | field-type | E1430 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000054 | field-type | E1431 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000054 | field-type | E1432 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000054 | field-type | E1433 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000081 | field-type | E1364 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E1365 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E1366 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000081 | field-type | E1367 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000081 | field-type | E1368 | Number | Not a component record in this worksheet |
| src-000081 | field-type | E1369 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000081 | field-type | E1370 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000081 | field-type | E1371 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000081 | field-type | E1372 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000081 | field-type | E1373 | CorporateActionOption | [CorporateActionOption](<bc-8e1bf225c7608bf4fb65.md>) |
| src-000081 | field-type | E1374 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000081 | field-type | E1375 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000081 | field-type | E1376 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000081 | field-type | E1377 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000081 | field-type | E1378 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000081 | field-type | E1379 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000081 | field-type | E1380 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000081 | field-type | E1381 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000081 | field-type | E1382 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000081 | field-type | E1383 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000081 | field-type | E1384 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000081 | field-type | E1385 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000081 | field-type | E1386 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000081 | field-type | E1387 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000081 | field-type | E1388 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000081 | field-type | E1389 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000081 | field-type | E1390 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000081 | field-type | E1391 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000081 | field-type | E1392 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000081 | field-type | E1393 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000081 | field-type | E1394 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000081 | field-type | E1395 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000081 | field-type | E1396 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000081 | field-type | E1397 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000081 | field-type | E1398 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000081 | field-type | E1399 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000081 | field-type | E1400 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000081 | field-type | E1401 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000081 | field-type | E1402 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000081 | field-type | E1403 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000081 | field-type | E1404 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000081 | field-type | E1405 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000081 | field-type | E1406 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000081 | field-type | E1407 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000081 | field-type | E1408 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-388f466e73d406c114c3.md>) |
| src-000081 | field-type | E1409 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000081 | field-type | E1410 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000081 | field-type | E1411 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000081 | field-type | E1412 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000081 | field-type | E1413 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000081 | field-type | E1414 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000081 | field-type | E1415 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000081 | field-type | E1416 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000081 | field-type | E1417 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000081 | field-type | E1418 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000081 | field-type | E1419 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000081 | field-type | E1420 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000081 | field-type | E1421 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000081 | field-type | E1422 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000081 | field-type | E1423 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000081 | field-type | E1424 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000081 | field-type | E1425 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000081 | field-type | E1426 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000081 | field-type | E1427 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000081 | field-type | E1428 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000081 | field-type | E1429 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000081 | field-type | E1430 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000081 | field-type | E1431 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000081 | field-type | E1432 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000081 | field-type | E1433 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000097 | field-type | E1364 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E1365 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E1366 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000097 | field-type | E1367 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000097 | field-type | E1368 | Number | Not a component record in this worksheet |
| src-000097 | field-type | E1369 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000097 | field-type | E1370 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000097 | field-type | E1371 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000097 | field-type | E1372 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000097 | field-type | E1373 | CorporateActionOption | [CorporateActionOption](<bc-8e1bf225c7608bf4fb65.md>) |
| src-000097 | field-type | E1374 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000097 | field-type | E1375 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000097 | field-type | E1376 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000097 | field-type | E1377 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000097 | field-type | E1378 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000097 | field-type | E1379 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000097 | field-type | E1380 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000097 | field-type | E1381 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000097 | field-type | E1382 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000097 | field-type | E1383 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000097 | field-type | E1384 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000097 | field-type | E1385 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000097 | field-type | E1386 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000097 | field-type | E1387 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000097 | field-type | E1388 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000097 | field-type | E1389 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000097 | field-type | E1390 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000097 | field-type | E1391 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000097 | field-type | E1392 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000097 | field-type | E1393 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000097 | field-type | E1394 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000097 | field-type | E1395 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000097 | field-type | E1396 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000097 | field-type | E1397 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000097 | field-type | E1398 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000097 | field-type | E1399 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000097 | field-type | E1400 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000097 | field-type | E1401 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000097 | field-type | E1402 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000097 | field-type | E1403 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000097 | field-type | E1404 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000097 | field-type | E1405 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000097 | field-type | E1406 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000097 | field-type | E1407 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000097 | field-type | E1408 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-388f466e73d406c114c3.md>) |
| src-000097 | field-type | E1409 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000097 | field-type | E1410 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000097 | field-type | E1411 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000097 | field-type | E1412 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000097 | field-type | E1413 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000097 | field-type | E1414 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000097 | field-type | E1415 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000097 | field-type | E1416 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000097 | field-type | E1417 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000097 | field-type | E1418 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000097 | field-type | E1419 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000097 | field-type | E1420 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000097 | field-type | E1421 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000097 | field-type | E1422 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000097 | field-type | E1423 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000097 | field-type | E1424 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000097 | field-type | E1425 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000097 | field-type | E1426 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000097 | field-type | E1427 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000097 | field-type | E1428 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000097 | field-type | E1429 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000097 | field-type | E1430 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000097 | field-type | E1431 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000097 | field-type | E1432 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000097 | field-type | E1433 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000164 | field-type | E1364 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E1365 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E1366 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000164 | field-type | E1367 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000164 | field-type | E1368 | Number | Not a component record in this worksheet |
| src-000164 | field-type | E1369 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000164 | field-type | E1370 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000164 | field-type | E1371 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000164 | field-type | E1372 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000164 | field-type | E1373 | CorporateActionOption | [CorporateActionOption](<bc-8e1bf225c7608bf4fb65.md>) |
| src-000164 | field-type | E1374 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000164 | field-type | E1375 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000164 | field-type | E1376 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000164 | field-type | E1377 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000164 | field-type | E1378 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000164 | field-type | E1379 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000164 | field-type | E1380 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000164 | field-type | E1381 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000164 | field-type | E1382 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000164 | field-type | E1383 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000164 | field-type | E1384 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000164 | field-type | E1385 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000164 | field-type | E1386 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000164 | field-type | E1387 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000164 | field-type | E1388 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000164 | field-type | E1389 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000164 | field-type | E1390 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000164 | field-type | E1391 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000164 | field-type | E1392 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000164 | field-type | E1393 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000164 | field-type | E1394 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000164 | field-type | E1395 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000164 | field-type | E1396 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000164 | field-type | E1397 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000164 | field-type | E1398 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000164 | field-type | E1399 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000164 | field-type | E1400 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000164 | field-type | E1401 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000164 | field-type | E1402 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000164 | field-type | E1403 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000164 | field-type | E1404 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000164 | field-type | E1405 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000164 | field-type | E1406 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000164 | field-type | E1407 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000164 | field-type | E1408 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-388f466e73d406c114c3.md>) |
| src-000164 | field-type | E1409 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000164 | field-type | E1410 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000164 | field-type | E1411 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000164 | field-type | E1412 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000164 | field-type | E1413 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000164 | field-type | E1414 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000164 | field-type | E1415 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000164 | field-type | E1416 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000164 | field-type | E1417 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000164 | field-type | E1418 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000164 | field-type | E1419 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000164 | field-type | E1420 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000164 | field-type | E1421 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000164 | field-type | E1422 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000164 | field-type | E1423 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000164 | field-type | E1424 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000164 | field-type | E1425 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000164 | field-type | E1426 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000164 | field-type | E1427 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000164 | field-type | E1428 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000164 | field-type | E1429 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000164 | field-type | E1430 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000164 | field-type | E1431 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000164 | field-type | E1432 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000164 | field-type | E1433 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000175 | field-type | E1364 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E1365 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E1366 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000175 | field-type | E1367 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000175 | field-type | E1368 | Number | Not a component record in this worksheet |
| src-000175 | field-type | E1369 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000175 | field-type | E1370 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000175 | field-type | E1371 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000175 | field-type | E1372 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000175 | field-type | E1373 | CorporateActionOption | [CorporateActionOption](<bc-8e1bf225c7608bf4fb65.md>) |
| src-000175 | field-type | E1374 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000175 | field-type | E1375 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000175 | field-type | E1376 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000175 | field-type | E1377 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000175 | field-type | E1378 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000175 | field-type | E1379 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000175 | field-type | E1380 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000175 | field-type | E1381 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000175 | field-type | E1382 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000175 | field-type | E1383 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000175 | field-type | E1384 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000175 | field-type | E1385 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000175 | field-type | E1386 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000175 | field-type | E1387 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000175 | field-type | E1388 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000175 | field-type | E1389 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000175 | field-type | E1390 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000175 | field-type | E1391 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000175 | field-type | E1392 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000175 | field-type | E1393 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000175 | field-type | E1394 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000175 | field-type | E1395 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000175 | field-type | E1396 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000175 | field-type | E1397 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000175 | field-type | E1398 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000175 | field-type | E1399 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000175 | field-type | E1400 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000175 | field-type | E1401 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000175 | field-type | E1402 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000175 | field-type | E1403 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000175 | field-type | E1404 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000175 | field-type | E1405 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000175 | field-type | E1406 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000175 | field-type | E1407 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000175 | field-type | E1408 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-388f466e73d406c114c3.md>) |
| src-000175 | field-type | E1409 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000175 | field-type | E1410 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000175 | field-type | E1411 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000175 | field-type | E1412 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000175 | field-type | E1413 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000175 | field-type | E1414 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000175 | field-type | E1415 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000175 | field-type | E1416 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000175 | field-type | E1417 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000175 | field-type | E1418 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000175 | field-type | E1419 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000175 | field-type | E1420 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000175 | field-type | E1421 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000175 | field-type | E1422 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000175 | field-type | E1423 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000175 | field-type | E1424 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000175 | field-type | E1425 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000175 | field-type | E1426 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000175 | field-type | E1427 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000175 | field-type | E1428 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000175 | field-type | E1429 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000175 | field-type | E1430 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000175 | field-type | E1431 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000175 | field-type | E1432 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000175 | field-type | E1433 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000182 | field-type | E1347 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E1348 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E1349 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000182 | field-type | E1350 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000182 | field-type | E1351 | Number | Not a component record in this worksheet |
| src-000182 | field-type | E1352 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000182 | field-type | E1353 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000182 | field-type | E1354 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000182 | field-type | E1355 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000182 | field-type | E1356 | CorporateActionOption | [CorporateActionOption](<bc-8e1bf225c7608bf4fb65.md>) |
| src-000182 | field-type | E1357 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000182 | field-type | E1358 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000182 | field-type | E1359 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000182 | field-type | E1360 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000182 | field-type | E1361 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000182 | field-type | E1362 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000182 | field-type | E1363 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000182 | field-type | E1364 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000182 | field-type | E1365 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000182 | field-type | E1366 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000182 | field-type | E1367 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000182 | field-type | E1368 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000182 | field-type | E1369 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000182 | field-type | E1370 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000182 | field-type | E1371 | CorporateActionEvent | [CorporateActionEvent](<bc-75065c4d72b4fc93dbd7.md>) |
| src-000182 | field-type | E1372 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000182 | field-type | E1373 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000182 | field-type | E1374 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000182 | field-type | E1375 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000182 | field-type | E1376 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000182 | field-type | E1377 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000182 | field-type | E1378 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000182 | field-type | E1379 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000182 | field-type | E1380 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000182 | field-type | E1381 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000182 | field-type | E1382 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000182 | field-type | E1383 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000182 | field-type | E1384 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000182 | field-type | E1385 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000182 | field-type | E1386 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000182 | field-type | E1387 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000182 | field-type | E1388 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000182 | field-type | E1389 | CorporateActionEvent | [CorporateActionEvent](<bc-75065c4d72b4fc93dbd7.md>) |
| src-000182 | field-type | E1390 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000182 | field-type | E1391 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-96b43f368fbd43460ca2.md>) |
| src-000182 | field-type | E1392 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000182 | field-type | E1393 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000182 | field-type | E1394 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000182 | field-type | E1395 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000182 | field-type | E1396 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000182 | field-type | E1397 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000182 | field-type | E1398 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000182 | field-type | E1399 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000182 | field-type | E1400 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000182 | field-type | E1401 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000182 | field-type | E1402 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000182 | field-type | E1403 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000182 | field-type | E1404 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000182 | field-type | E1405 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000182 | field-type | E1406 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000182 | field-type | E1407 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000182 | field-type | E1408 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000182 | field-type | E1409 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000182 | field-type | E1410 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000182 | field-type | E1411 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000182 | field-type | E1412 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000182 | field-type | E1413 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000182 | field-type | E1414 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000182 | field-type | E1415 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000182 | field-type | E1416 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000198 | field-type | E1364 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E1365 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E1366 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000198 | field-type | E1367 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000198 | field-type | E1368 | Number | Not a component record in this worksheet |
| src-000198 | field-type | E1369 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000198 | field-type | E1370 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000198 | field-type | E1371 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000198 | field-type | E1372 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000198 | field-type | E1373 | CorporateActionOption | [CorporateActionOption](<bc-8e1bf225c7608bf4fb65.md>) |
| src-000198 | field-type | E1374 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000198 | field-type | E1375 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000198 | field-type | E1376 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000198 | field-type | E1377 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000198 | field-type | E1378 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000198 | field-type | E1379 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000198 | field-type | E1380 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000198 | field-type | E1381 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000198 | field-type | E1382 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000198 | field-type | E1383 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000198 | field-type | E1384 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000198 | field-type | E1385 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000198 | field-type | E1386 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000198 | field-type | E1387 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000198 | field-type | E1388 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000198 | field-type | E1389 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000198 | field-type | E1390 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000198 | field-type | E1391 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000198 | field-type | E1392 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000198 | field-type | E1393 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000198 | field-type | E1394 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000198 | field-type | E1395 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000198 | field-type | E1396 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000198 | field-type | E1397 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000198 | field-type | E1398 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000198 | field-type | E1399 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000198 | field-type | E1400 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000198 | field-type | E1401 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000198 | field-type | E1402 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000198 | field-type | E1403 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000198 | field-type | E1404 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000198 | field-type | E1405 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000198 | field-type | E1406 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000198 | field-type | E1407 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000198 | field-type | E1408 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-388f466e73d406c114c3.md>) |
| src-000198 | field-type | E1409 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000198 | field-type | E1410 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000198 | field-type | E1411 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000198 | field-type | E1412 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000198 | field-type | E1413 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000198 | field-type | E1414 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000198 | field-type | E1415 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000198 | field-type | E1416 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000198 | field-type | E1417 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000198 | field-type | E1418 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000198 | field-type | E1419 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000198 | field-type | E1420 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000198 | field-type | E1421 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000198 | field-type | E1422 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000198 | field-type | E1423 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000198 | field-type | E1424 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000198 | field-type | E1425 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000198 | field-type | E1426 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000198 | field-type | E1427 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000198 | field-type | E1428 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000198 | field-type | E1429 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000198 | field-type | E1430 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000198 | field-type | E1431 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000198 | field-type | E1432 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000198 | field-type | E1433 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000322 | field-type | E1360 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E1361 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E1362 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000322 | field-type | E1363 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000322 | field-type | E1364 | Number | Not a component record in this worksheet |
| src-000322 | field-type | E1365 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000322 | field-type | E1366 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000322 | field-type | E1367 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000322 | field-type | E1368 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000322 | field-type | E1369 | CorporateActionOption | [CorporateActionOption](<bc-8e1bf225c7608bf4fb65.md>) |
| src-000322 | field-type | E1370 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000322 | field-type | E1371 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000322 | field-type | E1372 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000322 | field-type | E1373 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000322 | field-type | E1374 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000322 | field-type | E1375 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000322 | field-type | E1376 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000322 | field-type | E1377 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000322 | field-type | E1378 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000322 | field-type | E1379 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000322 | field-type | E1380 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000322 | field-type | E1381 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000322 | field-type | E1382 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000322 | field-type | E1383 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000322 | field-type | E1384 | CorporateActionEvent | [CorporateActionEvent](<bc-75065c4d72b4fc93dbd7.md>) |
| src-000322 | field-type | E1385 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000322 | field-type | E1386 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000322 | field-type | E1387 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000322 | field-type | E1388 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000322 | field-type | E1389 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000322 | field-type | E1390 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000322 | field-type | E1391 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000322 | field-type | E1392 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000322 | field-type | E1393 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000322 | field-type | E1394 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000322 | field-type | E1395 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000322 | field-type | E1396 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000322 | field-type | E1397 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000322 | field-type | E1398 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000322 | field-type | E1399 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000322 | field-type | E1400 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000322 | field-type | E1401 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000322 | field-type | E1402 | CorporateActionEvent | [CorporateActionEvent](<bc-75065c4d72b4fc93dbd7.md>) |
| src-000322 | field-type | E1403 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000322 | field-type | E1404 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-96b43f368fbd43460ca2.md>) |
| src-000322 | field-type | E1405 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000322 | field-type | E1406 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000322 | field-type | E1407 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000322 | field-type | E1408 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000322 | field-type | E1409 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000322 | field-type | E1410 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000322 | field-type | E1411 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000322 | field-type | E1412 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000322 | field-type | E1413 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000322 | field-type | E1414 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000322 | field-type | E1415 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000322 | field-type | E1416 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000322 | field-type | E1417 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000322 | field-type | E1418 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000322 | field-type | E1419 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000322 | field-type | E1420 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000322 | field-type | E1421 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000322 | field-type | E1422 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000322 | field-type | E1423 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000322 | field-type | E1424 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000322 | field-type | E1425 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000322 | field-type | E1426 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000322 | field-type | E1427 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000322 | field-type | E1428 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000322 | field-type | E1429 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000345 | field-type | E694 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E695 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E696 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000345 | field-type | E697 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000345 | field-type | E698 | Number | Not a component record in this worksheet |
| src-000345 | field-type | E699 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000345 | field-type | E700 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000345 | field-type | E701 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000345 | field-type | E702 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000345 | field-type | E703 | CorporateActionOption | [CorporateActionOption](<bc-7e0e3887362514d352fa.md>) |
| src-000345 | field-type | E704 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000345 | field-type | E705 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000345 | field-type | E706 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000345 | field-type | E707 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000345 | field-type | E708 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000345 | field-type | E709 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000345 | field-type | E710 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000345 | field-type | E711 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000345 | field-type | E712 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000345 | field-type | E713 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000345 | field-type | E714 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000345 | field-type | E715 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000345 | field-type | E716 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000345 | field-type | E717 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000345 | field-type | E718 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000345 | field-type | E719 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000345 | field-type | E720 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000345 | field-type | E721 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000345 | field-type | E722 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000345 | field-type | E723 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000345 | field-type | E724 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000345 | field-type | E725 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000345 | field-type | E726 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000345 | field-type | E727 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000345 | field-type | E728 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000345 | field-type | E729 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000345 | field-type | E730 | Invoice | [Invoice](<bc-486d470ade846a71a268.md>) |
| src-000345 | field-type | E731 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000345 | field-type | E732 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000345 | field-type | E733 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000345 | field-type | E734 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000345 | field-type | E735 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000345 | field-type | E736 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000345 | field-type | E737 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000345 | field-type | E738 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-96b43f368fbd43460ca2.md>) |
| src-000345 | field-type | E739 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000345 | field-type | E740 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000345 | field-type | E741 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000345 | field-type | E742 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000345 | field-type | E743 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000345 | field-type | E744 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000345 | field-type | E745 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000345 | field-type | E746 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000345 | field-type | E747 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000345 | field-type | E748 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000345 | field-type | E749 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000345 | field-type | E750 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000345 | field-type | E751 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000345 | field-type | E752 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000345 | field-type | E753 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000345 | field-type | E754 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000345 | field-type | E755 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000345 | field-type | E756 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000345 | field-type | E757 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000345 | field-type | E758 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000345 | field-type | E759 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000345 | field-type | E760 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000345 | field-type | E761 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000345 | field-type | E762 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000345 | field-type | E763 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000348 | field-type | E1360 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E1361 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E1362 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000348 | field-type | E1363 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000348 | field-type | E1364 | Number | Not a component record in this worksheet |
| src-000348 | field-type | E1365 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000348 | field-type | E1366 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000348 | field-type | E1367 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000348 | field-type | E1368 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000348 | field-type | E1369 | CorporateActionOption | [CorporateActionOption](<bc-8e1bf225c7608bf4fb65.md>) |
| src-000348 | field-type | E1370 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000348 | field-type | E1371 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000348 | field-type | E1372 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000348 | field-type | E1373 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000348 | field-type | E1374 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000348 | field-type | E1375 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000348 | field-type | E1376 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000348 | field-type | E1377 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000348 | field-type | E1378 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000348 | field-type | E1379 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000348 | field-type | E1380 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000348 | field-type | E1381 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000348 | field-type | E1382 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000348 | field-type | E1383 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000348 | field-type | E1384 | CorporateActionEvent | [CorporateActionEvent](<bc-75065c4d72b4fc93dbd7.md>) |
| src-000348 | field-type | E1385 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000348 | field-type | E1386 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000348 | field-type | E1387 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000348 | field-type | E1388 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000348 | field-type | E1389 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000348 | field-type | E1390 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000348 | field-type | E1391 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000348 | field-type | E1392 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000348 | field-type | E1393 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000348 | field-type | E1394 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000348 | field-type | E1395 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000348 | field-type | E1396 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000348 | field-type | E1397 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000348 | field-type | E1398 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000348 | field-type | E1399 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000348 | field-type | E1400 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000348 | field-type | E1401 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000348 | field-type | E1402 | CorporateActionEvent | [CorporateActionEvent](<bc-75065c4d72b4fc93dbd7.md>) |
| src-000348 | field-type | E1403 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000348 | field-type | E1404 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-96b43f368fbd43460ca2.md>) |
| src-000348 | field-type | E1405 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000348 | field-type | E1406 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000348 | field-type | E1407 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000348 | field-type | E1408 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000348 | field-type | E1409 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000348 | field-type | E1410 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000348 | field-type | E1411 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000348 | field-type | E1412 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000348 | field-type | E1413 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000348 | field-type | E1414 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000348 | field-type | E1415 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000348 | field-type | E1416 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000348 | field-type | E1417 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000348 | field-type | E1418 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000348 | field-type | E1419 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000348 | field-type | E1420 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000348 | field-type | E1421 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000348 | field-type | E1422 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000348 | field-type | E1423 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000348 | field-type | E1424 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000348 | field-type | E1425 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000348 | field-type | E1426 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000348 | field-type | E1427 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000348 | field-type | E1428 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000348 | field-type | E1429 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000352 | field-type | E1364 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E1365 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E1366 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000352 | field-type | E1367 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000352 | field-type | E1368 | Number | Not a component record in this worksheet |
| src-000352 | field-type | E1369 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000352 | field-type | E1370 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000352 | field-type | E1371 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000352 | field-type | E1372 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000352 | field-type | E1373 | CorporateActionOption | [CorporateActionOption](<bc-8e1bf225c7608bf4fb65.md>) |
| src-000352 | field-type | E1374 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000352 | field-type | E1375 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000352 | field-type | E1376 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000352 | field-type | E1377 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000352 | field-type | E1378 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000352 | field-type | E1379 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000352 | field-type | E1380 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000352 | field-type | E1381 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000352 | field-type | E1382 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000352 | field-type | E1383 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000352 | field-type | E1384 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000352 | field-type | E1385 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000352 | field-type | E1386 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000352 | field-type | E1387 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000352 | field-type | E1388 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000352 | field-type | E1389 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000352 | field-type | E1390 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000352 | field-type | E1391 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000352 | field-type | E1392 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000352 | field-type | E1393 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000352 | field-type | E1394 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000352 | field-type | E1395 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000352 | field-type | E1396 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000352 | field-type | E1397 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000352 | field-type | E1398 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000352 | field-type | E1399 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000352 | field-type | E1400 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000352 | field-type | E1401 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000352 | field-type | E1402 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000352 | field-type | E1403 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000352 | field-type | E1404 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000352 | field-type | E1405 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000352 | field-type | E1406 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000352 | field-type | E1407 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000352 | field-type | E1408 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-388f466e73d406c114c3.md>) |
| src-000352 | field-type | E1409 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000352 | field-type | E1410 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000352 | field-type | E1411 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000352 | field-type | E1412 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000352 | field-type | E1413 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000352 | field-type | E1414 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000352 | field-type | E1415 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000352 | field-type | E1416 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000352 | field-type | E1417 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000352 | field-type | E1418 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000352 | field-type | E1419 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000352 | field-type | E1420 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000352 | field-type | E1421 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000352 | field-type | E1422 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000352 | field-type | E1423 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000352 | field-type | E1424 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000352 | field-type | E1425 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000352 | field-type | E1426 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000352 | field-type | E1427 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000352 | field-type | E1428 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000352 | field-type | E1429 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000352 | field-type | E1430 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000352 | field-type | E1431 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000352 | field-type | E1432 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000352 | field-type | E1433 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000355 | field-type | E1336 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E1337 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E1338 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000355 | field-type | E1339 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000355 | field-type | E1340 | Number | Not a component record in this worksheet |
| src-000355 | field-type | E1341 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000355 | field-type | E1342 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000355 | field-type | E1343 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000355 | field-type | E1344 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000355 | field-type | E1345 | CorporateActionOption | [CorporateActionOption](<bc-7e0e3887362514d352fa.md>) |
| src-000355 | field-type | E1346 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000355 | field-type | E1347 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000355 | field-type | E1348 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000355 | field-type | E1349 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000355 | field-type | E1350 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000355 | field-type | E1351 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000355 | field-type | E1352 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000355 | field-type | E1353 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000355 | field-type | E1354 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000355 | field-type | E1355 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000355 | field-type | E1356 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000355 | field-type | E1357 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000355 | field-type | E1358 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000355 | field-type | E1359 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000355 | field-type | E1360 | CorporateActionEvent | [CorporateActionEvent](<bc-9a03dfa9ef86b81a3985.md>) |
| src-000355 | field-type | E1361 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000355 | field-type | E1362 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000355 | field-type | E1363 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000355 | field-type | E1364 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000355 | field-type | E1365 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000355 | field-type | E1366 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000355 | field-type | E1367 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000355 | field-type | E1368 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000355 | field-type | E1369 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000355 | field-type | E1370 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000355 | field-type | E1371 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000355 | field-type | E1372 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000355 | field-type | E1373 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000355 | field-type | E1374 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000355 | field-type | E1375 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000355 | field-type | E1376 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000355 | field-type | E1377 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000355 | field-type | E1378 | CorporateActionEvent | [CorporateActionEvent](<bc-9a03dfa9ef86b81a3985.md>) |
| src-000355 | field-type | E1379 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000355 | field-type | E1380 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-96b43f368fbd43460ca2.md>) |
| src-000355 | field-type | E1381 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000355 | field-type | E1382 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000355 | field-type | E1383 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000355 | field-type | E1384 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000355 | field-type | E1385 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000355 | field-type | E1386 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000355 | field-type | E1387 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000355 | field-type | E1388 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000355 | field-type | E1389 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000355 | field-type | E1390 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000355 | field-type | E1391 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000355 | field-type | E1392 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000355 | field-type | E1393 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000355 | field-type | E1394 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000355 | field-type | E1395 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000355 | field-type | E1396 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000355 | field-type | E1397 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000355 | field-type | E1398 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000355 | field-type | E1399 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000355 | field-type | E1400 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000355 | field-type | E1401 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000355 | field-type | E1402 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000355 | field-type | E1403 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000355 | field-type | E1404 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000355 | field-type | E1405 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000358 | field-type | E694 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E695 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E696 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000358 | field-type | E697 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000358 | field-type | E698 | Number | Not a component record in this worksheet |
| src-000358 | field-type | E699 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000358 | field-type | E700 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000358 | field-type | E701 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000358 | field-type | E702 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000358 | field-type | E703 | CorporateActionOption | [CorporateActionOption](<bc-7e0e3887362514d352fa.md>) |
| src-000358 | field-type | E704 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000358 | field-type | E705 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000358 | field-type | E706 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000358 | field-type | E707 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000358 | field-type | E708 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000358 | field-type | E709 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000358 | field-type | E710 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000358 | field-type | E711 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000358 | field-type | E712 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000358 | field-type | E713 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000358 | field-type | E714 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000358 | field-type | E715 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000358 | field-type | E716 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000358 | field-type | E717 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000358 | field-type | E718 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000358 | field-type | E719 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000358 | field-type | E720 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000358 | field-type | E721 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000358 | field-type | E722 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000358 | field-type | E723 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000358 | field-type | E724 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000358 | field-type | E725 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000358 | field-type | E726 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000358 | field-type | E727 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000358 | field-type | E728 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000358 | field-type | E729 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000358 | field-type | E730 | Invoice | [Invoice](<bc-486d470ade846a71a268.md>) |
| src-000358 | field-type | E731 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000358 | field-type | E732 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000358 | field-type | E733 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000358 | field-type | E734 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000358 | field-type | E735 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000358 | field-type | E736 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000358 | field-type | E737 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000358 | field-type | E738 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-96b43f368fbd43460ca2.md>) |
| src-000358 | field-type | E739 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000358 | field-type | E740 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000358 | field-type | E741 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000358 | field-type | E742 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000358 | field-type | E743 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000358 | field-type | E744 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000358 | field-type | E745 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000358 | field-type | E746 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000358 | field-type | E747 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000358 | field-type | E748 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000358 | field-type | E749 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000358 | field-type | E750 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000358 | field-type | E751 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000358 | field-type | E752 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000358 | field-type | E753 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000358 | field-type | E754 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000358 | field-type | E755 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000358 | field-type | E756 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000358 | field-type | E757 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000358 | field-type | E758 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000358 | field-type | E759 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000358 | field-type | E760 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000358 | field-type | E761 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000358 | field-type | E762 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000358 | field-type | E763 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000361 | field-type | E694 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E695 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E696 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000361 | field-type | E697 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000361 | field-type | E698 | Number | Not a component record in this worksheet |
| src-000361 | field-type | E699 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000361 | field-type | E700 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000361 | field-type | E701 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000361 | field-type | E702 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000361 | field-type | E703 | CorporateActionOption | [CorporateActionOption](<bc-7e0e3887362514d352fa.md>) |
| src-000361 | field-type | E704 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000361 | field-type | E705 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000361 | field-type | E706 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000361 | field-type | E707 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000361 | field-type | E708 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000361 | field-type | E709 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000361 | field-type | E710 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000361 | field-type | E711 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000361 | field-type | E712 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000361 | field-type | E713 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000361 | field-type | E714 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000361 | field-type | E715 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000361 | field-type | E716 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000361 | field-type | E717 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000361 | field-type | E718 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000361 | field-type | E719 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000361 | field-type | E720 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000361 | field-type | E721 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000361 | field-type | E722 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000361 | field-type | E723 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000361 | field-type | E724 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000361 | field-type | E725 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000361 | field-type | E726 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000361 | field-type | E727 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000361 | field-type | E728 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000361 | field-type | E729 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000361 | field-type | E730 | Invoice | [Invoice](<bc-486d470ade846a71a268.md>) |
| src-000361 | field-type | E731 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000361 | field-type | E732 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000361 | field-type | E733 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000361 | field-type | E734 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000361 | field-type | E735 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000361 | field-type | E736 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000361 | field-type | E737 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000361 | field-type | E738 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-96b43f368fbd43460ca2.md>) |
| src-000361 | field-type | E739 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000361 | field-type | E740 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000361 | field-type | E741 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000361 | field-type | E742 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000361 | field-type | E743 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000361 | field-type | E744 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000361 | field-type | E745 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000361 | field-type | E746 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000361 | field-type | E747 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000361 | field-type | E748 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000361 | field-type | E749 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000361 | field-type | E750 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000361 | field-type | E751 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000361 | field-type | E752 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000361 | field-type | E753 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000361 | field-type | E754 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000361 | field-type | E755 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000361 | field-type | E756 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000361 | field-type | E757 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000361 | field-type | E758 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000361 | field-type | E759 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000361 | field-type | E760 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000361 | field-type | E761 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000361 | field-type | E762 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000361 | field-type | E763 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000364 | field-type | E1336 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E1337 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E1338 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000364 | field-type | E1339 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000364 | field-type | E1340 | Number | Not a component record in this worksheet |
| src-000364 | field-type | E1341 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000364 | field-type | E1342 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000364 | field-type | E1343 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000364 | field-type | E1344 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000364 | field-type | E1345 | CorporateActionOption | [CorporateActionOption](<bc-7e0e3887362514d352fa.md>) |
| src-000364 | field-type | E1346 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000364 | field-type | E1347 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000364 | field-type | E1348 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000364 | field-type | E1349 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000364 | field-type | E1350 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000364 | field-type | E1351 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000364 | field-type | E1352 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000364 | field-type | E1353 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000364 | field-type | E1354 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000364 | field-type | E1355 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000364 | field-type | E1356 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000364 | field-type | E1357 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000364 | field-type | E1358 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000364 | field-type | E1359 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000364 | field-type | E1360 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000364 | field-type | E1361 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000364 | field-type | E1362 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000364 | field-type | E1363 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000364 | field-type | E1364 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000364 | field-type | E1365 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000364 | field-type | E1366 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000364 | field-type | E1367 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000364 | field-type | E1368 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000364 | field-type | E1369 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000364 | field-type | E1370 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000364 | field-type | E1371 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000364 | field-type | E1372 | Invoice | [Invoice](<bc-486d470ade846a71a268.md>) |
| src-000364 | field-type | E1373 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000364 | field-type | E1374 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000364 | field-type | E1375 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000364 | field-type | E1376 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000364 | field-type | E1377 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000364 | field-type | E1378 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000364 | field-type | E1379 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000364 | field-type | E1380 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-96b43f368fbd43460ca2.md>) |
| src-000364 | field-type | E1381 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000364 | field-type | E1382 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000364 | field-type | E1383 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000364 | field-type | E1384 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000364 | field-type | E1385 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000364 | field-type | E1386 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000364 | field-type | E1387 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000364 | field-type | E1388 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000364 | field-type | E1389 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000364 | field-type | E1390 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000364 | field-type | E1391 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000364 | field-type | E1392 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000364 | field-type | E1393 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000364 | field-type | E1394 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000364 | field-type | E1395 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000364 | field-type | E1396 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000364 | field-type | E1397 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000364 | field-type | E1398 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000364 | field-type | E1399 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000364 | field-type | E1400 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000364 | field-type | E1401 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000364 | field-type | E1402 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000364 | field-type | E1403 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000364 | field-type | E1404 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000364 | field-type | E1405 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000367 | field-type | E1336 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E1337 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E1338 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000367 | field-type | E1339 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000367 | field-type | E1340 | Number | Not a component record in this worksheet |
| src-000367 | field-type | E1341 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000367 | field-type | E1342 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000367 | field-type | E1343 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000367 | field-type | E1344 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000367 | field-type | E1345 | CorporateActionOption | [CorporateActionOption](<bc-7e0e3887362514d352fa.md>) |
| src-000367 | field-type | E1346 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000367 | field-type | E1347 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000367 | field-type | E1348 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000367 | field-type | E1349 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000367 | field-type | E1350 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000367 | field-type | E1351 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000367 | field-type | E1352 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000367 | field-type | E1353 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000367 | field-type | E1354 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000367 | field-type | E1355 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000367 | field-type | E1356 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000367 | field-type | E1357 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000367 | field-type | E1358 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000367 | field-type | E1359 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000367 | field-type | E1360 | CorporateActionEvent | [CorporateActionEvent](<bc-9a03dfa9ef86b81a3985.md>) |
| src-000367 | field-type | E1361 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000367 | field-type | E1362 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000367 | field-type | E1363 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000367 | field-type | E1364 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000367 | field-type | E1365 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000367 | field-type | E1366 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000367 | field-type | E1367 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000367 | field-type | E1368 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000367 | field-type | E1369 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000367 | field-type | E1370 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000367 | field-type | E1371 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000367 | field-type | E1372 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000367 | field-type | E1373 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000367 | field-type | E1374 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000367 | field-type | E1375 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000367 | field-type | E1376 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000367 | field-type | E1377 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000367 | field-type | E1378 | CorporateActionEvent | [CorporateActionEvent](<bc-9a03dfa9ef86b81a3985.md>) |
| src-000367 | field-type | E1379 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000367 | field-type | E1380 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-96b43f368fbd43460ca2.md>) |
| src-000367 | field-type | E1381 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000367 | field-type | E1382 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000367 | field-type | E1383 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000367 | field-type | E1384 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000367 | field-type | E1385 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000367 | field-type | E1386 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000367 | field-type | E1387 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000367 | field-type | E1388 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000367 | field-type | E1389 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000367 | field-type | E1390 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000367 | field-type | E1391 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000367 | field-type | E1392 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000367 | field-type | E1393 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000367 | field-type | E1394 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000367 | field-type | E1395 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000367 | field-type | E1396 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000367 | field-type | E1397 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000367 | field-type | E1398 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000367 | field-type | E1399 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000367 | field-type | E1400 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000367 | field-type | E1401 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000367 | field-type | E1402 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000367 | field-type | E1403 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000367 | field-type | E1404 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000367 | field-type | E1405 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000370 | field-type | E694 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E695 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E696 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000370 | field-type | E697 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000370 | field-type | E698 | Number | Not a component record in this worksheet |
| src-000370 | field-type | E699 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000370 | field-type | E700 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000370 | field-type | E701 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000370 | field-type | E702 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000370 | field-type | E703 | CorporateActionOption | [CorporateActionOption](<bc-7e0e3887362514d352fa.md>) |
| src-000370 | field-type | E704 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000370 | field-type | E705 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000370 | field-type | E706 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000370 | field-type | E707 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000370 | field-type | E708 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000370 | field-type | E709 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000370 | field-type | E710 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000370 | field-type | E711 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000370 | field-type | E712 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000370 | field-type | E713 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000370 | field-type | E714 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000370 | field-type | E715 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000370 | field-type | E716 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000370 | field-type | E717 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000370 | field-type | E718 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000370 | field-type | E719 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000370 | field-type | E720 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000370 | field-type | E721 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000370 | field-type | E722 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000370 | field-type | E723 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000370 | field-type | E724 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000370 | field-type | E725 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000370 | field-type | E726 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000370 | field-type | E727 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000370 | field-type | E728 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000370 | field-type | E729 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000370 | field-type | E730 | Invoice | [Invoice](<bc-486d470ade846a71a268.md>) |
| src-000370 | field-type | E731 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000370 | field-type | E732 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000370 | field-type | E733 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000370 | field-type | E734 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000370 | field-type | E735 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000370 | field-type | E736 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000370 | field-type | E737 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000370 | field-type | E738 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-96b43f368fbd43460ca2.md>) |
| src-000370 | field-type | E739 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000370 | field-type | E740 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000370 | field-type | E741 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000370 | field-type | E742 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000370 | field-type | E743 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000370 | field-type | E744 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000370 | field-type | E745 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000370 | field-type | E746 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000370 | field-type | E747 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000370 | field-type | E748 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000370 | field-type | E749 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000370 | field-type | E750 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000370 | field-type | E751 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000370 | field-type | E752 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000370 | field-type | E753 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000370 | field-type | E754 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000370 | field-type | E755 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000370 | field-type | E756 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000370 | field-type | E757 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000370 | field-type | E758 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000370 | field-type | E759 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000370 | field-type | E760 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000370 | field-type | E761 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000370 | field-type | E762 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000370 | field-type | E763 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000373 | field-type | E694 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E695 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E696 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000373 | field-type | E697 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000373 | field-type | E698 | Number | Not a component record in this worksheet |
| src-000373 | field-type | E699 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000373 | field-type | E700 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000373 | field-type | E701 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000373 | field-type | E702 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000373 | field-type | E703 | CorporateActionOption | [CorporateActionOption](<bc-7e0e3887362514d352fa.md>) |
| src-000373 | field-type | E704 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000373 | field-type | E705 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000373 | field-type | E706 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000373 | field-type | E707 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000373 | field-type | E708 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000373 | field-type | E709 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000373 | field-type | E710 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000373 | field-type | E711 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000373 | field-type | E712 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000373 | field-type | E713 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000373 | field-type | E714 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000373 | field-type | E715 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000373 | field-type | E716 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000373 | field-type | E717 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000373 | field-type | E718 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000373 | field-type | E719 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000373 | field-type | E720 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000373 | field-type | E721 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000373 | field-type | E722 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000373 | field-type | E723 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000373 | field-type | E724 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000373 | field-type | E725 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000373 | field-type | E726 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000373 | field-type | E727 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000373 | field-type | E728 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000373 | field-type | E729 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000373 | field-type | E730 | Invoice | [Invoice](<bc-486d470ade846a71a268.md>) |
| src-000373 | field-type | E731 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000373 | field-type | E732 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000373 | field-type | E733 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000373 | field-type | E734 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000373 | field-type | E735 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000373 | field-type | E736 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000373 | field-type | E737 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000373 | field-type | E738 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-96b43f368fbd43460ca2.md>) |
| src-000373 | field-type | E739 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000373 | field-type | E740 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000373 | field-type | E741 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000373 | field-type | E742 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000373 | field-type | E743 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000373 | field-type | E744 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000373 | field-type | E745 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000373 | field-type | E746 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000373 | field-type | E747 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000373 | field-type | E748 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000373 | field-type | E749 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000373 | field-type | E750 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000373 | field-type | E751 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000373 | field-type | E752 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000373 | field-type | E753 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000373 | field-type | E754 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000373 | field-type | E755 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000373 | field-type | E756 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000373 | field-type | E757 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000373 | field-type | E758 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000373 | field-type | E759 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000373 | field-type | E760 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000373 | field-type | E761 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000373 | field-type | E762 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000373 | field-type | E763 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000376 | field-type | E1364 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E1365 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E1366 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000376 | field-type | E1367 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000376 | field-type | E1368 | Number | Not a component record in this worksheet |
| src-000376 | field-type | E1369 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000376 | field-type | E1370 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000376 | field-type | E1371 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000376 | field-type | E1372 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000376 | field-type | E1373 | CorporateActionOption | [CorporateActionOption](<bc-8e1bf225c7608bf4fb65.md>) |
| src-000376 | field-type | E1374 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000376 | field-type | E1375 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000376 | field-type | E1376 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000376 | field-type | E1377 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000376 | field-type | E1378 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000376 | field-type | E1379 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000376 | field-type | E1380 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000376 | field-type | E1381 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000376 | field-type | E1382 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000376 | field-type | E1383 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000376 | field-type | E1384 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000376 | field-type | E1385 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000376 | field-type | E1386 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000376 | field-type | E1387 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000376 | field-type | E1388 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000376 | field-type | E1389 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000376 | field-type | E1390 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000376 | field-type | E1391 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000376 | field-type | E1392 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000376 | field-type | E1393 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000376 | field-type | E1394 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000376 | field-type | E1395 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000376 | field-type | E1396 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000376 | field-type | E1397 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000376 | field-type | E1398 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000376 | field-type | E1399 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000376 | field-type | E1400 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000376 | field-type | E1401 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000376 | field-type | E1402 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000376 | field-type | E1403 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000376 | field-type | E1404 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000376 | field-type | E1405 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000376 | field-type | E1406 | CorporateActionEvent | [CorporateActionEvent](<bc-648c01dd074600c5fc56.md>) |
| src-000376 | field-type | E1407 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000376 | field-type | E1408 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-388f466e73d406c114c3.md>) |
| src-000376 | field-type | E1409 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000376 | field-type | E1410 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000376 | field-type | E1411 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000376 | field-type | E1412 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000376 | field-type | E1413 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000376 | field-type | E1414 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000376 | field-type | E1415 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000376 | field-type | E1416 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000376 | field-type | E1417 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000376 | field-type | E1418 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000376 | field-type | E1419 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000376 | field-type | E1420 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000376 | field-type | E1421 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000376 | field-type | E1422 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000376 | field-type | E1423 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000376 | field-type | E1424 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000376 | field-type | E1425 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000376 | field-type | E1426 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000376 | field-type | E1427 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000376 | field-type | E1428 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000376 | field-type | E1429 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000376 | field-type | E1430 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000376 | field-type | E1431 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000376 | field-type | E1432 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000376 | field-type | E1433 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000379 | field-type | E694 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E695 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E696 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000379 | field-type | E697 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000379 | field-type | E698 | Number | Not a component record in this worksheet |
| src-000379 | field-type | E699 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000379 | field-type | E700 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000379 | field-type | E701 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000379 | field-type | E702 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000379 | field-type | E703 | CorporateActionOption | [CorporateActionOption](<bc-7e0e3887362514d352fa.md>) |
| src-000379 | field-type | E704 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000379 | field-type | E705 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000379 | field-type | E706 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000379 | field-type | E707 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000379 | field-type | E708 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000379 | field-type | E709 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000379 | field-type | E710 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000379 | field-type | E711 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000379 | field-type | E712 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000379 | field-type | E713 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000379 | field-type | E714 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000379 | field-type | E715 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000379 | field-type | E716 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000379 | field-type | E717 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000379 | field-type | E718 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000379 | field-type | E719 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000379 | field-type | E720 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000379 | field-type | E721 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000379 | field-type | E722 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000379 | field-type | E723 | Debt | [Debt](<bc-2a294c399ae2b508abad.md>) |
| src-000379 | field-type | E724 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000379 | field-type | E725 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000379 | field-type | E726 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000379 | field-type | E727 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000379 | field-type | E728 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000379 | field-type | E729 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000379 | field-type | E730 | Invoice | [Invoice](<bc-486d470ade846a71a268.md>) |
| src-000379 | field-type | E731 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000379 | field-type | E732 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000379 | field-type | E733 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000379 | field-type | E734 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000379 | field-type | E735 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000379 | field-type | E736 | CorporateActionEvent | [CorporateActionEvent](<bc-9b9747a4637220eff0d2.md>) |
| src-000379 | field-type | E737 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000379 | field-type | E738 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-96b43f368fbd43460ca2.md>) |
| src-000379 | field-type | E739 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000379 | field-type | E740 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000379 | field-type | E741 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000379 | field-type | E742 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000379 | field-type | E743 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000379 | field-type | E744 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000379 | field-type | E745 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000379 | field-type | E746 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000379 | field-type | E747 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000379 | field-type | E748 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000379 | field-type | E749 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000379 | field-type | E750 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000379 | field-type | E751 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000379 | field-type | E752 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000379 | field-type | E753 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000379 | field-type | E754 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000379 | field-type | E755 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000379 | field-type | E756 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000379 | field-type | E757 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000379 | field-type | E758 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000379 | field-type | E759 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000379 | field-type | E760 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000379 | field-type | E761 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000379 | field-type | E762 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000379 | field-type | E763 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000382 | field-type | E1360 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E1361 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E1362 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000382 | field-type | E1363 | PaymentInstruction | [PaymentInstruction](<bc-9f8c7b115d0de238dc20.md>) |
| src-000382 | field-type | E1364 | Number | Not a component record in this worksheet |
| src-000382 | field-type | E1365 | ValuationStatistics | [ValuationStatistics](<bc-58d1f3577205956e2c3b.md>) |
| src-000382 | field-type | E1366 | PerformanceFactors | [PerformanceFactors](<bc-823eb2a8e1fa344f1e2a.md>) |
| src-000382 | field-type | E1367 | Status | [Status](<bc-cd117310c18d18111ba9.md>) |
| src-000382 | field-type | E1368 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000382 | field-type | E1369 | CorporateActionOption | [CorporateActionOption](<bc-8e1bf225c7608bf4fb65.md>) |
| src-000382 | field-type | E1370 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000382 | field-type | E1371 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000382 | field-type | E1372 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000382 | field-type | E1373 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000382 | field-type | E1374 | BiddingConditions | [BiddingConditions](<bc-03ea41473db29299a288.md>) |
| src-000382 | field-type | E1375 | ClassAction | [ClassAction](<bc-731391afbc0c819dc0c6.md>) |
| src-000382 | field-type | E1376 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000382 | field-type | E1377 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000382 | field-type | E1378 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000382 | field-type | E1379 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000382 | field-type | E1380 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000382 | field-type | E1381 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000382 | field-type | E1382 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000382 | field-type | E1383 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000382 | field-type | E1384 | CorporateActionEvent | [CorporateActionEvent](<bc-75065c4d72b4fc93dbd7.md>) |
| src-000382 | field-type | E1385 | SuspensionPeriod | [SuspensionPeriod](<bc-1e32db318414c9d731b6.md>) |
| src-000382 | field-type | E1386 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000382 | field-type | E1387 | SecuritiesConversion | [SecuritiesConversion](<bc-6cba2571ac467da74105.md>) |
| src-000382 | field-type | E1388 | YieldCalculation | [YieldCalculation](<bc-395aa2c32917fb07e66c.md>) |
| src-000382 | field-type | E1389 | Debt | [Debt](<bc-dda11c63c9c9363eec9e.md>) |
| src-000382 | field-type | E1390 | TaxPeriod | [TaxPeriod](<bc-7ba422480d7169962c8d.md>) |
| src-000382 | field-type | E1391 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000382 | field-type | E1392 | Agreement | [Agreement](<bc-ec362d290bd9bb2d6fcb.md>) |
| src-000382 | field-type | E1393 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000382 | field-type | E1394 | SecuritiesProceedsDefinition | [SecuritiesProceedsDefinition](<bc-1f9faee2c115bc82feb8.md>) |
| src-000382 | field-type | E1395 | ProductDelivery | [ProductDelivery](<bc-6220ee03b66332d3348e.md>) |
| src-000382 | field-type | E1396 | Invoice | [Invoice](<bc-58d9698dd014ab423e8e.md>) |
| src-000382 | field-type | E1397 | TradeCertificate | [TradeCertificate](<bc-d5788ed888c60ba1331d.md>) |
| src-000382 | field-type | E1398 | PortfolioValuation | [PortfolioValuation](<bc-3d1b0305059b5a2d6394.md>) |
| src-000382 | field-type | E1399 | System | [System](<bc-f68b7e24501e8aa531fa.md>) |
| src-000382 | field-type | E1400 | AccountRestriction | [AccountRestriction](<bc-2317831c44747ea56254.md>) |
| src-000382 | field-type | E1401 | BankOperation | [BankOperation](<bc-1ce292b5acd3a5feb72d.md>) |
| src-000382 | field-type | E1402 | CorporateActionEvent | [CorporateActionEvent](<bc-75065c4d72b4fc93dbd7.md>) |
| src-000382 | field-type | E1403 | Limit | [Limit](<bc-8116c8e114f27d7b69e7.md>) |
| src-000382 | field-type | E1404 | PartyIdentificationInformation | [PartyIdentificationInformation](<bc-96b43f368fbd43460ca2.md>) |
| src-000382 | field-type | E1405 | Scheme | [Scheme](<bc-d1f693e80748689f9def.md>) |
| src-000382 | field-type | E1406 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000382 | field-type | E1407 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000382 | field-type | E1408 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000382 | field-type | E1409 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000382 | field-type | E1410 | Guarantee | [Guarantee](<bc-c6d9f2a6d64e0c089a5c.md>) |
| src-000382 | field-type | E1411 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000382 | field-type | E1412 | Distribution | [Distribution](<bc-9fb857d7f47b6f3c7dae.md>) |
| src-000382 | field-type | E1413 | ComponentSecurity | [ComponentSecurity](<bc-3d3231fd42b14eff4d9b.md>) |
| src-000382 | field-type | E1414 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000382 | field-type | E1415 | FinancialInstrumentSwap | [FinancialInstrumentSwap](<bc-287b7da0d7a5c8810190.md>) |
| src-000382 | field-type | E1416 | PostalAddress | [PostalAddress](<bc-d3a5828362027d35d596.md>) |
| src-000382 | field-type | E1417 | RedemptionSchedule | [RedemptionSchedule](<bc-07c22d7741e80e90afc8.md>) |
| src-000382 | field-type | E1418 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000382 | field-type | E1419 | Adjustment | [Adjustment](<bc-04aa963ac0863527945c.md>) |
| src-000382 | field-type | E1420 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000382 | field-type | E1421 | StandingSettlementInstruction | [StandingSettlementInstruction](<bc-22be43d596af4eaf1474.md>) |
| src-000382 | field-type | E1422 | BasicSecuritiesRegistration | [BasicSecuritiesRegistration](<bc-6e889f70f6c2b1265ebd.md>) |
| src-000382 | field-type | E1423 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000382 | field-type | E1424 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000382 | field-type | E1425 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000382 | field-type | E1426 | PaymentTerms | [PaymentTerms](<bc-5c8400ec3182d5d8c619.md>) |
| src-000382 | field-type | E1427 | PercentageAndPeriod | [PercentageAndPeriod](<bc-c5f3f085a5863b5d8af2.md>) |
| src-000382 | field-type | E1428 | RolePlayer | [RolePlayer](<bc-8a44e8f7860da50f2259.md>) |
| src-000382 | field-type | E1429 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
