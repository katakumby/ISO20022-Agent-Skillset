---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "camt.042.001.04"
message_family: "camt.042"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.042.001.04"
source_ids: ["src-000096", "src-000105"]
source_editions: ["2025-2026", "May 2026"]
message_name: "FundDetailedEstimatedCashForecastReportV04"
business_area: "camt"
message_version: "04"
message_sets: ["investment-funds"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000096", "file_pages": [116, 125], "heading": "9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04"}]
---

# camt.042.001.04 — FundDetailedEstimatedCashForecastReportV04

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `FundDetailedEstimatedCashForecastReportV04`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | camt.042.001.04 | [src-000105](../../../../../raw-input/investment_funds/camt.042.001.04.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:camt.042.001.04 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Investment Funds | raw-input/investment_funds/camt.042.001.04.xsd |

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


<!-- FUNDS-EARLY-FLOW-331 -->
[Fund Cash Forecast Reporting / Detailed Estimated and Confirmed  / Detailed Estimated](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p331-detailed-estimated.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-331 -->

<!-- FUNDS-EARLY-FLOW-334 -->
[Fund Cash Forecast Reporting / Detailed Estimated and Confirmed  / Detailed Estimated and Confirmed](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p334-detailed-estimated-and-confirmed.md) — source95 Part1 flow at family/name level; exact structures remain separately scoped.
<!-- /FUNDS-EARLY-FLOW-334 -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
