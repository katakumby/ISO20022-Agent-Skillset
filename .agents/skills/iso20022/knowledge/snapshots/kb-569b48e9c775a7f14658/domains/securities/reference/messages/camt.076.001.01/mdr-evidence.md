---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "camt.076.001.01"
message_family: "camt.076"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.076.001.01"
source_ids: ["src-000233", "src-000346"]
source_locations: [{"source_id": "src-000233", "heading": "14 camt.076.001.01 BillingReportRequestV01", "file_pages": [233, 239]}, {"source_id": "src-000346", "heading": "2 camt.076.001.01 BillingReportRequestV01", "file_pages": [4, 10]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["August 2026", "december-2025"]
---

# camt.076.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000233 — 14 camt.076.001.01 BillingReportRequestV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); file pp233–239; publication August 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000233, 14 camt.076.001.01 BillingReportRequestV01, Functionality, file p233.**

The BillingReportRequest message is sent by the system member to the system transaction
administrator to request cumulative or itemised billing data. The billing data may be cumulative
information or aggregated information on the level of a single securities or a dedicated cash account
within a given period for each service item.
Outline
The BillingReportRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Defines the characteristics specific to the message, such as the identification or the creation date
and time.
B. SearchCriteria
Defines the criteria to be used to extract the billing data.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.076.001.01 BillingReportRequestV01
Target2-Securities 233 August 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s/august-2026/documents/src-000233/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [14 camt.076.001.01 BillingReportRequestV01](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00180.md) | 233–233 |
| [14 camt.076.001.01 BillingReportRequestV01 / 14.2 Structure](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00181.md) | 234–234 |
| [14 camt.076.001.01 BillingReportRequestV01 / 14.4 Message Building Blocks](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00182.md) | 235–235 |
| [14 camt.076.001.01 BillingReportRequestV01 / 14.4 Message Building Blocks / 14.4.2 SearchCriteria &lt;SchCrit&gt; / 14.4.2.1 Service &lt;Svc&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00183.md) | 236–236 |
| [14 camt.076.001.01 BillingReportRequestV01 / 14.4 Message Building Blocks / 14.4.2 SearchCriteria &lt;SchCrit&gt; / 14.4.2.2 BillingIdentification &lt;BllgId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00184.md) | 237–237 |
| [14 camt.076.001.01 BillingReportRequestV01 / 14.4 Message Building Blocks / 14.4.2 SearchCriteria &lt;SchCrit&gt; / 14.4.2.6 AccountIdentification &lt;AcctId&gt;](../../message-sets/t2s/august-2026/documents/src-000233/sections/section-00185.md) | 238–239 |

## src-000346 — 2 camt.076.001.01 BillingReportRequestV01

[src-000346](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`; file pp4–10; publication december-2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000346, 2 camt.076.001.01 BillingReportRequestV01, Functionality, file p4.**

The BillingReportRequest message is sent by the system member to the system transaction
administrator to request cumulative or itemised billing data. The billing data may be cumulative
information or aggregated information on the level of a single securities or a dedicated cash account
within a given period for each service item.
Outline
The BillingReportRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Defines the characteristics specific to the message, such as the identification or the creation date
and time.
B. SearchCriteria
Defines the criteria to be used to extract the billing data.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.076.001.01 BillingReportRequestV01
Target2-Securities - Billing 4 December 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/t2s-billing/december-2025/documents/src-000346/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 camt.076.001.01 BillingReportRequestV01](../../message-sets/t2s-billing/december-2025/documents/src-000346/sections/section-00004.md) | 4–4 |
| [2 camt.076.001.01 BillingReportRequestV01 / 2.2 Structure](../../message-sets/t2s-billing/december-2025/documents/src-000346/sections/section-00005.md) | 5–5 |
| [2 camt.076.001.01 BillingReportRequestV01 / 2.4 Message Building Blocks](../../message-sets/t2s-billing/december-2025/documents/src-000346/sections/section-00006.md) | 6–6 |
| [2 camt.076.001.01 BillingReportRequestV01 / 2.4 Message Building Blocks / 2.4.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.1 Service &lt;Svc&gt;](../../message-sets/t2s-billing/december-2025/documents/src-000346/sections/section-00007.md) | 7–7 |
| [2 camt.076.001.01 BillingReportRequestV01 / 2.4 Message Building Blocks / 2.4.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.2 BillingIdentification &lt;BllgId&gt;](../../message-sets/t2s-billing/december-2025/documents/src-000346/sections/section-00008.md) | 8–8 |
| [2 camt.076.001.01 BillingReportRequestV01 / 2.4 Message Building Blocks / 2.4.2 SearchCriteria &lt;SchCrit&gt; / 2.4.2.6 AccountIdentification &lt;AcctId&gt;](../../message-sets/t2s-billing/december-2025/documents/src-000346/sections/section-00009.md) | 9–10 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Account Owner](../../../../../shared/reference/participants/participant-src-000347-account-owner.md) | participant | src-000347 |
| [Account Servicer](../../../../../shared/reference/participants/participant-src-000347-account-servicer.md) | participant | src-000347 |
| [Central Database System](../../../../../shared/reference/participants/participant-src-000347-central-database-system.md) | participant | src-000347 |
| [Central Securities Depository (CSD)](../../../../../shared/reference/participants/participant-src-000347-central-securities-depository-csd.md) | participant | src-000347 |
| [Central Security Depository (CSD)](../../../../../shared/reference/participants/participant-src-000347-central-security-depository-csd.md) | participant | src-000347 |
| [Collateral Management System](../../../../../shared/reference/participants/participant-src-000347-collateral-management-system.md) | participant | src-000347 |
| [Executing / Servicing Party](../../../../../shared/reference/participants/participant-src-000347-executing-servicing-party.md) | participant | src-000347 |
| [Instructing Party](../../../../../shared/reference/participants/participant-src-000347-instructing-party.md) | participant | src-000347 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000347-market-infrastructure.md) | participant | src-000347 |
| [National Central Bank](../../../../../shared/reference/participants/participant-src-000347-national-central-bank.md) | participant | src-000347 |
| [Payment Bank](../../../../../shared/reference/participants/participant-src-000347-payment-bank.md) | participant | src-000347 |
| [Billing Report](../../message-sets/t2s-billing/december-2025/flows/flow-src-000347-p110-billing-report.md) | business-flow | src-000347 |
| [Query Billing Information](../../message-sets/t2s-billing/december-2025/flows/flow-src-000347-p116-query-billing-information.md) | business-flow | src-000347 |
| [Billing Report](../../message-sets/t2s-billing/december-2025/flows/flow-src-000347-p121-billing-report.md) | business-flow | src-000347 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
