---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "semt.007.001.02"
message_family: "semt.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.007.001.02"
source_ids: ["src-000096", "src-000119"]
source_editions: ["2025-2026", "May 2026"]
message_name: "StatementOfInvestmentFundTransactionsCancellationV02"
business_area: "semt"
message_version: "02"
message_sets: ["investment-funds"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000096", "file_pages": [427, 432], "heading": "23 semt.007.001.02 StatementOfInvestmentFundTransactionsCancellationV02"}]
---

# semt.007.001.02 — StatementOfInvestmentFundTransactionsCancellationV02

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `StatementOfInvestmentFundTransactionsCancellationV02`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | semt.007.001.02 | [src-000119](../../../../../raw-input/investment_funds/semt.007.001.02.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:semt.007.001.02 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Investment Funds | raw-input/investment_funds/semt.007.001.02.xsd |

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


<!-- FUNDS-FLOW-0141-START -->
[Investment fund transaction statement cancellation](../../message-sets/investment-funds/2025-2026/flows/flow-src-000095-p951-statement-of-investment-fund-transactions-cancellation.md) — source-supported business flow and participant directions.
<!-- FUNDS-FLOW-0141-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
