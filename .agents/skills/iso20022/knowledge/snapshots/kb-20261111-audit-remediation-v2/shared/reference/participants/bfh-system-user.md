---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
participant_id: "bfh-system-user"
aliases: ["SystemUser", "SysUsr"]
source_ids: ["src-000349"]
source_locations: ["file/printed page 7 §2.4.1.2.1 SystemUser"]
domains: ["shared"]
message_sets: ["t2s-business-file-header"]
message_ids: ["head.002.001.01"]
flows: ["bfh-file-exchange"]
limitations: ["Scoped functional role; no institutional equivalence inferred.", "All supplied BFH MDR pages inspected; no substantive source diagrams."]
source_editions: ["june-2024"]
---

# Business File Header system user

## Definition and role scope

A user account defined in static data. It represents an individual or application interacting with a system administrator such as T2S. It is a functional access role, not an institution.

## Responsibilities and actions

Triggers available functions. Available functions follow the privileges granted to that user. The administrator provides no attribute distinguishing individuals from applications.

## Identifiers

SystemUser is optional Max140Text within optional ApplicationSpecifics; the source defines a static-data account but no globally unique identifier scheme.

## Relationships and applicability

[bfh-system-administrator](bfh-system-administrator.md). The supplied BFH context is T2S; equivalence to unrelated roles is not established.

## Flows

No separate ordered BFH business flow is defined by the cited SystemUser section.

## Evidence and limitations

- [src-000349](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf, file/printed page 7 §2.4.1.2.1 SystemUser.

Source labels are scoped aliases, not identity assertions about institutions. All BFH MDR pages and tables have visual-review evidence; the source provides no detailed ordered process for this role. [BAH and BFH context](../concepts/business-application-header-and-business-file-header.md).

## Related file context

[File-exchange context, with derived ordering explicitly qualified](../message-sets/t2s-business-file-header/june-2024/flows/file-exchange.md).
