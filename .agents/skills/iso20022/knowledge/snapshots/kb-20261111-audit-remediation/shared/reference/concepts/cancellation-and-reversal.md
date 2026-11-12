---
template: false
document_kind: concept
review_status: needs-review
concept_id: concept-securities-cancellation-and-reversal
title: Cancellation requests, message cancellations and reversals
domain: securities
domains: [securities]
message_sets: [settlement-and-reconciliation, corporate-actions]
message_ids: [sese.020.001.09, sese.026.001.12, semt.020.001.07, seev.037.001.17, seev.044.001.13]
source_ids: [src-000196, src-000197, src-000079, src-000080]
source_editions: ["Maintenance 2025 - 2026"]
search_terms: [cancellation request, settlement reversal, corporate action movement reversal, reversal pre-advice, account owner, account servicer]
limitations: ["Part1 and Part2 cancellation-advice statements conflict; issue-000013 remains open.", "This is a curated comparison of supplied definitions, not a rule for unsupplied message versions."]
---

# Cancellation requests, message cancellations and reversals

The object being cancelled or reversed, its lifecycle state, and the sender/receiver direction determine which supplied definition applies. The following comparison is a derived retrieval aid; its factual entries cite the supplied source definitions.

| Intent | Supplied definition | Sender → receiver | Source-defined scope and evidence |
| --- | --- | --- | --- |
| Request cancellation of a securities transaction | [sese.020.001.09](../../../domains/securities/reference/messages/sese.020.001.09/index.md) | Account owner → account servicer | Request cancellation of a settlement transaction, intra-position movement or securities financing transaction. Part1 describes an open transaction for which cancellation is possible; request submission is not completion. src-000197 §14.1 p458; src-000196 §4 table19 and §6.12 P608–P612. [Exact MDR evidence](../../../domains/securities/reference/messages/sese.020.001.09/mdr-evidence.md). |
| Reverse a settlement confirmation | [sese.026.001.12](../../../domains/securities/reference/messages/sese.026.001.12/index.md) | Account servicer → account owner | Reverse confirmation of a partial or full delivery/receipt, free/against payment, physically/by book-entry. Part1 says the underlying instruction remains in settlement processing and the owner receives statuses and confirmations. src-000197 §20.1 p654; src-000196 §4 table22 and §6.14 P625. [Exact MDR evidence](../../../domains/securities/reference/messages/sese.026.001.12/mdr-evidence.md). |
| Cancel a previously sent securities message | [semt.020.001.07](../../../domains/securities/reference/messages/semt.020.001.07/index.md) | Account servicer → account owner | Cancel a prior message of the types allowed in §11.1. The exact definition expressly excludes **all status-advice messages**: send a new status advice with the correct status instead. src-000197 §11.1 p406. This differs from broader Part1 examples; see the conflict below. [Exact MDR evidence](../../../domains/securities/reference/messages/semt.020.001.07/mdr-evidence.md). |
| Reverse confirmed corporate-action cash/securities postings | [seev.037.001.17](../../../domains/securities/reference/messages/seev.037.001.17/index.md) | Account servicer → account owner or designated agent | Reverse a previously confirmed posting. Part1 process definition permits only full movement reversal and requires a previous movement confirmation. src-000080 §9.1 p665; src-000079 §4 table17. [Exact MDR evidence](../../../domains/securities/reference/messages/seev.037.001.17/mdr-evidence.md). |
| Cancel a previously announced corporate-action preliminary advice | [seev.044.001.13](../../../domains/securities/reference/messages/seev.044.001.13/index.md) | Account servicer → account owner or designated agent | Cancel CorporateActionMovementPreliminaryAdvice. In the reversal-pre-advice scenario, use this cancellation when announced movements will not actually be reversed. src-000080 §15.1 p813; src-000079 §6 Confirmation and Reversal / Reversal Pre-Advice Cancellation, P278–P279. [Exact MDR evidence](../../../domains/securities/reference/messages/seev.044.001.13/mdr-evidence.md). |

## Corporate-action reversal sequence

After the account servicer has confirmed movements, it may optionally pre-advise their reversal using CorporateActionMovementPreliminaryAdvice. It must also send CorporateActionMovementReversalAdvice to confirm the reversal has been carried out. The reason may be stated. If the movements will not be reversed, the servicer cancels the reversal preliminary advice. An announced reversal therefore does not itself prove that a posting was reversed. Evidence: src-000079, BusinessTransactions / Confirmation and Reversal, [Reversal P272–P273](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000079/sections/section-0050.md) and [Reversal Pre-Advice Cancellation P278–P279](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000079/sections/section-0051.md).

The corporate-action process definition includes calculation/rate changes, tax updates that alter confirmed distributions, and calculation errors as triggers. Its preconditions include reversal of the cash/securities postings in the owner's accounts. [Complete table17](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000079/tables/tbl-0017.md), src-000079 §4, rows2–6. This process context is distinct from putting a confirmed settlement transaction back into open status.

## Conflicting cancellation-advice evidence

src-000196 Part1 §5.13 table46 and §6.13 P620 include cancellation of a status advice among the examples. src-000197 Part2 §11.1 p406 explicitly prohibits this for semt.020.001.07 and requires a corrected status advice. These source claims are retained separately. In addition, Part1 §5.13 P308 routes an instruction cancelled by a servicer/third party to instruction-status reporting, while §6.13 P619 points to reversal advice. [issue-000013](../../../tracking/issues.md) remains open. Do not treat the broad Part1 sequence label “AnyAdviceOrAnyStatement” as unrestricted permission in the exact .07 definition.

## Related flows and scoped participants

- [Settlement cancellation request](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-request.md)
- [Settlement reversal](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/reversal-advice.md)
- [Message cancellation advice and its source conflicts](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-advice.md)
- [Corporate-action movement reversal process](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/flows/flow-src-000079-p153-movement-reversal.md)
- [Settlement account owner](../participants/settlement-reconciliation-account-owner.md) and [account servicer](../participants/settlement-reconciliation-account-servicer.md)
- [Corporate-action account owner](../participants/participant-src-000079-account-owner.md) and [account servicer](../participants/participant-src-000079-account-servicer.md)

Role labels are contextual. This comparison does not merge the two message sets' participant definitions or equate either functional role with one institution type.
