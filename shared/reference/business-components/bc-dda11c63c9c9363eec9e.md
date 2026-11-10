---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-dda11c63c9c9363eec9e"
title: "Debt"
business_component_name: "Debt"
aliases: []
domain: "shared"
domains: ["payments", "securities"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-link-reference-data", "t2s-securities-and-penalty-reporting", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000348", "src-000352", "src-000355", "src-000367", "src-000376", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2024", "december-2025", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A1452:F1516"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A1435:F1499"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A1452:F1516"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A1452:F1516"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A1452:F1516"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A1452:F1516"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A1452:F1516"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A1435:F1499"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A1452:F1516"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A1448:F1512"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A1448:F1512"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A1452:F1516"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A1424:F1488"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A1424:F1488"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A1452:F1516"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A1448:F1512"]}]
content_sha256: "dda11c63c9c9363eec9ea46a58cb20d1a3fa7aac4925e867af469eec68d86fb9"
parent_names: ["Security"]
related_component_names: ["CurrencyAndAmount", "CurrencyCode", "DateTimePeriod", "DebtInstrumentSeniorityTypeCode", "DecimalNumber", "DistributionPolicyCode", "FrequencyCode", "ISODateTime", "InterestCalculation", "Max15NumericText", "Max350Text", "Max35Text", "Number", "PaymentDirectionIndicator", "PercentageRate", "PrePaymentSpeedCode", "SecuritiesPricing", "SecuritiesQuantity", "YesNoIndicator"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# Debt

## Definition

Financial instruments evidencing moneys owed by the issuer to the holder on terms as specified.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Debt | ∅ | Security | Financial instruments evidencing moneys owed by the issuer to the holder on terms as specified. | ∅ | ∅ |
| 2 | Debt | PaymentDirectionIndicator | ∅ | Indicates the direction of payment for asset or mortgage backed securities, ie, whether the repaid capital is distributed (payment direction is down) or capitalized (payment direction is up). | PaymentDirectionIndicator | ∅ |
| 3 | Debt | NextCallableDate | ∅ | Next date/time at which the issuer has the right to pay the securitiy prior to maturity. | ISODateTime | ∅ |
| 4 | Debt | PutableDate | ∅ | Date at which the holder has the right to ask for redemption of the security prior to final maturity. | ISODateTime | ∅ |
| 5 | Debt | DatedDate | ∅ | First date/time at which a security begins to accrue interest. | ISODateTime | ∅ |
| 6 | Debt | FirstPaymentDate | ∅ | Date/time at which the first interest payment is due to holders of the security. | ISODateTime | ∅ |
| 7 | Debt | Factor | ∅ | Rate that defines the outstanding principal of the factored security. Factored securities are debt instruments that have a factor that is used in the calculation of net money and market value.  Factors can be specified as current, next, previous or end factors. End factor: portion of principal that is still due at the end of the financing period. Previous factor: portion of principal that is still due before the current factor becomes applicable. Next factor: rate that will be applicable as of the next factor date. | PercentageRate | ∅ |
| 8 | Debt | PoolNumber | ∅ | Number identifying a group of underlying assets assigned by the issuer of a factored security. | Max15NumericText | ∅ |
| 9 | Debt | VariableRateIndicator | ∅ | Indicates whether the interest rate of an interest bearing instrument is reset periodically. | YesNoIndicator | ∅ |
| 10 | Debt | CallableIndicator | ∅ | Indicates whether the issuer has the right to pay the security prior to maturity. Also called RetractableIndicator. | YesNoIndicator | ∅ |
| 11 | Debt | PutableIndicator | ∅ | Indicates whether the holder has the right to ask for redemption of the security prior to final maturity. Also called RedeemableIndicator. | YesNoIndicator | ∅ |
| 12 | Debt | YieldToMaturityRate | ∅ | Rate of return anticipated on a bond when held until maturity date. | PercentageRate | ∅ |
| 13 | Debt | AccruedCapitalisationAmount | ∅ | Amount of unpaid interest (on bonds which have defaulted and have subsequently restructured), which is capitalized and added to the original principal amount of the bond. | CurrencyAndAmount | ∅ |
| 14 | Debt | NextCouponDate | ∅ | Next payment date of an interest bearing financial instrument. | ISODateTime | ∅ |
| 15 | Debt | NextFactorDate | ∅ | The date that the current factor will be changed to a new factor. | ISODateTime | ∅ |
| 16 | Debt | OddCouponIndicator | ∅ | Specifies whether the payment of the coupon (interest) on a bond is off the normal schedule. | YesNoIndicator | ∅ |
| 17 | Debt | CPProgram | ∅ | The program under which a commercial paper is issued. The values that are most used are:0 = N/A1 = 3(a)32 = 4(2)3 = 3(a)44 = 3(c)75 = 144A6 = 3(a)299 = Other | Number | ∅ |
| 18 | Debt | CPRegistrationType | ∅ | Registration type of a commercial paper issuance. | Max350Text | ∅ |
| 19 | Debt | ConvertibleIndicator | ∅ | Indicates whether the interest bearing security is convertible into another type of security. | YesNoIndicator | ∅ |
| 20 | Debt | PreFundedIndicator | ∅ | Indicates whether an interest bearing instrument is deposited in a fund that will be used to pay debt service on refunded securities. | YesNoIndicator | ∅ |
| 21 | Debt | EscrowedIndicator | ∅ | Indicates whether an interest bearing instrument is being escrowed or collateralized either by direct obligations guaranteed by the US government, or by other types of securities. The maturity schedules of the securities in the escrow fund are determined in such a way to pay the maturity value, coupon, and premium payments (if any) of the refunded bonds. | YesNoIndicator | ∅ |
| 22 | Debt | PerpetualIndicator | ∅ | Indicates whether the security has no maturity date. | YesNoIndicator | ∅ |
| 23 | Debt | SubordinatedIndicator | ∅ | Indicates whether the security is a subordinated security. | YesNoIndicator | ∅ |
| 24 | Debt | ExtendibleIndicator | ∅ | Indicates whether the security is extendible,eg, repayment may be extended or maturity changed. | YesNoIndicator | ∅ |
| 25 | Debt | ExtendiblePeriod | ∅ | Period during which a date might be extended. | DateTimePeriod | ExtendiblePeriodDebt |
| 26 | Debt | OverAllotmentAmount | ∅ | Amount for which a security can be overalloted (as in greenshoe option). | CurrencyAndAmount | ∅ |
| 27 | Debt | OverAllotmentRate | ∅ | Percentage for which a security can be overalloted (as in greenshoe option). | PercentageRate | ∅ |
| 28 | Debt | AmortisableIndicator | ∅ | Indicates whether repayment is made via regular principal and interest payments over time. | YesNoIndicator | ∅ |
| 29 | Debt | CapitalisedInterest | ∅ | Specifies whether the interest amount is capitalised until maturity date or paid out at each interest payment date. | DistributionPolicyCode | ∅ |
| 30 | Debt | ActualDenominationAmount | ∅ | Nominal value per security unit. | CurrencyAndAmount | ∅ |
| 31 | Debt | Pieces | ∅ | Number of pieces composing a pool of financial assets. | DecimalNumber | ∅ |
| 32 | Debt | PoolsMaximum | ∅ | Collection of assets by which a security is backed. | DecimalNumber | ∅ |
| 33 | Debt | PoolsPerMillion | ∅ | Indicates per million the collection of loans, mortgages or other assets assembled by an originator as the basis for a security. | DecimalNumber | ∅ |
| 34 | Debt | PoolsPerLot | ∅ | Indicates per lot the collection of loans, mortgages or other assets assembled by an originator as the basis for a security. | DecimalNumber | ∅ |
| 35 | Debt | PoolsPerTrade | ∅ | Indicates per trade the collection of loans, mortgages or other assets assembled by an originator as the basis for a security. | DecimalNumber | ∅ |
| 36 | Debt | ConstantPrePaymentPenalty | ∅ | Indicates whether a penalty might be imposed to the borrower of a mortgage in case of prepayments occurring during the lockout period. | YesNoIndicator | ∅ |
| 37 | Debt | PrePaymentSpeed | ∅ | Speed of unscheduled partial or complete payment of the principal amount outstanding on a debt obligation before its due date. | PrePaymentSpeedCode | ∅ |
| 38 | Debt | ConstantPrePaymentYield | ∅ | Measure of prepayment as a yield of the current outstanding loan balance. | PercentageRate | ∅ |
| 39 | Debt | WeightedAverageCoupon | ∅ | Contains the weighted average coupon of the fixed income instrument (expressed as a percentage). | PercentageRate | ∅ |
| 40 | Debt | WeightedAverageLife | ∅ | Contains the weighted average life of the fixed income instrument (expressed in months). | DecimalNumber | ∅ |
| 41 | Debt | WeightedAverageLoan | ∅ | Contains the weighted average loan of the fixed income instrument (expressed in months). | DecimalNumber | ∅ |
| 42 | Debt | WeightedAverageMaturity | ∅ | Contains the weighted average maturity of the fixed income instrument (expressed in months). | DecimalNumber | ∅ |
| 43 | Debt | InsuredIndicator | ∅ | Indicates whether the instruments is backed by any kind of asset or not. | YesNoIndicator | ∅ |
| 44 | Debt | BankQualified | ∅ | Indicates whether the security is bank qualified (usually applies to loan products). | YesNoIndicator | ∅ |
| 45 | Debt | AutoReinvestment | ∅ | Indicates an instruction to reinvest dividends in the underlying security (or proceeds at maturity in a similar instrument) if the current rate equals the rate specified or better. | PercentageRate | ∅ |
| 46 | Debt | CustomDate | ∅ | Indicates an instruction to override an investment's default start and/or end date with a custom date. | DateTimePeriod | CustomDateDebt |
| 47 | Debt | LookBack | ∅ | Indicates an instruction or attribute giving the number of days to be included in the look-back period for the investment. Some options allow exercise based on the underlying asset's optimal value over the look-back period. | Number | ∅ |
| 48 | Debt | MinimumDenomination | ∅ | Indicates the minimum denomination of a security. | SecuritiesQuantity | MinimumDenominationDebt |
| 49 | Debt | MaximumSubstitution | ∅ | Maximum number of time the collateral can be substitute. | Number | ∅ |
| 50 | Debt | MinimumIncrement | ∅ | Indicates the minimum tradable increments of a security. | SecuritiesQuantity | MinimumIncrementDebt |
| 51 | Debt | Production | ∅ | Indicates a search criterion used when looking to buy a bond, particularly an mortgage back security (MBS), issued in a particular year. | Max350Text | ∅ |
| 52 | Debt | Restricted | ∅ | Identifies if the securities is restricted or not (as per Rule 144). | YesNoIndicator | ∅ |
| 53 | Debt | PriceFrequency | ∅ | Indicates the frequency at which the bond is re-rated and therefore re-priced (bond attribute, particularly of floating rate and index linked instruments). | FrequencyCode | ∅ |
| 54 | Debt | SubstitutionFrequency | ∅ | Indicates the maximum number of times collateral can be substituted. | FrequencyCode | ∅ |
| 55 | Debt | SubstitutionLeft | ∅ | Number of remaining times the collateral can be substitute. | Number | ∅ |
| 56 | Debt | WholePool | ∅ | Indicates a search criterion when looking to buy an mortgage back security (MBS) that either is [yes] or is not [no] an entire pool. | YesNoIndicator | ∅ |
| 57 | Debt | AlternativeMinimumTax | ∅ | Identifies whether the issue is subject to alternative minimum taxation (used for municipal bonds). | YesNoIndicator | ∅ |
| 58 | Debt | NextInterest | ∅ | Specifies the interest applicable to the next interest payment period. | InterestCalculation | DebtInstrument |
| 59 | Debt | ExtendibleDate | ∅ | Date/time to which a date might be extended. | ISODateTime | ∅ |
| 60 | Debt | SinkableIndicator | ∅ | Indicates whether the security is a sinkung fund. A sinking fund is a bond in which part of the total principal amount is repaid according to agreed schedules of dates, amounts and prices. | YesNoIndicator | ∅ |
| 61 | Debt | Insured | ∅ | Identifies whether the lender is assured partial or full payment by a third party if the borrower defaults. | YesNoIndicator | ∅ |
| 62 | Debt | Geographics | ∅ | Type of stipulation expressing geographical constraints on a fixed income instrument. It is expressed with a state or country abbreviation and a minimum or maximum percentage. Example: CA 0-80 (minimum of 80 percent in Californian assets). | Max35Text | ∅ |
| 63 | Debt | PaymentCurrency | ∅ | Currency of the payment. | CurrencyCode | ∅ |
| 64 | Debt | DirtyPrice | ∅ | Price that includes interest that has accrued since issue of the most recent coupon payment. | SecuritiesPricing | ∅ |
| 65 | Debt | DebtSeniority | ∅ | Seniority of a specific debt instrument, that is the order of repayment in the event of a sale or bankruptcy of the issuer of the debt. | DebtInstrumentSeniorityTypeCode | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `dda11c63c9c9363eec9ea46a58cb20d1a3fa7aac4925e867af469eec68d86fb9`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A1452:F1516 | 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516 | [src-000006 original](<../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart3_BanktoCustomerCashManagement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md>) |
| src-000016 | FullBusinessModel!A1435:F1499 | 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499 | [src-000016 original](<../../../raw-input/cash_management/ISO20022_MDRPart3_CashManagement_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md>) |
| src-000054 | FullBusinessModel!A1452:F1516 | 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516 | [src-000054 original](<../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart3_CentralCounterParty_SecuritiesClearing_Maintenance_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md>) |
| src-000081 | FullBusinessModel!A1452:F1516 | 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516 | [src-000081 original](<../../../raw-input/corporate_actions/ISO20022_MDRPart3_CorporateActions_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md>) |
| src-000097 | FullBusinessModel!A1452:F1516 | 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516 | [src-000097 original](<../../../raw-input/investment_funds/ISO20022_MDRPart3_Investment-Funds_2025_2026_v2.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md>) |
| src-000164 | FullBusinessModel!A1452:F1516 | 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516 | [src-000164 original](<../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart3_PaymentsClearingandSettlement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md>) |
| src-000175 | FullBusinessModel!A1452:F1516 | 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516 | [src-000175 original](<../../../raw-input/payments_initiation/ISO20022_MDRPart3_PaymentsInitiation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md>) |
| src-000182 | FullBusinessModel!A1435:F1499 | 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499 | [src-000182 original](<../../../raw-input/post_trade_matching/ISO20022_MDRPart3_PostTradeMatching_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md>) |
| src-000198 | FullBusinessModel!A1452:F1516 | 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516 | [src-000198 original](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart3_SettlementAndReconciliation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md>) |
| src-000322 | FullBusinessModel!A1448:F1512 | 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512 | [src-000322 original](<../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart3_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md>) |
| src-000348 | FullBusinessModel!A1448:F1512 | 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512 | [src-000348 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md>) |
| src-000352 | FullBusinessModel!A1452:F1516 | 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516 | [src-000352 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md>) |
| src-000355 | FullBusinessModel!A1424:F1488 | 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488 | [src-000355 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md>) |
| src-000367 | FullBusinessModel!A1424:F1488 | 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488 | [src-000367 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md>) |
| src-000376 | FullBusinessModel!A1452:F1516 | 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516 | [src-000376 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md>) |
| src-000382 | FullBusinessModel!A1448:F1512 | 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512 | [src-000382 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | parent | C1452 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000006 | field-type | E1453 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1454 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E1455 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E1456 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E1457 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E1458 | PercentageRate | Not a component record in this worksheet |
| src-000006 | field-type | E1459 | Max15NumericText | Not a component record in this worksheet |
| src-000006 | field-type | E1460 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1461 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1462 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1463 | PercentageRate | Not a component record in this worksheet |
| src-000006 | field-type | E1464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E1465 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E1466 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E1467 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1468 | Number | Not a component record in this worksheet |
| src-000006 | field-type | E1469 | Max350Text | Not a component record in this worksheet |
| src-000006 | field-type | E1470 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1471 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1472 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1473 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1474 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1475 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1476 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000006 | field-type | E1477 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E1478 | PercentageRate | Not a component record in this worksheet |
| src-000006 | field-type | E1479 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1480 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000006 | field-type | E1481 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E1482 | DecimalNumber | Not a component record in this worksheet |
| src-000006 | field-type | E1483 | DecimalNumber | Not a component record in this worksheet |
| src-000006 | field-type | E1484 | DecimalNumber | Not a component record in this worksheet |
| src-000006 | field-type | E1485 | DecimalNumber | Not a component record in this worksheet |
| src-000006 | field-type | E1486 | DecimalNumber | Not a component record in this worksheet |
| src-000006 | field-type | E1487 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1488 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000006 | field-type | E1489 | PercentageRate | Not a component record in this worksheet |
| src-000006 | field-type | E1490 | PercentageRate | Not a component record in this worksheet |
| src-000006 | field-type | E1491 | DecimalNumber | Not a component record in this worksheet |
| src-000006 | field-type | E1492 | DecimalNumber | Not a component record in this worksheet |
| src-000006 | field-type | E1493 | DecimalNumber | Not a component record in this worksheet |
| src-000006 | field-type | E1494 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1495 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1496 | PercentageRate | Not a component record in this worksheet |
| src-000006 | field-type | E1497 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000006 | field-type | E1498 | Number | Not a component record in this worksheet |
| src-000006 | field-type | E1499 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000006 | field-type | E1500 | Number | Not a component record in this worksheet |
| src-000006 | field-type | E1501 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000006 | field-type | E1502 | Max350Text | Not a component record in this worksheet |
| src-000006 | field-type | E1503 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1504 | FrequencyCode | Not a component record in this worksheet |
| src-000006 | field-type | E1505 | FrequencyCode | Not a component record in this worksheet |
| src-000006 | field-type | E1506 | Number | Not a component record in this worksheet |
| src-000006 | field-type | E1507 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1508 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1509 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000006 | field-type | E1510 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E1511 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1512 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E1513 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E1514 | CurrencyCode | Not a component record in this worksheet |
| src-000006 | field-type | E1515 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000006 | field-type | E1516 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000016 | parent | C1435 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000016 | field-type | E1436 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1437 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E1438 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E1439 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E1440 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E1441 | PercentageRate | Not a component record in this worksheet |
| src-000016 | field-type | E1442 | Max15NumericText | Not a component record in this worksheet |
| src-000016 | field-type | E1443 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1444 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1445 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1446 | PercentageRate | Not a component record in this worksheet |
| src-000016 | field-type | E1447 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E1448 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E1449 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E1450 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1451 | Number | Not a component record in this worksheet |
| src-000016 | field-type | E1452 | Max350Text | Not a component record in this worksheet |
| src-000016 | field-type | E1453 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1454 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1455 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1456 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1457 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1458 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1459 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000016 | field-type | E1460 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E1461 | PercentageRate | Not a component record in this worksheet |
| src-000016 | field-type | E1462 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1463 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000016 | field-type | E1464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E1465 | DecimalNumber | Not a component record in this worksheet |
| src-000016 | field-type | E1466 | DecimalNumber | Not a component record in this worksheet |
| src-000016 | field-type | E1467 | DecimalNumber | Not a component record in this worksheet |
| src-000016 | field-type | E1468 | DecimalNumber | Not a component record in this worksheet |
| src-000016 | field-type | E1469 | DecimalNumber | Not a component record in this worksheet |
| src-000016 | field-type | E1470 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1471 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000016 | field-type | E1472 | PercentageRate | Not a component record in this worksheet |
| src-000016 | field-type | E1473 | PercentageRate | Not a component record in this worksheet |
| src-000016 | field-type | E1474 | DecimalNumber | Not a component record in this worksheet |
| src-000016 | field-type | E1475 | DecimalNumber | Not a component record in this worksheet |
| src-000016 | field-type | E1476 | DecimalNumber | Not a component record in this worksheet |
| src-000016 | field-type | E1477 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1478 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1479 | PercentageRate | Not a component record in this worksheet |
| src-000016 | field-type | E1480 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000016 | field-type | E1481 | Number | Not a component record in this worksheet |
| src-000016 | field-type | E1482 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000016 | field-type | E1483 | Number | Not a component record in this worksheet |
| src-000016 | field-type | E1484 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000016 | field-type | E1485 | Max350Text | Not a component record in this worksheet |
| src-000016 | field-type | E1486 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1487 | FrequencyCode | Not a component record in this worksheet |
| src-000016 | field-type | E1488 | FrequencyCode | Not a component record in this worksheet |
| src-000016 | field-type | E1489 | Number | Not a component record in this worksheet |
| src-000016 | field-type | E1490 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1491 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1492 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000016 | field-type | E1493 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E1494 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1495 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E1496 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E1497 | CurrencyCode | Not a component record in this worksheet |
| src-000016 | field-type | E1498 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000016 | field-type | E1499 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000054 | parent | C1452 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000054 | field-type | E1453 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1454 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E1455 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E1456 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E1457 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E1458 | PercentageRate | Not a component record in this worksheet |
| src-000054 | field-type | E1459 | Max15NumericText | Not a component record in this worksheet |
| src-000054 | field-type | E1460 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1461 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1462 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1463 | PercentageRate | Not a component record in this worksheet |
| src-000054 | field-type | E1464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E1465 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E1466 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E1467 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1468 | Number | Not a component record in this worksheet |
| src-000054 | field-type | E1469 | Max350Text | Not a component record in this worksheet |
| src-000054 | field-type | E1470 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1471 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1472 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1473 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1474 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1475 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1476 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000054 | field-type | E1477 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E1478 | PercentageRate | Not a component record in this worksheet |
| src-000054 | field-type | E1479 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1480 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000054 | field-type | E1481 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E1482 | DecimalNumber | Not a component record in this worksheet |
| src-000054 | field-type | E1483 | DecimalNumber | Not a component record in this worksheet |
| src-000054 | field-type | E1484 | DecimalNumber | Not a component record in this worksheet |
| src-000054 | field-type | E1485 | DecimalNumber | Not a component record in this worksheet |
| src-000054 | field-type | E1486 | DecimalNumber | Not a component record in this worksheet |
| src-000054 | field-type | E1487 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1488 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000054 | field-type | E1489 | PercentageRate | Not a component record in this worksheet |
| src-000054 | field-type | E1490 | PercentageRate | Not a component record in this worksheet |
| src-000054 | field-type | E1491 | DecimalNumber | Not a component record in this worksheet |
| src-000054 | field-type | E1492 | DecimalNumber | Not a component record in this worksheet |
| src-000054 | field-type | E1493 | DecimalNumber | Not a component record in this worksheet |
| src-000054 | field-type | E1494 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1495 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1496 | PercentageRate | Not a component record in this worksheet |
| src-000054 | field-type | E1497 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000054 | field-type | E1498 | Number | Not a component record in this worksheet |
| src-000054 | field-type | E1499 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000054 | field-type | E1500 | Number | Not a component record in this worksheet |
| src-000054 | field-type | E1501 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000054 | field-type | E1502 | Max350Text | Not a component record in this worksheet |
| src-000054 | field-type | E1503 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1504 | FrequencyCode | Not a component record in this worksheet |
| src-000054 | field-type | E1505 | FrequencyCode | Not a component record in this worksheet |
| src-000054 | field-type | E1506 | Number | Not a component record in this worksheet |
| src-000054 | field-type | E1507 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1508 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1509 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000054 | field-type | E1510 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E1511 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1512 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E1513 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E1514 | CurrencyCode | Not a component record in this worksheet |
| src-000054 | field-type | E1515 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000054 | field-type | E1516 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000081 | parent | C1452 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000081 | field-type | E1453 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1454 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E1455 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E1456 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E1457 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E1458 | PercentageRate | Not a component record in this worksheet |
| src-000081 | field-type | E1459 | Max15NumericText | Not a component record in this worksheet |
| src-000081 | field-type | E1460 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1461 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1462 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1463 | PercentageRate | Not a component record in this worksheet |
| src-000081 | field-type | E1464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E1465 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E1466 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E1467 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1468 | Number | Not a component record in this worksheet |
| src-000081 | field-type | E1469 | Max350Text | Not a component record in this worksheet |
| src-000081 | field-type | E1470 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1471 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1472 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1473 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1474 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1475 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1476 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000081 | field-type | E1477 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E1478 | PercentageRate | Not a component record in this worksheet |
| src-000081 | field-type | E1479 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1480 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000081 | field-type | E1481 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E1482 | DecimalNumber | Not a component record in this worksheet |
| src-000081 | field-type | E1483 | DecimalNumber | Not a component record in this worksheet |
| src-000081 | field-type | E1484 | DecimalNumber | Not a component record in this worksheet |
| src-000081 | field-type | E1485 | DecimalNumber | Not a component record in this worksheet |
| src-000081 | field-type | E1486 | DecimalNumber | Not a component record in this worksheet |
| src-000081 | field-type | E1487 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1488 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000081 | field-type | E1489 | PercentageRate | Not a component record in this worksheet |
| src-000081 | field-type | E1490 | PercentageRate | Not a component record in this worksheet |
| src-000081 | field-type | E1491 | DecimalNumber | Not a component record in this worksheet |
| src-000081 | field-type | E1492 | DecimalNumber | Not a component record in this worksheet |
| src-000081 | field-type | E1493 | DecimalNumber | Not a component record in this worksheet |
| src-000081 | field-type | E1494 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1495 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1496 | PercentageRate | Not a component record in this worksheet |
| src-000081 | field-type | E1497 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000081 | field-type | E1498 | Number | Not a component record in this worksheet |
| src-000081 | field-type | E1499 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000081 | field-type | E1500 | Number | Not a component record in this worksheet |
| src-000081 | field-type | E1501 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000081 | field-type | E1502 | Max350Text | Not a component record in this worksheet |
| src-000081 | field-type | E1503 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1504 | FrequencyCode | Not a component record in this worksheet |
| src-000081 | field-type | E1505 | FrequencyCode | Not a component record in this worksheet |
| src-000081 | field-type | E1506 | Number | Not a component record in this worksheet |
| src-000081 | field-type | E1507 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1508 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1509 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000081 | field-type | E1510 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E1511 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1512 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E1513 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E1514 | CurrencyCode | Not a component record in this worksheet |
| src-000081 | field-type | E1515 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000081 | field-type | E1516 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000097 | parent | C1452 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000097 | field-type | E1453 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1454 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E1455 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E1456 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E1457 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E1458 | PercentageRate | Not a component record in this worksheet |
| src-000097 | field-type | E1459 | Max15NumericText | Not a component record in this worksheet |
| src-000097 | field-type | E1460 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1461 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1462 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1463 | PercentageRate | Not a component record in this worksheet |
| src-000097 | field-type | E1464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E1465 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E1466 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E1467 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1468 | Number | Not a component record in this worksheet |
| src-000097 | field-type | E1469 | Max350Text | Not a component record in this worksheet |
| src-000097 | field-type | E1470 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1471 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1472 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1473 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1474 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1475 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1476 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000097 | field-type | E1477 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E1478 | PercentageRate | Not a component record in this worksheet |
| src-000097 | field-type | E1479 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1480 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000097 | field-type | E1481 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E1482 | DecimalNumber | Not a component record in this worksheet |
| src-000097 | field-type | E1483 | DecimalNumber | Not a component record in this worksheet |
| src-000097 | field-type | E1484 | DecimalNumber | Not a component record in this worksheet |
| src-000097 | field-type | E1485 | DecimalNumber | Not a component record in this worksheet |
| src-000097 | field-type | E1486 | DecimalNumber | Not a component record in this worksheet |
| src-000097 | field-type | E1487 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1488 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000097 | field-type | E1489 | PercentageRate | Not a component record in this worksheet |
| src-000097 | field-type | E1490 | PercentageRate | Not a component record in this worksheet |
| src-000097 | field-type | E1491 | DecimalNumber | Not a component record in this worksheet |
| src-000097 | field-type | E1492 | DecimalNumber | Not a component record in this worksheet |
| src-000097 | field-type | E1493 | DecimalNumber | Not a component record in this worksheet |
| src-000097 | field-type | E1494 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1495 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1496 | PercentageRate | Not a component record in this worksheet |
| src-000097 | field-type | E1497 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000097 | field-type | E1498 | Number | Not a component record in this worksheet |
| src-000097 | field-type | E1499 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000097 | field-type | E1500 | Number | Not a component record in this worksheet |
| src-000097 | field-type | E1501 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000097 | field-type | E1502 | Max350Text | Not a component record in this worksheet |
| src-000097 | field-type | E1503 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1504 | FrequencyCode | Not a component record in this worksheet |
| src-000097 | field-type | E1505 | FrequencyCode | Not a component record in this worksheet |
| src-000097 | field-type | E1506 | Number | Not a component record in this worksheet |
| src-000097 | field-type | E1507 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1508 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1509 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000097 | field-type | E1510 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E1511 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1512 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E1513 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E1514 | CurrencyCode | Not a component record in this worksheet |
| src-000097 | field-type | E1515 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000097 | field-type | E1516 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000164 | parent | C1452 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000164 | field-type | E1453 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1454 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E1455 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E1456 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E1457 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E1458 | PercentageRate | Not a component record in this worksheet |
| src-000164 | field-type | E1459 | Max15NumericText | Not a component record in this worksheet |
| src-000164 | field-type | E1460 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1461 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1462 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1463 | PercentageRate | Not a component record in this worksheet |
| src-000164 | field-type | E1464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E1465 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E1466 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E1467 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1468 | Number | Not a component record in this worksheet |
| src-000164 | field-type | E1469 | Max350Text | Not a component record in this worksheet |
| src-000164 | field-type | E1470 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1471 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1472 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1473 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1474 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1475 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1476 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000164 | field-type | E1477 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E1478 | PercentageRate | Not a component record in this worksheet |
| src-000164 | field-type | E1479 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1480 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000164 | field-type | E1481 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E1482 | DecimalNumber | Not a component record in this worksheet |
| src-000164 | field-type | E1483 | DecimalNumber | Not a component record in this worksheet |
| src-000164 | field-type | E1484 | DecimalNumber | Not a component record in this worksheet |
| src-000164 | field-type | E1485 | DecimalNumber | Not a component record in this worksheet |
| src-000164 | field-type | E1486 | DecimalNumber | Not a component record in this worksheet |
| src-000164 | field-type | E1487 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1488 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000164 | field-type | E1489 | PercentageRate | Not a component record in this worksheet |
| src-000164 | field-type | E1490 | PercentageRate | Not a component record in this worksheet |
| src-000164 | field-type | E1491 | DecimalNumber | Not a component record in this worksheet |
| src-000164 | field-type | E1492 | DecimalNumber | Not a component record in this worksheet |
| src-000164 | field-type | E1493 | DecimalNumber | Not a component record in this worksheet |
| src-000164 | field-type | E1494 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1495 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1496 | PercentageRate | Not a component record in this worksheet |
| src-000164 | field-type | E1497 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000164 | field-type | E1498 | Number | Not a component record in this worksheet |
| src-000164 | field-type | E1499 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000164 | field-type | E1500 | Number | Not a component record in this worksheet |
| src-000164 | field-type | E1501 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000164 | field-type | E1502 | Max350Text | Not a component record in this worksheet |
| src-000164 | field-type | E1503 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1504 | FrequencyCode | Not a component record in this worksheet |
| src-000164 | field-type | E1505 | FrequencyCode | Not a component record in this worksheet |
| src-000164 | field-type | E1506 | Number | Not a component record in this worksheet |
| src-000164 | field-type | E1507 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1508 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1509 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000164 | field-type | E1510 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E1511 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1512 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E1513 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E1514 | CurrencyCode | Not a component record in this worksheet |
| src-000164 | field-type | E1515 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000164 | field-type | E1516 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000175 | parent | C1452 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000175 | field-type | E1453 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1454 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E1455 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E1456 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E1457 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E1458 | PercentageRate | Not a component record in this worksheet |
| src-000175 | field-type | E1459 | Max15NumericText | Not a component record in this worksheet |
| src-000175 | field-type | E1460 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1461 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1462 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1463 | PercentageRate | Not a component record in this worksheet |
| src-000175 | field-type | E1464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E1465 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E1466 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E1467 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1468 | Number | Not a component record in this worksheet |
| src-000175 | field-type | E1469 | Max350Text | Not a component record in this worksheet |
| src-000175 | field-type | E1470 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1471 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1472 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1473 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1474 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1475 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1476 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000175 | field-type | E1477 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E1478 | PercentageRate | Not a component record in this worksheet |
| src-000175 | field-type | E1479 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1480 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000175 | field-type | E1481 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E1482 | DecimalNumber | Not a component record in this worksheet |
| src-000175 | field-type | E1483 | DecimalNumber | Not a component record in this worksheet |
| src-000175 | field-type | E1484 | DecimalNumber | Not a component record in this worksheet |
| src-000175 | field-type | E1485 | DecimalNumber | Not a component record in this worksheet |
| src-000175 | field-type | E1486 | DecimalNumber | Not a component record in this worksheet |
| src-000175 | field-type | E1487 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1488 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000175 | field-type | E1489 | PercentageRate | Not a component record in this worksheet |
| src-000175 | field-type | E1490 | PercentageRate | Not a component record in this worksheet |
| src-000175 | field-type | E1491 | DecimalNumber | Not a component record in this worksheet |
| src-000175 | field-type | E1492 | DecimalNumber | Not a component record in this worksheet |
| src-000175 | field-type | E1493 | DecimalNumber | Not a component record in this worksheet |
| src-000175 | field-type | E1494 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1495 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1496 | PercentageRate | Not a component record in this worksheet |
| src-000175 | field-type | E1497 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000175 | field-type | E1498 | Number | Not a component record in this worksheet |
| src-000175 | field-type | E1499 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000175 | field-type | E1500 | Number | Not a component record in this worksheet |
| src-000175 | field-type | E1501 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000175 | field-type | E1502 | Max350Text | Not a component record in this worksheet |
| src-000175 | field-type | E1503 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1504 | FrequencyCode | Not a component record in this worksheet |
| src-000175 | field-type | E1505 | FrequencyCode | Not a component record in this worksheet |
| src-000175 | field-type | E1506 | Number | Not a component record in this worksheet |
| src-000175 | field-type | E1507 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1508 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1509 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000175 | field-type | E1510 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E1511 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1512 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E1513 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E1514 | CurrencyCode | Not a component record in this worksheet |
| src-000175 | field-type | E1515 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000175 | field-type | E1516 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000182 | parent | C1435 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000182 | field-type | E1436 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1437 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E1438 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E1439 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E1440 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E1441 | PercentageRate | Not a component record in this worksheet |
| src-000182 | field-type | E1442 | Max15NumericText | Not a component record in this worksheet |
| src-000182 | field-type | E1443 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1444 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1445 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1446 | PercentageRate | Not a component record in this worksheet |
| src-000182 | field-type | E1447 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E1448 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E1449 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E1450 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1451 | Number | Not a component record in this worksheet |
| src-000182 | field-type | E1452 | Max350Text | Not a component record in this worksheet |
| src-000182 | field-type | E1453 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1454 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1455 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1456 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1457 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1458 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1459 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000182 | field-type | E1460 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E1461 | PercentageRate | Not a component record in this worksheet |
| src-000182 | field-type | E1462 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1463 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000182 | field-type | E1464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E1465 | DecimalNumber | Not a component record in this worksheet |
| src-000182 | field-type | E1466 | DecimalNumber | Not a component record in this worksheet |
| src-000182 | field-type | E1467 | DecimalNumber | Not a component record in this worksheet |
| src-000182 | field-type | E1468 | DecimalNumber | Not a component record in this worksheet |
| src-000182 | field-type | E1469 | DecimalNumber | Not a component record in this worksheet |
| src-000182 | field-type | E1470 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1471 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000182 | field-type | E1472 | PercentageRate | Not a component record in this worksheet |
| src-000182 | field-type | E1473 | PercentageRate | Not a component record in this worksheet |
| src-000182 | field-type | E1474 | DecimalNumber | Not a component record in this worksheet |
| src-000182 | field-type | E1475 | DecimalNumber | Not a component record in this worksheet |
| src-000182 | field-type | E1476 | DecimalNumber | Not a component record in this worksheet |
| src-000182 | field-type | E1477 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1478 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1479 | PercentageRate | Not a component record in this worksheet |
| src-000182 | field-type | E1480 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000182 | field-type | E1481 | Number | Not a component record in this worksheet |
| src-000182 | field-type | E1482 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000182 | field-type | E1483 | Number | Not a component record in this worksheet |
| src-000182 | field-type | E1484 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000182 | field-type | E1485 | Max350Text | Not a component record in this worksheet |
| src-000182 | field-type | E1486 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1487 | FrequencyCode | Not a component record in this worksheet |
| src-000182 | field-type | E1488 | FrequencyCode | Not a component record in this worksheet |
| src-000182 | field-type | E1489 | Number | Not a component record in this worksheet |
| src-000182 | field-type | E1490 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1491 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1492 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000182 | field-type | E1493 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E1494 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1495 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E1496 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E1497 | CurrencyCode | Not a component record in this worksheet |
| src-000182 | field-type | E1498 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000182 | field-type | E1499 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000198 | parent | C1452 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000198 | field-type | E1453 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1454 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E1455 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E1456 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E1457 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E1458 | PercentageRate | Not a component record in this worksheet |
| src-000198 | field-type | E1459 | Max15NumericText | Not a component record in this worksheet |
| src-000198 | field-type | E1460 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1461 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1462 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1463 | PercentageRate | Not a component record in this worksheet |
| src-000198 | field-type | E1464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E1465 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E1466 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E1467 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1468 | Number | Not a component record in this worksheet |
| src-000198 | field-type | E1469 | Max350Text | Not a component record in this worksheet |
| src-000198 | field-type | E1470 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1471 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1472 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1473 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1474 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1475 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1476 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000198 | field-type | E1477 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E1478 | PercentageRate | Not a component record in this worksheet |
| src-000198 | field-type | E1479 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1480 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000198 | field-type | E1481 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E1482 | DecimalNumber | Not a component record in this worksheet |
| src-000198 | field-type | E1483 | DecimalNumber | Not a component record in this worksheet |
| src-000198 | field-type | E1484 | DecimalNumber | Not a component record in this worksheet |
| src-000198 | field-type | E1485 | DecimalNumber | Not a component record in this worksheet |
| src-000198 | field-type | E1486 | DecimalNumber | Not a component record in this worksheet |
| src-000198 | field-type | E1487 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1488 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000198 | field-type | E1489 | PercentageRate | Not a component record in this worksheet |
| src-000198 | field-type | E1490 | PercentageRate | Not a component record in this worksheet |
| src-000198 | field-type | E1491 | DecimalNumber | Not a component record in this worksheet |
| src-000198 | field-type | E1492 | DecimalNumber | Not a component record in this worksheet |
| src-000198 | field-type | E1493 | DecimalNumber | Not a component record in this worksheet |
| src-000198 | field-type | E1494 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1495 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1496 | PercentageRate | Not a component record in this worksheet |
| src-000198 | field-type | E1497 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000198 | field-type | E1498 | Number | Not a component record in this worksheet |
| src-000198 | field-type | E1499 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000198 | field-type | E1500 | Number | Not a component record in this worksheet |
| src-000198 | field-type | E1501 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000198 | field-type | E1502 | Max350Text | Not a component record in this worksheet |
| src-000198 | field-type | E1503 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1504 | FrequencyCode | Not a component record in this worksheet |
| src-000198 | field-type | E1505 | FrequencyCode | Not a component record in this worksheet |
| src-000198 | field-type | E1506 | Number | Not a component record in this worksheet |
| src-000198 | field-type | E1507 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1508 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1509 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000198 | field-type | E1510 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E1511 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1512 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E1513 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E1514 | CurrencyCode | Not a component record in this worksheet |
| src-000198 | field-type | E1515 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000198 | field-type | E1516 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000322 | parent | C1448 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000322 | field-type | E1449 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1450 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E1451 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E1452 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E1453 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E1454 | PercentageRate | Not a component record in this worksheet |
| src-000322 | field-type | E1455 | Max15NumericText | Not a component record in this worksheet |
| src-000322 | field-type | E1456 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1457 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1458 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1459 | PercentageRate | Not a component record in this worksheet |
| src-000322 | field-type | E1460 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E1461 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E1462 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E1463 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1464 | Number | Not a component record in this worksheet |
| src-000322 | field-type | E1465 | Max350Text | Not a component record in this worksheet |
| src-000322 | field-type | E1466 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1467 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1468 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1469 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1470 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1471 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1472 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000322 | field-type | E1473 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E1474 | PercentageRate | Not a component record in this worksheet |
| src-000322 | field-type | E1475 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1476 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000322 | field-type | E1477 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E1478 | DecimalNumber | Not a component record in this worksheet |
| src-000322 | field-type | E1479 | DecimalNumber | Not a component record in this worksheet |
| src-000322 | field-type | E1480 | DecimalNumber | Not a component record in this worksheet |
| src-000322 | field-type | E1481 | DecimalNumber | Not a component record in this worksheet |
| src-000322 | field-type | E1482 | DecimalNumber | Not a component record in this worksheet |
| src-000322 | field-type | E1483 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1484 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000322 | field-type | E1485 | PercentageRate | Not a component record in this worksheet |
| src-000322 | field-type | E1486 | PercentageRate | Not a component record in this worksheet |
| src-000322 | field-type | E1487 | DecimalNumber | Not a component record in this worksheet |
| src-000322 | field-type | E1488 | DecimalNumber | Not a component record in this worksheet |
| src-000322 | field-type | E1489 | DecimalNumber | Not a component record in this worksheet |
| src-000322 | field-type | E1490 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1491 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1492 | PercentageRate | Not a component record in this worksheet |
| src-000322 | field-type | E1493 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000322 | field-type | E1494 | Number | Not a component record in this worksheet |
| src-000322 | field-type | E1495 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000322 | field-type | E1496 | Number | Not a component record in this worksheet |
| src-000322 | field-type | E1497 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000322 | field-type | E1498 | Max350Text | Not a component record in this worksheet |
| src-000322 | field-type | E1499 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1500 | FrequencyCode | Not a component record in this worksheet |
| src-000322 | field-type | E1501 | FrequencyCode | Not a component record in this worksheet |
| src-000322 | field-type | E1502 | Number | Not a component record in this worksheet |
| src-000322 | field-type | E1503 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1504 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1505 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000322 | field-type | E1506 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E1507 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1508 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E1509 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E1510 | CurrencyCode | Not a component record in this worksheet |
| src-000322 | field-type | E1511 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000322 | field-type | E1512 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000348 | parent | C1448 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000348 | field-type | E1449 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1450 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E1451 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E1452 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E1453 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E1454 | PercentageRate | Not a component record in this worksheet |
| src-000348 | field-type | E1455 | Max15NumericText | Not a component record in this worksheet |
| src-000348 | field-type | E1456 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1457 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1458 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1459 | PercentageRate | Not a component record in this worksheet |
| src-000348 | field-type | E1460 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E1461 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E1462 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E1463 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1464 | Number | Not a component record in this worksheet |
| src-000348 | field-type | E1465 | Max350Text | Not a component record in this worksheet |
| src-000348 | field-type | E1466 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1467 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1468 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1469 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1470 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1471 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1472 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000348 | field-type | E1473 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E1474 | PercentageRate | Not a component record in this worksheet |
| src-000348 | field-type | E1475 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1476 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000348 | field-type | E1477 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E1478 | DecimalNumber | Not a component record in this worksheet |
| src-000348 | field-type | E1479 | DecimalNumber | Not a component record in this worksheet |
| src-000348 | field-type | E1480 | DecimalNumber | Not a component record in this worksheet |
| src-000348 | field-type | E1481 | DecimalNumber | Not a component record in this worksheet |
| src-000348 | field-type | E1482 | DecimalNumber | Not a component record in this worksheet |
| src-000348 | field-type | E1483 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1484 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000348 | field-type | E1485 | PercentageRate | Not a component record in this worksheet |
| src-000348 | field-type | E1486 | PercentageRate | Not a component record in this worksheet |
| src-000348 | field-type | E1487 | DecimalNumber | Not a component record in this worksheet |
| src-000348 | field-type | E1488 | DecimalNumber | Not a component record in this worksheet |
| src-000348 | field-type | E1489 | DecimalNumber | Not a component record in this worksheet |
| src-000348 | field-type | E1490 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1491 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1492 | PercentageRate | Not a component record in this worksheet |
| src-000348 | field-type | E1493 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000348 | field-type | E1494 | Number | Not a component record in this worksheet |
| src-000348 | field-type | E1495 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000348 | field-type | E1496 | Number | Not a component record in this worksheet |
| src-000348 | field-type | E1497 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000348 | field-type | E1498 | Max350Text | Not a component record in this worksheet |
| src-000348 | field-type | E1499 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1500 | FrequencyCode | Not a component record in this worksheet |
| src-000348 | field-type | E1501 | FrequencyCode | Not a component record in this worksheet |
| src-000348 | field-type | E1502 | Number | Not a component record in this worksheet |
| src-000348 | field-type | E1503 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1504 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1505 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000348 | field-type | E1506 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E1507 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1508 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E1509 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E1510 | CurrencyCode | Not a component record in this worksheet |
| src-000348 | field-type | E1511 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000348 | field-type | E1512 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000352 | parent | C1452 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000352 | field-type | E1453 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1454 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E1455 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E1456 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E1457 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E1458 | PercentageRate | Not a component record in this worksheet |
| src-000352 | field-type | E1459 | Max15NumericText | Not a component record in this worksheet |
| src-000352 | field-type | E1460 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1461 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1462 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1463 | PercentageRate | Not a component record in this worksheet |
| src-000352 | field-type | E1464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E1465 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E1466 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E1467 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1468 | Number | Not a component record in this worksheet |
| src-000352 | field-type | E1469 | Max350Text | Not a component record in this worksheet |
| src-000352 | field-type | E1470 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1471 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1472 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1473 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1474 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1475 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1476 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000352 | field-type | E1477 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E1478 | PercentageRate | Not a component record in this worksheet |
| src-000352 | field-type | E1479 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1480 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000352 | field-type | E1481 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E1482 | DecimalNumber | Not a component record in this worksheet |
| src-000352 | field-type | E1483 | DecimalNumber | Not a component record in this worksheet |
| src-000352 | field-type | E1484 | DecimalNumber | Not a component record in this worksheet |
| src-000352 | field-type | E1485 | DecimalNumber | Not a component record in this worksheet |
| src-000352 | field-type | E1486 | DecimalNumber | Not a component record in this worksheet |
| src-000352 | field-type | E1487 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1488 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000352 | field-type | E1489 | PercentageRate | Not a component record in this worksheet |
| src-000352 | field-type | E1490 | PercentageRate | Not a component record in this worksheet |
| src-000352 | field-type | E1491 | DecimalNumber | Not a component record in this worksheet |
| src-000352 | field-type | E1492 | DecimalNumber | Not a component record in this worksheet |
| src-000352 | field-type | E1493 | DecimalNumber | Not a component record in this worksheet |
| src-000352 | field-type | E1494 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1495 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1496 | PercentageRate | Not a component record in this worksheet |
| src-000352 | field-type | E1497 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000352 | field-type | E1498 | Number | Not a component record in this worksheet |
| src-000352 | field-type | E1499 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000352 | field-type | E1500 | Number | Not a component record in this worksheet |
| src-000352 | field-type | E1501 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000352 | field-type | E1502 | Max350Text | Not a component record in this worksheet |
| src-000352 | field-type | E1503 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1504 | FrequencyCode | Not a component record in this worksheet |
| src-000352 | field-type | E1505 | FrequencyCode | Not a component record in this worksheet |
| src-000352 | field-type | E1506 | Number | Not a component record in this worksheet |
| src-000352 | field-type | E1507 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1508 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1509 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000352 | field-type | E1510 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E1511 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1512 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E1513 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E1514 | CurrencyCode | Not a component record in this worksheet |
| src-000352 | field-type | E1515 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000352 | field-type | E1516 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000355 | parent | C1424 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000355 | field-type | E1425 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1426 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E1427 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E1428 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E1429 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E1430 | PercentageRate | Not a component record in this worksheet |
| src-000355 | field-type | E1431 | Max15NumericText | Not a component record in this worksheet |
| src-000355 | field-type | E1432 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1433 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1434 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1435 | PercentageRate | Not a component record in this worksheet |
| src-000355 | field-type | E1436 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E1437 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E1438 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E1439 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1440 | Number | Not a component record in this worksheet |
| src-000355 | field-type | E1441 | Max350Text | Not a component record in this worksheet |
| src-000355 | field-type | E1442 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1443 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1444 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1445 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1446 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1447 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1448 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000355 | field-type | E1449 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E1450 | PercentageRate | Not a component record in this worksheet |
| src-000355 | field-type | E1451 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1452 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000355 | field-type | E1453 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E1454 | DecimalNumber | Not a component record in this worksheet |
| src-000355 | field-type | E1455 | DecimalNumber | Not a component record in this worksheet |
| src-000355 | field-type | E1456 | DecimalNumber | Not a component record in this worksheet |
| src-000355 | field-type | E1457 | DecimalNumber | Not a component record in this worksheet |
| src-000355 | field-type | E1458 | DecimalNumber | Not a component record in this worksheet |
| src-000355 | field-type | E1459 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1460 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000355 | field-type | E1461 | PercentageRate | Not a component record in this worksheet |
| src-000355 | field-type | E1462 | PercentageRate | Not a component record in this worksheet |
| src-000355 | field-type | E1463 | DecimalNumber | Not a component record in this worksheet |
| src-000355 | field-type | E1464 | DecimalNumber | Not a component record in this worksheet |
| src-000355 | field-type | E1465 | DecimalNumber | Not a component record in this worksheet |
| src-000355 | field-type | E1466 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1467 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1468 | PercentageRate | Not a component record in this worksheet |
| src-000355 | field-type | E1469 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000355 | field-type | E1470 | Number | Not a component record in this worksheet |
| src-000355 | field-type | E1471 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000355 | field-type | E1472 | Number | Not a component record in this worksheet |
| src-000355 | field-type | E1473 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000355 | field-type | E1474 | Max350Text | Not a component record in this worksheet |
| src-000355 | field-type | E1475 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1476 | FrequencyCode | Not a component record in this worksheet |
| src-000355 | field-type | E1477 | FrequencyCode | Not a component record in this worksheet |
| src-000355 | field-type | E1478 | Number | Not a component record in this worksheet |
| src-000355 | field-type | E1479 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1480 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1481 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000355 | field-type | E1482 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E1483 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1484 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E1485 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E1486 | CurrencyCode | Not a component record in this worksheet |
| src-000355 | field-type | E1487 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000355 | field-type | E1488 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000367 | parent | C1424 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000367 | field-type | E1425 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1426 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E1427 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E1428 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E1429 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E1430 | PercentageRate | Not a component record in this worksheet |
| src-000367 | field-type | E1431 | Max15NumericText | Not a component record in this worksheet |
| src-000367 | field-type | E1432 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1433 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1434 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1435 | PercentageRate | Not a component record in this worksheet |
| src-000367 | field-type | E1436 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E1437 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E1438 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E1439 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1440 | Number | Not a component record in this worksheet |
| src-000367 | field-type | E1441 | Max350Text | Not a component record in this worksheet |
| src-000367 | field-type | E1442 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1443 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1444 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1445 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1446 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1447 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1448 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000367 | field-type | E1449 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E1450 | PercentageRate | Not a component record in this worksheet |
| src-000367 | field-type | E1451 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1452 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000367 | field-type | E1453 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E1454 | DecimalNumber | Not a component record in this worksheet |
| src-000367 | field-type | E1455 | DecimalNumber | Not a component record in this worksheet |
| src-000367 | field-type | E1456 | DecimalNumber | Not a component record in this worksheet |
| src-000367 | field-type | E1457 | DecimalNumber | Not a component record in this worksheet |
| src-000367 | field-type | E1458 | DecimalNumber | Not a component record in this worksheet |
| src-000367 | field-type | E1459 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1460 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000367 | field-type | E1461 | PercentageRate | Not a component record in this worksheet |
| src-000367 | field-type | E1462 | PercentageRate | Not a component record in this worksheet |
| src-000367 | field-type | E1463 | DecimalNumber | Not a component record in this worksheet |
| src-000367 | field-type | E1464 | DecimalNumber | Not a component record in this worksheet |
| src-000367 | field-type | E1465 | DecimalNumber | Not a component record in this worksheet |
| src-000367 | field-type | E1466 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1467 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1468 | PercentageRate | Not a component record in this worksheet |
| src-000367 | field-type | E1469 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000367 | field-type | E1470 | Number | Not a component record in this worksheet |
| src-000367 | field-type | E1471 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000367 | field-type | E1472 | Number | Not a component record in this worksheet |
| src-000367 | field-type | E1473 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000367 | field-type | E1474 | Max350Text | Not a component record in this worksheet |
| src-000367 | field-type | E1475 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1476 | FrequencyCode | Not a component record in this worksheet |
| src-000367 | field-type | E1477 | FrequencyCode | Not a component record in this worksheet |
| src-000367 | field-type | E1478 | Number | Not a component record in this worksheet |
| src-000367 | field-type | E1479 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1480 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1481 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000367 | field-type | E1482 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E1483 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1484 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E1485 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E1486 | CurrencyCode | Not a component record in this worksheet |
| src-000367 | field-type | E1487 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000367 | field-type | E1488 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000376 | parent | C1452 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000376 | field-type | E1453 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1454 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E1455 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E1456 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E1457 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E1458 | PercentageRate | Not a component record in this worksheet |
| src-000376 | field-type | E1459 | Max15NumericText | Not a component record in this worksheet |
| src-000376 | field-type | E1460 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1461 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1462 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1463 | PercentageRate | Not a component record in this worksheet |
| src-000376 | field-type | E1464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E1465 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E1466 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E1467 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1468 | Number | Not a component record in this worksheet |
| src-000376 | field-type | E1469 | Max350Text | Not a component record in this worksheet |
| src-000376 | field-type | E1470 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1471 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1472 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1473 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1474 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1475 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1476 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000376 | field-type | E1477 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E1478 | PercentageRate | Not a component record in this worksheet |
| src-000376 | field-type | E1479 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1480 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000376 | field-type | E1481 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E1482 | DecimalNumber | Not a component record in this worksheet |
| src-000376 | field-type | E1483 | DecimalNumber | Not a component record in this worksheet |
| src-000376 | field-type | E1484 | DecimalNumber | Not a component record in this worksheet |
| src-000376 | field-type | E1485 | DecimalNumber | Not a component record in this worksheet |
| src-000376 | field-type | E1486 | DecimalNumber | Not a component record in this worksheet |
| src-000376 | field-type | E1487 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1488 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000376 | field-type | E1489 | PercentageRate | Not a component record in this worksheet |
| src-000376 | field-type | E1490 | PercentageRate | Not a component record in this worksheet |
| src-000376 | field-type | E1491 | DecimalNumber | Not a component record in this worksheet |
| src-000376 | field-type | E1492 | DecimalNumber | Not a component record in this worksheet |
| src-000376 | field-type | E1493 | DecimalNumber | Not a component record in this worksheet |
| src-000376 | field-type | E1494 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1495 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1496 | PercentageRate | Not a component record in this worksheet |
| src-000376 | field-type | E1497 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000376 | field-type | E1498 | Number | Not a component record in this worksheet |
| src-000376 | field-type | E1499 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000376 | field-type | E1500 | Number | Not a component record in this worksheet |
| src-000376 | field-type | E1501 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000376 | field-type | E1502 | Max350Text | Not a component record in this worksheet |
| src-000376 | field-type | E1503 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1504 | FrequencyCode | Not a component record in this worksheet |
| src-000376 | field-type | E1505 | FrequencyCode | Not a component record in this worksheet |
| src-000376 | field-type | E1506 | Number | Not a component record in this worksheet |
| src-000376 | field-type | E1507 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1508 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1509 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000376 | field-type | E1510 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E1511 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1512 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E1513 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E1514 | CurrencyCode | Not a component record in this worksheet |
| src-000376 | field-type | E1515 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000376 | field-type | E1516 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |
| src-000382 | parent | C1448 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000382 | field-type | E1449 | PaymentDirectionIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1450 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E1451 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E1452 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E1453 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E1454 | PercentageRate | Not a component record in this worksheet |
| src-000382 | field-type | E1455 | Max15NumericText | Not a component record in this worksheet |
| src-000382 | field-type | E1456 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1457 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1458 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1459 | PercentageRate | Not a component record in this worksheet |
| src-000382 | field-type | E1460 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E1461 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E1462 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E1463 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1464 | Number | Not a component record in this worksheet |
| src-000382 | field-type | E1465 | Max350Text | Not a component record in this worksheet |
| src-000382 | field-type | E1466 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1467 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1468 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1469 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1470 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1471 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1472 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000382 | field-type | E1473 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E1474 | PercentageRate | Not a component record in this worksheet |
| src-000382 | field-type | E1475 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1476 | DistributionPolicyCode | Not a component record in this worksheet |
| src-000382 | field-type | E1477 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E1478 | DecimalNumber | Not a component record in this worksheet |
| src-000382 | field-type | E1479 | DecimalNumber | Not a component record in this worksheet |
| src-000382 | field-type | E1480 | DecimalNumber | Not a component record in this worksheet |
| src-000382 | field-type | E1481 | DecimalNumber | Not a component record in this worksheet |
| src-000382 | field-type | E1482 | DecimalNumber | Not a component record in this worksheet |
| src-000382 | field-type | E1483 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1484 | PrePaymentSpeedCode | Not a component record in this worksheet |
| src-000382 | field-type | E1485 | PercentageRate | Not a component record in this worksheet |
| src-000382 | field-type | E1486 | PercentageRate | Not a component record in this worksheet |
| src-000382 | field-type | E1487 | DecimalNumber | Not a component record in this worksheet |
| src-000382 | field-type | E1488 | DecimalNumber | Not a component record in this worksheet |
| src-000382 | field-type | E1489 | DecimalNumber | Not a component record in this worksheet |
| src-000382 | field-type | E1490 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1491 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1492 | PercentageRate | Not a component record in this worksheet |
| src-000382 | field-type | E1493 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000382 | field-type | E1494 | Number | Not a component record in this worksheet |
| src-000382 | field-type | E1495 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000382 | field-type | E1496 | Number | Not a component record in this worksheet |
| src-000382 | field-type | E1497 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000382 | field-type | E1498 | Max350Text | Not a component record in this worksheet |
| src-000382 | field-type | E1499 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1500 | FrequencyCode | Not a component record in this worksheet |
| src-000382 | field-type | E1501 | FrequencyCode | Not a component record in this worksheet |
| src-000382 | field-type | E1502 | Number | Not a component record in this worksheet |
| src-000382 | field-type | E1503 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1504 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1505 | InterestCalculation | [InterestCalculation](<bc-38534959a5f65ef56096.md>) |
| src-000382 | field-type | E1506 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E1507 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1508 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E1509 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E1510 | CurrencyCode | Not a component record in this worksheet |
| src-000382 | field-type | E1511 | SecuritiesPricing | [SecuritiesPricing](<bc-7300499c86791ac12ffd.md>) |
| src-000382 | field-type | E1512 | DebtInstrumentSeniorityTypeCode | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
