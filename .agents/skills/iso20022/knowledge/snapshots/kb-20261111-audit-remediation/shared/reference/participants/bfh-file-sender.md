---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
participant_id: "bfh-file-sender"
aliases: ["sender of the file", "sender"]
source_ids: ["src-000349"]
source_edition: "June 2024"
source_locations: ["§2.1 p4; §2.4.1.1.1–2 p6"]
domains: ["shared"]
message_sets: ["t2s-business-file-header"]
message_ids: ["head.002.001.01"]
flows: ["bfh-file-exchange"]
limitations: ["Source defines file roles and fields but no complete ordered business-process model."]
source_editions: ["june-2024"]
---

# File sender

## Definition and role scope

The participant that creates and delivers the file in the BFH exchange. It is scoped to file delivery, and is not automatically the BAH creator of every contained message. [src-000349](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.1 p4; §2.4.1.1.1–2 p6.

## Responsibilities and actions

Assigns the unique PayloadIdentifier and CreationDateAndTime. Supplies the file and its description, message types and processing information for the receiver. [src-000349](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.1 p4; §2.4.1.1.1–2 p6.

## Identifiers

PayloadIdentifier uniquely identifies the delivered file; it is not an institution identity. No mandatory sender identifier scheme is defined by this MDR. [src-000349](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.1 p4; §2.4.1.1.1–2 p6.

## Relationships and applicability

- [bfh-file-receiver](bfh-file-receiver.md).
- [bfh-service-provider](bfh-service-provider.md).
- [bfh-authorised-signatory](bfh-authorised-signatory.md).

No institution equivalence or automatic collapse into BAH participants is inferred.

## Flow and exact message

[File-exchange reference](../message-sets/t2s-business-file-header/june-2024/flows/file-exchange.md) · [Exact BFH business reference](../messages/head.002.001.01/business.md)
