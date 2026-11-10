---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
participant_id: "bfh-file-receiver"
aliases: ["receiving party", "two business applications (receiving side)"]
source_ids: ["src-000349"]
source_edition: "June 2024"
source_locations: ["§2.1 p4; §2.4.1.1.3 pp6–7; §2.4.1.2.3 p7"]
domains: ["shared"]
message_sets: ["t2s-business-file-header"]
message_ids: ["head.002.001.01"]
flows: ["bfh-file-exchange"]
limitations: ["Source defines file roles and fields but no complete ordered business-process model."]
source_editions: ["june-2024"]
---

# Receiving party in a file exchange

## Definition and role scope

The participant receiving a file and the BFH information needed to interpret its content and structure. This functional role does not determine the contained messages’ account-owner/servicer roles. [src-000349](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.1 p4; §2.4.1.1.3 pp6–7; §2.4.1.2.3 p7.

## Responsibilities and actions

Receives processing information such as total number of message instances. The duplicate flag indicates a possible duplicate of the file; no detailed receiver decision algorithm is specified here. [src-000349](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.1 p4; §2.4.1.1.3 pp6–7; §2.4.1.2.3 p7.

## Identifiers

No receiver identifier scheme is defined in the cited MDR. [src-000349](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.1 p4; §2.4.1.1.3 pp6–7; §2.4.1.2.3 p7.

## Relationships and applicability

- [bfh-file-sender](bfh-file-sender.md).
- [bfh-service-provider](bfh-service-provider.md).
- [bfh-authorised-signatory](bfh-authorised-signatory.md).

No institution equivalence or automatic collapse into BAH participants is inferred.

## Flow and exact message

[File-exchange reference](../message-sets/t2s-business-file-header/june-2024/flows/file-exchange.md) · [Exact BFH business reference](../messages/head.002.001.01/business.md)
