---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
participant_id: "bfh-service-provider"
aliases: ["service provider"]
source_ids: ["src-000349"]
source_edition: "June 2024"
source_locations: ["§2.4.1.2 p7"]
domains: ["shared"]
message_sets: ["t2s-business-file-header"]
message_ids: ["head.002.001.01"]
flows: ["bfh-file-exchange"]
limitations: ["Source defines file roles and fields but no complete ordered business-process model."]
source_editions: ["june-2024"]
---

# Provider requiring application-specific file information

## Definition and role scope

The service-context participant whose requirements determine necessary ApplicationSpecifics business information. The source does not equate this role with the system administrator or the sending/receiving institution. [src-000349](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.4.1.2 p7.

## Responsibilities and actions

Determines necessary service-specific business information in ApplicationSpecifics. The MDR does not list an independent sequence of provider actions. [src-000349](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.4.1.2 p7.

## Identifiers

No identifier scheme for the service provider is specified. [src-000349](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.4.1.2 p7.

## Relationships and applicability

- [bfh-file-sender](bfh-file-sender.md).
- [bfh-file-receiver](bfh-file-receiver.md).
- [bfh-authorised-signatory](bfh-authorised-signatory.md).

No institution equivalence or automatic collapse into BAH participants is inferred.

## Flow and exact message

[File-exchange reference](../message-sets/t2s-business-file-header/june-2024/flows/file-exchange.md) · [Exact BFH business reference](../messages/head.002.001.01/business.md)
