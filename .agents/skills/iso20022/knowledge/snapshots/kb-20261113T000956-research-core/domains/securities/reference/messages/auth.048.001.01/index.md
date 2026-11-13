---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "auth.048.001.01"
message_family: "auth.048"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.048.001.01"
source_ids: ["src-000321", "src-000338"]
source_editions: ["2025", "July 2025"]
message_name: "FinancialInstrumentReportingCurrencyCodeReportV01"
business_area: "auth"
message_version: "01"
message_sets: ["fitrr"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000321", "file_pages": [247, 251], "heading": "17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01"}]
---

# auth.048.001.01 — FinancialInstrumentReportingCurrencyCodeReportV01

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `FinancialInstrumentReportingCurrencyCodeReportV01`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | auth.048.001.01 | [src-000338](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/auth.048.001.01.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:auth.048.001.01 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Transactions and Financial Instruments Data Reporting | raw-input/transactions_and_financial_instruments_data_reporting_fitrr/auth.048.001.01.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/fitrr/2025/index.md)
- [Source extraction coverage](../../message-sets/fitrr/2025/coverage.md)
- [Shared participants](../../../../../catalog/participants.md)
- [Business flows](../../../../../catalog/flows.md)
- [Source identities and original occurrences](../../../../../tracking/source-register.md)
- [Known gaps and review requirements](../../../../../tracking/issues.md)

## Review

Complete supplied schema declarations have focused pages with literal XML, qualified references and nested paths. Automated schema compilation: **pass**. Extraction is **needs-review**; this does not claim that source documentation, tables or diagrams have passed visual review.


<!-- MDR-NAV-START -->
## Supplied business evidence

[Purpose, usage, actors and detailed MDR evidence](mdr-evidence.md)
<!-- MDR-NAV-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
