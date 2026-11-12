---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-9fb857d7f47b6f3c7dae"
title: "Distribution"
business_component_name: "Distribution"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A1621:F1644"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A1596:F1619"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A1621:F1644"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A1621:F1644"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A1621:F1644"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A1621:F1644"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A1621:F1644"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A1596:F1619"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A1621:F1644"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A1609:F1632"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A4064:F4087"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A1609:F1632"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A1621:F1644"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A1585:F1608"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A4064:F4087"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A4064:F4087"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A1585:F1608"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A1585:F1608"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A4064:F4087"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A4064:F4087"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A1621:F1644"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A4064:F4087"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A1609:F1632"]}]
content_sha256: "9fb857d7f47b6f3c7daedc77cc08cd5aaa58ad246d8ab3f985ae55d5acd23628"
parent_names: []
related_component_names: ["CorporateActionOptionCode", "CurrencyAndAmount", "CurrencyCode", "DateTimePeriod", "Dividend", "ISODateTime", "IncentivePremium", "Max350Text", "PercentageRate", "SecuritiesPricing", "Tax"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# Distribution

## Definition

Distributions in cash and/or securities following a corporate event.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Distribution | ∅ | ∅ | Distributions in cash and/or securities following a corporate event. | ∅ | ∅ |
| 2 | Distribution | ExercisePeriod | ∅ | Period during which the right and/or privilege on an underlying financial instrument may be executed. | DateTimePeriod | ExercisePeriodDistribution |
| 3 | Distribution | OfferPeriod | ∅ | Period during which an open offer remains valid. | DateTimePeriod | OfferPeriodDistribution |
| 4 | Distribution | TradingPeriod | ∅ | Period during which a financial instrument is available for trading. | DateTimePeriod | TradingPeriodDistribution |
| 5 | Distribution | BlockingPeriod | ∅ | Period, set by the issuer, during which the security is blocked, ie, not available for exchange. | DateTimePeriod | BlockingPeriodDistribution |
| 6 | Distribution | InterestPeriod | ∅ | Period during which interest has accrued. | DateTimePeriod | CashDistribution |
| 7 | Distribution | DistributionTax | ∅ | Provides the tax description associated with the corporate event. | Tax | RelatedCorporateActionDistribution |
| 8 | Distribution | OfferPrice | ∅ | Price, determined by the offerer, at which the investor is entitled to take part in an event. | SecuritiesPricing | Distribution |
| 9 | Distribution | IncentivePremium | ∅ | Cash premium made available to encourage participation by a certain deadline (avoids to have a second call). | IncentivePremium | CorporateActionDistribution |
| 10 | Distribution | EffectiveDate | ∅ | Date/time at which the event or part of the event, for example, an option, becomes valid and should be processed and/or applied to holdings. | ISODateTime | ∅ |
| 11 | Distribution | EventConditions | ∅ | Conditions that the issuer has placed on the completion of the event, for example, tender percentage required. | Max350Text | ∅ |
| 12 | Distribution | ExDate | ∅ | Date/time as from which trading (including exchange and OTC trading) occurs on the underlying security without the benefit. | ISODateTime | ∅ |
| 13 | Distribution | GrossRate | ∅ | Percentage paid before deductions and/or allowances have been made. | PercentageRate | ∅ |
| 14 | Distribution | MeetingDate | ∅ | Date/time at which the meeting will take place. | ISODateTime | ∅ |
| 15 | Distribution | NetRate | ∅ | Percentage paid after deductions and/or allowances have been made. | PercentageRate | ∅ |
| 16 | Distribution | NewFaceValue | ∅ | New unit value of a debt security. | CurrencyAndAmount | ∅ |
| 17 | Distribution | NewParValue | ∅ | New nominal value of an equity security. | CurrencyAndAmount | ∅ |
| 18 | Distribution | PaymentDate | ∅ | Date/time at which the distribution is due to take place (cash and/or securities). | ISODateTime | ∅ |
| 19 | Distribution | Dividend | ∅ | Dividend per financial instrument. | Dividend | RelatedDistribution |
| 20 | Distribution | CorporateActionOption | ∅ | Specifies information about the choices offered to the holder of a corporate action. | CorporateActionOptionCode | ∅ |
| 21 | Distribution | CurrencyOption | ∅ | Currency choice given to the investor. | CurrencyCode | ∅ |
| 22 | Distribution | DecreaseAmount | ∅ | Amount by which the issuer devalues a share  (in a decrease value event). | CurrencyAndAmount | ∅ |
| 23 | Distribution | DecreaseRate | ∅ | Amount, expressed as a percentage, by which the issuer devalues a share  (in a decrease value event). | PercentageRate | ∅ |
| 24 | Distribution | OfferPriceFixingDate | ∅ | Date/time at which an offer price is determined (as compared to its reset date if applicable). | ISODateTime | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `9fb857d7f47b6f3c7daedc77cc08cd5aaa58ad246d8ab3f985ae55d5acd23628`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A1621:F1644 | 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644 | [src-000006 original](../../../evidence/omitted/5e0f6b7d43fcbbe816624756.md) | [Lookup](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md) |
| src-000016 | FullBusinessModel!A1596:F1619 | 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619 | [src-000016 original](../../../evidence/omitted/42cf3c4088baf4d4c6dc07c1.md) | [Lookup](../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md) |
| src-000054 | FullBusinessModel!A1621:F1644 | 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644 | [src-000054 original](../../../evidence/omitted/ea96e6afbf1f8819d68ca6f6.md) | [Lookup](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md) |
| src-000081 | FullBusinessModel!A1621:F1644 | 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644 | [src-000081 original](../../../evidence/omitted/5d05ada13720516836bc5043.md) | [Lookup](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md) |
| src-000097 | FullBusinessModel!A1621:F1644 | 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644 | [src-000097 original](../../../evidence/omitted/3ea6002607634c1b65cb5c88.md) | [Lookup](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md) |
| src-000164 | FullBusinessModel!A1621:F1644 | 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644 | [src-000164 original](../../../evidence/omitted/87020353dd81a550a7b6ed6f.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md) |
| src-000175 | FullBusinessModel!A1621:F1644 | 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644 | [src-000175 original](../../../evidence/omitted/807236f9f4d5f25826f3ba17.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md) |
| src-000182 | FullBusinessModel!A1596:F1619 | 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619 | [src-000182 original](../../../evidence/omitted/5096efb167050baf43bfb32a.md) | [Lookup](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md) |
| src-000198 | FullBusinessModel!A1621:F1644 | 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644 | [src-000198 original](../../../evidence/omitted/c6a84c22fb63cab3b848bd88.md) | [Lookup](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md) |
| src-000322 | FullBusinessModel!A1609:F1632 | 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632 | [src-000322 original](../../../evidence/omitted/f39eee3c04bb287d206cc6a3.md) | [Lookup](../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md) |
| src-000345 | FullBusinessModel!A4064:F4087 | 4064, 4065, 4066, 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087 | [src-000345 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md) |
| src-000348 | FullBusinessModel!A1609:F1632 | 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632 | [src-000348 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md) |
| src-000352 | FullBusinessModel!A1621:F1644 | 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644 | [src-000352 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md) |
| src-000355 | FullBusinessModel!A1585:F1608 | 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608 | [src-000355 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md) |
| src-000358 | FullBusinessModel!A4064:F4087 | 4064, 4065, 4066, 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087 | [src-000358 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md) |
| src-000361 | FullBusinessModel!A4064:F4087 | 4064, 4065, 4066, 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087 | [src-000361 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md) |
| src-000364 | FullBusinessModel!A1585:F1608 | 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608 | [src-000364 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md) |
| src-000367 | FullBusinessModel!A1585:F1608 | 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608 | [src-000367 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md) |
| src-000370 | FullBusinessModel!A4064:F4087 | 4064, 4065, 4066, 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087 | [src-000370 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md) |
| src-000373 | FullBusinessModel!A4064:F4087 | 4064, 4065, 4066, 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087 | [src-000373 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md) |
| src-000376 | FullBusinessModel!A1621:F1644 | 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644 | [src-000376 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md) |
| src-000379 | FullBusinessModel!A4064:F4087 | 4064, 4065, 4066, 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087 | [src-000379 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md) |
| src-000382 | FullBusinessModel!A1609:F1632 | 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632 | [src-000382 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | field-type | E1622 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000006 | field-type | E1623 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000006 | field-type | E1624 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000006 | field-type | E1625 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000006 | field-type | E1626 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000006 | field-type | E1627 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000006 | field-type | E1628 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000006 | field-type | E1629 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000006 | field-type | E1630 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E1631 | Max350Text | Not a component record in this worksheet |
| src-000006 | field-type | E1632 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E1633 | PercentageRate | Not a component record in this worksheet |
| src-000006 | field-type | E1634 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E1635 | PercentageRate | Not a component record in this worksheet |
| src-000006 | field-type | E1636 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E1637 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E1638 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E1639 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000006 | field-type | E1640 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000006 | field-type | E1641 | CurrencyCode | Not a component record in this worksheet |
| src-000006 | field-type | E1642 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E1643 | PercentageRate | Not a component record in this worksheet |
| src-000006 | field-type | E1644 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E1597 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000016 | field-type | E1598 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000016 | field-type | E1599 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000016 | field-type | E1600 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000016 | field-type | E1601 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000016 | field-type | E1602 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000016 | field-type | E1603 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000016 | field-type | E1604 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000016 | field-type | E1605 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E1606 | Max350Text | Not a component record in this worksheet |
| src-000016 | field-type | E1607 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E1608 | PercentageRate | Not a component record in this worksheet |
| src-000016 | field-type | E1609 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E1610 | PercentageRate | Not a component record in this worksheet |
| src-000016 | field-type | E1611 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E1612 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E1613 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E1614 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000016 | field-type | E1615 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000016 | field-type | E1616 | CurrencyCode | Not a component record in this worksheet |
| src-000016 | field-type | E1617 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E1618 | PercentageRate | Not a component record in this worksheet |
| src-000016 | field-type | E1619 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E1622 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000054 | field-type | E1623 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000054 | field-type | E1624 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000054 | field-type | E1625 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000054 | field-type | E1626 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000054 | field-type | E1627 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000054 | field-type | E1628 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000054 | field-type | E1629 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000054 | field-type | E1630 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E1631 | Max350Text | Not a component record in this worksheet |
| src-000054 | field-type | E1632 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E1633 | PercentageRate | Not a component record in this worksheet |
| src-000054 | field-type | E1634 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E1635 | PercentageRate | Not a component record in this worksheet |
| src-000054 | field-type | E1636 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E1637 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E1638 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E1639 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000054 | field-type | E1640 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000054 | field-type | E1641 | CurrencyCode | Not a component record in this worksheet |
| src-000054 | field-type | E1642 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E1643 | PercentageRate | Not a component record in this worksheet |
| src-000054 | field-type | E1644 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E1622 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000081 | field-type | E1623 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000081 | field-type | E1624 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000081 | field-type | E1625 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000081 | field-type | E1626 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000081 | field-type | E1627 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000081 | field-type | E1628 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000081 | field-type | E1629 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000081 | field-type | E1630 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E1631 | Max350Text | Not a component record in this worksheet |
| src-000081 | field-type | E1632 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E1633 | PercentageRate | Not a component record in this worksheet |
| src-000081 | field-type | E1634 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E1635 | PercentageRate | Not a component record in this worksheet |
| src-000081 | field-type | E1636 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E1637 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E1638 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E1639 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000081 | field-type | E1640 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000081 | field-type | E1641 | CurrencyCode | Not a component record in this worksheet |
| src-000081 | field-type | E1642 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E1643 | PercentageRate | Not a component record in this worksheet |
| src-000081 | field-type | E1644 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E1622 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000097 | field-type | E1623 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000097 | field-type | E1624 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000097 | field-type | E1625 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000097 | field-type | E1626 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000097 | field-type | E1627 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000097 | field-type | E1628 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000097 | field-type | E1629 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000097 | field-type | E1630 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E1631 | Max350Text | Not a component record in this worksheet |
| src-000097 | field-type | E1632 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E1633 | PercentageRate | Not a component record in this worksheet |
| src-000097 | field-type | E1634 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E1635 | PercentageRate | Not a component record in this worksheet |
| src-000097 | field-type | E1636 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E1637 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E1638 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E1639 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000097 | field-type | E1640 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000097 | field-type | E1641 | CurrencyCode | Not a component record in this worksheet |
| src-000097 | field-type | E1642 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E1643 | PercentageRate | Not a component record in this worksheet |
| src-000097 | field-type | E1644 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E1622 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000164 | field-type | E1623 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000164 | field-type | E1624 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000164 | field-type | E1625 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000164 | field-type | E1626 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000164 | field-type | E1627 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000164 | field-type | E1628 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000164 | field-type | E1629 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000164 | field-type | E1630 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E1631 | Max350Text | Not a component record in this worksheet |
| src-000164 | field-type | E1632 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E1633 | PercentageRate | Not a component record in this worksheet |
| src-000164 | field-type | E1634 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E1635 | PercentageRate | Not a component record in this worksheet |
| src-000164 | field-type | E1636 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E1637 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E1638 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E1639 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000164 | field-type | E1640 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000164 | field-type | E1641 | CurrencyCode | Not a component record in this worksheet |
| src-000164 | field-type | E1642 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E1643 | PercentageRate | Not a component record in this worksheet |
| src-000164 | field-type | E1644 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E1622 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000175 | field-type | E1623 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000175 | field-type | E1624 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000175 | field-type | E1625 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000175 | field-type | E1626 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000175 | field-type | E1627 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000175 | field-type | E1628 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000175 | field-type | E1629 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000175 | field-type | E1630 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E1631 | Max350Text | Not a component record in this worksheet |
| src-000175 | field-type | E1632 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E1633 | PercentageRate | Not a component record in this worksheet |
| src-000175 | field-type | E1634 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E1635 | PercentageRate | Not a component record in this worksheet |
| src-000175 | field-type | E1636 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E1637 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E1638 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E1639 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000175 | field-type | E1640 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000175 | field-type | E1641 | CurrencyCode | Not a component record in this worksheet |
| src-000175 | field-type | E1642 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E1643 | PercentageRate | Not a component record in this worksheet |
| src-000175 | field-type | E1644 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E1597 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000182 | field-type | E1598 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000182 | field-type | E1599 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000182 | field-type | E1600 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000182 | field-type | E1601 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000182 | field-type | E1602 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000182 | field-type | E1603 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000182 | field-type | E1604 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000182 | field-type | E1605 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E1606 | Max350Text | Not a component record in this worksheet |
| src-000182 | field-type | E1607 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E1608 | PercentageRate | Not a component record in this worksheet |
| src-000182 | field-type | E1609 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E1610 | PercentageRate | Not a component record in this worksheet |
| src-000182 | field-type | E1611 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E1612 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E1613 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E1614 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000182 | field-type | E1615 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000182 | field-type | E1616 | CurrencyCode | Not a component record in this worksheet |
| src-000182 | field-type | E1617 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E1618 | PercentageRate | Not a component record in this worksheet |
| src-000182 | field-type | E1619 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E1622 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000198 | field-type | E1623 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000198 | field-type | E1624 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000198 | field-type | E1625 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000198 | field-type | E1626 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000198 | field-type | E1627 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000198 | field-type | E1628 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000198 | field-type | E1629 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000198 | field-type | E1630 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E1631 | Max350Text | Not a component record in this worksheet |
| src-000198 | field-type | E1632 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E1633 | PercentageRate | Not a component record in this worksheet |
| src-000198 | field-type | E1634 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E1635 | PercentageRate | Not a component record in this worksheet |
| src-000198 | field-type | E1636 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E1637 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E1638 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E1639 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000198 | field-type | E1640 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000198 | field-type | E1641 | CurrencyCode | Not a component record in this worksheet |
| src-000198 | field-type | E1642 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E1643 | PercentageRate | Not a component record in this worksheet |
| src-000198 | field-type | E1644 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E1610 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000322 | field-type | E1611 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000322 | field-type | E1612 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000322 | field-type | E1613 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000322 | field-type | E1614 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000322 | field-type | E1615 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000322 | field-type | E1616 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000322 | field-type | E1617 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000322 | field-type | E1618 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E1619 | Max350Text | Not a component record in this worksheet |
| src-000322 | field-type | E1620 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E1621 | PercentageRate | Not a component record in this worksheet |
| src-000322 | field-type | E1622 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E1623 | PercentageRate | Not a component record in this worksheet |
| src-000322 | field-type | E1624 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E1625 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E1626 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E1627 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000322 | field-type | E1628 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000322 | field-type | E1629 | CurrencyCode | Not a component record in this worksheet |
| src-000322 | field-type | E1630 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E1631 | PercentageRate | Not a component record in this worksheet |
| src-000322 | field-type | E1632 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E4065 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000345 | field-type | E4066 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000345 | field-type | E4067 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000345 | field-type | E4068 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000345 | field-type | E4069 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000345 | field-type | E4070 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000345 | field-type | E4071 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000345 | field-type | E4072 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000345 | field-type | E4073 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E4074 | Max350Text | Not a component record in this worksheet |
| src-000345 | field-type | E4075 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E4076 | PercentageRate | Not a component record in this worksheet |
| src-000345 | field-type | E4077 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E4078 | PercentageRate | Not a component record in this worksheet |
| src-000345 | field-type | E4079 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E4080 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E4081 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E4082 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000345 | field-type | E4083 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000345 | field-type | E4084 | CurrencyCode | Not a component record in this worksheet |
| src-000345 | field-type | E4085 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E4086 | PercentageRate | Not a component record in this worksheet |
| src-000345 | field-type | E4087 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E1610 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000348 | field-type | E1611 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000348 | field-type | E1612 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000348 | field-type | E1613 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000348 | field-type | E1614 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000348 | field-type | E1615 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000348 | field-type | E1616 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000348 | field-type | E1617 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000348 | field-type | E1618 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E1619 | Max350Text | Not a component record in this worksheet |
| src-000348 | field-type | E1620 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E1621 | PercentageRate | Not a component record in this worksheet |
| src-000348 | field-type | E1622 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E1623 | PercentageRate | Not a component record in this worksheet |
| src-000348 | field-type | E1624 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E1625 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E1626 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E1627 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000348 | field-type | E1628 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000348 | field-type | E1629 | CurrencyCode | Not a component record in this worksheet |
| src-000348 | field-type | E1630 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E1631 | PercentageRate | Not a component record in this worksheet |
| src-000348 | field-type | E1632 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E1622 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000352 | field-type | E1623 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000352 | field-type | E1624 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000352 | field-type | E1625 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000352 | field-type | E1626 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000352 | field-type | E1627 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000352 | field-type | E1628 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000352 | field-type | E1629 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000352 | field-type | E1630 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E1631 | Max350Text | Not a component record in this worksheet |
| src-000352 | field-type | E1632 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E1633 | PercentageRate | Not a component record in this worksheet |
| src-000352 | field-type | E1634 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E1635 | PercentageRate | Not a component record in this worksheet |
| src-000352 | field-type | E1636 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E1637 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E1638 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E1639 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000352 | field-type | E1640 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000352 | field-type | E1641 | CurrencyCode | Not a component record in this worksheet |
| src-000352 | field-type | E1642 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E1643 | PercentageRate | Not a component record in this worksheet |
| src-000352 | field-type | E1644 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E1586 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000355 | field-type | E1587 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000355 | field-type | E1588 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000355 | field-type | E1589 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000355 | field-type | E1590 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000355 | field-type | E1591 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000355 | field-type | E1592 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000355 | field-type | E1593 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000355 | field-type | E1594 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E1595 | Max350Text | Not a component record in this worksheet |
| src-000355 | field-type | E1596 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E1597 | PercentageRate | Not a component record in this worksheet |
| src-000355 | field-type | E1598 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E1599 | PercentageRate | Not a component record in this worksheet |
| src-000355 | field-type | E1600 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E1601 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E1602 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E1603 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000355 | field-type | E1604 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000355 | field-type | E1605 | CurrencyCode | Not a component record in this worksheet |
| src-000355 | field-type | E1606 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E1607 | PercentageRate | Not a component record in this worksheet |
| src-000355 | field-type | E1608 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E4065 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000358 | field-type | E4066 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000358 | field-type | E4067 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000358 | field-type | E4068 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000358 | field-type | E4069 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000358 | field-type | E4070 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000358 | field-type | E4071 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000358 | field-type | E4072 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000358 | field-type | E4073 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E4074 | Max350Text | Not a component record in this worksheet |
| src-000358 | field-type | E4075 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E4076 | PercentageRate | Not a component record in this worksheet |
| src-000358 | field-type | E4077 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E4078 | PercentageRate | Not a component record in this worksheet |
| src-000358 | field-type | E4079 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E4080 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E4081 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E4082 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000358 | field-type | E4083 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000358 | field-type | E4084 | CurrencyCode | Not a component record in this worksheet |
| src-000358 | field-type | E4085 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E4086 | PercentageRate | Not a component record in this worksheet |
| src-000358 | field-type | E4087 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E4065 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000361 | field-type | E4066 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000361 | field-type | E4067 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000361 | field-type | E4068 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000361 | field-type | E4069 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000361 | field-type | E4070 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000361 | field-type | E4071 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000361 | field-type | E4072 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000361 | field-type | E4073 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E4074 | Max350Text | Not a component record in this worksheet |
| src-000361 | field-type | E4075 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E4076 | PercentageRate | Not a component record in this worksheet |
| src-000361 | field-type | E4077 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E4078 | PercentageRate | Not a component record in this worksheet |
| src-000361 | field-type | E4079 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E4080 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E4081 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E4082 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000361 | field-type | E4083 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000361 | field-type | E4084 | CurrencyCode | Not a component record in this worksheet |
| src-000361 | field-type | E4085 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E4086 | PercentageRate | Not a component record in this worksheet |
| src-000361 | field-type | E4087 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E1586 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000364 | field-type | E1587 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000364 | field-type | E1588 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000364 | field-type | E1589 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000364 | field-type | E1590 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000364 | field-type | E1591 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000364 | field-type | E1592 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000364 | field-type | E1593 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000364 | field-type | E1594 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E1595 | Max350Text | Not a component record in this worksheet |
| src-000364 | field-type | E1596 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E1597 | PercentageRate | Not a component record in this worksheet |
| src-000364 | field-type | E1598 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E1599 | PercentageRate | Not a component record in this worksheet |
| src-000364 | field-type | E1600 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E1601 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E1602 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E1603 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000364 | field-type | E1604 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000364 | field-type | E1605 | CurrencyCode | Not a component record in this worksheet |
| src-000364 | field-type | E1606 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E1607 | PercentageRate | Not a component record in this worksheet |
| src-000364 | field-type | E1608 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E1586 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000367 | field-type | E1587 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000367 | field-type | E1588 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000367 | field-type | E1589 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000367 | field-type | E1590 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000367 | field-type | E1591 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000367 | field-type | E1592 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000367 | field-type | E1593 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000367 | field-type | E1594 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E1595 | Max350Text | Not a component record in this worksheet |
| src-000367 | field-type | E1596 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E1597 | PercentageRate | Not a component record in this worksheet |
| src-000367 | field-type | E1598 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E1599 | PercentageRate | Not a component record in this worksheet |
| src-000367 | field-type | E1600 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E1601 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E1602 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E1603 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000367 | field-type | E1604 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000367 | field-type | E1605 | CurrencyCode | Not a component record in this worksheet |
| src-000367 | field-type | E1606 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E1607 | PercentageRate | Not a component record in this worksheet |
| src-000367 | field-type | E1608 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E4065 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000370 | field-type | E4066 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000370 | field-type | E4067 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000370 | field-type | E4068 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000370 | field-type | E4069 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000370 | field-type | E4070 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000370 | field-type | E4071 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000370 | field-type | E4072 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000370 | field-type | E4073 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E4074 | Max350Text | Not a component record in this worksheet |
| src-000370 | field-type | E4075 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E4076 | PercentageRate | Not a component record in this worksheet |
| src-000370 | field-type | E4077 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E4078 | PercentageRate | Not a component record in this worksheet |
| src-000370 | field-type | E4079 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E4080 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E4081 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E4082 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000370 | field-type | E4083 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000370 | field-type | E4084 | CurrencyCode | Not a component record in this worksheet |
| src-000370 | field-type | E4085 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E4086 | PercentageRate | Not a component record in this worksheet |
| src-000370 | field-type | E4087 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E4065 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000373 | field-type | E4066 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000373 | field-type | E4067 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000373 | field-type | E4068 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000373 | field-type | E4069 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000373 | field-type | E4070 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000373 | field-type | E4071 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000373 | field-type | E4072 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000373 | field-type | E4073 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E4074 | Max350Text | Not a component record in this worksheet |
| src-000373 | field-type | E4075 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E4076 | PercentageRate | Not a component record in this worksheet |
| src-000373 | field-type | E4077 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E4078 | PercentageRate | Not a component record in this worksheet |
| src-000373 | field-type | E4079 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E4080 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E4081 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E4082 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000373 | field-type | E4083 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000373 | field-type | E4084 | CurrencyCode | Not a component record in this worksheet |
| src-000373 | field-type | E4085 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E4086 | PercentageRate | Not a component record in this worksheet |
| src-000373 | field-type | E4087 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E1622 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000376 | field-type | E1623 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000376 | field-type | E1624 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000376 | field-type | E1625 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000376 | field-type | E1626 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000376 | field-type | E1627 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000376 | field-type | E1628 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000376 | field-type | E1629 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000376 | field-type | E1630 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E1631 | Max350Text | Not a component record in this worksheet |
| src-000376 | field-type | E1632 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E1633 | PercentageRate | Not a component record in this worksheet |
| src-000376 | field-type | E1634 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E1635 | PercentageRate | Not a component record in this worksheet |
| src-000376 | field-type | E1636 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E1637 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E1638 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E1639 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000376 | field-type | E1640 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000376 | field-type | E1641 | CurrencyCode | Not a component record in this worksheet |
| src-000376 | field-type | E1642 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E1643 | PercentageRate | Not a component record in this worksheet |
| src-000376 | field-type | E1644 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E4065 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000379 | field-type | E4066 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000379 | field-type | E4067 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000379 | field-type | E4068 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000379 | field-type | E4069 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000379 | field-type | E4070 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000379 | field-type | E4071 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000379 | field-type | E4072 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000379 | field-type | E4073 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E4074 | Max350Text | Not a component record in this worksheet |
| src-000379 | field-type | E4075 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E4076 | PercentageRate | Not a component record in this worksheet |
| src-000379 | field-type | E4077 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E4078 | PercentageRate | Not a component record in this worksheet |
| src-000379 | field-type | E4079 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E4080 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E4081 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E4082 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000379 | field-type | E4083 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000379 | field-type | E4084 | CurrencyCode | Not a component record in this worksheet |
| src-000379 | field-type | E4085 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E4086 | PercentageRate | Not a component record in this worksheet |
| src-000379 | field-type | E4087 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E1610 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000382 | field-type | E1611 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000382 | field-type | E1612 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000382 | field-type | E1613 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000382 | field-type | E1614 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000382 | field-type | E1615 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000382 | field-type | E1616 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000382 | field-type | E1617 | IncentivePremium | [IncentivePremium](bc-1614c54fc85d25e21980.md) |
| src-000382 | field-type | E1618 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E1619 | Max350Text | Not a component record in this worksheet |
| src-000382 | field-type | E1620 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E1621 | PercentageRate | Not a component record in this worksheet |
| src-000382 | field-type | E1622 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E1623 | PercentageRate | Not a component record in this worksheet |
| src-000382 | field-type | E1624 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E1625 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E1626 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E1627 | Dividend | [Dividend](bc-8b9f113a5fc8f5f4111d.md) |
| src-000382 | field-type | E1628 | CorporateActionOptionCode | Not a component record in this worksheet |
| src-000382 | field-type | E1629 | CurrencyCode | Not a component record in this worksheet |
| src-000382 | field-type | E1630 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E1631 | PercentageRate | Not a component record in this worksheet |
| src-000382 | field-type | E1632 | ISODateTime | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](index.md) · [Known limitations and issues](../../../tracking/issues.md)
