---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "reda.005.001.03"
message_family: "reda.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.005.001.03"
source_ids: ["src-000096", "src-000112"]
source_editions: ["2025-2026", "May 2026"]
message_name: "InvestmentFundReportRequestV03"
business_area: "reda"
message_version: "03"
message_sets: ["investment-funds"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000096", "file_pages": [365, 370], "heading": "16 reda.005.001.03 InvestmentFundReportRequestV03"}]
---

# reda.005.001.03 — InvestmentFundReportRequestV03

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `InvestmentFundReportRequestV03`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | reda.005.001.03 | [src-000112](../../../../../raw-input/investment_funds/reda.005.001.03.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:reda.005.001.03 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Investment Funds | raw-input/investment_funds/reda.005.001.03.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/investment-funds/2025-2026/index.md)
- [Source extraction coverage](../../message-sets/investment-funds/2025-2026/coverage.md)
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


<!-- FUNDS-EARLY-FLOW-351 -->
[Fund Reference Data Reporting / Fund Reference Data Report – Solicited (requested)](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p351-fund-reference-data-report-solicited-requested.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-351 -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
