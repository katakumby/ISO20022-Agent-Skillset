---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
flow_id: "flow-src-000343-p131-technical-processing"
title: "Resend request technical validation and routing"
domain: "shared"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_sets: ["t2s-administration"]
participant_ids: ["participant-src-000343-system-member", "participant-src-000343-system-transaction-administrator"]
participants: ["participant-src-000343-system-member", "participant-src-000343-system-transaction-administrator"]
message_ids: ["admi.006.001.01", "admi.007.001.01"]
source_locations: [{"source_id": "src-000343", "figure_id": "fig-0003", "locator": "direct-body paragraph P131", "xml_path": "/w:document/w:body/w:p[131]", "heading_path": ["BusinessProcess Description", "Resend Request"], "rendered_file_page": 16}]
limitations: ["These are source-defined technical processing activities, not additional institutional roles or universal ISO messaging requirements."]
---

# Resend request technical validation and routing

[src-000343](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`; direct-body paragraph P131.

## Purpose and trigger

Process a received resend request through schema checking, parsing, privilege and resend permission; return the result and duplicate where permitted.

## Participants and responsibilities

[System Member](../../../../participants/participant-src-000343-system-member.md) supplies or receives the A2A communication. [System Transaction Administrator](../../../../participants/participant-src-000343-system-transaction-administrator.md) is the source-defined central-system role. The module boxes are technical responsibilities inside that system; they are not separate institutions.

## Ordered activities, conditions and outcomes

[Complete step, condition and relationship inventory](../diagrams/administration-modules/fig-0003.md)

The diagrams preserve all positive, negative, queue, restart and permission paths actually drawn. A missing connector is not interpreted as a confirmed absence of operational behavior. The two parallel permission-success outputs are Validation result - resend and Resend message; the data stores supply resendable messages and permission-relevant static data.

## Preconditions and scope

The drawing states local branch guards. General authentication, access-right and header usage qualifications remain in [the administration business references](../diagrams/administration/index.md). No additional contractual precondition, cancellation/reversal operation or final business outcome is inferred.
