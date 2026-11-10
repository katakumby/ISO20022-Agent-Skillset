---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-74555cc7e4d659fadfbd"
title: "DigitalPaymentSettlement"
business_component_name: "DigitalPaymentSettlement"
aliases: []
domain: "shared"
domains: ["payments", "securities"]
message_sets: ["bank-to-customer-cash-management", "ccp-clearing", "corporate-actions", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "settlement-and-reconciliation", "t2s-cash-account-query-and-report", "t2s-securities-and-penalty-reporting"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000198", "src-000352", "src-000376"]
source_editions: ["2025-2026", "august-2026", "march-2026"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A1567:F1574"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A1567:F1574"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A1567:F1574"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A1567:F1574"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A1567:F1574"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A1567:F1574"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A1567:F1574"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A1567:F1574"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A1567:F1574"]}]
content_sha256: "74555cc7e4d659fadfbdf9485f4aaa821f4185dad197e2df4763fc716ddcd4d5"
parent_names: ["Settlement"]
related_component_names: ["AnyBICDec2014Identifier", "DTI2024Identifier", "ISINOct2015Identifier", "LEIIdentifier", "Max30DecimalNumber", "SecuritiesIdentification"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# DigitalPaymentSettlement

## Definition

Specifies the information related to the digital payment settlement.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | DigitalPaymentSettlement | ∅ | Settlement | Specifies the information related to the digital payment settlement. | ∅ | ∅ |
| 2 | DigitalPaymentSettlement | FinancialInstrumentIdentification | ∅ | Financial instrument representing a sum of rights of the investor vis-a-vis the issuer. | SecuritiesIdentification | ∅ |
| 3 | DigitalPaymentSettlement | NetworkFeeQuantity | ∅ | Quantity of digital assets for network fee assigned to a transaction on a DLT network. | Max30DecimalNumber | ∅ |
| 4 | DigitalPaymentSettlement | ElectronicMoneyTokenSettlementQuantity | ∅ | Quantity of E-money token for the settlement payment. | Max30DecimalNumber | ∅ |
| 5 | DigitalPaymentSettlement | DigitalLedgerIdentification | ∅ | Place of safekeeping expressed with a Digital Ledger Identifier. It identifies a digital ledger or distributed ledger system (for example, blockchain or similar platforms). | DTI2024Identifier | ∅ |
| 6 | DigitalPaymentSettlement | ISIN | ∅ | International Securities Identification Number (ISIN). A numbering system designed by the United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-character prefix representing the country of issue, followed by the national security number (if one exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for securities in that country. | ISINOct2015Identifier | ∅ |
| 7 | DigitalPaymentSettlement | AnyBIC | ∅ | Unique and unambiguous way to identify an organisation. | AnyBICDec2014Identifier | ∅ |
| 8 | DigitalPaymentSettlement | LEI | ∅ | Legal entity identification as an alternate identification for a place of safekeeping. | LEIIdentifier | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `74555cc7e4d659fadfbdf9485f4aaa821f4185dad197e2df4763fc716ddcd4d5`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A1567:F1574 | 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574 | [src-000006 original](<../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart3_BanktoCustomerCashManagement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md>) |
| src-000054 | FullBusinessModel!A1567:F1574 | 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574 | [src-000054 original](<../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart3_CentralCounterParty_SecuritiesClearing_Maintenance_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md>) |
| src-000081 | FullBusinessModel!A1567:F1574 | 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574 | [src-000081 original](<../../../raw-input/corporate_actions/ISO20022_MDRPart3_CorporateActions_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md>) |
| src-000097 | FullBusinessModel!A1567:F1574 | 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574 | [src-000097 original](<../../../raw-input/investment_funds/ISO20022_MDRPart3_Investment-Funds_2025_2026_v2.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md>) |
| src-000164 | FullBusinessModel!A1567:F1574 | 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574 | [src-000164 original](<../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart3_PaymentsClearingandSettlement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md>) |
| src-000175 | FullBusinessModel!A1567:F1574 | 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574 | [src-000175 original](<../../../raw-input/payments_initiation/ISO20022_MDRPart3_PaymentsInitiation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md>) |
| src-000198 | FullBusinessModel!A1567:F1574 | 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574 | [src-000198 original](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart3_SettlementAndReconciliation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md>) |
| src-000352 | FullBusinessModel!A1567:F1574 | 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574 | [src-000352 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md>) |
| src-000376 | FullBusinessModel!A1567:F1574 | 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574 | [src-000376 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | parent | C1567 | Settlement | [Settlement](<bc-1ef4f3d8bd8495730563.md>) |
| src-000006 | field-type | E1568 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000006 | field-type | E1569 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000006 | field-type | E1570 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000006 | field-type | E1571 | DTI2024Identifier | Not a component record in this worksheet |
| src-000006 | field-type | E1572 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000006 | field-type | E1573 | AnyBICDec2014Identifier | Not a component record in this worksheet |
| src-000006 | field-type | E1574 | LEIIdentifier | Not a component record in this worksheet |
| src-000054 | parent | C1567 | Settlement | [Settlement](<bc-1ef4f3d8bd8495730563.md>) |
| src-000054 | field-type | E1568 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000054 | field-type | E1569 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000054 | field-type | E1570 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000054 | field-type | E1571 | DTI2024Identifier | Not a component record in this worksheet |
| src-000054 | field-type | E1572 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000054 | field-type | E1573 | AnyBICDec2014Identifier | Not a component record in this worksheet |
| src-000054 | field-type | E1574 | LEIIdentifier | Not a component record in this worksheet |
| src-000081 | parent | C1567 | Settlement | [Settlement](<bc-1ef4f3d8bd8495730563.md>) |
| src-000081 | field-type | E1568 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000081 | field-type | E1569 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000081 | field-type | E1570 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000081 | field-type | E1571 | DTI2024Identifier | Not a component record in this worksheet |
| src-000081 | field-type | E1572 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000081 | field-type | E1573 | AnyBICDec2014Identifier | Not a component record in this worksheet |
| src-000081 | field-type | E1574 | LEIIdentifier | Not a component record in this worksheet |
| src-000097 | parent | C1567 | Settlement | [Settlement](<bc-1ef4f3d8bd8495730563.md>) |
| src-000097 | field-type | E1568 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000097 | field-type | E1569 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000097 | field-type | E1570 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000097 | field-type | E1571 | DTI2024Identifier | Not a component record in this worksheet |
| src-000097 | field-type | E1572 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000097 | field-type | E1573 | AnyBICDec2014Identifier | Not a component record in this worksheet |
| src-000097 | field-type | E1574 | LEIIdentifier | Not a component record in this worksheet |
| src-000164 | parent | C1567 | Settlement | [Settlement](<bc-1ef4f3d8bd8495730563.md>) |
| src-000164 | field-type | E1568 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000164 | field-type | E1569 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000164 | field-type | E1570 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000164 | field-type | E1571 | DTI2024Identifier | Not a component record in this worksheet |
| src-000164 | field-type | E1572 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000164 | field-type | E1573 | AnyBICDec2014Identifier | Not a component record in this worksheet |
| src-000164 | field-type | E1574 | LEIIdentifier | Not a component record in this worksheet |
| src-000175 | parent | C1567 | Settlement | [Settlement](<bc-1ef4f3d8bd8495730563.md>) |
| src-000175 | field-type | E1568 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000175 | field-type | E1569 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000175 | field-type | E1570 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000175 | field-type | E1571 | DTI2024Identifier | Not a component record in this worksheet |
| src-000175 | field-type | E1572 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000175 | field-type | E1573 | AnyBICDec2014Identifier | Not a component record in this worksheet |
| src-000175 | field-type | E1574 | LEIIdentifier | Not a component record in this worksheet |
| src-000198 | parent | C1567 | Settlement | [Settlement](<bc-1ef4f3d8bd8495730563.md>) |
| src-000198 | field-type | E1568 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000198 | field-type | E1569 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000198 | field-type | E1570 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000198 | field-type | E1571 | DTI2024Identifier | Not a component record in this worksheet |
| src-000198 | field-type | E1572 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000198 | field-type | E1573 | AnyBICDec2014Identifier | Not a component record in this worksheet |
| src-000198 | field-type | E1574 | LEIIdentifier | Not a component record in this worksheet |
| src-000352 | parent | C1567 | Settlement | [Settlement](<bc-1ef4f3d8bd8495730563.md>) |
| src-000352 | field-type | E1568 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000352 | field-type | E1569 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000352 | field-type | E1570 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000352 | field-type | E1571 | DTI2024Identifier | Not a component record in this worksheet |
| src-000352 | field-type | E1572 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000352 | field-type | E1573 | AnyBICDec2014Identifier | Not a component record in this worksheet |
| src-000352 | field-type | E1574 | LEIIdentifier | Not a component record in this worksheet |
| src-000376 | parent | C1567 | Settlement | [Settlement](<bc-1ef4f3d8bd8495730563.md>) |
| src-000376 | field-type | E1568 | SecuritiesIdentification | [SecuritiesIdentification](<bc-c64cae8a077d4eaad41e.md>) |
| src-000376 | field-type | E1569 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000376 | field-type | E1570 | Max30DecimalNumber | Not a component record in this worksheet |
| src-000376 | field-type | E1571 | DTI2024Identifier | Not a component record in this worksheet |
| src-000376 | field-type | E1572 | ISINOct2015Identifier | Not a component record in this worksheet |
| src-000376 | field-type | E1573 | AnyBICDec2014Identifier | Not a component record in this worksheet |
| src-000376 | field-type | E1574 | LEIIdentifier | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
