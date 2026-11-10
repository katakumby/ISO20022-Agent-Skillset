---
template: false
document_kind: "message-business-context"
review_status: "needs-review"
title: "sese.023.001.13 business context"
domain: "securities"
source_ids: ["src-000196", "src-000197", "src-000198"]
source_editions: ["2025-2026", "March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.023.001.13"
participant_ids: ["participant-settlement-reconciliation-account-owner", "participant-settlement-reconciliation-account-servicer", "participant-settlement-reconciliation-instructing-party", "participant-settlement-reconciliation-executing-servicing-party"]
flow_ids: ["flow-settlement-reconciliation-instruction-confirmation", "flow-settlement-reconciliation-partial-settlement", "flow-settlement-reconciliation-cancellation-request", "flow-settlement-reconciliation-cancellation-advice", "flow-settlement-reconciliation-reversal-advice", "flow-settlement-reconciliation-reporting-push", "flow-settlement-reconciliation-reporting-pull", "flow-settlement-reconciliation-portfolio-transfer", "flow-settlement-reconciliation-transaction-generation"]
limitations: ["Part1 §7.16 heading uses .13 but example prose/XML uses .07.", "Part1 formal executing/servicing definition is truncated.", "Full table, figure and rule visual review remains required."]
---

# sese.023.001.13 business context

## Purpose and usage

An account owner sends this instruction to an account servicer to instruct receipt or delivery of financial instruments, with/without payment, physically or by book-entry. It can link settlement instructions for turnaround/back-to-back processing or other transactions such as an FX deal. Relevant Business Application Header elements support resending, information copies to a third party, and resending copies. **Evidence:** [src-000197](<../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf>), §17.1, file/printed p491.

## Roles and institutional relationships

- [account owner](<../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md>)
- [account servicer](<../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md>)
- [instructing party](<../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md>)
- [executing servicing party](<../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md>)

Source examples involve global/local custodians, investment management institutions with fund accounts at custodians, brokers with custodian accounts, CSD participants, CSDs with other servicing institutions, and CCPs/stock exchanges/trade matching utilities instructing a CSD or settlement market infrastructure. These are contextual examples, not fixed institution-to-role mappings. Evidence: src-000197, §17.1 p491.

## Shared context and flows

[Message-set participants](<../../message-sets/settlement-and-reconciliation/2025-2026/participants.md>) · [Reusable flows](<../../message-sets/settlement-and-reconciliation/2025-2026/flows/index.md>) · [Pilot source diagrams](<../../message-sets/settlement-and-reconciliation/2025-2026/diagrams/pilot/index.md>)

## Business constraints and schema

[80 source MDR constraints](<rules-business.md>) · [Exact .13 schema structure](<structure.md>)

MDR Part1 §2.3 paragraph151 requires head.001 BAH. It does not specify the separately supplied BAH version. Keep BAH-version selection explicit and do not substitute Business File Header for BAH.

## Version and source limitations

Part1 §7.16 heading (paragraph1730) identifies .13, but paragraph1732 and accompanying XML identify .07. This historical example is not a .13 validation example. Part2 §17 and the supplied .13 namespace establish the exact definition documented here.

Source cancellation routing also conflicts: §5.13 paragraph308 points to instruction-status reporting for an instruction cancelled by servicer/third party; §6.13 paragraph619 points to reversal advice. See [the preserved conflict](<../../message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-advice.md>).

Tracked issues: [issue-000005, issue-000006, issue-000007, issue-000013](<../../../../../tracking/issues.md>).

[Reviewed XSD-derived top-level structure](diagrams/fig-0001.md).
