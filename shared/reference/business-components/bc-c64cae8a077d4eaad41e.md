---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-c64cae8a077d4eaad41e"
title: "SecuritiesIdentification"
business_component_name: "SecuritiesIdentification"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A4067:F4090"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A3997:F4020"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A4067:F4090"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A4067:F4090"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A4067:F4090"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A4067:F4090"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A4067:F4090"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A3997:F4020"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A4067:F4090"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A4036:F4059"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A111:F134"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A4036:F4059"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A4067:F4090"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A3975:F3998"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A111:F134"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A111:F134"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A3975:F3998"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A3975:F3998"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A111:F134"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A111:F134"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A4067:F4090"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A111:F134"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A4036:F4059"]}]
content_sha256: "c64cae8a077d4eaad41ef15c4d59a2fe0f2f08942b1e57118e21d7bf9787795c"
parent_names: []
related_component_names: ["BelgianIdentifier", "Bloomberg2Identifier", "CUSIPIdentifier", "ConsolidatedTapeAssociationIdentifier", "DateTimePeriod", "DutchIdentifier", "EuroclearClearstreamIdentifier", "GenericIdentification", "ISINOct2015Identifier", "LocalName", "Max35Text", "Max70Text", "QUICKIdentifier", "RICIdentifier", "SEDOLIdentifier", "SecuritiesIdentification", "Security", "SicovamIdentifier", "TickerIdentifier", "TradingMarket", "ValorenIdentifier", "WertpapierIdentifier"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# SecuritiesIdentification

## Definition

Unique and unambiguous identifier of a security, assigned under a formal or proprietary identification scheme.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SecuritiesIdentification | ∅ | ∅ | Unique and unambiguous identifier of a security, assigned under a formal or proprietary identification scheme. | ∅ | ∅ |
| 2 | SecuritiesIdentification | IdentifiedSecurity | ∅ | Security for which an identification is provided. | Security | Identification |
| 3 | SecuritiesIdentification | SecurityIdentification | ∅ | Identification of a security by an ISIN. | ISINOct2015Identifier | ∅ |
| 4 | SecuritiesIdentification | RIC | ∅ | Reuters Identification Code (RIC). A numbering system used within the Reuters system to identify instruments worldwide. The RIC contains an X-character market specific code (can be the CUSIP or EPIC codes) followed by a full stop, then the two-digit ISO country code, eg, IBM in UK is IBM.UK. | RICIdentifier | ∅ |
| 5 | SecuritiesIdentification | TickerSymbol | ∅ | Letters that identify a stock traded on a stock exchange. The Ticker Symbol is a short and convenient way of identifying a stock, eg, RTR.L for Reuters quoted in London. | TickerIdentifier | ∅ |
| 6 | SecuritiesIdentification | Bloomberg | ∅ | Identifier of a security assigned by the Bloomberg organisation. | Bloomberg2Identifier | ∅ |
| 7 | SecuritiesIdentification | CTA | ∅ | Identifier of a security assigned by the Consolidated Tape Association. | ConsolidatedTapeAssociationIdentifier | ∅ |
| 8 | SecuritiesIdentification | Common | ∅ | Identifier of securities issued in Luxembourg.  The common code is a 9-digit code that replaces the CEDEL (Clearstream) and Euroclear codes. | EuroclearClearstreamIdentifier | ∅ |
| 9 | SecuritiesIdentification | Name | ∅ | Name of the financial instrument in free format text. | LocalName | RelatedSecurity |
| 10 | SecuritiesIdentification | SEDOL | ∅ | Stock Exchange Daily Official List (SEDOL) number.  A code used by the London Stock Exchange to identify foreign stocks, especially those that aren't actively traded in the US and don't have a CUSIP number. | SEDOLIdentifier | ∅ |
| 11 | SecuritiesIdentification | CUSIP | ∅ | Committee on Uniform Securities and Identification Procedures (CUSIP). The standards body that created and maintains the securities classification system in the US. The CUSIP is composed of a 9-character number that uniquely identifies a particular security.  Non-US securities have a similar number called the CINS number. | CUSIPIdentifier | ∅ |
| 12 | SecuritiesIdentification | QUICK | ∅ | Identifier of a security assigned by the Japanese QUICK identification scheme for financial instruments. | QUICKIdentifier | ∅ |
| 13 | SecuritiesIdentification | Wertpapier | ∅ | Wertpapier Kenn-nummer.  A number issued in Germany by the Wertpapier Mitteilungen. The Wertpapier Kenn-nummer, sometimes called WPK, contains 6-digits, but no check digit. There are different ranges of numbers representing different classes of securities. | WertpapierIdentifier | ∅ |
| 14 | SecuritiesIdentification | Dutch | ∅ | Identifier for Dutch securities. | DutchIdentifier | ∅ |
| 15 | SecuritiesIdentification | Valoren | ∅ | Identifier for Swiss securities assigned by Telekurs Financial, the Swiss numbering agency. | ValorenIdentifier | ∅ |
| 16 | SecuritiesIdentification | Sicovam | ∅ | Identifier for French securities assigned by the Societe Interprofessionnelle Pour La Compensation des Valeurs Mobilieres in France.  The Sicovam is composed of 5-digits. | SicovamIdentifier | ∅ |
| 17 | SecuritiesIdentification | Belgian | ∅ | Identifier for Belgian securities. | BelgianIdentifier | ∅ |
| 18 | SecuritiesIdentification | IdentificationSuffix | ∅ | Identifies the suffix of the security identification. | Max35Text | ∅ |
| 19 | SecuritiesIdentification | GenericIdentification | ∅ | Proprietary identification of a security assigned by an institution or organisation. | GenericIdentification | RelatedSecuritiesIdentification |
| 20 | SecuritiesIdentification | ValidityPeriod | ∅ | Specifies the period during which an identification is valid. | DateTimePeriod | RelatedSecuritiesIdentification |
| 21 | SecuritiesIdentification | ApplicableTradingMarket | ∅ | Market(s) on which the trading identification is used. | TradingMarket | ListedSecurityTradingIdentification |
| 22 | SecuritiesIdentification | PrimeIdentification | ∅ | Specifies the main identification of a security. | SecuritiesIdentification | RelatedOtherIdentification |
| 23 | SecuritiesIdentification | RelatedOtherIdentification | ∅ | Alternate security identification(s) related to the security trading identification. | SecuritiesIdentification | PrimeIdentification |
| 24 | SecuritiesIdentification | TradingIdentification | ∅ | Security identifier specific to a trading market or markets, for example, Ticker. | Max70Text | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `c64cae8a077d4eaad41ef15c4d59a2fe0f2f08942b1e57118e21d7bf9787795c`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A4067:F4090 | 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087, 4088, 4089, 4090 | [src-000006 original](<../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart3_BanktoCustomerCashManagement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md>) |
| src-000016 | FullBusinessModel!A3997:F4020 | 3997, 3998, 3999, 4000, 4001, 4002, 4003, 4004, 4005, 4006, 4007, 4008, 4009, 4010, 4011, 4012, 4013, 4014, 4015, 4016, 4017, 4018, 4019, 4020 | [src-000016 original](<../../../raw-input/cash_management/ISO20022_MDRPart3_CashManagement_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md>) |
| src-000054 | FullBusinessModel!A4067:F4090 | 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087, 4088, 4089, 4090 | [src-000054 original](<../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart3_CentralCounterParty_SecuritiesClearing_Maintenance_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md>) |
| src-000081 | FullBusinessModel!A4067:F4090 | 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087, 4088, 4089, 4090 | [src-000081 original](<../../../raw-input/corporate_actions/ISO20022_MDRPart3_CorporateActions_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md>) |
| src-000097 | FullBusinessModel!A4067:F4090 | 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087, 4088, 4089, 4090 | [src-000097 original](<../../../raw-input/investment_funds/ISO20022_MDRPart3_Investment-Funds_2025_2026_v2.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md>) |
| src-000164 | FullBusinessModel!A4067:F4090 | 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087, 4088, 4089, 4090 | [src-000164 original](<../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart3_PaymentsClearingandSettlement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md>) |
| src-000175 | FullBusinessModel!A4067:F4090 | 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087, 4088, 4089, 4090 | [src-000175 original](<../../../raw-input/payments_initiation/ISO20022_MDRPart3_PaymentsInitiation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md>) |
| src-000182 | FullBusinessModel!A3997:F4020 | 3997, 3998, 3999, 4000, 4001, 4002, 4003, 4004, 4005, 4006, 4007, 4008, 4009, 4010, 4011, 4012, 4013, 4014, 4015, 4016, 4017, 4018, 4019, 4020 | [src-000182 original](<../../../raw-input/post_trade_matching/ISO20022_MDRPart3_PostTradeMatching_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md>) |
| src-000198 | FullBusinessModel!A4067:F4090 | 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087, 4088, 4089, 4090 | [src-000198 original](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart3_SettlementAndReconciliation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md>) |
| src-000322 | FullBusinessModel!A4036:F4059 | 4036, 4037, 4038, 4039, 4040, 4041, 4042, 4043, 4044, 4045, 4046, 4047, 4048, 4049, 4050, 4051, 4052, 4053, 4054, 4055, 4056, 4057, 4058, 4059 | [src-000322 original](<../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart3_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md>) |
| src-000345 | FullBusinessModel!A111:F134 | 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134 | [src-000345 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](<../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md>) |
| src-000348 | FullBusinessModel!A4036:F4059 | 4036, 4037, 4038, 4039, 4040, 4041, 4042, 4043, 4044, 4045, 4046, 4047, 4048, 4049, 4050, 4051, 4052, 4053, 4054, 4055, 4056, 4057, 4058, 4059 | [src-000348 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md>) |
| src-000352 | FullBusinessModel!A4067:F4090 | 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087, 4088, 4089, 4090 | [src-000352 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md>) |
| src-000355 | FullBusinessModel!A3975:F3998 | 3975, 3976, 3977, 3978, 3979, 3980, 3981, 3982, 3983, 3984, 3985, 3986, 3987, 3988, 3989, 3990, 3991, 3992, 3993, 3994, 3995, 3996, 3997, 3998 | [src-000355 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md>) |
| src-000358 | FullBusinessModel!A111:F134 | 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134 | [src-000358 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md>) |
| src-000361 | FullBusinessModel!A111:F134 | 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134 | [src-000361 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md>) |
| src-000364 | FullBusinessModel!A3975:F3998 | 3975, 3976, 3977, 3978, 3979, 3980, 3981, 3982, 3983, 3984, 3985, 3986, 3987, 3988, 3989, 3990, 3991, 3992, 3993, 3994, 3995, 3996, 3997, 3998 | [src-000364 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md>) |
| src-000367 | FullBusinessModel!A3975:F3998 | 3975, 3976, 3977, 3978, 3979, 3980, 3981, 3982, 3983, 3984, 3985, 3986, 3987, 3988, 3989, 3990, 3991, 3992, 3993, 3994, 3995, 3996, 3997, 3998 | [src-000367 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md>) |
| src-000370 | FullBusinessModel!A111:F134 | 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134 | [src-000370 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md>) |
| src-000373 | FullBusinessModel!A111:F134 | 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134 | [src-000373 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md>) |
| src-000376 | FullBusinessModel!A4067:F4090 | 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4087, 4088, 4089, 4090 | [src-000376 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md>) |
| src-000379 | FullBusinessModel!A111:F134 | 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134 | [src-000379 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md>) |
| src-000382 | FullBusinessModel!A4036:F4059 | 4036, 4037, 4038, 4039, 4040, 4041, 4042, 4043, 4044, 4045, 4046, 4047, 4048, 4049, 4050, 4051, 4052, 4053, 4054, 4055, 4056, 4057, 4058, 4059 | [src-000382 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | field-type | E4068 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000006 | field-type | E4069 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000006 | field-type | E4070 | RICIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E4071 | TickerIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E4072 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000006 | field-type | E4073 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E4074 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E4075 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000006 | field-type | E4076 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E4077 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E4078 | QUICKIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E4079 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E4080 | DutchIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E4081 | ValorenIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E4082 | SicovamIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E4083 | BelgianIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E4084 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4085 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000006 | field-type | E4086 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000006 | field-type | E4087 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000006 | field-type | E4088 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000006 | field-type | E4089 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000006 | field-type | E4090 | Max70Text | Not a component record in this worksheet |
| src-000016 | field-type | E3998 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000016 | field-type | E3999 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000016 | field-type | E4000 | RICIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E4001 | TickerIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E4002 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000016 | field-type | E4003 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E4004 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E4005 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000016 | field-type | E4006 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E4007 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E4008 | QUICKIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E4009 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E4010 | DutchIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E4011 | ValorenIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E4012 | SicovamIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E4013 | BelgianIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E4014 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4015 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000016 | field-type | E4016 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000016 | field-type | E4017 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000016 | field-type | E4018 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000016 | field-type | E4019 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000016 | field-type | E4020 | Max70Text | Not a component record in this worksheet |
| src-000054 | field-type | E4068 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000054 | field-type | E4069 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000054 | field-type | E4070 | RICIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E4071 | TickerIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E4072 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000054 | field-type | E4073 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E4074 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E4075 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000054 | field-type | E4076 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E4077 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E4078 | QUICKIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E4079 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E4080 | DutchIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E4081 | ValorenIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E4082 | SicovamIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E4083 | BelgianIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E4084 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4085 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000054 | field-type | E4086 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000054 | field-type | E4087 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000054 | field-type | E4088 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000054 | field-type | E4089 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000054 | field-type | E4090 | Max70Text | Not a component record in this worksheet |
| src-000081 | field-type | E4068 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000081 | field-type | E4069 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000081 | field-type | E4070 | RICIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E4071 | TickerIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E4072 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000081 | field-type | E4073 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E4074 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E4075 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000081 | field-type | E4076 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E4077 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E4078 | QUICKIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E4079 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E4080 | DutchIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E4081 | ValorenIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E4082 | SicovamIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E4083 | BelgianIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E4084 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4085 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000081 | field-type | E4086 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000081 | field-type | E4087 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000081 | field-type | E4088 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000081 | field-type | E4089 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000081 | field-type | E4090 | Max70Text | Not a component record in this worksheet |
| src-000097 | field-type | E4068 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000097 | field-type | E4069 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000097 | field-type | E4070 | RICIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E4071 | TickerIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E4072 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000097 | field-type | E4073 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E4074 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E4075 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000097 | field-type | E4076 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E4077 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E4078 | QUICKIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E4079 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E4080 | DutchIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E4081 | ValorenIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E4082 | SicovamIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E4083 | BelgianIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E4084 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4085 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000097 | field-type | E4086 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000097 | field-type | E4087 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000097 | field-type | E4088 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000097 | field-type | E4089 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000097 | field-type | E4090 | Max70Text | Not a component record in this worksheet |
| src-000164 | field-type | E4068 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000164 | field-type | E4069 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000164 | field-type | E4070 | RICIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E4071 | TickerIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E4072 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000164 | field-type | E4073 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E4074 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E4075 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000164 | field-type | E4076 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E4077 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E4078 | QUICKIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E4079 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E4080 | DutchIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E4081 | ValorenIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E4082 | SicovamIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E4083 | BelgianIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E4084 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4085 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000164 | field-type | E4086 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000164 | field-type | E4087 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000164 | field-type | E4088 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000164 | field-type | E4089 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000164 | field-type | E4090 | Max70Text | Not a component record in this worksheet |
| src-000175 | field-type | E4068 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000175 | field-type | E4069 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000175 | field-type | E4070 | RICIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E4071 | TickerIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E4072 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000175 | field-type | E4073 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E4074 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E4075 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000175 | field-type | E4076 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E4077 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E4078 | QUICKIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E4079 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E4080 | DutchIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E4081 | ValorenIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E4082 | SicovamIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E4083 | BelgianIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E4084 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4085 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000175 | field-type | E4086 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000175 | field-type | E4087 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000175 | field-type | E4088 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000175 | field-type | E4089 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000175 | field-type | E4090 | Max70Text | Not a component record in this worksheet |
| src-000182 | field-type | E3998 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000182 | field-type | E3999 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000182 | field-type | E4000 | RICIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E4001 | TickerIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E4002 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000182 | field-type | E4003 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E4004 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E4005 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000182 | field-type | E4006 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E4007 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E4008 | QUICKIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E4009 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E4010 | DutchIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E4011 | ValorenIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E4012 | SicovamIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E4013 | BelgianIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E4014 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4015 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000182 | field-type | E4016 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000182 | field-type | E4017 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000182 | field-type | E4018 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000182 | field-type | E4019 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000182 | field-type | E4020 | Max70Text | Not a component record in this worksheet |
| src-000198 | field-type | E4068 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000198 | field-type | E4069 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000198 | field-type | E4070 | RICIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E4071 | TickerIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E4072 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000198 | field-type | E4073 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E4074 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E4075 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000198 | field-type | E4076 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E4077 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E4078 | QUICKIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E4079 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E4080 | DutchIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E4081 | ValorenIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E4082 | SicovamIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E4083 | BelgianIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E4084 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4085 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000198 | field-type | E4086 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000198 | field-type | E4087 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000198 | field-type | E4088 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000198 | field-type | E4089 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000198 | field-type | E4090 | Max70Text | Not a component record in this worksheet |
| src-000322 | field-type | E4037 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000322 | field-type | E4038 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000322 | field-type | E4039 | RICIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E4040 | TickerIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E4041 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000322 | field-type | E4042 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E4043 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E4044 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000322 | field-type | E4045 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E4046 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E4047 | QUICKIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E4048 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E4049 | DutchIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E4050 | ValorenIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E4051 | SicovamIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E4052 | BelgianIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E4053 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4054 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000322 | field-type | E4055 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000322 | field-type | E4056 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000322 | field-type | E4057 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000322 | field-type | E4058 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000322 | field-type | E4059 | Max70Text | Not a component record in this worksheet |
| src-000345 | field-type | E112 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000345 | field-type | E113 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000345 | field-type | E114 | RICIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E115 | TickerIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E116 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000345 | field-type | E117 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E118 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E119 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000345 | field-type | E120 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E121 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E122 | QUICKIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E123 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E124 | DutchIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E125 | ValorenIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E126 | SicovamIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E127 | BelgianIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E128 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E129 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000345 | field-type | E130 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000345 | field-type | E131 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000345 | field-type | E132 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000345 | field-type | E133 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000345 | field-type | E134 | Max70Text | Not a component record in this worksheet |
| src-000348 | field-type | E4037 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000348 | field-type | E4038 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000348 | field-type | E4039 | RICIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E4040 | TickerIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E4041 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000348 | field-type | E4042 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E4043 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E4044 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000348 | field-type | E4045 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E4046 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E4047 | QUICKIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E4048 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E4049 | DutchIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E4050 | ValorenIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E4051 | SicovamIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E4052 | BelgianIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E4053 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4054 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000348 | field-type | E4055 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000348 | field-type | E4056 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000348 | field-type | E4057 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000348 | field-type | E4058 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000348 | field-type | E4059 | Max70Text | Not a component record in this worksheet |
| src-000352 | field-type | E4068 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000352 | field-type | E4069 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000352 | field-type | E4070 | RICIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E4071 | TickerIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E4072 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000352 | field-type | E4073 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E4074 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E4075 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000352 | field-type | E4076 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E4077 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E4078 | QUICKIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E4079 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E4080 | DutchIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E4081 | ValorenIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E4082 | SicovamIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E4083 | BelgianIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E4084 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4085 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000352 | field-type | E4086 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000352 | field-type | E4087 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000352 | field-type | E4088 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000352 | field-type | E4089 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000352 | field-type | E4090 | Max70Text | Not a component record in this worksheet |
| src-000355 | field-type | E3976 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000355 | field-type | E3977 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000355 | field-type | E3978 | RICIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E3979 | TickerIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E3980 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000355 | field-type | E3981 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E3982 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E3983 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000355 | field-type | E3984 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E3985 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E3986 | QUICKIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E3987 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E3988 | DutchIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E3989 | ValorenIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E3990 | SicovamIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E3991 | BelgianIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E3992 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E3993 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000355 | field-type | E3994 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000355 | field-type | E3995 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000355 | field-type | E3996 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000355 | field-type | E3997 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000355 | field-type | E3998 | Max70Text | Not a component record in this worksheet |
| src-000358 | field-type | E112 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000358 | field-type | E113 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000358 | field-type | E114 | RICIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E115 | TickerIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E116 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000358 | field-type | E117 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E118 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E119 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000358 | field-type | E120 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E121 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E122 | QUICKIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E123 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E124 | DutchIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E125 | ValorenIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E126 | SicovamIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E127 | BelgianIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E128 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E129 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000358 | field-type | E130 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000358 | field-type | E131 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000358 | field-type | E132 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000358 | field-type | E133 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000358 | field-type | E134 | Max70Text | Not a component record in this worksheet |
| src-000361 | field-type | E112 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000361 | field-type | E113 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000361 | field-type | E114 | RICIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E115 | TickerIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E116 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000361 | field-type | E117 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E118 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E119 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000361 | field-type | E120 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E121 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E122 | QUICKIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E123 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E124 | DutchIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E125 | ValorenIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E126 | SicovamIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E127 | BelgianIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E128 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E129 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000361 | field-type | E130 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000361 | field-type | E131 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000361 | field-type | E132 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000361 | field-type | E133 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000361 | field-type | E134 | Max70Text | Not a component record in this worksheet |
| src-000364 | field-type | E3976 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000364 | field-type | E3977 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000364 | field-type | E3978 | RICIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E3979 | TickerIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E3980 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000364 | field-type | E3981 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E3982 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E3983 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000364 | field-type | E3984 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E3985 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E3986 | QUICKIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E3987 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E3988 | DutchIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E3989 | ValorenIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E3990 | SicovamIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E3991 | BelgianIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E3992 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E3993 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000364 | field-type | E3994 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000364 | field-type | E3995 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000364 | field-type | E3996 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000364 | field-type | E3997 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000364 | field-type | E3998 | Max70Text | Not a component record in this worksheet |
| src-000367 | field-type | E3976 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000367 | field-type | E3977 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000367 | field-type | E3978 | RICIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E3979 | TickerIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E3980 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000367 | field-type | E3981 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E3982 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E3983 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000367 | field-type | E3984 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E3985 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E3986 | QUICKIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E3987 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E3988 | DutchIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E3989 | ValorenIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E3990 | SicovamIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E3991 | BelgianIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E3992 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E3993 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000367 | field-type | E3994 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000367 | field-type | E3995 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000367 | field-type | E3996 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000367 | field-type | E3997 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000367 | field-type | E3998 | Max70Text | Not a component record in this worksheet |
| src-000370 | field-type | E112 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000370 | field-type | E113 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000370 | field-type | E114 | RICIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E115 | TickerIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E116 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000370 | field-type | E117 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E118 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E119 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000370 | field-type | E120 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E121 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E122 | QUICKIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E123 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E124 | DutchIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E125 | ValorenIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E126 | SicovamIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E127 | BelgianIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E128 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E129 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000370 | field-type | E130 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000370 | field-type | E131 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000370 | field-type | E132 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000370 | field-type | E133 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000370 | field-type | E134 | Max70Text | Not a component record in this worksheet |
| src-000373 | field-type | E112 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000373 | field-type | E113 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000373 | field-type | E114 | RICIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E115 | TickerIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E116 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000373 | field-type | E117 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E118 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E119 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000373 | field-type | E120 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E121 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E122 | QUICKIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E123 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E124 | DutchIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E125 | ValorenIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E126 | SicovamIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E127 | BelgianIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E128 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E129 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000373 | field-type | E130 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000373 | field-type | E131 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000373 | field-type | E132 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000373 | field-type | E133 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000373 | field-type | E134 | Max70Text | Not a component record in this worksheet |
| src-000376 | field-type | E4068 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000376 | field-type | E4069 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000376 | field-type | E4070 | RICIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E4071 | TickerIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E4072 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000376 | field-type | E4073 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E4074 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E4075 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000376 | field-type | E4076 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E4077 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E4078 | QUICKIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E4079 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E4080 | DutchIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E4081 | ValorenIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E4082 | SicovamIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E4083 | BelgianIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E4084 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4085 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000376 | field-type | E4086 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000376 | field-type | E4087 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000376 | field-type | E4088 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000376 | field-type | E4089 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000376 | field-type | E4090 | Max70Text | Not a component record in this worksheet |
| src-000379 | field-type | E112 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000379 | field-type | E113 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000379 | field-type | E114 | RICIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E115 | TickerIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E116 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000379 | field-type | E117 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E118 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E119 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000379 | field-type | E120 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E121 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E122 | QUICKIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E123 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E124 | DutchIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E125 | ValorenIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E126 | SicovamIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E127 | BelgianIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E128 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E129 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000379 | field-type | E130 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000379 | field-type | E131 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000379 | field-type | E132 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000379 | field-type | E133 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000379 | field-type | E134 | Max70Text | Not a component record in this worksheet |
| src-000382 | field-type | E4037 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000382 | field-type | E4038 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000382 | field-type | E4039 | RICIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E4040 | TickerIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E4041 | Bloomberg2Identifier | Not a component record in this worksheet |
| src-000382 | field-type | E4042 | ConsolidatedTapeAssociationIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E4043 | EuroclearClearstreamIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E4044 | LocalName | [LocalName](<bc-27430e4340ce33e67420.md>) |
| src-000382 | field-type | E4045 | SEDOLIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E4046 | CUSIPIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E4047 | QUICKIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E4048 | WertpapierIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E4049 | DutchIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E4050 | ValorenIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E4051 | SicovamIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E4052 | BelgianIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E4053 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4054 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000382 | field-type | E4055 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000382 | field-type | E4056 | TradingMarket | [TradingMarket](<bc-e6d979e9ac91f3dfb08c.md>) |
| src-000382 | field-type | E4057 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000382 | field-type | E4058 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000382 | field-type | E4059 | Max70Text | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
