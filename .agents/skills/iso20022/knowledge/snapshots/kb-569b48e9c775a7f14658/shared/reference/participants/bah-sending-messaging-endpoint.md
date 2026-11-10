---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
participant_id: "bah-sending-messaging-endpoint"
aliases: ["Sending MessagingEndpoint", "From", "Business Application A (in MUG sender scenarios)"]
source_ids: ["src-000011", "src-000012"]
source_locations: ["file/printed page 4 §2.1; page 5 §2.1 D; page 9 §2.4.2", "file/printed pages 9–11 §2.2"]
domains: ["shared"]
message_sets: ["business-application-header"]
message_ids: ["head.001.001.04"]
flows: ["bah-business-message-exchange", "bah-character-set", "bah-business-service", "bah-market-practice", "bah-business-processing-date", "bah-copy", "bah-duplicate", "bah-duplicate-of-copy", "bah-possible-duplicate", "bah-priority", "bah-signed-message", "bah-related-message"]
limitations: ["Scoped functional role; no institutional equivalence inferred.", "Source guide diagram comparisons recorded; source/version discrepancies remain explicit."]
source_editions: ["Version 3.0 2021-11-03", "Version 4 March 2024"]
---

# Sending MessagingEndpoint

## Definition and role scope

The endpoint that creates this Business Message for a receiving endpoint that will process it. This is a functional role for a particular message, not an institution class.

## Responsibilities and actions

Creates a new Business Message and accompanying BAH for each business event. Identifies its business recipient in To. The transport sending address may differ. Its BusinessMessageIdentifier identifies the message unambiguously to its creator.

## Identifiers

The From field uses Party51Choice: organisation/person identification or financial-institution identification. BICFI, clearing-system member identification, LEI and other identifiers are optional choices within the selected structures; none is a universal identity requirement for this role (src-000011 pp9–11).

## Relationships and applicability

- [bah-receiving-messaging-endpoint](bah-receiving-messaging-endpoint.md).
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

- [src-000011](../../../evidence/omitted/b1a725a8c57af20c03e238c2.md), file/printed page 4 §2.1; page 5 §2.1 D; page 9 §2.4.2.
- [src-000012](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), file/printed pages 9–11 §2.2.

Source labels are scoped aliases, not identity assertions about institutions. Diagram cross-checks are recorded in the MUG visual coverage; exact-version applicability and source direction discrepancies remain needs-review. [BAH and BFH context](../concepts/business-application-header-and-business-file-header.md).

## Human operator in the source narrative

The guide expressly interprets BusinessApplication broadly: it may be a payment factory or an operator entering business information. Its John Doe / Bank A example has the same person prepare payments, create the activity report at 09:00 UTC and sign at 09:50 UTC. This example supports a human-operated endpoint; it does not make every endpoint a person or assert that every sender is the authorised signatory. [§2.2 p11](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012). [Complete annotated example](../message-sets/business-application-header/2021-11-03-v3.0/documents/src-000012/examples/creation-date-example.md).

## Reviewed source diagrams

[MUG diagram/table coverage and precise visual-review evidence](../message-sets/business-application-header/2021-11-03-v3.0/documents/src-000012/visual-coverage.md).
