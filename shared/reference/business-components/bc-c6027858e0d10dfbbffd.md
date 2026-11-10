---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-c6027858e0d10dfbbffd"
title: "CashClearingSystemMember"
business_component_name: "CashClearingSystemMember"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A634:F657"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A619:F642"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A634:F657"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A634:F657"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A634:F657"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A634:F657"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A634:F657"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A619:F642"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A634:F657"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A631:F654"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A1288:F1311"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A631:F654"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A634:F657"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A619:F642"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A1288:F1311"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A1288:F1311"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A619:F642"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A619:F642"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A1288:F1311"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A1288:F1311"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A634:F657"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A1288:F1311"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A631:F654"]}]
content_sha256: "c6027858e0d10dfbbffd66bb63b01a022a9869264968452d7a44d5072fa7f26f"
parent_names: []
related_component_names: ["AustralianBSBIdentification", "AustrianBankleitzahlIdentifier", "CHIPSParticipantIdentifier", "CHIPSUniversalIdentifier", "CanadianPaymentsARNIdentifier", "ClearingMemberRole", "FedwireRoutingNumberIdentifier", "GermanBankleitzahlIdentifier", "HellenicBankIdentificationCodeIdentifier", "HongKongBankIdentifier", "IndianFinancialSystemCodeIdentifier", "IrishNSCIdentifier", "ItalianDomesticIdentifier", "NewZealandNCCIdentifier", "OrganisationIdentification", "PolishNationalClearingCodeIdentifier", "PortugueseNCCIdentifier", "RussianCentralBankIdentificationCodeIdentifier", "SouthAfricanNCCIdentifier", "SpanishDomesticInterbankingIdentifier", "SwissBCIdentifier", "SwissSICIdentifier", "UKDomesticSortCodeIdentifier"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# CashClearingSystemMember

## Definition

Unique and unambiguous identifier for a clearing system member, as assigned by the clearing system. In some clearing systems, the accounts of the clearing system members are also assigned an identifier. The identifier can be used when transmitting, reconciling and confirming payment orders or security transfer instructions prior to settlement, and may include the netting of instructions and the establishment of final positions for settlement.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | CashClearingSystemMember | ∅ | ∅ | Unique and unambiguous identifier for a clearing system member, as assigned by the clearing system. In some clearing systems, the accounts of the clearing system members are also assigned an identifier. The identifier can be used when transmitting, reconciling and confirming payment orders or security transfer instructions prior to settlement, and may include the netting of instructions and the establishment of final positions for settlement. | ∅ | ∅ |
| 2 | CashClearingSystemMember | OrganisationIdentification | ∅ | Identification parameters which include clearing system member identification. | OrganisationIdentification | ClearingSystemMemberIdentificationType |
| 3 | CashClearingSystemMember | CHIPSUniversalIdentification | ∅ | (United States) Clearing House Interbank Payments System (CHIPS) Universal Identification (UID) - identifies entities that own accounts at CHIPS participating financial institutions, through which CHIPS payments are effected. The CHIPS UID is assigned by the New York Clearing House. | CHIPSUniversalIdentifier | ∅ |
| 4 | CashClearingSystemMember | NewZealandNCC | ∅ | New Zealand Bank/Branch Code - identifies New Zealand institutions on the New Zealand national clearing system. The code is assigned by the New Zealand Bankers' Association (NZBA). | NewZealandNCCIdentifier | ∅ |
| 5 | CashClearingSystemMember | IrishNSC | ∅ | Irish National Sorting Code - identifies Irish financial institutions on the Irish national clearing system. The code is assigned by the Irish Payments Services Organisation (IPSO). | IrishNSCIdentifier | ∅ |
| 6 | CashClearingSystemMember | UKSortCode | ∅ | United Kingdom (UK) Sort Code - identifies British financial institutions on the British national clearing systems. The sort code is assigned by the Association for Payments and Clearing Services (APACS). | UKDomesticSortCodeIdentifier | ∅ |
| 7 | CashClearingSystemMember | CHIPSParticipantIdentification | ∅ | (United States) Clearing House Interbank Payment System (CHIPS) Participant Identifier (ID) - identifies financial institutions participating on CHIPS. The CHIPS Participant ID is assigned by the New York Clearing House. | CHIPSParticipantIdentifier | ∅ |
| 8 | CashClearingSystemMember | SwissBC | ∅ | Swiss Bank Code - identifies Swiss institutions on the Swiss national clearing system. | SwissBCIdentifier | ∅ |
| 9 | CashClearingSystemMember | FedwireRoutingNumber | ∅ | Fed wire Routing Number - identifies financial institutions, in the US, on the Fed wire system. The routing number is assigned by the American Bankers Association (ABA). | FedwireRoutingNumberIdentifier | ∅ |
| 10 | CashClearingSystemMember | PortugueseNCC | ∅ | Portuguese National Clearing Code - identifies Portuguese financial institutions on the Portuguese national clearing system. | PortugueseNCCIdentifier | ∅ |
| 11 | CashClearingSystemMember | RussianCentralBankIdentificationCode | ∅ | Russian Central Bank Identification Code - identifies Russian financial institutions on the Russian national clearing system. | RussianCentralBankIdentificationCodeIdentifier | ∅ |
| 12 | CashClearingSystemMember | ItalianDomesticIdentificationCode | ∅ | Italian Domestic Identification Code - identifies Italian financial institutions on the Italian national clearing system. The code is assigned by the Associazione Bancaria Italiana (ABI). | ItalianDomesticIdentifier | ∅ |
| 13 | CashClearingSystemMember | AustrianBankleitzahl | ∅ | Austrian Bankleitzahl - identifies Austrian financial institutions on the Austrian national clearing system. | AustrianBankleitzahlIdentifier | ∅ |
| 14 | CashClearingSystemMember | CanadianPaymentsAssociationRoutingNumber | ∅ | Canadian Payments Association Routing Number - identifies Canadian financial institutions on the Canadian national clearing system. | CanadianPaymentsARNIdentifier | ∅ |
| 15 | CashClearingSystemMember | SwissSIC | ∅ | Swiss Interbank Clearing (SIC) Code - identifies Swiss financial institutions domestically, on the Swiss national clearing system. | SwissSICIdentifier | ∅ |
| 16 | CashClearingSystemMember | GermanBankleitzahl | ∅ | German Bankleitzahl - identifies German financial institutions on the German national clearing systems. | GermanBankleitzahlIdentifier | ∅ |
| 17 | CashClearingSystemMember | SpanishDomesticInterbankingCode | ∅ | Spanish Domestic Interbanking Code - identifies Spanish financial institutions on the Spanish national clearing system. The code is assigned by the Centro de Cooperacion Interbancaria (CCI). | SpanishDomesticInterbankingIdentifier | ∅ |
| 18 | CashClearingSystemMember | SouthAfricanNCC | ∅ | South African National Clearing Code (NCC) - identifies South African financial institutions on the South African national clearing system. The code is assigned by the South African Bankers Services Company Ltd. (BankServ). | SouthAfricanNCCIdentifier | ∅ |
| 19 | CashClearingSystemMember | HongKongBankCode | ∅ | Hong Kong Bank Code - identifies Hong Kong financial institutions on the Hong Kong local clearing system. | HongKongBankIdentifier | ∅ |
| 20 | CashClearingSystemMember | ClearingMember | ∅ | Clearing system member for which a clearing system member identification is specified. | ClearingMemberRole | ClearingSystemMemberIdentification |
| 21 | CashClearingSystemMember | IndianFinancialSystemCode | ∅ | Indian Financial System Code - identifies Indian financial institutions on the Indian local clearing system. | IndianFinancialSystemCodeIdentifier | ∅ |
| 22 | CashClearingSystemMember | HellenicBankIdentificationCode | ∅ | Hellenic Bank Identification Code - identifies Hellenic financial institutions on the Hellenic national clearing system. | HellenicBankIdentificationCodeIdentifier | ∅ |
| 23 | CashClearingSystemMember | PolishNationalClearingCode | ∅ | Polish National Clearing Code - identifies Polish financial institutions on the Polish national clearing system. | PolishNationalClearingCodeIdentifier | ∅ |
| 24 | CashClearingSystemMember | AustralianBSBCode | ∅ | Australian Bank State Branch (BSB) Code - identifies Australian financial institutions on the Australian national clearing system. The code is assigned by the Australian Payments Clearing Association (APCA). | AustralianBSBIdentification | ClearingSystemMemberIdentificationType |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `c6027858e0d10dfbbffd66bb63b01a022a9869264968452d7a44d5072fa7f26f`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A634:F657 | 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657 | [src-000006 original](<../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart3_BanktoCustomerCashManagement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md>) |
| src-000016 | FullBusinessModel!A619:F642 | 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642 | [src-000016 original](<../../../raw-input/cash_management/ISO20022_MDRPart3_CashManagement_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md>) |
| src-000054 | FullBusinessModel!A634:F657 | 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657 | [src-000054 original](<../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart3_CentralCounterParty_SecuritiesClearing_Maintenance_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md>) |
| src-000081 | FullBusinessModel!A634:F657 | 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657 | [src-000081 original](<../../../raw-input/corporate_actions/ISO20022_MDRPart3_CorporateActions_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md>) |
| src-000097 | FullBusinessModel!A634:F657 | 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657 | [src-000097 original](<../../../raw-input/investment_funds/ISO20022_MDRPart3_Investment-Funds_2025_2026_v2.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md>) |
| src-000164 | FullBusinessModel!A634:F657 | 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657 | [src-000164 original](<../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart3_PaymentsClearingandSettlement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md>) |
| src-000175 | FullBusinessModel!A634:F657 | 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657 | [src-000175 original](<../../../raw-input/payments_initiation/ISO20022_MDRPart3_PaymentsInitiation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md>) |
| src-000182 | FullBusinessModel!A619:F642 | 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642 | [src-000182 original](<../../../raw-input/post_trade_matching/ISO20022_MDRPart3_PostTradeMatching_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md>) |
| src-000198 | FullBusinessModel!A634:F657 | 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657 | [src-000198 original](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart3_SettlementAndReconciliation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md>) |
| src-000322 | FullBusinessModel!A631:F654 | 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 | [src-000322 original](<../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart3_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md>) |
| src-000345 | FullBusinessModel!A1288:F1311 | 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311 | [src-000345 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](<../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md>) |
| src-000348 | FullBusinessModel!A631:F654 | 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 | [src-000348 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md>) |
| src-000352 | FullBusinessModel!A634:F657 | 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657 | [src-000352 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md>) |
| src-000355 | FullBusinessModel!A619:F642 | 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642 | [src-000355 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md>) |
| src-000358 | FullBusinessModel!A1288:F1311 | 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311 | [src-000358 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md>) |
| src-000361 | FullBusinessModel!A1288:F1311 | 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311 | [src-000361 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md>) |
| src-000364 | FullBusinessModel!A619:F642 | 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642 | [src-000364 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md>) |
| src-000367 | FullBusinessModel!A619:F642 | 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642 | [src-000367 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md>) |
| src-000370 | FullBusinessModel!A1288:F1311 | 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311 | [src-000370 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md>) |
| src-000373 | FullBusinessModel!A1288:F1311 | 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311 | [src-000373 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md>) |
| src-000376 | FullBusinessModel!A634:F657 | 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657 | [src-000376 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md>) |
| src-000379 | FullBusinessModel!A1288:F1311 | 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311 | [src-000379 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md>) |
| src-000382 | FullBusinessModel!A631:F654 | 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 | [src-000382 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | field-type | E635 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000006 | field-type | E636 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E637 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E638 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E639 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E640 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E641 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E642 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E643 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E644 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E645 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E646 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E647 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E648 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E649 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E650 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E651 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E652 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E653 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000006 | field-type | E654 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E655 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E656 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000006 | field-type | E657 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000016 | field-type | E620 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000016 | field-type | E621 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E622 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E623 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E624 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E625 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E626 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E627 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E628 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E629 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E630 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E631 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E632 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E633 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E634 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E635 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E636 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E637 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E638 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000016 | field-type | E639 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E640 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E641 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000016 | field-type | E642 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000054 | field-type | E635 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000054 | field-type | E636 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E637 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E638 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E639 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E640 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E641 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E642 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E643 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E644 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E645 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E646 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E647 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E648 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E649 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E650 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E651 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E652 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E653 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000054 | field-type | E654 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E655 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E656 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000054 | field-type | E657 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000081 | field-type | E635 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000081 | field-type | E636 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E637 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E638 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E639 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E640 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E641 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E642 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E643 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E644 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E645 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E646 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E647 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E648 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E649 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E650 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E651 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E652 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E653 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000081 | field-type | E654 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E655 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E656 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000081 | field-type | E657 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000097 | field-type | E635 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000097 | field-type | E636 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E637 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E638 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E639 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E640 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E641 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E642 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E643 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E644 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E645 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E646 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E647 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E648 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E649 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E650 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E651 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E652 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E653 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000097 | field-type | E654 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E655 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E656 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000097 | field-type | E657 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000164 | field-type | E635 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000164 | field-type | E636 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E637 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E638 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E639 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E640 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E641 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E642 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E643 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E644 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E645 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E646 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E647 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E648 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E649 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E650 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E651 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E652 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E653 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000164 | field-type | E654 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E655 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E656 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000164 | field-type | E657 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000175 | field-type | E635 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000175 | field-type | E636 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E637 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E638 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E639 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E640 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E641 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E642 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E643 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E644 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E645 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E646 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E647 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E648 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E649 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E650 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E651 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E652 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E653 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000175 | field-type | E654 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E655 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E656 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000175 | field-type | E657 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000182 | field-type | E620 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000182 | field-type | E621 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E622 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E623 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E624 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E625 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E626 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E627 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E628 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E629 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E630 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E631 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E632 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E633 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E634 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E635 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E636 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E637 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E638 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000182 | field-type | E639 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E640 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E641 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000182 | field-type | E642 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000198 | field-type | E635 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000198 | field-type | E636 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E637 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E638 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E639 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E640 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E641 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E642 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E643 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E644 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E645 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E646 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E647 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E648 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E649 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E650 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E651 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E652 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E653 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000198 | field-type | E654 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E655 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E656 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000198 | field-type | E657 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000322 | field-type | E632 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000322 | field-type | E633 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E634 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E635 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E636 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E637 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E638 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E639 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E640 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E641 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E642 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E643 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E644 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E645 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E646 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E647 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E648 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E649 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E650 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000322 | field-type | E651 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E652 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E653 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000322 | field-type | E654 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000345 | field-type | E1289 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000345 | field-type | E1290 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1291 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1292 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1293 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1294 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1295 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1296 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1297 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1298 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1299 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1300 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1301 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1302 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1303 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1304 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1305 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1306 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1307 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000345 | field-type | E1308 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1309 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1310 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000345 | field-type | E1311 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-374918ceb119c1d1655e.md>) |
| src-000348 | field-type | E632 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000348 | field-type | E633 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E634 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E635 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E636 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E637 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E638 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E639 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E640 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E641 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E642 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E643 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E644 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E645 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E646 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E647 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E648 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E649 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E650 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000348 | field-type | E651 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E652 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E653 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000348 | field-type | E654 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000352 | field-type | E635 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000352 | field-type | E636 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E637 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E638 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E639 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E640 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E641 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E642 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E643 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E644 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E645 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E646 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E647 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E648 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E649 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E650 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E651 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E652 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E653 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000352 | field-type | E654 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E655 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E656 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000352 | field-type | E657 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000355 | field-type | E620 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000355 | field-type | E621 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E622 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E623 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E624 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E625 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E626 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E627 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E628 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E629 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E630 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E631 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E632 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E633 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E634 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E635 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E636 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E637 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E638 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000355 | field-type | E639 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E640 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E641 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000355 | field-type | E642 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000358 | field-type | E1289 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000358 | field-type | E1290 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1291 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1292 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1293 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1294 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1295 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1296 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1297 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1298 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1299 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1300 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1301 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1302 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1303 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1304 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1305 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1306 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1307 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000358 | field-type | E1308 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1309 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1310 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000358 | field-type | E1311 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-374918ceb119c1d1655e.md>) |
| src-000361 | field-type | E1289 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000361 | field-type | E1290 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1291 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1292 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1293 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1294 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1295 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1296 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1297 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1298 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1299 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1300 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1301 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1302 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1303 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1304 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1305 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1306 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1307 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000361 | field-type | E1308 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1309 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1310 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000361 | field-type | E1311 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-374918ceb119c1d1655e.md>) |
| src-000364 | field-type | E620 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000364 | field-type | E621 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E622 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E623 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E624 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E625 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E626 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E627 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E628 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E629 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E630 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E631 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E632 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E633 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E634 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E635 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E636 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E637 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E638 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000364 | field-type | E639 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E640 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E641 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000364 | field-type | E642 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-374918ceb119c1d1655e.md>) |
| src-000367 | field-type | E620 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000367 | field-type | E621 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E622 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E623 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E624 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E625 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E626 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E627 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E628 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E629 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E630 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E631 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E632 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E633 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E634 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E635 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E636 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E637 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E638 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000367 | field-type | E639 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E640 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E641 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000367 | field-type | E642 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000370 | field-type | E1289 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000370 | field-type | E1290 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1291 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1292 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1293 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1294 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1295 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1296 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1297 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1298 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1299 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1300 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1301 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1302 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1303 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1304 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1305 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1306 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1307 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000370 | field-type | E1308 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1309 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1310 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000370 | field-type | E1311 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-374918ceb119c1d1655e.md>) |
| src-000373 | field-type | E1289 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000373 | field-type | E1290 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1291 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1292 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1293 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1294 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1295 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1296 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1297 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1298 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1299 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1300 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1301 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1302 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1303 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1304 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1305 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1306 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1307 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000373 | field-type | E1308 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1309 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1310 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000373 | field-type | E1311 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-374918ceb119c1d1655e.md>) |
| src-000376 | field-type | E635 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000376 | field-type | E636 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E637 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E638 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E639 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E640 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E641 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E642 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E643 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E644 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E645 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E646 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E647 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E648 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E649 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E650 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E651 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E652 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E653 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000376 | field-type | E654 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E655 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E656 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000376 | field-type | E657 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |
| src-000379 | field-type | E1289 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000379 | field-type | E1290 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1291 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1292 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1293 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1294 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1295 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1296 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1297 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1298 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1299 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1300 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1301 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1302 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1303 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1304 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1305 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1306 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1307 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000379 | field-type | E1308 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1309 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1310 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000379 | field-type | E1311 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-374918ceb119c1d1655e.md>) |
| src-000382 | field-type | E632 | OrganisationIdentification | [OrganisationIdentification](<bc-2d36a612f791ed8b82bb.md>) |
| src-000382 | field-type | E633 | CHIPSUniversalIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E634 | NewZealandNCCIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E635 | IrishNSCIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E636 | UKDomesticSortCodeIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E637 | CHIPSParticipantIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E638 | SwissBCIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E639 | FedwireRoutingNumberIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E640 | PortugueseNCCIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E641 | RussianCentralBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E642 | ItalianDomesticIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E643 | AustrianBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E644 | CanadianPaymentsARNIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E645 | SwissSICIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E646 | GermanBankleitzahlIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E647 | SpanishDomesticInterbankingIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E648 | SouthAfricanNCCIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E649 | HongKongBankIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E650 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000382 | field-type | E651 | IndianFinancialSystemCodeIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E652 | HellenicBankIdentificationCodeIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E653 | PolishNationalClearingCodeIdentifier | Not a component record in this worksheet |
| src-000382 | field-type | E654 | AustralianBSBIdentification | [AustralianBSBIdentification](<bc-28150025c91feab89bd5.md>) |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
