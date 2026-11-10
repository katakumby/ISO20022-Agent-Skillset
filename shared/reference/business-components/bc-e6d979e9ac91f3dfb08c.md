---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-e6d979e9ac91f3dfb08c"
title: "TradingMarket"
business_component_name: "TradingMarket"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A5146:F5166"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A5076:F5096"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A5146:F5166"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A5146:F5166"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A5146:F5166"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A5146:F5166"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A5146:F5166"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A5076:F5096"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A5146:F5166"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A5115:F5135"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A633:F653"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A5115:F5135"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A5146:F5166"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A5050:F5070"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A633:F653"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A633:F653"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A5050:F5070"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A5050:F5070"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A633:F653"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A633:F653"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A5146:F5166"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A633:F653"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A5115:F5135"]}]
content_sha256: "e6d979e9ac91f3dfb08c3498cae9269cf2e25e211f42e0cd71a2d4ebcb5c72b8"
parent_names: ["Market"]
related_component_names: ["CurrencyCode", "ISODateTime", "Issuance", "LotBreakdown", "MarketTypeCode", "PlaceOfSettlement", "SecuritiesIdentification", "SecuritiesOrder", "SecuritiesQuantity", "Security", "SourceOfPrice", "StockExchange", "TradingSession"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# TradingMarket

## Definition

Context or geographic environment in which trading parties may meet in order to negotiate and execute trades among themselves. It also identifies the primary market where an asset is issued.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | TradingMarket | ∅ | Market | Context or geographic environment in which trading parties may meet in order to negotiate and execute trades among themselves. It also identifies the primary market where an asset is issued. | ∅ | ∅ |
| 2 | TradingMarket | TradedSecurity | ∅ | Security which is traded on a specific market. | Security | TradingMarket |
| 3 | TradingMarket | Type | ∅ | Nature of a market in which transactions take place. | MarketTypeCode | ∅ |
| 4 | TradingMarket | ListedSecurity | ∅ | Security whch is listed on a specific market. | Security | PlaceOfListing |
| 5 | TradingMarket | SourceOfPrice | ∅ | Party which provides a price on a market. | SourceOfPrice | MarketIdentification |
| 6 | TradingMarket | TradeLotSize | ∅ | Specifies the number of securities that have to be traded in one lot . | LotBreakdown | TradeLotMarket |
| 7 | TradingMarket | MinimumTradedNominalQuantity | ∅ | Minimum number of securities that can be traded. | SecuritiesQuantity | MinimumTradedQuantityMarket |
| 8 | TradingMarket | ListingDate | ∅ | Date/time at which the security is listed at the specific exchange. | ISODateTime | ∅ |
| 9 | TradingMarket | RelatedOrder | ∅ | Order for which a place of trade is requested. | SecuritiesOrder | PlaceOfTrade |
| 10 | TradingMarket | TradingCurrency | ∅ | Currency of the trading. | CurrencyCode | ∅ |
| 11 | TradingMarket | MaximumTradedNominalQuantity | ∅ | Miaximum number of securities that can be traded. | SecuritiesQuantity | MaximumTradedQuantityMarket |
| 12 | TradingMarket | StockExchange | ∅ | Stock exchange which operates on a specific market. | StockExchange | Market |
| 13 | TradingMarket | QuoteLot | ∅ | Lot size associated with the price. Most exchanges require that pricing be quoted in round lot size. However, some exchanges have pricing quoted in many different lot sizes, for example, Latin America, some Asian markets, Turkey. | LotBreakdown | QuoteLotMarket |
| 14 | TradingMarket | RoundLot | ∅ | Minimum quantity of securities that can be purchased without incurring a larger fee. For example, if the round lot size is 100 and the trade is for 125  shares, then 100 will be processed without a fee and the remaining 25 will incur a service fee for being an odd lot size. | LotBreakdown | RoundLotMarket |
| 15 | TradingMarket | TradingSession | ∅ | Trading session associated with a market. | TradingSession | Market |
| 16 | TradingMarket | ListedSecurityTradingIdentification | ∅ | Trading identification used on this trading market. | SecuritiesIdentification | ApplicableTradingMarket |
| 17 | TradingMarket | DefaultCurrency | ∅ | Default currency for the securities trading on this market. | CurrencyCode | ∅ |
| 18 | TradingMarket | FirstTradingDate | ∅ | First date/time at which the security is eligible for trading. | ISODateTime | ∅ |
| 19 | TradingMarket | LastTradingDate | ∅ | Last date/time at which the security is eligible for trading. | ISODateTime | ∅ |
| 20 | TradingMarket | Issuance | ∅ | Issuance for which the place has been defined. | Issuance | IssuePlace |
| 21 | TradingMarket | RelatedPlaceOfSettlement | ∅ | Place of settlement for which a settlement market is specified. | PlaceOfSettlement | SettlementMarket |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `e6d979e9ac91f3dfb08c3498cae9269cf2e25e211f42e0cd71a2d4ebcb5c72b8`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A5146:F5166 | 5146, 5147, 5148, 5149, 5150, 5151, 5152, 5153, 5154, 5155, 5156, 5157, 5158, 5159, 5160, 5161, 5162, 5163, 5164, 5165, 5166 | [src-000006 original](<../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart3_BanktoCustomerCashManagement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md>) |
| src-000016 | FullBusinessModel!A5076:F5096 | 5076, 5077, 5078, 5079, 5080, 5081, 5082, 5083, 5084, 5085, 5086, 5087, 5088, 5089, 5090, 5091, 5092, 5093, 5094, 5095, 5096 | [src-000016 original](<../../../raw-input/cash_management/ISO20022_MDRPart3_CashManagement_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md>) |
| src-000054 | FullBusinessModel!A5146:F5166 | 5146, 5147, 5148, 5149, 5150, 5151, 5152, 5153, 5154, 5155, 5156, 5157, 5158, 5159, 5160, 5161, 5162, 5163, 5164, 5165, 5166 | [src-000054 original](<../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart3_CentralCounterParty_SecuritiesClearing_Maintenance_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md>) |
| src-000081 | FullBusinessModel!A5146:F5166 | 5146, 5147, 5148, 5149, 5150, 5151, 5152, 5153, 5154, 5155, 5156, 5157, 5158, 5159, 5160, 5161, 5162, 5163, 5164, 5165, 5166 | [src-000081 original](<../../../raw-input/corporate_actions/ISO20022_MDRPart3_CorporateActions_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md>) |
| src-000097 | FullBusinessModel!A5146:F5166 | 5146, 5147, 5148, 5149, 5150, 5151, 5152, 5153, 5154, 5155, 5156, 5157, 5158, 5159, 5160, 5161, 5162, 5163, 5164, 5165, 5166 | [src-000097 original](<../../../raw-input/investment_funds/ISO20022_MDRPart3_Investment-Funds_2025_2026_v2.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md>) |
| src-000164 | FullBusinessModel!A5146:F5166 | 5146, 5147, 5148, 5149, 5150, 5151, 5152, 5153, 5154, 5155, 5156, 5157, 5158, 5159, 5160, 5161, 5162, 5163, 5164, 5165, 5166 | [src-000164 original](<../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart3_PaymentsClearingandSettlement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md>) |
| src-000175 | FullBusinessModel!A5146:F5166 | 5146, 5147, 5148, 5149, 5150, 5151, 5152, 5153, 5154, 5155, 5156, 5157, 5158, 5159, 5160, 5161, 5162, 5163, 5164, 5165, 5166 | [src-000175 original](<../../../raw-input/payments_initiation/ISO20022_MDRPart3_PaymentsInitiation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md>) |
| src-000182 | FullBusinessModel!A5076:F5096 | 5076, 5077, 5078, 5079, 5080, 5081, 5082, 5083, 5084, 5085, 5086, 5087, 5088, 5089, 5090, 5091, 5092, 5093, 5094, 5095, 5096 | [src-000182 original](<../../../raw-input/post_trade_matching/ISO20022_MDRPart3_PostTradeMatching_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md>) |
| src-000198 | FullBusinessModel!A5146:F5166 | 5146, 5147, 5148, 5149, 5150, 5151, 5152, 5153, 5154, 5155, 5156, 5157, 5158, 5159, 5160, 5161, 5162, 5163, 5164, 5165, 5166 | [src-000198 original](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart3_SettlementAndReconciliation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md>) |
| src-000322 | FullBusinessModel!A5115:F5135 | 5115, 5116, 5117, 5118, 5119, 5120, 5121, 5122, 5123, 5124, 5125, 5126, 5127, 5128, 5129, 5130, 5131, 5132, 5133, 5134, 5135 | [src-000322 original](<../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart3_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md>) |
| src-000345 | FullBusinessModel!A633:F653 | 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653 | [src-000345 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](<../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md>) |
| src-000348 | FullBusinessModel!A5115:F5135 | 5115, 5116, 5117, 5118, 5119, 5120, 5121, 5122, 5123, 5124, 5125, 5126, 5127, 5128, 5129, 5130, 5131, 5132, 5133, 5134, 5135 | [src-000348 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md>) |
| src-000352 | FullBusinessModel!A5146:F5166 | 5146, 5147, 5148, 5149, 5150, 5151, 5152, 5153, 5154, 5155, 5156, 5157, 5158, 5159, 5160, 5161, 5162, 5163, 5164, 5165, 5166 | [src-000352 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md>) |
| src-000355 | FullBusinessModel!A5050:F5070 | 5050, 5051, 5052, 5053, 5054, 5055, 5056, 5057, 5058, 5059, 5060, 5061, 5062, 5063, 5064, 5065, 5066, 5067, 5068, 5069, 5070 | [src-000355 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md>) |
| src-000358 | FullBusinessModel!A633:F653 | 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653 | [src-000358 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md>) |
| src-000361 | FullBusinessModel!A633:F653 | 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653 | [src-000361 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md>) |
| src-000364 | FullBusinessModel!A5050:F5070 | 5050, 5051, 5052, 5053, 5054, 5055, 5056, 5057, 5058, 5059, 5060, 5061, 5062, 5063, 5064, 5065, 5066, 5067, 5068, 5069, 5070 | [src-000364 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md>) |
| src-000367 | FullBusinessModel!A5050:F5070 | 5050, 5051, 5052, 5053, 5054, 5055, 5056, 5057, 5058, 5059, 5060, 5061, 5062, 5063, 5064, 5065, 5066, 5067, 5068, 5069, 5070 | [src-000367 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md>) |
| src-000370 | FullBusinessModel!A633:F653 | 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653 | [src-000370 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md>) |
| src-000373 | FullBusinessModel!A633:F653 | 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653 | [src-000373 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md>) |
| src-000376 | FullBusinessModel!A5146:F5166 | 5146, 5147, 5148, 5149, 5150, 5151, 5152, 5153, 5154, 5155, 5156, 5157, 5158, 5159, 5160, 5161, 5162, 5163, 5164, 5165, 5166 | [src-000376 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md>) |
| src-000379 | FullBusinessModel!A633:F653 | 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653 | [src-000379 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md>) |
| src-000382 | FullBusinessModel!A5115:F5135 | 5115, 5116, 5117, 5118, 5119, 5120, 5121, 5122, 5123, 5124, 5125, 5126, 5127, 5128, 5129, 5130, 5131, 5132, 5133, 5134, 5135 | [src-000382 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | parent | C5146 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000006 | field-type | E5147 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000006 | field-type | E5148 | MarketTypeCode | Not a component record in this worksheet |
| src-000006 | field-type | E5149 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000006 | field-type | E5150 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000006 | field-type | E5151 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000006 | field-type | E5152 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000006 | field-type | E5153 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E5154 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000006 | field-type | E5155 | CurrencyCode | Not a component record in this worksheet |
| src-000006 | field-type | E5156 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000006 | field-type | E5157 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000006 | field-type | E5158 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000006 | field-type | E5159 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000006 | field-type | E5160 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000006 | field-type | E5161 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000006 | field-type | E5162 | CurrencyCode | Not a component record in this worksheet |
| src-000006 | field-type | E5163 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E5164 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E5165 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000006 | field-type | E5166 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000016 | parent | C5076 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000016 | field-type | E5077 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000016 | field-type | E5078 | MarketTypeCode | Not a component record in this worksheet |
| src-000016 | field-type | E5079 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000016 | field-type | E5080 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000016 | field-type | E5081 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000016 | field-type | E5082 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000016 | field-type | E5083 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E5084 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000016 | field-type | E5085 | CurrencyCode | Not a component record in this worksheet |
| src-000016 | field-type | E5086 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000016 | field-type | E5087 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000016 | field-type | E5088 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000016 | field-type | E5089 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000016 | field-type | E5090 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000016 | field-type | E5091 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000016 | field-type | E5092 | CurrencyCode | Not a component record in this worksheet |
| src-000016 | field-type | E5093 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E5094 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E5095 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000016 | field-type | E5096 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000054 | parent | C5146 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000054 | field-type | E5147 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000054 | field-type | E5148 | MarketTypeCode | Not a component record in this worksheet |
| src-000054 | field-type | E5149 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000054 | field-type | E5150 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000054 | field-type | E5151 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000054 | field-type | E5152 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000054 | field-type | E5153 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E5154 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000054 | field-type | E5155 | CurrencyCode | Not a component record in this worksheet |
| src-000054 | field-type | E5156 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000054 | field-type | E5157 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000054 | field-type | E5158 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000054 | field-type | E5159 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000054 | field-type | E5160 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000054 | field-type | E5161 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000054 | field-type | E5162 | CurrencyCode | Not a component record in this worksheet |
| src-000054 | field-type | E5163 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E5164 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E5165 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000054 | field-type | E5166 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000081 | parent | C5146 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000081 | field-type | E5147 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000081 | field-type | E5148 | MarketTypeCode | Not a component record in this worksheet |
| src-000081 | field-type | E5149 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000081 | field-type | E5150 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000081 | field-type | E5151 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000081 | field-type | E5152 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000081 | field-type | E5153 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E5154 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000081 | field-type | E5155 | CurrencyCode | Not a component record in this worksheet |
| src-000081 | field-type | E5156 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000081 | field-type | E5157 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000081 | field-type | E5158 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000081 | field-type | E5159 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000081 | field-type | E5160 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000081 | field-type | E5161 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000081 | field-type | E5162 | CurrencyCode | Not a component record in this worksheet |
| src-000081 | field-type | E5163 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E5164 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E5165 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000081 | field-type | E5166 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000097 | parent | C5146 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000097 | field-type | E5147 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000097 | field-type | E5148 | MarketTypeCode | Not a component record in this worksheet |
| src-000097 | field-type | E5149 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000097 | field-type | E5150 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000097 | field-type | E5151 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000097 | field-type | E5152 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000097 | field-type | E5153 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E5154 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000097 | field-type | E5155 | CurrencyCode | Not a component record in this worksheet |
| src-000097 | field-type | E5156 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000097 | field-type | E5157 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000097 | field-type | E5158 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000097 | field-type | E5159 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000097 | field-type | E5160 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000097 | field-type | E5161 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000097 | field-type | E5162 | CurrencyCode | Not a component record in this worksheet |
| src-000097 | field-type | E5163 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E5164 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E5165 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000097 | field-type | E5166 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000164 | parent | C5146 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000164 | field-type | E5147 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000164 | field-type | E5148 | MarketTypeCode | Not a component record in this worksheet |
| src-000164 | field-type | E5149 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000164 | field-type | E5150 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000164 | field-type | E5151 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000164 | field-type | E5152 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000164 | field-type | E5153 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E5154 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000164 | field-type | E5155 | CurrencyCode | Not a component record in this worksheet |
| src-000164 | field-type | E5156 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000164 | field-type | E5157 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000164 | field-type | E5158 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000164 | field-type | E5159 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000164 | field-type | E5160 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000164 | field-type | E5161 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000164 | field-type | E5162 | CurrencyCode | Not a component record in this worksheet |
| src-000164 | field-type | E5163 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E5164 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E5165 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000164 | field-type | E5166 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000175 | parent | C5146 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000175 | field-type | E5147 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000175 | field-type | E5148 | MarketTypeCode | Not a component record in this worksheet |
| src-000175 | field-type | E5149 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000175 | field-type | E5150 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000175 | field-type | E5151 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000175 | field-type | E5152 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000175 | field-type | E5153 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E5154 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000175 | field-type | E5155 | CurrencyCode | Not a component record in this worksheet |
| src-000175 | field-type | E5156 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000175 | field-type | E5157 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000175 | field-type | E5158 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000175 | field-type | E5159 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000175 | field-type | E5160 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000175 | field-type | E5161 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000175 | field-type | E5162 | CurrencyCode | Not a component record in this worksheet |
| src-000175 | field-type | E5163 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E5164 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E5165 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000175 | field-type | E5166 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000182 | parent | C5076 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000182 | field-type | E5077 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000182 | field-type | E5078 | MarketTypeCode | Not a component record in this worksheet |
| src-000182 | field-type | E5079 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000182 | field-type | E5080 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000182 | field-type | E5081 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000182 | field-type | E5082 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000182 | field-type | E5083 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E5084 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000182 | field-type | E5085 | CurrencyCode | Not a component record in this worksheet |
| src-000182 | field-type | E5086 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000182 | field-type | E5087 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000182 | field-type | E5088 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000182 | field-type | E5089 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000182 | field-type | E5090 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000182 | field-type | E5091 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000182 | field-type | E5092 | CurrencyCode | Not a component record in this worksheet |
| src-000182 | field-type | E5093 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E5094 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E5095 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000182 | field-type | E5096 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000198 | parent | C5146 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000198 | field-type | E5147 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000198 | field-type | E5148 | MarketTypeCode | Not a component record in this worksheet |
| src-000198 | field-type | E5149 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000198 | field-type | E5150 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000198 | field-type | E5151 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000198 | field-type | E5152 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000198 | field-type | E5153 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E5154 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000198 | field-type | E5155 | CurrencyCode | Not a component record in this worksheet |
| src-000198 | field-type | E5156 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000198 | field-type | E5157 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000198 | field-type | E5158 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000198 | field-type | E5159 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000198 | field-type | E5160 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000198 | field-type | E5161 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000198 | field-type | E5162 | CurrencyCode | Not a component record in this worksheet |
| src-000198 | field-type | E5163 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E5164 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E5165 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000198 | field-type | E5166 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000322 | parent | C5115 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000322 | field-type | E5116 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000322 | field-type | E5117 | MarketTypeCode | Not a component record in this worksheet |
| src-000322 | field-type | E5118 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000322 | field-type | E5119 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000322 | field-type | E5120 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000322 | field-type | E5121 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000322 | field-type | E5122 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E5123 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000322 | field-type | E5124 | CurrencyCode | Not a component record in this worksheet |
| src-000322 | field-type | E5125 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000322 | field-type | E5126 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000322 | field-type | E5127 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000322 | field-type | E5128 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000322 | field-type | E5129 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000322 | field-type | E5130 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000322 | field-type | E5131 | CurrencyCode | Not a component record in this worksheet |
| src-000322 | field-type | E5132 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E5133 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E5134 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000322 | field-type | E5135 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000345 | parent | C633 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000345 | field-type | E634 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000345 | field-type | E635 | MarketTypeCode | Not a component record in this worksheet |
| src-000345 | field-type | E636 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000345 | field-type | E637 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000345 | field-type | E638 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000345 | field-type | E639 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000345 | field-type | E640 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E641 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000345 | field-type | E642 | CurrencyCode | Not a component record in this worksheet |
| src-000345 | field-type | E643 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000345 | field-type | E644 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000345 | field-type | E645 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000345 | field-type | E646 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000345 | field-type | E647 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000345 | field-type | E648 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000345 | field-type | E649 | CurrencyCode | Not a component record in this worksheet |
| src-000345 | field-type | E650 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E651 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E652 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000345 | field-type | E653 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000348 | parent | C5115 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000348 | field-type | E5116 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000348 | field-type | E5117 | MarketTypeCode | Not a component record in this worksheet |
| src-000348 | field-type | E5118 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000348 | field-type | E5119 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000348 | field-type | E5120 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000348 | field-type | E5121 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000348 | field-type | E5122 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E5123 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000348 | field-type | E5124 | CurrencyCode | Not a component record in this worksheet |
| src-000348 | field-type | E5125 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000348 | field-type | E5126 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000348 | field-type | E5127 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000348 | field-type | E5128 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000348 | field-type | E5129 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000348 | field-type | E5130 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000348 | field-type | E5131 | CurrencyCode | Not a component record in this worksheet |
| src-000348 | field-type | E5132 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E5133 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E5134 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000348 | field-type | E5135 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000352 | parent | C5146 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000352 | field-type | E5147 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000352 | field-type | E5148 | MarketTypeCode | Not a component record in this worksheet |
| src-000352 | field-type | E5149 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000352 | field-type | E5150 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000352 | field-type | E5151 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000352 | field-type | E5152 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000352 | field-type | E5153 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E5154 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000352 | field-type | E5155 | CurrencyCode | Not a component record in this worksheet |
| src-000352 | field-type | E5156 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000352 | field-type | E5157 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000352 | field-type | E5158 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000352 | field-type | E5159 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000352 | field-type | E5160 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000352 | field-type | E5161 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000352 | field-type | E5162 | CurrencyCode | Not a component record in this worksheet |
| src-000352 | field-type | E5163 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E5164 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E5165 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000352 | field-type | E5166 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000355 | parent | C5050 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000355 | field-type | E5051 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000355 | field-type | E5052 | MarketTypeCode | Not a component record in this worksheet |
| src-000355 | field-type | E5053 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000355 | field-type | E5054 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000355 | field-type | E5055 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000355 | field-type | E5056 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000355 | field-type | E5057 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E5058 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000355 | field-type | E5059 | CurrencyCode | Not a component record in this worksheet |
| src-000355 | field-type | E5060 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000355 | field-type | E5061 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000355 | field-type | E5062 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000355 | field-type | E5063 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000355 | field-type | E5064 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000355 | field-type | E5065 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000355 | field-type | E5066 | CurrencyCode | Not a component record in this worksheet |
| src-000355 | field-type | E5067 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E5068 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E5069 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000355 | field-type | E5070 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000358 | parent | C633 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000358 | field-type | E634 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000358 | field-type | E635 | MarketTypeCode | Not a component record in this worksheet |
| src-000358 | field-type | E636 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000358 | field-type | E637 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000358 | field-type | E638 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000358 | field-type | E639 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000358 | field-type | E640 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E641 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000358 | field-type | E642 | CurrencyCode | Not a component record in this worksheet |
| src-000358 | field-type | E643 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000358 | field-type | E644 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000358 | field-type | E645 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000358 | field-type | E646 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000358 | field-type | E647 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000358 | field-type | E648 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000358 | field-type | E649 | CurrencyCode | Not a component record in this worksheet |
| src-000358 | field-type | E650 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E651 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E652 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000358 | field-type | E653 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000361 | parent | C633 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000361 | field-type | E634 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000361 | field-type | E635 | MarketTypeCode | Not a component record in this worksheet |
| src-000361 | field-type | E636 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000361 | field-type | E637 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000361 | field-type | E638 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000361 | field-type | E639 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000361 | field-type | E640 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E641 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000361 | field-type | E642 | CurrencyCode | Not a component record in this worksheet |
| src-000361 | field-type | E643 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000361 | field-type | E644 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000361 | field-type | E645 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000361 | field-type | E646 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000361 | field-type | E647 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000361 | field-type | E648 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000361 | field-type | E649 | CurrencyCode | Not a component record in this worksheet |
| src-000361 | field-type | E650 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E651 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E652 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000361 | field-type | E653 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000364 | parent | C5050 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000364 | field-type | E5051 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000364 | field-type | E5052 | MarketTypeCode | Not a component record in this worksheet |
| src-000364 | field-type | E5053 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000364 | field-type | E5054 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000364 | field-type | E5055 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000364 | field-type | E5056 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000364 | field-type | E5057 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E5058 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000364 | field-type | E5059 | CurrencyCode | Not a component record in this worksheet |
| src-000364 | field-type | E5060 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000364 | field-type | E5061 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000364 | field-type | E5062 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000364 | field-type | E5063 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000364 | field-type | E5064 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000364 | field-type | E5065 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000364 | field-type | E5066 | CurrencyCode | Not a component record in this worksheet |
| src-000364 | field-type | E5067 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E5068 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E5069 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000364 | field-type | E5070 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000367 | parent | C5050 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000367 | field-type | E5051 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000367 | field-type | E5052 | MarketTypeCode | Not a component record in this worksheet |
| src-000367 | field-type | E5053 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000367 | field-type | E5054 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000367 | field-type | E5055 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000367 | field-type | E5056 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000367 | field-type | E5057 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E5058 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000367 | field-type | E5059 | CurrencyCode | Not a component record in this worksheet |
| src-000367 | field-type | E5060 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000367 | field-type | E5061 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000367 | field-type | E5062 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000367 | field-type | E5063 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000367 | field-type | E5064 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000367 | field-type | E5065 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000367 | field-type | E5066 | CurrencyCode | Not a component record in this worksheet |
| src-000367 | field-type | E5067 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E5068 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E5069 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000367 | field-type | E5070 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000370 | parent | C633 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000370 | field-type | E634 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000370 | field-type | E635 | MarketTypeCode | Not a component record in this worksheet |
| src-000370 | field-type | E636 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000370 | field-type | E637 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000370 | field-type | E638 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000370 | field-type | E639 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000370 | field-type | E640 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E641 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000370 | field-type | E642 | CurrencyCode | Not a component record in this worksheet |
| src-000370 | field-type | E643 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000370 | field-type | E644 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000370 | field-type | E645 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000370 | field-type | E646 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000370 | field-type | E647 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000370 | field-type | E648 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000370 | field-type | E649 | CurrencyCode | Not a component record in this worksheet |
| src-000370 | field-type | E650 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E651 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E652 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000370 | field-type | E653 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000373 | parent | C633 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000373 | field-type | E634 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000373 | field-type | E635 | MarketTypeCode | Not a component record in this worksheet |
| src-000373 | field-type | E636 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000373 | field-type | E637 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000373 | field-type | E638 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000373 | field-type | E639 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000373 | field-type | E640 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E641 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000373 | field-type | E642 | CurrencyCode | Not a component record in this worksheet |
| src-000373 | field-type | E643 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000373 | field-type | E644 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000373 | field-type | E645 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000373 | field-type | E646 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000373 | field-type | E647 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000373 | field-type | E648 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000373 | field-type | E649 | CurrencyCode | Not a component record in this worksheet |
| src-000373 | field-type | E650 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E651 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E652 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000373 | field-type | E653 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000376 | parent | C5146 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000376 | field-type | E5147 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000376 | field-type | E5148 | MarketTypeCode | Not a component record in this worksheet |
| src-000376 | field-type | E5149 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000376 | field-type | E5150 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000376 | field-type | E5151 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000376 | field-type | E5152 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000376 | field-type | E5153 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E5154 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000376 | field-type | E5155 | CurrencyCode | Not a component record in this worksheet |
| src-000376 | field-type | E5156 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000376 | field-type | E5157 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000376 | field-type | E5158 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000376 | field-type | E5159 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000376 | field-type | E5160 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000376 | field-type | E5161 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000376 | field-type | E5162 | CurrencyCode | Not a component record in this worksheet |
| src-000376 | field-type | E5163 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E5164 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E5165 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000376 | field-type | E5166 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000379 | parent | C633 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000379 | field-type | E634 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000379 | field-type | E635 | MarketTypeCode | Not a component record in this worksheet |
| src-000379 | field-type | E636 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000379 | field-type | E637 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000379 | field-type | E638 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000379 | field-type | E639 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000379 | field-type | E640 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E641 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000379 | field-type | E642 | CurrencyCode | Not a component record in this worksheet |
| src-000379 | field-type | E643 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000379 | field-type | E644 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000379 | field-type | E645 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000379 | field-type | E646 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000379 | field-type | E647 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000379 | field-type | E648 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000379 | field-type | E649 | CurrencyCode | Not a component record in this worksheet |
| src-000379 | field-type | E650 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E651 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E652 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000379 | field-type | E653 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |
| src-000382 | parent | C5115 | Market | [Market](<bc-52f11ada74049ed3578f.md>) |
| src-000382 | field-type | E5116 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000382 | field-type | E5117 | MarketTypeCode | Not a component record in this worksheet |
| src-000382 | field-type | E5118 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000382 | field-type | E5119 | SourceOfPrice | [SourceOfPrice](<bc-eff806a915d8a016ae85.md>) |
| src-000382 | field-type | E5120 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000382 | field-type | E5121 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000382 | field-type | E5122 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E5123 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000382 | field-type | E5124 | CurrencyCode | Not a component record in this worksheet |
| src-000382 | field-type | E5125 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000382 | field-type | E5126 | StockExchange | [StockExchange](<bc-0e2b372cbfe3d5a2887d.md>) |
| src-000382 | field-type | E5127 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000382 | field-type | E5128 | LotBreakdown | [LotBreakdown](<bc-08236811cf351f1681e6.md>) |
| src-000382 | field-type | E5129 | TradingSession | [TradingSession](<bc-45cd462d5902b8aeef50.md>) |
| src-000382 | field-type | E5130 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000382 | field-type | E5131 | CurrencyCode | Not a component record in this worksheet |
| src-000382 | field-type | E5132 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E5133 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E5134 | Issuance | [Issuance](<bc-7d8739f474d308a4a300.md>) |
| src-000382 | field-type | E5135 | PlaceOfSettlement | [PlaceOfSettlement](<bc-d95ef3975d0a864f6418.md>) |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
