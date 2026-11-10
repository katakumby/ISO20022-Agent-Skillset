---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-bd0cd42d14c188c2ad1a"
title: "SecuritiesTradeIdentification"
business_component_name: "SecuritiesTradeIdentification"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A4591:F4607"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A4521:F4537"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A4591:F4607"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A4591:F4607"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A4591:F4607"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A4591:F4607"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A4591:F4607"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A4521:F4537"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A4591:F4607"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A4560:F4576"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A1367:F1383"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A4560:F4576"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A4591:F4607"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A4495:F4511"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A1367:F1383"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A1367:F1383"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A4495:F4511"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A4495:F4511"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A1367:F1383"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A1367:F1383"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A4591:F4607"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A1367:F1383"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A4560:F4576"]}]
content_sha256: "bd0cd42d14c188c2ad1a902729d051300992b3ce5284d5cf016e309537ae2a4a"
parent_names: ["TradeIdentification"]
related_component_names: ["Max35Text", "SecuritiesTrade"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# SecuritiesTradeIdentification

## Definition

Specifies the different identifications associated with a securities transaction.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SecuritiesTradeIdentification | ∅ | TradeIdentification | Specifies the different identifications associated with a securities transaction. | ∅ | ∅ |
| 2 | SecuritiesTradeIdentification | IdentifiedTrade | ∅ | Trade for which one or more identifications are provided. | SecuritiesTrade | SecuritiesTradeRelatedIdentifications |
| 3 | SecuritiesTradeIdentification | MarketInfrastructureTransactionIdentification | ∅ | Identification of a transaction assigned by a market infrastructure other than a central securities depository, for example, Target2-Securities. | Max35Text | ∅ |
| 4 | SecuritiesTradeIdentification | ProcessorTransactionIdentification | ∅ | Identification of the transaction assigned by the processor of the instruction other than the account owner the account servicer and the market infrastructure. | Max35Text | ∅ |
| 5 | SecuritiesTradeIdentification | PoolIdentification | ∅ | Collective reference identifying a set of messages. | Max35Text | ∅ |
| 6 | SecuritiesTradeIdentification | CollateralTransactionIdentification | ∅ | Unambiguous identification of a collateral transaction. | Max35Text | ∅ |
| 7 | SecuritiesTradeIdentification | ClientTripartyCollateralTransactionIdentification | ∅ | Unique reference identifying the triparty collateral management transaction from the client's point of view. | Max35Text | ∅ |
| 8 | SecuritiesTradeIdentification | TripartyAgentCollateralTransactionIdentification | ∅ | Unique reference identifying the triparty collateral management transaction from the triparty agent's point of view. | Max35Text | ∅ |
| 9 | SecuritiesTradeIdentification | BasketIdentification | ∅ | Identification of a basket trade. | Max35Text | ∅ |
| 10 | SecuritiesTradeIdentification | ProgramIdentification | ∅ | Program reference which identifies a program trade. | Max35Text | ∅ |
| 11 | SecuritiesTradeIdentification | BlockIdentification | ∅ | Reference of the linked message at the trade/block level which identifies a centrally matched transaction. | Max35Text | ∅ |
| 12 | SecuritiesTradeIdentification | AllocationIdentification | ∅ | Identification at the allocation level. | Max35Text | ∅ |
| 13 | SecuritiesTradeIdentification | ComplianceIdentification | ∅ | Identification which represents this transaction for compliance purposes. | Max35Text | ∅ |
| 14 | SecuritiesTradeIdentification | CSDTransactionIdentification | ∅ | Identification given by the central securities depository  to the transaction. | Max35Text | ∅ |
| 15 | SecuritiesTradeIdentification | CentralCounterpartyTransactionIdentification | ∅ | Identification of the transaction assigned by the central counterparty. | Max35Text | ∅ |
| 16 | SecuritiesTradeIdentification | CancellationRequestIdentification | ∅ | Unambiguous identification of the cancellation request as known by the instructing party. | Max35Text | ∅ |
| 17 | SecuritiesTradeIdentification | CounterpartyMarketInfrastructureTransactionIdentification | ∅ | Identification of a counterparty transaction assigned by a market infrastructure other than a central securities depository, for example, Target2-Securities. | Max35Text | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `bd0cd42d14c188c2ad1a902729d051300992b3ce5284d5cf016e309537ae2a4a`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A4591:F4607 | 4591, 4592, 4593, 4594, 4595, 4596, 4597, 4598, 4599, 4600, 4601, 4602, 4603, 4604, 4605, 4606, 4607 | [src-000006 original](../../../evidence/omitted/5e0f6b7d43fcbbe816624756.md) | [Lookup](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md) |
| src-000016 | FullBusinessModel!A4521:F4537 | 4521, 4522, 4523, 4524, 4525, 4526, 4527, 4528, 4529, 4530, 4531, 4532, 4533, 4534, 4535, 4536, 4537 | [src-000016 original](../../../evidence/omitted/42cf3c4088baf4d4c6dc07c1.md) | [Lookup](../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md) |
| src-000054 | FullBusinessModel!A4591:F4607 | 4591, 4592, 4593, 4594, 4595, 4596, 4597, 4598, 4599, 4600, 4601, 4602, 4603, 4604, 4605, 4606, 4607 | [src-000054 original](../../../evidence/omitted/ea96e6afbf1f8819d68ca6f6.md) | [Lookup](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md) |
| src-000081 | FullBusinessModel!A4591:F4607 | 4591, 4592, 4593, 4594, 4595, 4596, 4597, 4598, 4599, 4600, 4601, 4602, 4603, 4604, 4605, 4606, 4607 | [src-000081 original](../../../evidence/omitted/5d05ada13720516836bc5043.md) | [Lookup](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md) |
| src-000097 | FullBusinessModel!A4591:F4607 | 4591, 4592, 4593, 4594, 4595, 4596, 4597, 4598, 4599, 4600, 4601, 4602, 4603, 4604, 4605, 4606, 4607 | [src-000097 original](../../../evidence/omitted/3ea6002607634c1b65cb5c88.md) | [Lookup](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md) |
| src-000164 | FullBusinessModel!A4591:F4607 | 4591, 4592, 4593, 4594, 4595, 4596, 4597, 4598, 4599, 4600, 4601, 4602, 4603, 4604, 4605, 4606, 4607 | [src-000164 original](../../../evidence/omitted/87020353dd81a550a7b6ed6f.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md) |
| src-000175 | FullBusinessModel!A4591:F4607 | 4591, 4592, 4593, 4594, 4595, 4596, 4597, 4598, 4599, 4600, 4601, 4602, 4603, 4604, 4605, 4606, 4607 | [src-000175 original](../../../evidence/omitted/807236f9f4d5f25826f3ba17.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md) |
| src-000182 | FullBusinessModel!A4521:F4537 | 4521, 4522, 4523, 4524, 4525, 4526, 4527, 4528, 4529, 4530, 4531, 4532, 4533, 4534, 4535, 4536, 4537 | [src-000182 original](../../../evidence/omitted/5096efb167050baf43bfb32a.md) | [Lookup](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md) |
| src-000198 | FullBusinessModel!A4591:F4607 | 4591, 4592, 4593, 4594, 4595, 4596, 4597, 4598, 4599, 4600, 4601, 4602, 4603, 4604, 4605, 4606, 4607 | [src-000198 original](../../../evidence/omitted/c6a84c22fb63cab3b848bd88.md) | [Lookup](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md) |
| src-000322 | FullBusinessModel!A4560:F4576 | 4560, 4561, 4562, 4563, 4564, 4565, 4566, 4567, 4568, 4569, 4570, 4571, 4572, 4573, 4574, 4575, 4576 | [src-000322 original](../../../evidence/omitted/f39eee3c04bb287d206cc6a3.md) | [Lookup](../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md) |
| src-000345 | FullBusinessModel!A1367:F1383 | 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383 | [src-000345 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md) |
| src-000348 | FullBusinessModel!A4560:F4576 | 4560, 4561, 4562, 4563, 4564, 4565, 4566, 4567, 4568, 4569, 4570, 4571, 4572, 4573, 4574, 4575, 4576 | [src-000348 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md) |
| src-000352 | FullBusinessModel!A4591:F4607 | 4591, 4592, 4593, 4594, 4595, 4596, 4597, 4598, 4599, 4600, 4601, 4602, 4603, 4604, 4605, 4606, 4607 | [src-000352 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md) |
| src-000355 | FullBusinessModel!A4495:F4511 | 4495, 4496, 4497, 4498, 4499, 4500, 4501, 4502, 4503, 4504, 4505, 4506, 4507, 4508, 4509, 4510, 4511 | [src-000355 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md) |
| src-000358 | FullBusinessModel!A1367:F1383 | 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383 | [src-000358 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md) |
| src-000361 | FullBusinessModel!A1367:F1383 | 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383 | [src-000361 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md) |
| src-000364 | FullBusinessModel!A4495:F4511 | 4495, 4496, 4497, 4498, 4499, 4500, 4501, 4502, 4503, 4504, 4505, 4506, 4507, 4508, 4509, 4510, 4511 | [src-000364 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md) |
| src-000367 | FullBusinessModel!A4495:F4511 | 4495, 4496, 4497, 4498, 4499, 4500, 4501, 4502, 4503, 4504, 4505, 4506, 4507, 4508, 4509, 4510, 4511 | [src-000367 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md) |
| src-000370 | FullBusinessModel!A1367:F1383 | 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383 | [src-000370 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md) |
| src-000373 | FullBusinessModel!A1367:F1383 | 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383 | [src-000373 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md) |
| src-000376 | FullBusinessModel!A4591:F4607 | 4591, 4592, 4593, 4594, 4595, 4596, 4597, 4598, 4599, 4600, 4601, 4602, 4603, 4604, 4605, 4606, 4607 | [src-000376 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md) |
| src-000379 | FullBusinessModel!A1367:F1383 | 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383 | [src-000379 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md) |
| src-000382 | FullBusinessModel!A4560:F4576 | 4560, 4561, 4562, 4563, 4564, 4565, 4566, 4567, 4568, 4569, 4570, 4571, 4572, 4573, 4574, 4575, 4576 | [src-000382 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | parent | C4591 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000006 | field-type | E4592 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000006 | field-type | E4593 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4594 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4595 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4596 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4597 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4598 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4599 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4600 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4601 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4602 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4603 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4604 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4605 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4606 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E4607 | Max35Text | Not a component record in this worksheet |
| src-000016 | parent | C4521 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000016 | field-type | E4522 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000016 | field-type | E4523 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4524 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4525 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4526 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4527 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4528 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4529 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4530 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4531 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4532 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4533 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4534 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4535 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4536 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E4537 | Max35Text | Not a component record in this worksheet |
| src-000054 | parent | C4591 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000054 | field-type | E4592 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000054 | field-type | E4593 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4594 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4595 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4596 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4597 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4598 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4599 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4600 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4601 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4602 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4603 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4604 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4605 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4606 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E4607 | Max35Text | Not a component record in this worksheet |
| src-000081 | parent | C4591 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000081 | field-type | E4592 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000081 | field-type | E4593 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4594 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4595 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4596 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4597 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4598 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4599 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4600 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4601 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4602 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4603 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4604 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4605 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4606 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E4607 | Max35Text | Not a component record in this worksheet |
| src-000097 | parent | C4591 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000097 | field-type | E4592 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000097 | field-type | E4593 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4594 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4595 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4596 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4597 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4598 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4599 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4600 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4601 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4602 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4603 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4604 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4605 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4606 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E4607 | Max35Text | Not a component record in this worksheet |
| src-000164 | parent | C4591 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000164 | field-type | E4592 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000164 | field-type | E4593 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4594 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4595 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4596 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4597 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4598 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4599 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4600 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4601 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4602 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4603 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4604 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4605 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4606 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E4607 | Max35Text | Not a component record in this worksheet |
| src-000175 | parent | C4591 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000175 | field-type | E4592 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000175 | field-type | E4593 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4594 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4595 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4596 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4597 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4598 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4599 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4600 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4601 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4602 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4603 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4604 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4605 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4606 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E4607 | Max35Text | Not a component record in this worksheet |
| src-000182 | parent | C4521 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000182 | field-type | E4522 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000182 | field-type | E4523 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4524 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4525 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4526 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4527 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4528 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4529 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4530 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4531 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4532 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4533 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4534 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4535 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4536 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E4537 | Max35Text | Not a component record in this worksheet |
| src-000198 | parent | C4591 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000198 | field-type | E4592 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000198 | field-type | E4593 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4594 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4595 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4596 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4597 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4598 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4599 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4600 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4601 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4602 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4603 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4604 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4605 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4606 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E4607 | Max35Text | Not a component record in this worksheet |
| src-000322 | parent | C4560 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000322 | field-type | E4561 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000322 | field-type | E4562 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4563 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4564 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4565 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4566 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4567 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4568 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4569 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4570 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4571 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4572 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4573 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4574 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4575 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E4576 | Max35Text | Not a component record in this worksheet |
| src-000345 | parent | C1367 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000345 | field-type | E1368 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000345 | field-type | E1369 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E1370 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E1371 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E1372 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E1373 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E1374 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E1375 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E1376 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E1377 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E1378 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E1379 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E1380 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E1381 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E1382 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E1383 | Max35Text | Not a component record in this worksheet |
| src-000348 | parent | C4560 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000348 | field-type | E4561 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000348 | field-type | E4562 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4563 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4564 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4565 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4566 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4567 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4568 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4569 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4570 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4571 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4572 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4573 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4574 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4575 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E4576 | Max35Text | Not a component record in this worksheet |
| src-000352 | parent | C4591 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000352 | field-type | E4592 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000352 | field-type | E4593 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4594 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4595 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4596 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4597 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4598 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4599 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4600 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4601 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4602 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4603 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4604 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4605 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4606 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E4607 | Max35Text | Not a component record in this worksheet |
| src-000355 | parent | C4495 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000355 | field-type | E4496 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000355 | field-type | E4497 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E4498 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E4499 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E4500 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E4501 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E4502 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E4503 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E4504 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E4505 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E4506 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E4507 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E4508 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E4509 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E4510 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E4511 | Max35Text | Not a component record in this worksheet |
| src-000358 | parent | C1367 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000358 | field-type | E1368 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000358 | field-type | E1369 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E1370 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E1371 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E1372 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E1373 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E1374 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E1375 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E1376 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E1377 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E1378 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E1379 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E1380 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E1381 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E1382 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E1383 | Max35Text | Not a component record in this worksheet |
| src-000361 | parent | C1367 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000361 | field-type | E1368 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000361 | field-type | E1369 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E1370 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E1371 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E1372 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E1373 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E1374 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E1375 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E1376 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E1377 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E1378 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E1379 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E1380 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E1381 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E1382 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E1383 | Max35Text | Not a component record in this worksheet |
| src-000364 | parent | C4495 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000364 | field-type | E4496 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000364 | field-type | E4497 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E4498 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E4499 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E4500 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E4501 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E4502 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E4503 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E4504 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E4505 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E4506 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E4507 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E4508 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E4509 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E4510 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E4511 | Max35Text | Not a component record in this worksheet |
| src-000367 | parent | C4495 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000367 | field-type | E4496 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000367 | field-type | E4497 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E4498 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E4499 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E4500 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E4501 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E4502 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E4503 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E4504 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E4505 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E4506 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E4507 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E4508 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E4509 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E4510 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E4511 | Max35Text | Not a component record in this worksheet |
| src-000370 | parent | C1367 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000370 | field-type | E1368 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000370 | field-type | E1369 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E1370 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E1371 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E1372 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E1373 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E1374 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E1375 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E1376 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E1377 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E1378 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E1379 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E1380 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E1381 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E1382 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E1383 | Max35Text | Not a component record in this worksheet |
| src-000373 | parent | C1367 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000373 | field-type | E1368 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000373 | field-type | E1369 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E1370 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E1371 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E1372 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E1373 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E1374 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E1375 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E1376 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E1377 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E1378 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E1379 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E1380 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E1381 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E1382 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E1383 | Max35Text | Not a component record in this worksheet |
| src-000376 | parent | C4591 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000376 | field-type | E4592 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000376 | field-type | E4593 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4594 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4595 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4596 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4597 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4598 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4599 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4600 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4601 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4602 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4603 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4604 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4605 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4606 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E4607 | Max35Text | Not a component record in this worksheet |
| src-000379 | parent | C1367 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000379 | field-type | E1368 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000379 | field-type | E1369 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E1370 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E1371 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E1372 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E1373 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E1374 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E1375 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E1376 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E1377 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E1378 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E1379 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E1380 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E1381 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E1382 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E1383 | Max35Text | Not a component record in this worksheet |
| src-000382 | parent | C4560 | TradeIdentification | [TradeIdentification](bc-7491dbca16fb0c775ca1.md) |
| src-000382 | field-type | E4561 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000382 | field-type | E4562 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4563 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4564 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4565 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4566 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4567 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4568 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4569 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4570 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4571 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4572 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4573 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4574 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4575 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E4576 | Max35Text | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](index.md) · [Known limitations and issues](../../../tracking/issues.md)
