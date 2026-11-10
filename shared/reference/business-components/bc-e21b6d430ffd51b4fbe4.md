---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-e21b6d430ffd51b4fbe4"
title: "CashAccount"
business_component_name: "CashAccount"
aliases: []
domain: "shared"
domains: ["payments", "securities"]
message_sets: ["bank-to-customer-cash-management", "ccp-clearing", "corporate-actions", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "settlement-and-reconciliation", "t2s-cash-account-query-and-report", "t2s-securities-and-penalty-reporting"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000198", "src-000352", "src-000376"]
source_editions: ["2025-2026", "august-2026", "march-2026"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A562:F591"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A562:F591"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A562:F591"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A562:F591"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A562:F591"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A562:F591"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A562:F591"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A562:F591"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A562:F591"]}]
content_sha256: "e21b6d430ffd51b4fbe484955d827075fa78323c47c93100d5ca5804586b31b9"
parent_names: ["Account"]
related_component_names: ["AccountLevelCode", "AccountLink", "AccountReportedMovement", "CashAccountContract", "CashAccountService", "CashAccountTypeCode", "CashBalance", "CashEntry", "CashSettlement", "CashSettlementInstructionPartyRole", "CashStandingOrder", "Charges", "Cheque", "CommercialTrade", "Commission", "CorporateActionElection", "CurrencyCode", "InvestmentAccount", "InvoiceFinancingPartyRole", "Payment", "PaymentCard", "PaymentPartyRole", "SecuritiesPartyRole", "StandingOrder", "Tax", "UndertakingUltimateObligor"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# CashAccount

## Definition

Account to or from which a cash entry is made.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | CashAccount | ∅ | Account | Account to or from which a cash entry is made. | ∅ | ∅ |
| 2 | CashAccount | CashAccountType | ∅ | Specifies the nature, or use, of the cash account. | CashAccountTypeCode | ∅ |
| 3 | CashAccount | RelatedInvestmentAccount | ∅ | Investment account for which a cash branch is specified. | InvestmentAccount | CashAccount |
| 4 | CashAccount | CashEntry | ∅ | Record of the cash movements into or out of a cash account. It is derived from the association between Account and Entry. | CashEntry | CashAccount |
| 5 | CashAccount | CashBalance | ∅ | Overall position representing the net debits and credits in an account at a specific point in time. It is derived from the association between Account and Balance. | CashBalance | CashAccount |
| 6 | CashAccount | PaymentPartyRole | ∅ | Specifies each role linked to a payment and using a specific cash account in the payment context.  | PaymentPartyRole | CashAccount |
| 7 | CashAccount | RelatedCreditStandingOrder | ∅ | Instruction given by an account holder to an account servicer to make regular transfers on given dates to the same beneficiary. | StandingOrder | CreditAccount |
| 8 | CashAccount | RelatedDebitStandingOrder | ∅ | Instruction given by an account holder to an account servicer to make regular transfers on given dates to the same beneficiary. | StandingOrder | DebitAccount |
| 9 | CashAccount | CashAccountContract | ∅ | Contract which manages the account. It is derived from the relation between AccountContract and Account. | CashAccountContract | CashAccount |
| 10 | CashAccount | RelatedCorporateActionElection | ∅ | Election process which uses specific cash accounts. | CorporateActionElection | CashAccount |
| 11 | CashAccount | Charges | ∅ | Specifies the charges which are debited from the account. | Charges | ChargesDebitAccount |
| 12 | CashAccount | Tax | ∅ | Tax charged on a cash account. | Tax | TaxAccount |
| 13 | CashAccount | RelatedSettlementInstruction | ∅ | Settlement process which uses specific cash accounts. | CashSettlement | SettlementAccount |
| 14 | CashAccount | CashSettlementPartyRole | ∅ | Specifies each role linked to a payment settlement and using a specific cash account in the payment context.  | CashSettlementInstructionPartyRole | CashAccount |
| 15 | CashAccount | UltimateObligor | ∅ | Party for which different types of cash accounts are specified. | UndertakingUltimateObligor | CashAccount |
| 16 | CashAccount | RelatedPaymentCard | ∅ | Payment card for which an account is specified. | PaymentCard | RelatedAccount |
| 17 | CashAccount | SecuritiesPartyRole | ∅ | Specifies the role which uses a cash account. | SecuritiesPartyRole | CashAccount |
| 18 | CashAccount | RelatedInvoiceFinancingPartyRole | ∅ | Specifies each role using a specific account in the context of invoice financing. | InvoiceFinancingPartyRole | CashAccount |
| 19 | CashAccount | RelatedCommercialTrade | ∅ | Commercial trade for which a purchase account is specified. | CommercialTrade | PurchaseAccount |
| 20 | CashAccount | Level | ∅ | Defines the level of an account within the account hierarchy. | AccountLevelCode | ∅ |
| 21 | CashAccount | SettlementCurrency | ∅ | Specifies the currency used for settlement, if different from the account currency. | CurrencyCode | ∅ |
| 22 | CashAccount | ReportedMovements | ∅ | Provides statistical information on the number of movements and their value for a particular account. | AccountReportedMovement | ReportedCashAccount |
| 23 | CashAccount | ClosedAccountContract | ∅ | Contract which specifies the cash account to/from which the balance of a closed account must be transferred. | CashAccountContract | TransferCashAccount |
| 24 | CashAccount | AccountLink | ∅ | Defines the link between a cash account and a securities account. | AccountLink | CashAccount |
| 25 | CashAccount | CashStandingOrder | ∅ | Standing order which applies on a specific account. | CashStandingOrder | CashAccount |
| 26 | CashAccount | Cheque | ∅ | Cheques drawn on a cash account. | Cheque | CashAccount |
| 27 | CashAccount | CashAccountService | ∅ | Services linked to the cash account and specified in the cash account contract. It is derived from the association between Account and AccountService. | CashAccountService | CashAccount |
| 28 | CashAccount | Payment | ∅ | Payment for which an account is specified. | Payment | Account |
| 29 | CashAccount | Commission | ∅ | Amount of money due to a party as compensation for a service. | Commission | Account |
| 30 | CashAccount | RelatedAccountVerification | ∅ | Information related to the verification of an account validity. | ∅ | CashAccountRelatedAccountVerification |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `e21b6d430ffd51b4fbe484955d827075fa78323c47c93100d5ca5804586b31b9`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A562:F591 | 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591 | [src-000006 original](<../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart3_BanktoCustomerCashManagement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md>) |
| src-000054 | FullBusinessModel!A562:F591 | 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591 | [src-000054 original](<../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart3_CentralCounterParty_SecuritiesClearing_Maintenance_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md>) |
| src-000081 | FullBusinessModel!A562:F591 | 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591 | [src-000081 original](<../../../raw-input/corporate_actions/ISO20022_MDRPart3_CorporateActions_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md>) |
| src-000097 | FullBusinessModel!A562:F591 | 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591 | [src-000097 original](<../../../raw-input/investment_funds/ISO20022_MDRPart3_Investment-Funds_2025_2026_v2.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md>) |
| src-000164 | FullBusinessModel!A562:F591 | 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591 | [src-000164 original](<../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart3_PaymentsClearingandSettlement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md>) |
| src-000175 | FullBusinessModel!A562:F591 | 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591 | [src-000175 original](<../../../raw-input/payments_initiation/ISO20022_MDRPart3_PaymentsInitiation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md>) |
| src-000198 | FullBusinessModel!A562:F591 | 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591 | [src-000198 original](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart3_SettlementAndReconciliation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md>) |
| src-000352 | FullBusinessModel!A562:F591 | 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591 | [src-000352 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md>) |
| src-000376 | FullBusinessModel!A562:F591 | 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591 | [src-000376 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | parent | C562 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000006 | field-type | E563 | CashAccountTypeCode | Not a component record in this worksheet |
| src-000006 | field-type | E564 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000006 | field-type | E565 | CashEntry | [CashEntry](<bc-a8cf407e691b4bb8d6b9.md>) |
| src-000006 | field-type | E566 | CashBalance | [CashBalance](<bc-1cc6c7bc3a6912fe9e11.md>) |
| src-000006 | field-type | E567 | PaymentPartyRole | [PaymentPartyRole](<bc-33076d1b4c725e29a920.md>) |
| src-000006 | field-type | E568 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000006 | field-type | E569 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000006 | field-type | E570 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000006 | field-type | E571 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000006 | field-type | E572 | Charges | [Charges](<bc-813965e3665c8b53be80.md>) |
| src-000006 | field-type | E573 | Tax | [Tax](<bc-b7e53c3a57e16730ee76.md>) |
| src-000006 | field-type | E574 | CashSettlement | [CashSettlement](<bc-7dd45f7ba002a592b2ff.md>) |
| src-000006 | field-type | E575 | CashSettlementInstructionPartyRole | [CashSettlementInstructionPartyRole](<bc-e2e020dbd1c46b8d10e9.md>) |
| src-000006 | field-type | E576 | UndertakingUltimateObligor | [UndertakingUltimateObligor](<bc-fd28e8f6a7a8a9377f3a.md>) |
| src-000006 | field-type | E577 | PaymentCard | [PaymentCard](<bc-5f22314057051750976e.md>) |
| src-000006 | field-type | E578 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000006 | field-type | E579 | InvoiceFinancingPartyRole | [InvoiceFinancingPartyRole](<bc-18641559c13bb0bb716c.md>) |
| src-000006 | field-type | E580 | CommercialTrade | [CommercialTrade](<bc-e2fa25cc2885e32f71d4.md>) |
| src-000006 | field-type | E581 | AccountLevelCode | Not a component record in this worksheet |
| src-000006 | field-type | E582 | CurrencyCode | Not a component record in this worksheet |
| src-000006 | field-type | E583 | AccountReportedMovement | [AccountReportedMovement](<bc-0a317c4f726ccb09f1fe.md>) |
| src-000006 | field-type | E584 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000006 | field-type | E585 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000006 | field-type | E586 | CashStandingOrder | [CashStandingOrder](<bc-7f85b916d0f1f84c3489.md>) |
| src-000006 | field-type | E587 | Cheque | [Cheque](<bc-5e807a141ab7d821e99a.md>) |
| src-000006 | field-type | E588 | CashAccountService | [CashAccountService](<bc-3a5ad9cdde28e2bf11c9.md>) |
| src-000006 | field-type | E589 | Payment | [Payment](<bc-d4f6ac96433338200303.md>) |
| src-000006 | field-type | E590 | Commission | [Commission](<bc-c2689a011979809dfda8.md>) |
| src-000054 | parent | C562 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000054 | field-type | E563 | CashAccountTypeCode | Not a component record in this worksheet |
| src-000054 | field-type | E564 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000054 | field-type | E565 | CashEntry | [CashEntry](<bc-a8cf407e691b4bb8d6b9.md>) |
| src-000054 | field-type | E566 | CashBalance | [CashBalance](<bc-1cc6c7bc3a6912fe9e11.md>) |
| src-000054 | field-type | E567 | PaymentPartyRole | [PaymentPartyRole](<bc-33076d1b4c725e29a920.md>) |
| src-000054 | field-type | E568 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000054 | field-type | E569 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000054 | field-type | E570 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000054 | field-type | E571 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000054 | field-type | E572 | Charges | [Charges](<bc-813965e3665c8b53be80.md>) |
| src-000054 | field-type | E573 | Tax | [Tax](<bc-b7e53c3a57e16730ee76.md>) |
| src-000054 | field-type | E574 | CashSettlement | [CashSettlement](<bc-7dd45f7ba002a592b2ff.md>) |
| src-000054 | field-type | E575 | CashSettlementInstructionPartyRole | [CashSettlementInstructionPartyRole](<bc-e2e020dbd1c46b8d10e9.md>) |
| src-000054 | field-type | E576 | UndertakingUltimateObligor | [UndertakingUltimateObligor](<bc-fd28e8f6a7a8a9377f3a.md>) |
| src-000054 | field-type | E577 | PaymentCard | [PaymentCard](<bc-5f22314057051750976e.md>) |
| src-000054 | field-type | E578 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000054 | field-type | E579 | InvoiceFinancingPartyRole | [InvoiceFinancingPartyRole](<bc-18641559c13bb0bb716c.md>) |
| src-000054 | field-type | E580 | CommercialTrade | [CommercialTrade](<bc-e2fa25cc2885e32f71d4.md>) |
| src-000054 | field-type | E581 | AccountLevelCode | Not a component record in this worksheet |
| src-000054 | field-type | E582 | CurrencyCode | Not a component record in this worksheet |
| src-000054 | field-type | E583 | AccountReportedMovement | [AccountReportedMovement](<bc-0a317c4f726ccb09f1fe.md>) |
| src-000054 | field-type | E584 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000054 | field-type | E585 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000054 | field-type | E586 | CashStandingOrder | [CashStandingOrder](<bc-7f85b916d0f1f84c3489.md>) |
| src-000054 | field-type | E587 | Cheque | [Cheque](<bc-5e807a141ab7d821e99a.md>) |
| src-000054 | field-type | E588 | CashAccountService | [CashAccountService](<bc-3a5ad9cdde28e2bf11c9.md>) |
| src-000054 | field-type | E589 | Payment | [Payment](<bc-d4f6ac96433338200303.md>) |
| src-000054 | field-type | E590 | Commission | [Commission](<bc-c2689a011979809dfda8.md>) |
| src-000081 | parent | C562 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000081 | field-type | E563 | CashAccountTypeCode | Not a component record in this worksheet |
| src-000081 | field-type | E564 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000081 | field-type | E565 | CashEntry | [CashEntry](<bc-a8cf407e691b4bb8d6b9.md>) |
| src-000081 | field-type | E566 | CashBalance | [CashBalance](<bc-1cc6c7bc3a6912fe9e11.md>) |
| src-000081 | field-type | E567 | PaymentPartyRole | [PaymentPartyRole](<bc-33076d1b4c725e29a920.md>) |
| src-000081 | field-type | E568 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000081 | field-type | E569 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000081 | field-type | E570 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000081 | field-type | E571 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000081 | field-type | E572 | Charges | [Charges](<bc-813965e3665c8b53be80.md>) |
| src-000081 | field-type | E573 | Tax | [Tax](<bc-b7e53c3a57e16730ee76.md>) |
| src-000081 | field-type | E574 | CashSettlement | [CashSettlement](<bc-7dd45f7ba002a592b2ff.md>) |
| src-000081 | field-type | E575 | CashSettlementInstructionPartyRole | [CashSettlementInstructionPartyRole](<bc-e2e020dbd1c46b8d10e9.md>) |
| src-000081 | field-type | E576 | UndertakingUltimateObligor | [UndertakingUltimateObligor](<bc-fd28e8f6a7a8a9377f3a.md>) |
| src-000081 | field-type | E577 | PaymentCard | [PaymentCard](<bc-5f22314057051750976e.md>) |
| src-000081 | field-type | E578 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000081 | field-type | E579 | InvoiceFinancingPartyRole | [InvoiceFinancingPartyRole](<bc-18641559c13bb0bb716c.md>) |
| src-000081 | field-type | E580 | CommercialTrade | [CommercialTrade](<bc-e2fa25cc2885e32f71d4.md>) |
| src-000081 | field-type | E581 | AccountLevelCode | Not a component record in this worksheet |
| src-000081 | field-type | E582 | CurrencyCode | Not a component record in this worksheet |
| src-000081 | field-type | E583 | AccountReportedMovement | [AccountReportedMovement](<bc-0a317c4f726ccb09f1fe.md>) |
| src-000081 | field-type | E584 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000081 | field-type | E585 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000081 | field-type | E586 | CashStandingOrder | [CashStandingOrder](<bc-7f85b916d0f1f84c3489.md>) |
| src-000081 | field-type | E587 | Cheque | [Cheque](<bc-5e807a141ab7d821e99a.md>) |
| src-000081 | field-type | E588 | CashAccountService | [CashAccountService](<bc-3a5ad9cdde28e2bf11c9.md>) |
| src-000081 | field-type | E589 | Payment | [Payment](<bc-d4f6ac96433338200303.md>) |
| src-000081 | field-type | E590 | Commission | [Commission](<bc-c2689a011979809dfda8.md>) |
| src-000097 | parent | C562 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000097 | field-type | E563 | CashAccountTypeCode | Not a component record in this worksheet |
| src-000097 | field-type | E564 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000097 | field-type | E565 | CashEntry | [CashEntry](<bc-a8cf407e691b4bb8d6b9.md>) |
| src-000097 | field-type | E566 | CashBalance | [CashBalance](<bc-1cc6c7bc3a6912fe9e11.md>) |
| src-000097 | field-type | E567 | PaymentPartyRole | [PaymentPartyRole](<bc-33076d1b4c725e29a920.md>) |
| src-000097 | field-type | E568 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000097 | field-type | E569 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000097 | field-type | E570 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000097 | field-type | E571 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000097 | field-type | E572 | Charges | [Charges](<bc-813965e3665c8b53be80.md>) |
| src-000097 | field-type | E573 | Tax | [Tax](<bc-b7e53c3a57e16730ee76.md>) |
| src-000097 | field-type | E574 | CashSettlement | [CashSettlement](<bc-7dd45f7ba002a592b2ff.md>) |
| src-000097 | field-type | E575 | CashSettlementInstructionPartyRole | [CashSettlementInstructionPartyRole](<bc-e2e020dbd1c46b8d10e9.md>) |
| src-000097 | field-type | E576 | UndertakingUltimateObligor | [UndertakingUltimateObligor](<bc-fd28e8f6a7a8a9377f3a.md>) |
| src-000097 | field-type | E577 | PaymentCard | [PaymentCard](<bc-5f22314057051750976e.md>) |
| src-000097 | field-type | E578 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000097 | field-type | E579 | InvoiceFinancingPartyRole | [InvoiceFinancingPartyRole](<bc-18641559c13bb0bb716c.md>) |
| src-000097 | field-type | E580 | CommercialTrade | [CommercialTrade](<bc-e2fa25cc2885e32f71d4.md>) |
| src-000097 | field-type | E581 | AccountLevelCode | Not a component record in this worksheet |
| src-000097 | field-type | E582 | CurrencyCode | Not a component record in this worksheet |
| src-000097 | field-type | E583 | AccountReportedMovement | [AccountReportedMovement](<bc-0a317c4f726ccb09f1fe.md>) |
| src-000097 | field-type | E584 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000097 | field-type | E585 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000097 | field-type | E586 | CashStandingOrder | [CashStandingOrder](<bc-7f85b916d0f1f84c3489.md>) |
| src-000097 | field-type | E587 | Cheque | [Cheque](<bc-5e807a141ab7d821e99a.md>) |
| src-000097 | field-type | E588 | CashAccountService | [CashAccountService](<bc-3a5ad9cdde28e2bf11c9.md>) |
| src-000097 | field-type | E589 | Payment | [Payment](<bc-d4f6ac96433338200303.md>) |
| src-000097 | field-type | E590 | Commission | [Commission](<bc-c2689a011979809dfda8.md>) |
| src-000164 | parent | C562 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000164 | field-type | E563 | CashAccountTypeCode | Not a component record in this worksheet |
| src-000164 | field-type | E564 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000164 | field-type | E565 | CashEntry | [CashEntry](<bc-a8cf407e691b4bb8d6b9.md>) |
| src-000164 | field-type | E566 | CashBalance | [CashBalance](<bc-1cc6c7bc3a6912fe9e11.md>) |
| src-000164 | field-type | E567 | PaymentPartyRole | [PaymentPartyRole](<bc-33076d1b4c725e29a920.md>) |
| src-000164 | field-type | E568 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000164 | field-type | E569 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000164 | field-type | E570 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000164 | field-type | E571 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000164 | field-type | E572 | Charges | [Charges](<bc-813965e3665c8b53be80.md>) |
| src-000164 | field-type | E573 | Tax | [Tax](<bc-b7e53c3a57e16730ee76.md>) |
| src-000164 | field-type | E574 | CashSettlement | [CashSettlement](<bc-7dd45f7ba002a592b2ff.md>) |
| src-000164 | field-type | E575 | CashSettlementInstructionPartyRole | [CashSettlementInstructionPartyRole](<bc-e2e020dbd1c46b8d10e9.md>) |
| src-000164 | field-type | E576 | UndertakingUltimateObligor | [UndertakingUltimateObligor](<bc-fd28e8f6a7a8a9377f3a.md>) |
| src-000164 | field-type | E577 | PaymentCard | [PaymentCard](<bc-5f22314057051750976e.md>) |
| src-000164 | field-type | E578 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000164 | field-type | E579 | InvoiceFinancingPartyRole | [InvoiceFinancingPartyRole](<bc-18641559c13bb0bb716c.md>) |
| src-000164 | field-type | E580 | CommercialTrade | [CommercialTrade](<bc-e2fa25cc2885e32f71d4.md>) |
| src-000164 | field-type | E581 | AccountLevelCode | Not a component record in this worksheet |
| src-000164 | field-type | E582 | CurrencyCode | Not a component record in this worksheet |
| src-000164 | field-type | E583 | AccountReportedMovement | [AccountReportedMovement](<bc-0a317c4f726ccb09f1fe.md>) |
| src-000164 | field-type | E584 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000164 | field-type | E585 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000164 | field-type | E586 | CashStandingOrder | [CashStandingOrder](<bc-7f85b916d0f1f84c3489.md>) |
| src-000164 | field-type | E587 | Cheque | [Cheque](<bc-5e807a141ab7d821e99a.md>) |
| src-000164 | field-type | E588 | CashAccountService | [CashAccountService](<bc-3a5ad9cdde28e2bf11c9.md>) |
| src-000164 | field-type | E589 | Payment | [Payment](<bc-d4f6ac96433338200303.md>) |
| src-000164 | field-type | E590 | Commission | [Commission](<bc-c2689a011979809dfda8.md>) |
| src-000175 | parent | C562 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000175 | field-type | E563 | CashAccountTypeCode | Not a component record in this worksheet |
| src-000175 | field-type | E564 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000175 | field-type | E565 | CashEntry | [CashEntry](<bc-a8cf407e691b4bb8d6b9.md>) |
| src-000175 | field-type | E566 | CashBalance | [CashBalance](<bc-1cc6c7bc3a6912fe9e11.md>) |
| src-000175 | field-type | E567 | PaymentPartyRole | [PaymentPartyRole](<bc-33076d1b4c725e29a920.md>) |
| src-000175 | field-type | E568 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000175 | field-type | E569 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000175 | field-type | E570 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000175 | field-type | E571 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000175 | field-type | E572 | Charges | [Charges](<bc-813965e3665c8b53be80.md>) |
| src-000175 | field-type | E573 | Tax | [Tax](<bc-b7e53c3a57e16730ee76.md>) |
| src-000175 | field-type | E574 | CashSettlement | [CashSettlement](<bc-7dd45f7ba002a592b2ff.md>) |
| src-000175 | field-type | E575 | CashSettlementInstructionPartyRole | [CashSettlementInstructionPartyRole](<bc-e2e020dbd1c46b8d10e9.md>) |
| src-000175 | field-type | E576 | UndertakingUltimateObligor | [UndertakingUltimateObligor](<bc-fd28e8f6a7a8a9377f3a.md>) |
| src-000175 | field-type | E577 | PaymentCard | [PaymentCard](<bc-5f22314057051750976e.md>) |
| src-000175 | field-type | E578 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000175 | field-type | E579 | InvoiceFinancingPartyRole | [InvoiceFinancingPartyRole](<bc-18641559c13bb0bb716c.md>) |
| src-000175 | field-type | E580 | CommercialTrade | [CommercialTrade](<bc-e2fa25cc2885e32f71d4.md>) |
| src-000175 | field-type | E581 | AccountLevelCode | Not a component record in this worksheet |
| src-000175 | field-type | E582 | CurrencyCode | Not a component record in this worksheet |
| src-000175 | field-type | E583 | AccountReportedMovement | [AccountReportedMovement](<bc-0a317c4f726ccb09f1fe.md>) |
| src-000175 | field-type | E584 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000175 | field-type | E585 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000175 | field-type | E586 | CashStandingOrder | [CashStandingOrder](<bc-7f85b916d0f1f84c3489.md>) |
| src-000175 | field-type | E587 | Cheque | [Cheque](<bc-5e807a141ab7d821e99a.md>) |
| src-000175 | field-type | E588 | CashAccountService | [CashAccountService](<bc-3a5ad9cdde28e2bf11c9.md>) |
| src-000175 | field-type | E589 | Payment | [Payment](<bc-d4f6ac96433338200303.md>) |
| src-000175 | field-type | E590 | Commission | [Commission](<bc-c2689a011979809dfda8.md>) |
| src-000198 | parent | C562 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000198 | field-type | E563 | CashAccountTypeCode | Not a component record in this worksheet |
| src-000198 | field-type | E564 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000198 | field-type | E565 | CashEntry | [CashEntry](<bc-a8cf407e691b4bb8d6b9.md>) |
| src-000198 | field-type | E566 | CashBalance | [CashBalance](<bc-1cc6c7bc3a6912fe9e11.md>) |
| src-000198 | field-type | E567 | PaymentPartyRole | [PaymentPartyRole](<bc-33076d1b4c725e29a920.md>) |
| src-000198 | field-type | E568 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000198 | field-type | E569 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000198 | field-type | E570 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000198 | field-type | E571 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000198 | field-type | E572 | Charges | [Charges](<bc-813965e3665c8b53be80.md>) |
| src-000198 | field-type | E573 | Tax | [Tax](<bc-b7e53c3a57e16730ee76.md>) |
| src-000198 | field-type | E574 | CashSettlement | [CashSettlement](<bc-7dd45f7ba002a592b2ff.md>) |
| src-000198 | field-type | E575 | CashSettlementInstructionPartyRole | [CashSettlementInstructionPartyRole](<bc-e2e020dbd1c46b8d10e9.md>) |
| src-000198 | field-type | E576 | UndertakingUltimateObligor | [UndertakingUltimateObligor](<bc-fd28e8f6a7a8a9377f3a.md>) |
| src-000198 | field-type | E577 | PaymentCard | [PaymentCard](<bc-5f22314057051750976e.md>) |
| src-000198 | field-type | E578 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000198 | field-type | E579 | InvoiceFinancingPartyRole | [InvoiceFinancingPartyRole](<bc-18641559c13bb0bb716c.md>) |
| src-000198 | field-type | E580 | CommercialTrade | [CommercialTrade](<bc-e2fa25cc2885e32f71d4.md>) |
| src-000198 | field-type | E581 | AccountLevelCode | Not a component record in this worksheet |
| src-000198 | field-type | E582 | CurrencyCode | Not a component record in this worksheet |
| src-000198 | field-type | E583 | AccountReportedMovement | [AccountReportedMovement](<bc-0a317c4f726ccb09f1fe.md>) |
| src-000198 | field-type | E584 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000198 | field-type | E585 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000198 | field-type | E586 | CashStandingOrder | [CashStandingOrder](<bc-7f85b916d0f1f84c3489.md>) |
| src-000198 | field-type | E587 | Cheque | [Cheque](<bc-5e807a141ab7d821e99a.md>) |
| src-000198 | field-type | E588 | CashAccountService | [CashAccountService](<bc-3a5ad9cdde28e2bf11c9.md>) |
| src-000198 | field-type | E589 | Payment | [Payment](<bc-d4f6ac96433338200303.md>) |
| src-000198 | field-type | E590 | Commission | [Commission](<bc-c2689a011979809dfda8.md>) |
| src-000352 | parent | C562 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000352 | field-type | E563 | CashAccountTypeCode | Not a component record in this worksheet |
| src-000352 | field-type | E564 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000352 | field-type | E565 | CashEntry | [CashEntry](<bc-a8cf407e691b4bb8d6b9.md>) |
| src-000352 | field-type | E566 | CashBalance | [CashBalance](<bc-1cc6c7bc3a6912fe9e11.md>) |
| src-000352 | field-type | E567 | PaymentPartyRole | [PaymentPartyRole](<bc-33076d1b4c725e29a920.md>) |
| src-000352 | field-type | E568 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000352 | field-type | E569 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000352 | field-type | E570 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000352 | field-type | E571 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000352 | field-type | E572 | Charges | [Charges](<bc-813965e3665c8b53be80.md>) |
| src-000352 | field-type | E573 | Tax | [Tax](<bc-b7e53c3a57e16730ee76.md>) |
| src-000352 | field-type | E574 | CashSettlement | [CashSettlement](<bc-7dd45f7ba002a592b2ff.md>) |
| src-000352 | field-type | E575 | CashSettlementInstructionPartyRole | [CashSettlementInstructionPartyRole](<bc-e2e020dbd1c46b8d10e9.md>) |
| src-000352 | field-type | E576 | UndertakingUltimateObligor | [UndertakingUltimateObligor](<bc-fd28e8f6a7a8a9377f3a.md>) |
| src-000352 | field-type | E577 | PaymentCard | [PaymentCard](<bc-5f22314057051750976e.md>) |
| src-000352 | field-type | E578 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000352 | field-type | E579 | InvoiceFinancingPartyRole | [InvoiceFinancingPartyRole](<bc-18641559c13bb0bb716c.md>) |
| src-000352 | field-type | E580 | CommercialTrade | [CommercialTrade](<bc-e2fa25cc2885e32f71d4.md>) |
| src-000352 | field-type | E581 | AccountLevelCode | Not a component record in this worksheet |
| src-000352 | field-type | E582 | CurrencyCode | Not a component record in this worksheet |
| src-000352 | field-type | E583 | AccountReportedMovement | [AccountReportedMovement](<bc-0a317c4f726ccb09f1fe.md>) |
| src-000352 | field-type | E584 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000352 | field-type | E585 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000352 | field-type | E586 | CashStandingOrder | [CashStandingOrder](<bc-7f85b916d0f1f84c3489.md>) |
| src-000352 | field-type | E587 | Cheque | [Cheque](<bc-5e807a141ab7d821e99a.md>) |
| src-000352 | field-type | E588 | CashAccountService | [CashAccountService](<bc-3a5ad9cdde28e2bf11c9.md>) |
| src-000352 | field-type | E589 | Payment | [Payment](<bc-d4f6ac96433338200303.md>) |
| src-000352 | field-type | E590 | Commission | [Commission](<bc-c2689a011979809dfda8.md>) |
| src-000376 | parent | C562 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000376 | field-type | E563 | CashAccountTypeCode | Not a component record in this worksheet |
| src-000376 | field-type | E564 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000376 | field-type | E565 | CashEntry | [CashEntry](<bc-a8cf407e691b4bb8d6b9.md>) |
| src-000376 | field-type | E566 | CashBalance | [CashBalance](<bc-1cc6c7bc3a6912fe9e11.md>) |
| src-000376 | field-type | E567 | PaymentPartyRole | [PaymentPartyRole](<bc-33076d1b4c725e29a920.md>) |
| src-000376 | field-type | E568 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000376 | field-type | E569 | StandingOrder | [StandingOrder](<bc-ad73b75eee324788080c.md>) |
| src-000376 | field-type | E570 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000376 | field-type | E571 | CorporateActionElection | [CorporateActionElection](<bc-214db61e201fbc40644b.md>) |
| src-000376 | field-type | E572 | Charges | [Charges](<bc-813965e3665c8b53be80.md>) |
| src-000376 | field-type | E573 | Tax | [Tax](<bc-b7e53c3a57e16730ee76.md>) |
| src-000376 | field-type | E574 | CashSettlement | [CashSettlement](<bc-7dd45f7ba002a592b2ff.md>) |
| src-000376 | field-type | E575 | CashSettlementInstructionPartyRole | [CashSettlementInstructionPartyRole](<bc-e2e020dbd1c46b8d10e9.md>) |
| src-000376 | field-type | E576 | UndertakingUltimateObligor | [UndertakingUltimateObligor](<bc-fd28e8f6a7a8a9377f3a.md>) |
| src-000376 | field-type | E577 | PaymentCard | [PaymentCard](<bc-5f22314057051750976e.md>) |
| src-000376 | field-type | E578 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000376 | field-type | E579 | InvoiceFinancingPartyRole | [InvoiceFinancingPartyRole](<bc-18641559c13bb0bb716c.md>) |
| src-000376 | field-type | E580 | CommercialTrade | [CommercialTrade](<bc-e2fa25cc2885e32f71d4.md>) |
| src-000376 | field-type | E581 | AccountLevelCode | Not a component record in this worksheet |
| src-000376 | field-type | E582 | CurrencyCode | Not a component record in this worksheet |
| src-000376 | field-type | E583 | AccountReportedMovement | [AccountReportedMovement](<bc-0a317c4f726ccb09f1fe.md>) |
| src-000376 | field-type | E584 | CashAccountContract | [CashAccountContract](<bc-6085a708e86cb7bb5db9.md>) |
| src-000376 | field-type | E585 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000376 | field-type | E586 | CashStandingOrder | [CashStandingOrder](<bc-7f85b916d0f1f84c3489.md>) |
| src-000376 | field-type | E587 | Cheque | [Cheque](<bc-5e807a141ab7d821e99a.md>) |
| src-000376 | field-type | E588 | CashAccountService | [CashAccountService](<bc-3a5ad9cdde28e2bf11c9.md>) |
| src-000376 | field-type | E589 | Payment | [Payment](<bc-d4f6ac96433338200303.md>) |
| src-000376 | field-type | E590 | Commission | [Commission](<bc-c2689a011979809dfda8.md>) |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
