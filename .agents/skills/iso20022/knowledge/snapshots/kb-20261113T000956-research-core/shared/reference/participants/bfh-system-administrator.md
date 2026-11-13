---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
participant_id: "bfh-system-administrator"
aliases: ["System administrator"]
source_ids: ["src-000349"]
source_locations: ["file/printed page 7 §2.4.1.2.1 SystemUser"]
domains: ["shared"]
message_sets: ["t2s-business-file-header"]
message_ids: ["head.002.001.01"]
flows: ["bfh-file-exchange"]
limitations: ["Scoped functional role; no institutional equivalence inferred.", "All supplied BFH MDR pages inspected; no substantive source diagrams."]
source_editions: ["june-2024"]
---

# Business File Header system administrator

## Definition and role scope

The system with which a system user interacts in the SystemUser definition. T2S is given as an example. This scoped role is not equated with an account servicer or any other institution role.

## Responsibilities and actions

Exposes functions that system users trigger according to the privileges for which they are grantees. The supplied SystemUser definition states no attribute distinguishing human users from applications.

## Identifiers

No identifier scheme for this role is defined in the cited section.

## Relationships and applicability

[bfh-system-user](bfh-system-user.md). The supplied BFH context is T2S; equivalence to unrelated roles is not established.

## Flows

No separate ordered BFH business flow is defined by the cited SystemUser section.

## Evidence and limitations

- [src-000349](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf, file/printed page 7 §2.4.1.2.1 SystemUser.

Source labels are scoped aliases, not identity assertions about institutions. All BFH MDR pages and tables have visual-review evidence; the source provides no detailed ordered process for this role. [BAH and BFH context](../concepts/business-application-header-and-business-file-header.md).

## Related file context

[File-exchange context, with derived ordering explicitly qualified](../message-sets/t2s-business-file-header/june-2024/flows/file-exchange.md).
