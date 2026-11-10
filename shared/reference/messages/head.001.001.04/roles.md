---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "head.001.001.04 participant and direction evidence"
domain: "shared"
message_id: "head.001.001.04"
message_family: "head.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:head.001.001.04"
source_ids: ["src-000011", "src-000013"]
message_sets: ["business-application-header"]
role_labels: ["sending MessagingEndpoint"]
search_terms: ["sending MessagingEndpoint"]
participant_ids: ["bah-sending-messaging-endpoint"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000011", "heading": "2 head.001.001.04 BusinessApplicationHeaderV04", "file_pages": [4, 25]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# head.001.001.04 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 1 uniquely resolved participant references.

## src-000011 — 2 head.001.001.04 BusinessApplicationHeaderV04

[src-000011](../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf); Functionality file pp4, 5, 6; publication Version 4 March 2024.

### Direction and initiation clauses

#### src-000011-head.001.001.04-p4-c001-d1

Kind: creator; message applicability: **business-message-with-accompanying-header**; src-000011 file p4, scope.

- Creator: **sending MessagingEndpoint**. [sending MessagingEndpoint](../../participants/bah-sending-messaging-endpoint.md).

> A single new Business Message (with its accompagnying business application header) is created - by the sending MessagingEndpoint - for each business event; that is each interaction in a Business Transaction.

The source creates a Business Message with its accompanying BAH for each business event. This is not a fixed sender/receiver pair for every header use.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000011-head.001.001.04-p4-c001 — file p4, scope.**

Mentioned roles: [sending MessagingEndpoint](../../participants/bah-sending-messaging-endpoint.md).

Literal actions: sending MessagingEndpoint created.

Reviewed clause disposition: **source-explicit-role-assertion**. Exact source Functionality was read. The retained role kind distinguishes creation/distribution/action from wire-message direction.

Quoted above in src-000011-head.001.001.04-p4-c001-d1.

**src-000011-head.001.001.04-p4-c002 — file p4, scope.**

> Each instance of a Business Actor has one Name.

**src-000011-head.001.001.04-p4-c003 — file p4, scope.**

> The Business Actor must not be referred to in the Transport Layer.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p4, scope.**

> The Business Layer deals with Business Messages.

**File p4, scope.**

> The behaviour of the Business Messages is fully described by the Business Transaction and the structure of the Business Messages is fully described by the Message Definitions and related Message Rules, Rules and Market Practices.

**File p4, scope.**

> All of which are registered in the ISO 20022 Repository.

**File p4, scope.**

> A Business Message adheres to the following principles: " A Business Message (and its business application header) must not contain information about the Message Transport System or the mechanics or mechanism of message sending, transportation, or receipt. " A Business Message must be comprehensible outside of the context of the Transport Message.

**File p4, scope.**

> That is the Business Message must not require knowledge of the Transport Message to be understood. " A Business Message may contain headers, footers, and envelopes that are meaningful for the business.

**File p4, scope.**

> When present, they are treated as any other message content, which means that they are considered part of the Message Definition of the Business Message and as such will be part of the ISO 20022 Repository. " A Business Message refers to Business Actors by their Name.

**File p4, scope.**

> Specific usage of this BusinessMessageHeader may be defined by the relevant SEG.

Functionality role scope was directly reviewed on 2026-11-09. No unstated sender/receiver is manufactured. Header composition, creation/distribution, source wording defects and action-only evidence remain distinct; curated Part1 flow evidence may supply broader context.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Curated message context](business.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../tracking/issues.md)
