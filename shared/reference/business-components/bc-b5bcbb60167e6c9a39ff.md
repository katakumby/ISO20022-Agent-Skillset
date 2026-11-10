---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-b5bcbb60167e6c9a39ff"
title: "ClearingMemberRole"
business_component_name: "ClearingMemberRole"
aliases: []
domain: "shared"
domains: ["payments", "securities"]
message_sets: ["bank-to-customer-cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "settlement-and-reconciliation", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-securities-and-penalty-reporting", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000198", "src-000322", "src-000348", "src-000352", "src-000376", "src-000382"]
source_editions: ["2025", "2025-2026", "august-2026", "december-2025", "march-2026", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A817:F826"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A817:F826"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A817:F826"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A817:F826"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A817:F826"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A817:F826"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A817:F826"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A814:F823"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A814:F823"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A817:F826"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A817:F826"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A814:F823"]}]
content_sha256: "b5bcbb60167e6c9a39ff47da87e6de7e4afa69b295c2409380736a564f80f90b"
parent_names: ["SystemPartyRole"]
related_component_names: ["Account", "ActiveCurrencyAndAmount", "CashClearingSystemMember", "ClearingMemberRole", "ClearingSideCode", "SecuritiesAccount"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# ClearingMemberRole

## Definition

Member of an exchange's clearing corporation, responsible for executing client trades and involved in the clearing of trades.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ClearingMemberRole | ∅ | SystemPartyRole | Member of an exchange's clearing corporation, responsible for executing client trades and involved in the clearing of trades. | ∅ | ∅ |
| 2 | ClearingMemberRole | ClearingSystemMemberIdentification | ∅ | Unique and unambiguous identifier of a clearing system member, assigned by the system or system administrator. | CashClearingSystemMember | ClearingMember |
| 3 | ClearingMemberRole | Side | ∅ | Specifies the side of the clearing member. | ClearingSideCode | ∅ |
| 4 | ClearingMemberRole | ClearingAccount | ∅ | Identifies the clearing member account at the CCP through which the trade must be cleared (sometimes called position account). | SecuritiesAccount | ClearingAccountOwner |
| 5 | ClearingMemberRole | MarginAccount | ∅ | Margin account where the negociation and liquidation risks will be calculated. | SecuritiesAccount | MarginAccountOwner |
| 6 | ClearingMemberRole | DeliveryAccount | ∅ | Account opened by the central counterparty in the name of the clearing member within the account structure, for settlement purposes (gives information about the clearing member account at central counterparty). | SecuritiesAccount | DeliveryAccountOwner |
| 7 | ClearingMemberRole | DefaultFundAccount | ∅ | Specifies the account identification of the clearing member at the ICSD (International Central Securities Depository) or at the Central Bank. | Account | DefaultFundAccountOwner |
| 8 | ClearingMemberRole | ClearingSegment | ∅ | Clearing segment within a clearing organisation that allows the segregation of flows coming from clearing counterparty's clearing system.  | ClearingMemberRole | RelatedClearingMemberRole |
| 9 | ClearingMemberRole | RelatedClearingMemberRole | ∅ | Clearing member for which a clearing segment is specified. | ClearingMemberRole | ClearingSegment |
| 10 | ClearingMemberRole | ClearingFee | ∅ | Charges related to the clearing. | ActiveCurrencyAndAmount | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `b5bcbb60167e6c9a39ff47da87e6de7e4afa69b295c2409380736a564f80f90b`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A817:F826 | 817, 818, 819, 820, 821, 822, 823, 824, 825, 826 | [src-000006 original](<../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart3_BanktoCustomerCashManagement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md>) |
| src-000054 | FullBusinessModel!A817:F826 | 817, 818, 819, 820, 821, 822, 823, 824, 825, 826 | [src-000054 original](<../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart3_CentralCounterParty_SecuritiesClearing_Maintenance_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md>) |
| src-000081 | FullBusinessModel!A817:F826 | 817, 818, 819, 820, 821, 822, 823, 824, 825, 826 | [src-000081 original](<../../../raw-input/corporate_actions/ISO20022_MDRPart3_CorporateActions_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md>) |
| src-000097 | FullBusinessModel!A817:F826 | 817, 818, 819, 820, 821, 822, 823, 824, 825, 826 | [src-000097 original](<../../../raw-input/investment_funds/ISO20022_MDRPart3_Investment-Funds_2025_2026_v2.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md>) |
| src-000164 | FullBusinessModel!A817:F826 | 817, 818, 819, 820, 821, 822, 823, 824, 825, 826 | [src-000164 original](<../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart3_PaymentsClearingandSettlement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md>) |
| src-000175 | FullBusinessModel!A817:F826 | 817, 818, 819, 820, 821, 822, 823, 824, 825, 826 | [src-000175 original](<../../../raw-input/payments_initiation/ISO20022_MDRPart3_PaymentsInitiation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md>) |
| src-000198 | FullBusinessModel!A817:F826 | 817, 818, 819, 820, 821, 822, 823, 824, 825, 826 | [src-000198 original](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart3_SettlementAndReconciliation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md>) |
| src-000322 | FullBusinessModel!A814:F823 | 814, 815, 816, 817, 818, 819, 820, 821, 822, 823 | [src-000322 original](<../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart3_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md>) |
| src-000348 | FullBusinessModel!A814:F823 | 814, 815, 816, 817, 818, 819, 820, 821, 822, 823 | [src-000348 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md>) |
| src-000352 | FullBusinessModel!A817:F826 | 817, 818, 819, 820, 821, 822, 823, 824, 825, 826 | [src-000352 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md>) |
| src-000376 | FullBusinessModel!A817:F826 | 817, 818, 819, 820, 821, 822, 823, 824, 825, 826 | [src-000376 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md>) |
| src-000382 | FullBusinessModel!A814:F823 | 814, 815, 816, 817, 818, 819, 820, 821, 822, 823 | [src-000382 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | parent | C817 | SystemPartyRole | [SystemPartyRole](<bc-2ae3edd86aaf19e171cd.md>) |
| src-000006 | field-type | E818 | CashClearingSystemMember | [CashClearingSystemMember](<bc-c6027858e0d10dfbbffd.md>) |
| src-000006 | field-type | E819 | ClearingSideCode | Not a component record in this worksheet |
| src-000006 | field-type | E820 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000006 | field-type | E821 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000006 | field-type | E822 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000006 | field-type | E823 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000006 | field-type | E824 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000006 | field-type | E825 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000006 | field-type | E826 | ActiveCurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | parent | C817 | SystemPartyRole | [SystemPartyRole](<bc-2ae3edd86aaf19e171cd.md>) |
| src-000054 | field-type | E818 | CashClearingSystemMember | [CashClearingSystemMember](<bc-c6027858e0d10dfbbffd.md>) |
| src-000054 | field-type | E819 | ClearingSideCode | Not a component record in this worksheet |
| src-000054 | field-type | E820 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000054 | field-type | E821 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000054 | field-type | E822 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000054 | field-type | E823 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000054 | field-type | E824 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000054 | field-type | E825 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000054 | field-type | E826 | ActiveCurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | parent | C817 | SystemPartyRole | [SystemPartyRole](<bc-2ae3edd86aaf19e171cd.md>) |
| src-000081 | field-type | E818 | CashClearingSystemMember | [CashClearingSystemMember](<bc-c6027858e0d10dfbbffd.md>) |
| src-000081 | field-type | E819 | ClearingSideCode | Not a component record in this worksheet |
| src-000081 | field-type | E820 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000081 | field-type | E821 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000081 | field-type | E822 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000081 | field-type | E823 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000081 | field-type | E824 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000081 | field-type | E825 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000081 | field-type | E826 | ActiveCurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | parent | C817 | SystemPartyRole | [SystemPartyRole](<bc-2ae3edd86aaf19e171cd.md>) |
| src-000097 | field-type | E818 | CashClearingSystemMember | [CashClearingSystemMember](<bc-c6027858e0d10dfbbffd.md>) |
| src-000097 | field-type | E819 | ClearingSideCode | Not a component record in this worksheet |
| src-000097 | field-type | E820 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000097 | field-type | E821 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000097 | field-type | E822 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000097 | field-type | E823 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000097 | field-type | E824 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000097 | field-type | E825 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000097 | field-type | E826 | ActiveCurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | parent | C817 | SystemPartyRole | [SystemPartyRole](<bc-2ae3edd86aaf19e171cd.md>) |
| src-000164 | field-type | E818 | CashClearingSystemMember | [CashClearingSystemMember](<bc-c6027858e0d10dfbbffd.md>) |
| src-000164 | field-type | E819 | ClearingSideCode | Not a component record in this worksheet |
| src-000164 | field-type | E820 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000164 | field-type | E821 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000164 | field-type | E822 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000164 | field-type | E823 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000164 | field-type | E824 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000164 | field-type | E825 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000164 | field-type | E826 | ActiveCurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | parent | C817 | SystemPartyRole | [SystemPartyRole](<bc-2ae3edd86aaf19e171cd.md>) |
| src-000175 | field-type | E818 | CashClearingSystemMember | [CashClearingSystemMember](<bc-c6027858e0d10dfbbffd.md>) |
| src-000175 | field-type | E819 | ClearingSideCode | Not a component record in this worksheet |
| src-000175 | field-type | E820 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000175 | field-type | E821 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000175 | field-type | E822 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000175 | field-type | E823 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000175 | field-type | E824 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000175 | field-type | E825 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000175 | field-type | E826 | ActiveCurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | parent | C817 | SystemPartyRole | [SystemPartyRole](<bc-2ae3edd86aaf19e171cd.md>) |
| src-000198 | field-type | E818 | CashClearingSystemMember | [CashClearingSystemMember](<bc-c6027858e0d10dfbbffd.md>) |
| src-000198 | field-type | E819 | ClearingSideCode | Not a component record in this worksheet |
| src-000198 | field-type | E820 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000198 | field-type | E821 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000198 | field-type | E822 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000198 | field-type | E823 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000198 | field-type | E824 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000198 | field-type | E825 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000198 | field-type | E826 | ActiveCurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | parent | C814 | SystemPartyRole | [SystemPartyRole](<bc-2ae3edd86aaf19e171cd.md>) |
| src-000322 | field-type | E815 | CashClearingSystemMember | [CashClearingSystemMember](<bc-c6027858e0d10dfbbffd.md>) |
| src-000322 | field-type | E816 | ClearingSideCode | Not a component record in this worksheet |
| src-000322 | field-type | E817 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000322 | field-type | E818 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000322 | field-type | E819 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000322 | field-type | E820 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000322 | field-type | E821 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000322 | field-type | E822 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000322 | field-type | E823 | ActiveCurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | parent | C814 | SystemPartyRole | [SystemPartyRole](<bc-2ae3edd86aaf19e171cd.md>) |
| src-000348 | field-type | E815 | CashClearingSystemMember | [CashClearingSystemMember](<bc-c6027858e0d10dfbbffd.md>) |
| src-000348 | field-type | E816 | ClearingSideCode | Not a component record in this worksheet |
| src-000348 | field-type | E817 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000348 | field-type | E818 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000348 | field-type | E819 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000348 | field-type | E820 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000348 | field-type | E821 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000348 | field-type | E822 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000348 | field-type | E823 | ActiveCurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | parent | C817 | SystemPartyRole | [SystemPartyRole](<bc-2ae3edd86aaf19e171cd.md>) |
| src-000352 | field-type | E818 | CashClearingSystemMember | [CashClearingSystemMember](<bc-c6027858e0d10dfbbffd.md>) |
| src-000352 | field-type | E819 | ClearingSideCode | Not a component record in this worksheet |
| src-000352 | field-type | E820 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000352 | field-type | E821 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000352 | field-type | E822 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000352 | field-type | E823 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000352 | field-type | E824 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000352 | field-type | E825 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000352 | field-type | E826 | ActiveCurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | parent | C817 | SystemPartyRole | [SystemPartyRole](<bc-2ae3edd86aaf19e171cd.md>) |
| src-000376 | field-type | E818 | CashClearingSystemMember | [CashClearingSystemMember](<bc-c6027858e0d10dfbbffd.md>) |
| src-000376 | field-type | E819 | ClearingSideCode | Not a component record in this worksheet |
| src-000376 | field-type | E820 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000376 | field-type | E821 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000376 | field-type | E822 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000376 | field-type | E823 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000376 | field-type | E824 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000376 | field-type | E825 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000376 | field-type | E826 | ActiveCurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | parent | C814 | SystemPartyRole | [SystemPartyRole](<bc-2ae3edd86aaf19e171cd.md>) |
| src-000382 | field-type | E815 | CashClearingSystemMember | [CashClearingSystemMember](<bc-c6027858e0d10dfbbffd.md>) |
| src-000382 | field-type | E816 | ClearingSideCode | Not a component record in this worksheet |
| src-000382 | field-type | E817 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000382 | field-type | E818 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000382 | field-type | E819 | SecuritiesAccount | [SecuritiesAccount](<bc-2ec6ceb3eba4a954f1a0.md>) |
| src-000382 | field-type | E820 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000382 | field-type | E821 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000382 | field-type | E822 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000382 | field-type | E823 | ActiveCurrencyAndAmount | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
