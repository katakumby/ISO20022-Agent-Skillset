---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
participant_id: "bfh-authorised-signatory"
aliases: ["Business Entity authorised to sign this Business File"]
source_ids: ["src-000349"]
source_edition: "June 2024"
source_locations: ["§2.3 C1 p5; §2.4.1.2.2 p7"]
domains: ["shared"]
message_sets: ["t2s-business-file-header"]
message_ids: ["head.002.001.01"]
flows: ["bfh-file-exchange"]
limitations: ["Source defines file roles and fields but no complete ordered business-process model."]
source_editions: ["june-2024"]
---

# Business entity authorised to sign a Business File

## Definition and role scope

The business entity authorised to sign the Business File. This file-signing role is kept distinct from the BAH-message signing role because this publication does not assert equivalence. [src-000349](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.3 C1 p5; §2.4.1.2.2 p7.

## Responsibilities and actions

Its digital signature may be included in optional ApplicationSpecifics/Signature. MDR C1 permits only the XML Signature root element. The MDR does not define who grants signing authority or a signature-verification business flow. [src-000349](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.3 C1 p5; §2.4.1.2.2 p7.

## Identifiers

No signatory identifier scheme is prescribed in the BFH MDR. The signature schema standard is referenced; it is not an institutional identification scheme. [src-000349](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.3 C1 p5; §2.4.1.2.2 p7.

## Relationships and applicability

- [bfh-file-sender](bfh-file-sender.md).
- [bfh-file-receiver](bfh-file-receiver.md).
- [bfh-service-provider](bfh-service-provider.md).

No institution equivalence or automatic collapse into BAH participants is inferred.

## Flow and exact message

[File-exchange reference](../message-sets/t2s-business-file-header/june-2024/flows/file-exchange.md) · [Exact BFH business reference](../messages/head.002.001.01/business.md)
