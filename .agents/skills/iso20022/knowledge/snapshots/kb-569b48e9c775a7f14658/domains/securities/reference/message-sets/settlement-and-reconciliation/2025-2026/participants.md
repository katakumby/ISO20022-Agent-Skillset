---
template: false
document_kind: "participant-index"
review_status: "needs-review"
title: "Settlement and Reconciliation participants"
domain: "securities"
source_ids: ["src-000196", "src-000198", "src-000197"]
source_editions: ["2025-2026", "March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-09"
---

# Settlement and Reconciliation participants

## Canonical scoped records

- [Account owner](../../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md) — functional account role
- [Account servicer](../../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md) — functional account role
- [Instructing party](../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md) — functional participant role
- [Executing/servicing party](../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md) — functional participant role
- [Third party in securities reporting](../../../../../../shared/reference/participants/settlement-reconciliation-reporting-third-party.md) — functional participant role
- [Portfolio transfer client](../../../../../../shared/reference/participants/settlement-reconciliation-portfolio-transfer-client.md) — functional participant role
- [Global Settlement Agent](../../../../../../shared/reference/participants/settlement-reconciliation-global-settlement-agent.md) — business role
- [Local Settlement Agent](../../../../../../shared/reference/participants/settlement-reconciliation-local-settlement-agent.md) — business role
- [Sell Side Party](../../../../../../shared/reference/participants/settlement-reconciliation-sell-side-party.md) — business role
- [Buy Side Party](../../../../../../shared/reference/participants/settlement-reconciliation-buy-side-party.md) — business role
- [Central Counterparty](../../../../../../shared/reference/participants/settlement-reconciliation-central-counterparty.md) — business role
- [Stock Exchange](../../../../../../shared/reference/participants/settlement-reconciliation-stock-exchange.md) — business role
- [Confirmation Party](../../../../../../shared/reference/participants/settlement-reconciliation-confirmation-party.md) — business role
- [CSD / ICSD](../../../../../../shared/reference/participants/settlement-reconciliation-csd-icsd.md) — business role
- [Settlement Infrastructure](../../../../../../shared/reference/participants/settlement-reconciliation-settlement-infrastructure.md) — business role

## Complete source role mapping

[Complete source table16](documents/src-000196/tables/tbl-0016.md) — [src-000196](../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md), §3.2, after paragraph176. Source Participant Account Servicer/Account Owner headers differ from functional labels in §3.1; preserve blank source cells.

## Source ambiguity

§1.1 table1 and §3 use differing wording for BusinessRole and Participant. §3.1 truncates Executing/Servicing Party definition; §3.2 uses account-role headers. Do not normalize these into unsupported identities.

[Reusable flows](flows/index.md)

<!-- NARRATIVE-PARTICIPANTS-START -->
[Additional participants explicitly named in message Functionality](participants-narrative.md)
<!-- NARRATIVE-PARTICIPANTS-END -->


<!-- ALL-SCOPED-RECORDS-START -->
## All maintained source-scoped participant records

| Participant | Role kind | Status |
| --- | --- | --- |
| [Account owner](../../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md) | functional account role | needs-review |
| [Account servicer](../../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md) | functional account role | needs-review |
| [Broker](../../../../../../shared/reference/participants/settlement-reconciliation-scope-broker.md) | illustrative institution/business participant; figure-scoped | needs-review |
| [Broker’s Local Agent — Account Owner 2](../../../../../../shared/reference/participants/settlement-reconciliation-scope-brokers-local-agent.md) | illustrative institution/business participant; figure-scoped | needs-review |
| [Buy Side Party](../../../../../../shared/reference/participants/settlement-reconciliation-buy-side-party.md) | business role | needs-review |
| [CSD / ICSD](../../../../../../shared/reference/participants/settlement-reconciliation-csd-icsd.md) | business role | needs-review |
| [Cash Leg Executing Party](../../../../../../shared/reference/participants/settlement-reconciliation-cash-leg-executing-party.md) | functional participant role | needs-review |
| [Central Counterparty](../../../../../../shared/reference/participants/settlement-reconciliation-central-counterparty.md) | business role | needs-review |
| [Client — split settlement](../../../../../../shared/reference/participants/settlement-reconciliation-split-settlement-client.md) | functional participant role | needs-review |
| [Confirmation Party](../../../../../../shared/reference/participants/settlement-reconciliation-confirmation-party.md) | business role | needs-review |
| [Custodian](../../../../../../shared/reference/participants/settlement-reconciliation-scope-custodian.md) | illustrative institution/business participant; figure-scoped | needs-review |
| [Customer](../../../../../../shared/reference/participants/settlement-reconciliation-scope-customer.md) | illustrative institution/business participant; figure-scoped | needs-review |
| [Executing/servicing party](../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md) | functional participant role | needs-review |
| [Global Settlement Agent](../../../../../../shared/reference/participants/settlement-reconciliation-global-settlement-agent.md) | business role | needs-review |
| [Instructing party](../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md) | functional participant role | needs-review |
| [Instructing/Splitting Party](../../../../../../shared/reference/participants/settlement-reconciliation-instructing-splitting-party.md) | functional participant role | needs-review |
| [Local Settlement Agent](../../../../../../shared/reference/participants/settlement-reconciliation-local-settlement-agent.md) | business role | needs-review |
| [Portfolio transfer client](../../../../../../shared/reference/participants/settlement-reconciliation-portfolio-transfer-client.md) | functional participant role | needs-review |
| [Securities Financing Instructing Party](../../../../../../shared/reference/participants/settlement-reconciliation-financing-instructing-party.md) | functional participant role | needs-review |
| [Securities Financing Servicing Party](../../../../../../shared/reference/participants/settlement-reconciliation-financing-servicing-party.md) | functional participant role | needs-review |
| [Securities Financing Servicing Party / Settlement Executing Party](../../../../../../shared/reference/participants/settlement-reconciliation-financing-servicing-settlement-executing-party.md) | functional participant role | needs-review |
| [Securities Leg Executing Party](../../../../../../shared/reference/participants/settlement-reconciliation-securities-leg-executing-party.md) | functional participant role | needs-review |
| [Securities/Cash Instruction Executing/Servicing Party](../../../../../../shared/reference/participants/settlement-reconciliation-cash-securities-split-servicing-party.md) | functional participant role | needs-review |
| [Sell Side Party](../../../../../../shared/reference/participants/settlement-reconciliation-sell-side-party.md) | business role | needs-review |
| [Settlement Executing Party](../../../../../../shared/reference/participants/settlement-reconciliation-settlement-executing-party.md) | functional participant role | needs-review |
| [Settlement Infrastructure](../../../../../../shared/reference/participants/settlement-reconciliation-settlement-infrastructure.md) | business role | needs-review |
| [Stock Exchange](../../../../../../shared/reference/participants/settlement-reconciliation-stock-exchange.md) | business role | needs-review |
| [Sub-Custodian — Account Owner 3](../../../../../../shared/reference/participants/settlement-reconciliation-scope-sub-custodian.md) | illustrative institution/business participant; figure-scoped | needs-review |
| [Third Party — portfolio settlement diagram](../../../../../../shared/reference/participants/settlement-reconciliation-portfolio-settlement-third-party.md) | functional participant role | needs-review |
| [Third party in securities reporting](../../../../../../shared/reference/participants/settlement-reconciliation-reporting-third-party.md) | functional participant role | needs-review |

<!-- ALL-SCOPED-RECORDS-END -->
