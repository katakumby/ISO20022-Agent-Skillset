---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-fa08203aa2af6ddee2df"
title: "Undertaking"
business_component_name: "Undertaking"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A5279:F5306"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A5209:F5236"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A5279:F5306"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A5279:F5306"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A5279:F5306"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A5279:F5306"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A5279:F5306"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A5209:F5236"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A5279:F5306"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A5248:F5275"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A3237:F3264"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A5248:F5275"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A5279:F5306"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A5182:F5209"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A3237:F3264"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A3237:F3264"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A5182:F5209"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A5182:F5209"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A3237:F3264"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A3237:F3264"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A5279:F5306"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A3237:F3264"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A5248:F5275"]}]
content_sha256: "fa08203aa2af6ddee2df738e7a56d6998916c18e4f0e8e33420d220b9813c5c2"
parent_names: []
related_component_names: ["AmendmentOfUndertaking", "AutomaticVariation", "Charges", "Demand", "ElectronicSignature", "Expiry", "ExternalTypeOfPartyCode", "ExternalUndertakingTypeCode", "ISODate", "ISODateTime", "Max35Text", "ModelForm", "Presentation", "UnderlyingTransaction", "UndertakingAmount", "UndertakingDocument", "UndertakingExtension", "UndertakingNameCode", "UndertakingPartyRole", "UndertakingStatus", "YesNoIndicator"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# Undertaking

## Definition

Independent undertaking, such as a demand guarantee or standby letter of credit, that provides financial assurance, to be collected on the presentation of documents that comply with its terms and conditions.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Undertaking | ∅ | ∅ | Independent undertaking, such as a demand guarantee or standby letter of credit, that provides financial assurance, to be collected on the presentation of documents that comply with its terms and conditions. | ∅ | ∅ |
| 2 | Undertaking | ElectronicSignature | ∅ | Digital signature. | ElectronicSignature | Undertaking |
| 3 | Undertaking | UndertakingStatus | ∅ | Status of the undertaking. | UndertakingStatus | Undertaking |
| 4 | Undertaking | Identification | ∅ | Unique and unambiguous identifier assigned to the undertaking issued by the guarantor/issuer. This reference is used throughout the life cycle of the undertaking. | Max35Text | ∅ |
| 5 | Undertaking | Demand | ∅ | Document signed by the beneficiary demanding payment under a demand guarantee or standby letter of credit. | Demand | Undertaking |
| 6 | Undertaking | TerminationDate | ∅ | Date when the undertaking terminates. | ISODate | ∅ |
| 7 | Undertaking | UndertakingAmount | ∅ | Amount of the undertaking. | UndertakingAmount | Undertaking |
| 8 | Undertaking | Expiry | ∅ | Expiry information about the undertaking. | Expiry | Undertaking |
| 9 | Undertaking | PartyRole | ∅ | Role played by a party in the context of an undertaking or in the context of the business linked to the undertaking. | UndertakingPartyRole | Undertaking |
| 10 | Undertaking | UndertakingAmendment | ∅ | Modification of an undertaking such as an guarantee or standby letter of credit. | AmendmentOfUndertaking | Undertaking |
| 11 | Undertaking | SpecifiedDocument | ∅ | Document related to the undertaking. | UndertakingDocument | Undertaking |
| 12 | Undertaking | DateOfAdvice | ∅ | Date on which the undertaking or its amendment is advised. | ISODateTime | ∅ |
| 13 | Undertaking | Purpose | ∅ | Description of the purpose of the undertaking. | Max35Text | ∅ |
| 14 | Undertaking | UndertakingName | ∅ | Name of undertaking such as, demand guarantee, standby letter of credit. | UndertakingNameCode | ∅ |
| 15 | Undertaking | Type | ∅ | Type of guarantee or standby letter of credit, for example, performance,  payment, etc. | ExternalUndertakingTypeCode | ∅ |
| 16 | Undertaking | ConfirmationIndicator | ∅ | Indicates whether the advising bank (confirmer) is requested to add its confirmation to the undertaking. | YesNoIndicator | ∅ |
| 17 | Undertaking | CounterUndertakingIndicator | ∅ | Indicates whether the undertaking is a counter-undertaking. | YesNoIndicator | ∅ |
| 18 | Undertaking | RelatedChargesPayableBy | ∅ | Indicates whether the applicant/obligor or beneficiary is responsible for payment of the charges. | ExternalTypeOfPartyCode | ∅ |
| 19 | Undertaking | StandardClaimDocumentIndicator | ∅ | Indication as to whether a claim is to utilise a standard claim form of the issuing institution. | YesNoIndicator | ∅ |
| 20 | Undertaking | UnderlyingTransaction | ∅ | Reference information on a commercial obligation between the beneficiary and applicant for which an undertaking is issued. | UnderlyingTransaction | Undertaking |
| 21 | Undertaking | ModelForm | ∅ | Wording template for the undertaking content made available for use with certain governance rules or made available by particular institutions.  | ModelForm | Undertaking |
| 22 | Undertaking | MultipleDemandIndicator | ∅ | Indicates whether multiple demands are permitted against the undertaking. | YesNoIndicator | ∅ |
| 23 | Undertaking | PartialDemandIndicator | ∅ | Indicates whether partial demands/drawings are permitted against the undertaking. | YesNoIndicator | ∅ |
| 24 | Undertaking | TransferIndicator | ∅ | Indicates whether the undertaking is transferrable. | YesNoIndicator | ∅ |
| 25 | Undertaking | PredefinedVariation | ∅ | Changes that may be made to the undertaking covered by clauses in the existing undertaking and its amendments. | AutomaticVariation | Undertaking |
| 26 | Undertaking | Charges | ∅ | Amount and currency of the commissions and changes. | Charges | RelatedUndertaking |
| 27 | Undertaking | Presentation | ∅ | Presentation information related to the undertaking. | Presentation | PresentedUndertaking |
| 28 | Undertaking | UndertakingExtension | ∅ | Specifies information related to the extension of an undertaking. | UndertakingExtension | Undertaking |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `fa08203aa2af6ddee2df738e7a56d6998916c18e4f0e8e33420d220b9813c5c2`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A5279:F5306 | 5279, 5280, 5281, 5282, 5283, 5284, 5285, 5286, 5287, 5288, 5289, 5290, 5291, 5292, 5293, 5294, 5295, 5296, 5297, 5298, 5299, 5300, 5301, 5302, 5303, 5304, 5305, 5306 | [src-000006 original](../../../evidence/omitted/5e0f6b7d43fcbbe816624756.md) | [Lookup](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md) |
| src-000016 | FullBusinessModel!A5209:F5236 | 5209, 5210, 5211, 5212, 5213, 5214, 5215, 5216, 5217, 5218, 5219, 5220, 5221, 5222, 5223, 5224, 5225, 5226, 5227, 5228, 5229, 5230, 5231, 5232, 5233, 5234, 5235, 5236 | [src-000016 original](../../../evidence/omitted/42cf3c4088baf4d4c6dc07c1.md) | [Lookup](../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md) |
| src-000054 | FullBusinessModel!A5279:F5306 | 5279, 5280, 5281, 5282, 5283, 5284, 5285, 5286, 5287, 5288, 5289, 5290, 5291, 5292, 5293, 5294, 5295, 5296, 5297, 5298, 5299, 5300, 5301, 5302, 5303, 5304, 5305, 5306 | [src-000054 original](../../../evidence/omitted/ea96e6afbf1f8819d68ca6f6.md) | [Lookup](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md) |
| src-000081 | FullBusinessModel!A5279:F5306 | 5279, 5280, 5281, 5282, 5283, 5284, 5285, 5286, 5287, 5288, 5289, 5290, 5291, 5292, 5293, 5294, 5295, 5296, 5297, 5298, 5299, 5300, 5301, 5302, 5303, 5304, 5305, 5306 | [src-000081 original](../../../evidence/omitted/5d05ada13720516836bc5043.md) | [Lookup](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md) |
| src-000097 | FullBusinessModel!A5279:F5306 | 5279, 5280, 5281, 5282, 5283, 5284, 5285, 5286, 5287, 5288, 5289, 5290, 5291, 5292, 5293, 5294, 5295, 5296, 5297, 5298, 5299, 5300, 5301, 5302, 5303, 5304, 5305, 5306 | [src-000097 original](../../../evidence/omitted/3ea6002607634c1b65cb5c88.md) | [Lookup](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md) |
| src-000164 | FullBusinessModel!A5279:F5306 | 5279, 5280, 5281, 5282, 5283, 5284, 5285, 5286, 5287, 5288, 5289, 5290, 5291, 5292, 5293, 5294, 5295, 5296, 5297, 5298, 5299, 5300, 5301, 5302, 5303, 5304, 5305, 5306 | [src-000164 original](../../../evidence/omitted/87020353dd81a550a7b6ed6f.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md) |
| src-000175 | FullBusinessModel!A5279:F5306 | 5279, 5280, 5281, 5282, 5283, 5284, 5285, 5286, 5287, 5288, 5289, 5290, 5291, 5292, 5293, 5294, 5295, 5296, 5297, 5298, 5299, 5300, 5301, 5302, 5303, 5304, 5305, 5306 | [src-000175 original](../../../evidence/omitted/807236f9f4d5f25826f3ba17.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md) |
| src-000182 | FullBusinessModel!A5209:F5236 | 5209, 5210, 5211, 5212, 5213, 5214, 5215, 5216, 5217, 5218, 5219, 5220, 5221, 5222, 5223, 5224, 5225, 5226, 5227, 5228, 5229, 5230, 5231, 5232, 5233, 5234, 5235, 5236 | [src-000182 original](../../../evidence/omitted/5096efb167050baf43bfb32a.md) | [Lookup](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md) |
| src-000198 | FullBusinessModel!A5279:F5306 | 5279, 5280, 5281, 5282, 5283, 5284, 5285, 5286, 5287, 5288, 5289, 5290, 5291, 5292, 5293, 5294, 5295, 5296, 5297, 5298, 5299, 5300, 5301, 5302, 5303, 5304, 5305, 5306 | [src-000198 original](../../../evidence/omitted/c6a84c22fb63cab3b848bd88.md) | [Lookup](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md) |
| src-000322 | FullBusinessModel!A5248:F5275 | 5248, 5249, 5250, 5251, 5252, 5253, 5254, 5255, 5256, 5257, 5258, 5259, 5260, 5261, 5262, 5263, 5264, 5265, 5266, 5267, 5268, 5269, 5270, 5271, 5272, 5273, 5274, 5275 | [src-000322 original](../../../evidence/omitted/f39eee3c04bb287d206cc6a3.md) | [Lookup](../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md) |
| src-000345 | FullBusinessModel!A3237:F3264 | 3237, 3238, 3239, 3240, 3241, 3242, 3243, 3244, 3245, 3246, 3247, 3248, 3249, 3250, 3251, 3252, 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264 | [src-000345 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md) |
| src-000348 | FullBusinessModel!A5248:F5275 | 5248, 5249, 5250, 5251, 5252, 5253, 5254, 5255, 5256, 5257, 5258, 5259, 5260, 5261, 5262, 5263, 5264, 5265, 5266, 5267, 5268, 5269, 5270, 5271, 5272, 5273, 5274, 5275 | [src-000348 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md) |
| src-000352 | FullBusinessModel!A5279:F5306 | 5279, 5280, 5281, 5282, 5283, 5284, 5285, 5286, 5287, 5288, 5289, 5290, 5291, 5292, 5293, 5294, 5295, 5296, 5297, 5298, 5299, 5300, 5301, 5302, 5303, 5304, 5305, 5306 | [src-000352 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md) |
| src-000355 | FullBusinessModel!A5182:F5209 | 5182, 5183, 5184, 5185, 5186, 5187, 5188, 5189, 5190, 5191, 5192, 5193, 5194, 5195, 5196, 5197, 5198, 5199, 5200, 5201, 5202, 5203, 5204, 5205, 5206, 5207, 5208, 5209 | [src-000355 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md) |
| src-000358 | FullBusinessModel!A3237:F3264 | 3237, 3238, 3239, 3240, 3241, 3242, 3243, 3244, 3245, 3246, 3247, 3248, 3249, 3250, 3251, 3252, 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264 | [src-000358 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md) |
| src-000361 | FullBusinessModel!A3237:F3264 | 3237, 3238, 3239, 3240, 3241, 3242, 3243, 3244, 3245, 3246, 3247, 3248, 3249, 3250, 3251, 3252, 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264 | [src-000361 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md) |
| src-000364 | FullBusinessModel!A5182:F5209 | 5182, 5183, 5184, 5185, 5186, 5187, 5188, 5189, 5190, 5191, 5192, 5193, 5194, 5195, 5196, 5197, 5198, 5199, 5200, 5201, 5202, 5203, 5204, 5205, 5206, 5207, 5208, 5209 | [src-000364 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md) |
| src-000367 | FullBusinessModel!A5182:F5209 | 5182, 5183, 5184, 5185, 5186, 5187, 5188, 5189, 5190, 5191, 5192, 5193, 5194, 5195, 5196, 5197, 5198, 5199, 5200, 5201, 5202, 5203, 5204, 5205, 5206, 5207, 5208, 5209 | [src-000367 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md) |
| src-000370 | FullBusinessModel!A3237:F3264 | 3237, 3238, 3239, 3240, 3241, 3242, 3243, 3244, 3245, 3246, 3247, 3248, 3249, 3250, 3251, 3252, 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264 | [src-000370 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md) |
| src-000373 | FullBusinessModel!A3237:F3264 | 3237, 3238, 3239, 3240, 3241, 3242, 3243, 3244, 3245, 3246, 3247, 3248, 3249, 3250, 3251, 3252, 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264 | [src-000373 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md) |
| src-000376 | FullBusinessModel!A5279:F5306 | 5279, 5280, 5281, 5282, 5283, 5284, 5285, 5286, 5287, 5288, 5289, 5290, 5291, 5292, 5293, 5294, 5295, 5296, 5297, 5298, 5299, 5300, 5301, 5302, 5303, 5304, 5305, 5306 | [src-000376 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md) |
| src-000379 | FullBusinessModel!A3237:F3264 | 3237, 3238, 3239, 3240, 3241, 3242, 3243, 3244, 3245, 3246, 3247, 3248, 3249, 3250, 3251, 3252, 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264 | [src-000379 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md) |
| src-000382 | FullBusinessModel!A5248:F5275 | 5248, 5249, 5250, 5251, 5252, 5253, 5254, 5255, 5256, 5257, 5258, 5259, 5260, 5261, 5262, 5263, 5264, 5265, 5266, 5267, 5268, 5269, 5270, 5271, 5272, 5273, 5274, 5275 | [src-000382 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | field-type | E5280 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000006 | field-type | E5281 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000006 | field-type | E5282 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E5283 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000006 | field-type | E5284 | ISODate | Not a component record in this worksheet |
| src-000006 | field-type | E5285 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000006 | field-type | E5286 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000006 | field-type | E5287 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000006 | field-type | E5288 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000006 | field-type | E5289 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000006 | field-type | E5290 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E5291 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E5292 | UndertakingNameCode | Not a component record in this worksheet |
| src-000006 | field-type | E5293 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000006 | field-type | E5294 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E5295 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E5296 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000006 | field-type | E5297 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E5298 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000006 | field-type | E5299 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000006 | field-type | E5300 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E5301 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E5302 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E5303 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000006 | field-type | E5304 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000006 | field-type | E5305 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000006 | field-type | E5306 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000016 | field-type | E5210 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000016 | field-type | E5211 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000016 | field-type | E5212 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E5213 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000016 | field-type | E5214 | ISODate | Not a component record in this worksheet |
| src-000016 | field-type | E5215 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000016 | field-type | E5216 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000016 | field-type | E5217 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000016 | field-type | E5218 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000016 | field-type | E5219 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000016 | field-type | E5220 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E5221 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E5222 | UndertakingNameCode | Not a component record in this worksheet |
| src-000016 | field-type | E5223 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000016 | field-type | E5224 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E5225 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E5226 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000016 | field-type | E5227 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E5228 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000016 | field-type | E5229 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000016 | field-type | E5230 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E5231 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E5232 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E5233 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000016 | field-type | E5234 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000016 | field-type | E5235 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000016 | field-type | E5236 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000054 | field-type | E5280 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000054 | field-type | E5281 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000054 | field-type | E5282 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E5283 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000054 | field-type | E5284 | ISODate | Not a component record in this worksheet |
| src-000054 | field-type | E5285 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000054 | field-type | E5286 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000054 | field-type | E5287 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000054 | field-type | E5288 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000054 | field-type | E5289 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000054 | field-type | E5290 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E5291 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E5292 | UndertakingNameCode | Not a component record in this worksheet |
| src-000054 | field-type | E5293 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000054 | field-type | E5294 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E5295 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E5296 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000054 | field-type | E5297 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E5298 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000054 | field-type | E5299 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000054 | field-type | E5300 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E5301 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E5302 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E5303 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000054 | field-type | E5304 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000054 | field-type | E5305 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000054 | field-type | E5306 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000081 | field-type | E5280 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000081 | field-type | E5281 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000081 | field-type | E5282 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E5283 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000081 | field-type | E5284 | ISODate | Not a component record in this worksheet |
| src-000081 | field-type | E5285 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000081 | field-type | E5286 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000081 | field-type | E5287 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000081 | field-type | E5288 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000081 | field-type | E5289 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000081 | field-type | E5290 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E5291 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E5292 | UndertakingNameCode | Not a component record in this worksheet |
| src-000081 | field-type | E5293 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000081 | field-type | E5294 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E5295 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E5296 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000081 | field-type | E5297 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E5298 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000081 | field-type | E5299 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000081 | field-type | E5300 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E5301 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E5302 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E5303 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000081 | field-type | E5304 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000081 | field-type | E5305 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000081 | field-type | E5306 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000097 | field-type | E5280 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000097 | field-type | E5281 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000097 | field-type | E5282 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E5283 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000097 | field-type | E5284 | ISODate | Not a component record in this worksheet |
| src-000097 | field-type | E5285 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000097 | field-type | E5286 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000097 | field-type | E5287 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000097 | field-type | E5288 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000097 | field-type | E5289 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000097 | field-type | E5290 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E5291 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E5292 | UndertakingNameCode | Not a component record in this worksheet |
| src-000097 | field-type | E5293 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000097 | field-type | E5294 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E5295 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E5296 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000097 | field-type | E5297 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E5298 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000097 | field-type | E5299 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000097 | field-type | E5300 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E5301 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E5302 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E5303 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000097 | field-type | E5304 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000097 | field-type | E5305 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000097 | field-type | E5306 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000164 | field-type | E5280 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000164 | field-type | E5281 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000164 | field-type | E5282 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E5283 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000164 | field-type | E5284 | ISODate | Not a component record in this worksheet |
| src-000164 | field-type | E5285 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000164 | field-type | E5286 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000164 | field-type | E5287 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000164 | field-type | E5288 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000164 | field-type | E5289 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000164 | field-type | E5290 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E5291 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E5292 | UndertakingNameCode | Not a component record in this worksheet |
| src-000164 | field-type | E5293 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000164 | field-type | E5294 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E5295 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E5296 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000164 | field-type | E5297 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E5298 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000164 | field-type | E5299 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000164 | field-type | E5300 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E5301 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E5302 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E5303 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000164 | field-type | E5304 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000164 | field-type | E5305 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000164 | field-type | E5306 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000175 | field-type | E5280 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000175 | field-type | E5281 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000175 | field-type | E5282 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E5283 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000175 | field-type | E5284 | ISODate | Not a component record in this worksheet |
| src-000175 | field-type | E5285 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000175 | field-type | E5286 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000175 | field-type | E5287 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000175 | field-type | E5288 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000175 | field-type | E5289 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000175 | field-type | E5290 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E5291 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E5292 | UndertakingNameCode | Not a component record in this worksheet |
| src-000175 | field-type | E5293 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000175 | field-type | E5294 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E5295 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E5296 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000175 | field-type | E5297 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E5298 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000175 | field-type | E5299 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000175 | field-type | E5300 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E5301 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E5302 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E5303 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000175 | field-type | E5304 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000175 | field-type | E5305 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000175 | field-type | E5306 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000182 | field-type | E5210 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000182 | field-type | E5211 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000182 | field-type | E5212 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E5213 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000182 | field-type | E5214 | ISODate | Not a component record in this worksheet |
| src-000182 | field-type | E5215 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000182 | field-type | E5216 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000182 | field-type | E5217 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000182 | field-type | E5218 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000182 | field-type | E5219 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000182 | field-type | E5220 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E5221 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E5222 | UndertakingNameCode | Not a component record in this worksheet |
| src-000182 | field-type | E5223 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000182 | field-type | E5224 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E5225 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E5226 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000182 | field-type | E5227 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E5228 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000182 | field-type | E5229 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000182 | field-type | E5230 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E5231 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E5232 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E5233 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000182 | field-type | E5234 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000182 | field-type | E5235 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000182 | field-type | E5236 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000198 | field-type | E5280 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000198 | field-type | E5281 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000198 | field-type | E5282 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E5283 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000198 | field-type | E5284 | ISODate | Not a component record in this worksheet |
| src-000198 | field-type | E5285 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000198 | field-type | E5286 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000198 | field-type | E5287 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000198 | field-type | E5288 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000198 | field-type | E5289 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000198 | field-type | E5290 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E5291 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E5292 | UndertakingNameCode | Not a component record in this worksheet |
| src-000198 | field-type | E5293 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000198 | field-type | E5294 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E5295 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E5296 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000198 | field-type | E5297 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E5298 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000198 | field-type | E5299 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000198 | field-type | E5300 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E5301 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E5302 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E5303 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000198 | field-type | E5304 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000198 | field-type | E5305 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000198 | field-type | E5306 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000322 | field-type | E5249 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000322 | field-type | E5250 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000322 | field-type | E5251 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E5252 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000322 | field-type | E5253 | ISODate | Not a component record in this worksheet |
| src-000322 | field-type | E5254 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000322 | field-type | E5255 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000322 | field-type | E5256 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000322 | field-type | E5257 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000322 | field-type | E5258 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000322 | field-type | E5259 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E5260 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E5261 | UndertakingNameCode | Not a component record in this worksheet |
| src-000322 | field-type | E5262 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000322 | field-type | E5263 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E5264 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E5265 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000322 | field-type | E5266 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E5267 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000322 | field-type | E5268 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000322 | field-type | E5269 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E5270 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E5271 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E5272 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000322 | field-type | E5273 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000322 | field-type | E5274 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000322 | field-type | E5275 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000345 | field-type | E3238 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000345 | field-type | E3239 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000345 | field-type | E3240 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E3241 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000345 | field-type | E3242 | ISODate | Not a component record in this worksheet |
| src-000345 | field-type | E3243 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000345 | field-type | E3244 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000345 | field-type | E3245 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000345 | field-type | E3246 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000345 | field-type | E3247 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000345 | field-type | E3248 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E3249 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E3250 | UndertakingNameCode | Not a component record in this worksheet |
| src-000345 | field-type | E3251 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000345 | field-type | E3252 | YesNoIndicator | Not a component record in this worksheet |
| src-000345 | field-type | E3253 | YesNoIndicator | Not a component record in this worksheet |
| src-000345 | field-type | E3254 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000345 | field-type | E3255 | YesNoIndicator | Not a component record in this worksheet |
| src-000345 | field-type | E3256 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000345 | field-type | E3257 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000345 | field-type | E3258 | YesNoIndicator | Not a component record in this worksheet |
| src-000345 | field-type | E3259 | YesNoIndicator | Not a component record in this worksheet |
| src-000345 | field-type | E3260 | YesNoIndicator | Not a component record in this worksheet |
| src-000345 | field-type | E3261 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000345 | field-type | E3262 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000345 | field-type | E3263 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000345 | field-type | E3264 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000348 | field-type | E5249 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000348 | field-type | E5250 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000348 | field-type | E5251 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E5252 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000348 | field-type | E5253 | ISODate | Not a component record in this worksheet |
| src-000348 | field-type | E5254 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000348 | field-type | E5255 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000348 | field-type | E5256 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000348 | field-type | E5257 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000348 | field-type | E5258 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000348 | field-type | E5259 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E5260 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E5261 | UndertakingNameCode | Not a component record in this worksheet |
| src-000348 | field-type | E5262 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000348 | field-type | E5263 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E5264 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E5265 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000348 | field-type | E5266 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E5267 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000348 | field-type | E5268 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000348 | field-type | E5269 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E5270 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E5271 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E5272 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000348 | field-type | E5273 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000348 | field-type | E5274 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000348 | field-type | E5275 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000352 | field-type | E5280 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000352 | field-type | E5281 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000352 | field-type | E5282 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E5283 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000352 | field-type | E5284 | ISODate | Not a component record in this worksheet |
| src-000352 | field-type | E5285 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000352 | field-type | E5286 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000352 | field-type | E5287 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000352 | field-type | E5288 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000352 | field-type | E5289 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000352 | field-type | E5290 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E5291 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E5292 | UndertakingNameCode | Not a component record in this worksheet |
| src-000352 | field-type | E5293 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000352 | field-type | E5294 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E5295 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E5296 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000352 | field-type | E5297 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E5298 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000352 | field-type | E5299 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000352 | field-type | E5300 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E5301 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E5302 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E5303 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000352 | field-type | E5304 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000352 | field-type | E5305 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000352 | field-type | E5306 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000355 | field-type | E5183 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000355 | field-type | E5184 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000355 | field-type | E5185 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E5186 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000355 | field-type | E5187 | ISODate | Not a component record in this worksheet |
| src-000355 | field-type | E5188 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000355 | field-type | E5189 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000355 | field-type | E5190 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000355 | field-type | E5191 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000355 | field-type | E5192 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000355 | field-type | E5193 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E5194 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E5195 | UndertakingNameCode | Not a component record in this worksheet |
| src-000355 | field-type | E5196 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000355 | field-type | E5197 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E5198 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E5199 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000355 | field-type | E5200 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E5201 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000355 | field-type | E5202 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000355 | field-type | E5203 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E5204 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E5205 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E5206 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000355 | field-type | E5207 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000355 | field-type | E5208 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000355 | field-type | E5209 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000358 | field-type | E3238 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000358 | field-type | E3239 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000358 | field-type | E3240 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E3241 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000358 | field-type | E3242 | ISODate | Not a component record in this worksheet |
| src-000358 | field-type | E3243 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000358 | field-type | E3244 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000358 | field-type | E3245 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000358 | field-type | E3246 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000358 | field-type | E3247 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000358 | field-type | E3248 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E3249 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E3250 | UndertakingNameCode | Not a component record in this worksheet |
| src-000358 | field-type | E3251 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000358 | field-type | E3252 | YesNoIndicator | Not a component record in this worksheet |
| src-000358 | field-type | E3253 | YesNoIndicator | Not a component record in this worksheet |
| src-000358 | field-type | E3254 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000358 | field-type | E3255 | YesNoIndicator | Not a component record in this worksheet |
| src-000358 | field-type | E3256 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000358 | field-type | E3257 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000358 | field-type | E3258 | YesNoIndicator | Not a component record in this worksheet |
| src-000358 | field-type | E3259 | YesNoIndicator | Not a component record in this worksheet |
| src-000358 | field-type | E3260 | YesNoIndicator | Not a component record in this worksheet |
| src-000358 | field-type | E3261 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000358 | field-type | E3262 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000358 | field-type | E3263 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000358 | field-type | E3264 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000361 | field-type | E3238 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000361 | field-type | E3239 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000361 | field-type | E3240 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E3241 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000361 | field-type | E3242 | ISODate | Not a component record in this worksheet |
| src-000361 | field-type | E3243 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000361 | field-type | E3244 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000361 | field-type | E3245 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000361 | field-type | E3246 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000361 | field-type | E3247 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000361 | field-type | E3248 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E3249 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E3250 | UndertakingNameCode | Not a component record in this worksheet |
| src-000361 | field-type | E3251 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000361 | field-type | E3252 | YesNoIndicator | Not a component record in this worksheet |
| src-000361 | field-type | E3253 | YesNoIndicator | Not a component record in this worksheet |
| src-000361 | field-type | E3254 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000361 | field-type | E3255 | YesNoIndicator | Not a component record in this worksheet |
| src-000361 | field-type | E3256 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000361 | field-type | E3257 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000361 | field-type | E3258 | YesNoIndicator | Not a component record in this worksheet |
| src-000361 | field-type | E3259 | YesNoIndicator | Not a component record in this worksheet |
| src-000361 | field-type | E3260 | YesNoIndicator | Not a component record in this worksheet |
| src-000361 | field-type | E3261 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000361 | field-type | E3262 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000361 | field-type | E3263 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000361 | field-type | E3264 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000364 | field-type | E5183 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000364 | field-type | E5184 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000364 | field-type | E5185 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E5186 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000364 | field-type | E5187 | ISODate | Not a component record in this worksheet |
| src-000364 | field-type | E5188 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000364 | field-type | E5189 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000364 | field-type | E5190 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000364 | field-type | E5191 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000364 | field-type | E5192 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000364 | field-type | E5193 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E5194 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E5195 | UndertakingNameCode | Not a component record in this worksheet |
| src-000364 | field-type | E5196 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000364 | field-type | E5197 | YesNoIndicator | Not a component record in this worksheet |
| src-000364 | field-type | E5198 | YesNoIndicator | Not a component record in this worksheet |
| src-000364 | field-type | E5199 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000364 | field-type | E5200 | YesNoIndicator | Not a component record in this worksheet |
| src-000364 | field-type | E5201 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000364 | field-type | E5202 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000364 | field-type | E5203 | YesNoIndicator | Not a component record in this worksheet |
| src-000364 | field-type | E5204 | YesNoIndicator | Not a component record in this worksheet |
| src-000364 | field-type | E5205 | YesNoIndicator | Not a component record in this worksheet |
| src-000364 | field-type | E5206 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000364 | field-type | E5207 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000364 | field-type | E5208 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000364 | field-type | E5209 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000367 | field-type | E5183 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000367 | field-type | E5184 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000367 | field-type | E5185 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E5186 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000367 | field-type | E5187 | ISODate | Not a component record in this worksheet |
| src-000367 | field-type | E5188 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000367 | field-type | E5189 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000367 | field-type | E5190 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000367 | field-type | E5191 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000367 | field-type | E5192 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000367 | field-type | E5193 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E5194 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E5195 | UndertakingNameCode | Not a component record in this worksheet |
| src-000367 | field-type | E5196 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000367 | field-type | E5197 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E5198 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E5199 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000367 | field-type | E5200 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E5201 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000367 | field-type | E5202 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000367 | field-type | E5203 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E5204 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E5205 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E5206 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000367 | field-type | E5207 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000367 | field-type | E5208 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000367 | field-type | E5209 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000370 | field-type | E3238 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000370 | field-type | E3239 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000370 | field-type | E3240 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E3241 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000370 | field-type | E3242 | ISODate | Not a component record in this worksheet |
| src-000370 | field-type | E3243 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000370 | field-type | E3244 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000370 | field-type | E3245 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000370 | field-type | E3246 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000370 | field-type | E3247 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000370 | field-type | E3248 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E3249 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E3250 | UndertakingNameCode | Not a component record in this worksheet |
| src-000370 | field-type | E3251 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000370 | field-type | E3252 | YesNoIndicator | Not a component record in this worksheet |
| src-000370 | field-type | E3253 | YesNoIndicator | Not a component record in this worksheet |
| src-000370 | field-type | E3254 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000370 | field-type | E3255 | YesNoIndicator | Not a component record in this worksheet |
| src-000370 | field-type | E3256 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000370 | field-type | E3257 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000370 | field-type | E3258 | YesNoIndicator | Not a component record in this worksheet |
| src-000370 | field-type | E3259 | YesNoIndicator | Not a component record in this worksheet |
| src-000370 | field-type | E3260 | YesNoIndicator | Not a component record in this worksheet |
| src-000370 | field-type | E3261 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000370 | field-type | E3262 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000370 | field-type | E3263 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000370 | field-type | E3264 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000373 | field-type | E3238 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000373 | field-type | E3239 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000373 | field-type | E3240 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E3241 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000373 | field-type | E3242 | ISODate | Not a component record in this worksheet |
| src-000373 | field-type | E3243 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000373 | field-type | E3244 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000373 | field-type | E3245 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000373 | field-type | E3246 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000373 | field-type | E3247 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000373 | field-type | E3248 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E3249 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E3250 | UndertakingNameCode | Not a component record in this worksheet |
| src-000373 | field-type | E3251 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000373 | field-type | E3252 | YesNoIndicator | Not a component record in this worksheet |
| src-000373 | field-type | E3253 | YesNoIndicator | Not a component record in this worksheet |
| src-000373 | field-type | E3254 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000373 | field-type | E3255 | YesNoIndicator | Not a component record in this worksheet |
| src-000373 | field-type | E3256 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000373 | field-type | E3257 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000373 | field-type | E3258 | YesNoIndicator | Not a component record in this worksheet |
| src-000373 | field-type | E3259 | YesNoIndicator | Not a component record in this worksheet |
| src-000373 | field-type | E3260 | YesNoIndicator | Not a component record in this worksheet |
| src-000373 | field-type | E3261 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000373 | field-type | E3262 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000373 | field-type | E3263 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000373 | field-type | E3264 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000376 | field-type | E5280 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000376 | field-type | E5281 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000376 | field-type | E5282 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E5283 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000376 | field-type | E5284 | ISODate | Not a component record in this worksheet |
| src-000376 | field-type | E5285 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000376 | field-type | E5286 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000376 | field-type | E5287 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000376 | field-type | E5288 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000376 | field-type | E5289 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000376 | field-type | E5290 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E5291 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E5292 | UndertakingNameCode | Not a component record in this worksheet |
| src-000376 | field-type | E5293 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000376 | field-type | E5294 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E5295 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E5296 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000376 | field-type | E5297 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E5298 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000376 | field-type | E5299 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000376 | field-type | E5300 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E5301 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E5302 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E5303 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000376 | field-type | E5304 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000376 | field-type | E5305 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000376 | field-type | E5306 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000379 | field-type | E3238 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000379 | field-type | E3239 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000379 | field-type | E3240 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E3241 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000379 | field-type | E3242 | ISODate | Not a component record in this worksheet |
| src-000379 | field-type | E3243 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000379 | field-type | E3244 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000379 | field-type | E3245 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000379 | field-type | E3246 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000379 | field-type | E3247 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000379 | field-type | E3248 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E3249 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E3250 | UndertakingNameCode | Not a component record in this worksheet |
| src-000379 | field-type | E3251 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000379 | field-type | E3252 | YesNoIndicator | Not a component record in this worksheet |
| src-000379 | field-type | E3253 | YesNoIndicator | Not a component record in this worksheet |
| src-000379 | field-type | E3254 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000379 | field-type | E3255 | YesNoIndicator | Not a component record in this worksheet |
| src-000379 | field-type | E3256 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000379 | field-type | E3257 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000379 | field-type | E3258 | YesNoIndicator | Not a component record in this worksheet |
| src-000379 | field-type | E3259 | YesNoIndicator | Not a component record in this worksheet |
| src-000379 | field-type | E3260 | YesNoIndicator | Not a component record in this worksheet |
| src-000379 | field-type | E3261 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000379 | field-type | E3262 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000379 | field-type | E3263 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000379 | field-type | E3264 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |
| src-000382 | field-type | E5249 | ElectronicSignature | [ElectronicSignature](bc-7cc3a7cf89765a8968f6.md) |
| src-000382 | field-type | E5250 | UndertakingStatus | [UndertakingStatus](bc-e682ac5852f12ad2a1af.md) |
| src-000382 | field-type | E5251 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E5252 | Demand | [Demand](bc-c95ff761f3e6a1538b6a.md) |
| src-000382 | field-type | E5253 | ISODate | Not a component record in this worksheet |
| src-000382 | field-type | E5254 | UndertakingAmount | [UndertakingAmount](bc-7de42cf89c22f1772376.md) |
| src-000382 | field-type | E5255 | Expiry | [Expiry](bc-801eb18844e1f0e6e1e5.md) |
| src-000382 | field-type | E5256 | UndertakingPartyRole | [UndertakingPartyRole](bc-9293566ddcc680ceacea.md) |
| src-000382 | field-type | E5257 | AmendmentOfUndertaking | [AmendmentOfUndertaking](bc-e9834d0f5ccc1992a967.md) |
| src-000382 | field-type | E5258 | UndertakingDocument | [UndertakingDocument](bc-27d9be33d2cff4924ef6.md) |
| src-000382 | field-type | E5259 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E5260 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E5261 | UndertakingNameCode | Not a component record in this worksheet |
| src-000382 | field-type | E5262 | ExternalUndertakingTypeCode | Not a component record in this worksheet |
| src-000382 | field-type | E5263 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E5264 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E5265 | ExternalTypeOfPartyCode | Not a component record in this worksheet |
| src-000382 | field-type | E5266 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E5267 | UnderlyingTransaction | [UnderlyingTransaction](bc-e6a975c53814274c0c25.md) |
| src-000382 | field-type | E5268 | ModelForm | [ModelForm](bc-39638db39b60076eecac.md) |
| src-000382 | field-type | E5269 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E5270 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E5271 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E5272 | AutomaticVariation | [AutomaticVariation](bc-d5e6f2e9c849eed63d0f.md) |
| src-000382 | field-type | E5273 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000382 | field-type | E5274 | Presentation | [Presentation](bc-67d3da67e0aca75bddd7.md) |
| src-000382 | field-type | E5275 | UndertakingExtension | [UndertakingExtension](bc-0b7fd2283fcb2ef5fe6d.md) |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](index.md) · [Known limitations and issues](../../../tracking/issues.md)
