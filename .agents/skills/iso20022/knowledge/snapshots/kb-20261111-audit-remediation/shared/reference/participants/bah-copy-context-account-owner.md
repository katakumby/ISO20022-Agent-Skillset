---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
participant_id: "bah-copy-context-account-owner"
aliases: ["account owner (CopyDuplicate1Code definitions)"]
source_ids: ["src-000011"]
source_edition: "March 2024"
source_locations: ["§2.4.10 p15; §2.4.14.10 p24; §3.2.1.3 p51"]
domains: ["shared"]
message_sets: ["business-application-header"]
message_ids: ["head.001.001.04"]
flows: []
limitations: ["Mentioned by code definitions; ownership relationship and responsibilities are not defined in this MDR.", "No equivalence to settlement AccountOwnerRole is established."]
source_editions: ["Version 4 March 2024"]
---

# Account owner in BAH copy-code definitions

The COPY and CODU definitions describe an information copy sent to a party other than the account owner. That is the complete supplied context for this role in these definitions; the MDR does not specify the account relationship, account identifier, institution class or owner actions. [src-000011](../../../evidence/omitted/b1a725a8c57af20c03e238c2.md), §2.4.10 p15; §2.4.14.10 p24; §3.2.1.3 p51.

This scoped mention is not merged with the settlement AccountOwnerRole merely because the label matches. The receiving information-copy party can occupy a [receiving messaging-endpoint role](bah-receiving-messaging-endpoint.md) for that message, but the source does not state that every original BAH receiver is an account owner. [Complete CopyDuplicate1Code table](../message-sets/business-application-header/march-2024/documents/src-000011/tables/tbl-0054.md).
