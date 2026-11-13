---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "auth.048.001.01"
message_family: "auth.048"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01"
source_ids: ["src-000321"]
source_locations: [{"source_id": "src-000321", "heading": "17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01", "file_pages": [247, 251]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["July 2025"]
---

# auth.048.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000321 — 17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01

[src-000321](../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md); file pp247–251; publication July 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000321, 17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01, Functionality, file p247.**

The MiFIRCurrencyCodeReport message provides the details the ISO 4217 currency codes and is
created by ESMA for distribution to National Competent Authorities.
Outline
The FinancialInstrumentReportingCurrencyCodeReportV01 MessageDefinition is composed of 2
MessageBuildingBlocks:
A. CurrencyData
Report all currencies and countries which use that currency.
B. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/fitrr/2025/documents/src-000321/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00203.md) | 247–247 |
| [17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01 / 17.3 Constraints](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00204.md) | 248–248 |
| [17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01 / 17.4 Message Building Blocks / 17.4.1 CurrencyData &lt;CcyData&gt; / 17.4.1.1 Currency &lt;Ccy&gt; / 17.4.1.1.1 Code &lt;Cd&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00205.md) | 249–249 |
| [17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01 / 17.4 Message Building Blocks / 17.4.1 CurrencyData &lt;CcyData&gt; / 17.4.1.5 Modification &lt;Mod&gt;](../../message-sets/fitrr/2025/documents/src-000321/sections/section-00206.md) | 250–251 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [APA](../../../../../shared/reference/participants/participant-src-000320-apa.md) | participant | src-000320 |
| [ARM](../../../../../shared/reference/participants/participant-src-000320-arm.md) | participant | src-000320 |
| [CA](../../../../../shared/reference/participants/participant-src-000320-ca.md) | participant | src-000320 |
| [Competent Authority](../../../../../shared/reference/participants/participant-src-000320-competent-authority.md) | participant | src-000320 |
| [CTP](../../../../../shared/reference/participants/participant-src-000320-ctp.md) | participant | src-000320 |
| [ESMA](../../../../../shared/reference/participants/participant-src-000320-esma.md) | participant | src-000320 |
| [IF](../../../../../shared/reference/participants/participant-src-000320-if.md) | participant | src-000320 |
| [MTF](../../../../../shared/reference/participants/participant-src-000320-mtf.md) | participant | src-000320 |
| [NCA](../../../../../shared/reference/participants/participant-src-000320-nca.md) | participant | src-000320 |
| [OTF](../../../../../shared/reference/participants/participant-src-000320-otf.md) | participant | src-000320 |
| [RE](../../../../../shared/reference/participants/participant-src-000320-re.md) | participant | src-000320 |
| [Relevant CA](../../../../../shared/reference/participants/participant-src-000320-relevant-ca.md) | participant | src-000320 |
| [Reporting Entity](../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md) | participant | src-000320 |
| [RM](../../../../../shared/reference/participants/participant-src-000320-rm.md) | participant | src-000320 |
| [SA](../../../../../shared/reference/participants/participant-src-000320-sa.md) | participant | src-000320 |
| [SI](../../../../../shared/reference/participants/participant-src-000320-si.md) | participant | src-000320 |
| [Supervisory Authority](../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md) | participant | src-000320 |
| [Reference Data](../../message-sets/fitrr/2025/flows/flow-src-000320-p127-reference-data.md) | business-flow | src-000320 |
| [Transparency Data](../../message-sets/fitrr/2025/flows/flow-src-000320-p131-transparency-data.md) | business-flow | src-000320 |
| [Trading Volume Cap](../../message-sets/fitrr/2025/flows/flow-src-000320-p135-trading-volume-cap.md) | business-flow | src-000320 |
| [Transaction Reporting Messages](../../message-sets/fitrr/2025/flows/flow-src-000320-p137-transaction-reporting-messages.md) | business-flow | src-000320 |
| [Reference Data Submission](../../message-sets/fitrr/2025/flows/flow-src-000320-p144-reference-data-submission.md) | business-flow | src-000320 |
| [Reference Data Distribution](../../message-sets/fitrr/2025/flows/flow-src-000320-p146-reference-data-distribution.md) | business-flow | src-000320 |
| [Non-Working Days](../../message-sets/fitrr/2025/flows/flow-src-000320-p148-non-working-days.md) | business-flow | src-000320 |
| [Missing / Incomplete Data Submission](../../message-sets/fitrr/2025/flows/flow-src-000320-p150-missing-incomplete-data-submission.md) | business-flow | src-000320 |
| [MiFIR specific additional Reference Data](../../message-sets/fitrr/2025/flows/flow-src-000320-p153-mi-fir-specific-additional-reference-data.md) | business-flow | src-000320 |
| [Transparency Trading Activity](../../message-sets/fitrr/2025/flows/flow-src-000320-p155-transparency-trading-activity.md) | business-flow | src-000320 |
| [Transparency Result Data](../../message-sets/fitrr/2025/flows/flow-src-000320-p157-transparency-result-data.md) | business-flow | src-000320 |
| [Trading Volume Cap](../../message-sets/fitrr/2025/flows/flow-src-000320-p159-trading-volume-cap.md) | business-flow | src-000320 |
| [Financial Instrument Transaction Report](../../message-sets/fitrr/2025/flows/flow-src-000320-p162-financial-instrument-transaction-report.md) | business-flow | src-000320 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)



<!-- FITRR-SEQUENCES -->
## Related FITRR business flows

- [Reference data distribution](../../message-sets/fitrr/2025/flows/flow-src-000320-p198-data-distribution-business-transaction.md) · [source sequence](../../message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0023.md)

These links use source-supported family context; exact-version applicability is separately documented in the message evidence.
