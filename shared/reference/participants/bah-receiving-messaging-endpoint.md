---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
participant_id: "bah-receiving-messaging-endpoint"
aliases: ["Receiving MessagingEndpoint", "To", "Business Application B (in MUG receiver scenarios)"]
source_ids: ["src-000011", "src-000012"]
source_locations: ["file/printed page 4 §2.1; page 11 §2.4.3; page 15 §2.4.11", "file/printed page 19 §2.10"]
domains: ["shared"]
message_sets: ["business-application-header"]
message_ids: ["head.001.001.04"]
flows: ["bah-business-message-exchange", "bah-character-set", "bah-business-service", "bah-market-practice", "bah-business-processing-date", "bah-copy", "bah-duplicate", "bah-duplicate-of-copy", "bah-possible-duplicate", "bah-priority", "bah-signed-message", "bah-related-message"]
limitations: ["Scoped functional role; no institutional equivalence inferred.", "Source guide diagram comparisons recorded; source/version discrepancies remain explicit."]
source_editions: ["Version 3.0 2021-11-03", "Version 4 March 2024"]
---

# Receiving MessagingEndpoint

## Definition and role scope

The endpoint designated by the sending endpoint as the ultimate processor of this Business Message. It is a functional recipient role, not a fixed type of institution.

## Responsibilities and actions

Processes the business message. In a possible-duplicate scenario, processes it as original only if the original was not received; otherwise takes action to avoid processing it again. Its transport receiving address may differ from this business identity.

## Identifiers

The To field uses Party51Choice with organisation/person or financial-institution identification. Particular identifiers depend on the chosen structure and implementation context (src-000011 pp11–13).

## Relationships and applicability

- [bah-sending-messaging-endpoint](bah-sending-messaging-endpoint.md).
- [bah-business-intermediary](bah-business-intermediary.md).
- [bah-technical-forwarder](bah-technical-forwarder.md).

The same real application or institution can occupy different roles in different exchanges. These records are scoped to BAH messaging and do not equate the roles with account owner, account servicer, bank, CSD or market infrastructure.

## Flows

- [bah-business-message-exchange](../message-sets/business-application-header/2021-11-03-v3.0/flows/business-message-exchange.md)
- [bah-character-set](../message-sets/business-application-header/2021-11-03-v3.0/flows/character-set.md)
- [bah-business-service](../message-sets/business-application-header/2021-11-03-v3.0/flows/business-service.md)
- [bah-market-practice](../message-sets/business-application-header/2021-11-03-v3.0/flows/market-practice.md)
- [bah-business-processing-date](../message-sets/business-application-header/2021-11-03-v3.0/flows/business-processing-date.md)
- [bah-copy](../message-sets/business-application-header/2021-11-03-v3.0/flows/copy.md)
- [bah-duplicate](../message-sets/business-application-header/2021-11-03-v3.0/flows/duplicate.md)
- [bah-duplicate-of-copy](../message-sets/business-application-header/2021-11-03-v3.0/flows/duplicate-of-copy.md)
- [bah-possible-duplicate](../message-sets/business-application-header/2021-11-03-v3.0/flows/possible-duplicate.md)
- [bah-priority](../message-sets/business-application-header/2021-11-03-v3.0/flows/priority.md)
- [bah-signed-message](../message-sets/business-application-header/2021-11-03-v3.0/flows/signed-message.md)
- [bah-related-message](../message-sets/business-application-header/2021-11-03-v3.0/flows/related-message.md)

## Evidence and limitations

- [src-000011](../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf), file/printed page 4 §2.1; page 11 §2.4.3; page 15 §2.4.11.
- [src-000012](../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf), file/printed page 19 §2.10.

Source labels are scoped aliases, not identity assertions about institutions. Diagram cross-checks are recorded in the MUG visual coverage; exact-version applicability and source direction discrepancies remain needs-review. [BAH and BFH context](../concepts/business-application-header-and-business-file-header.md).

## Reviewed source diagrams

[MUG diagram/table coverage and precise visual-review evidence](../message-sets/business-application-header/2021-11-03-v3.0/documents/src-000012/visual-coverage.md).
