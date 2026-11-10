---
template: false
document_kind: "business-rules"
manual_curated: true
review_status: "needs-review"
title: "Bank-to-customer reporting scope, roles and usage conditions"
domain: "payments"
source_ids: ["src-000004"]
source_locations: [{"source_id": "src-000004", "locator": "P69-P85 Word7-8; T6-T17/P89-P124 Word9-18; P129-P153 Word19-21"}]
message_sets: ["bank-to-customer-cash-management"]
message_ids: ["camt.052.001.14", "camt.053.001.14", "camt.054.001.14", "camt.060.001.07"]
issue_ids: ["issue-000060"]
limitations: ["Part1 business-process conditions are separate from XSD constraints. Generic payment-status flow has no exact message version specified."]
source_editions: ["March 2026"]
---

# Bank-to-customer reporting scope, roles and usage conditions

[src-000004](../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart1_BankToCustomerCashManagement_2025_2026_v2.docx); focused locators below.

P73/Word7 explicitly scopes debit/credit advices and statements from an account servicing institution to private/corporate account owners, excluding advices/statements between financial intermediaries. This collection is distinct from operational Cash Management even when both use camt identifiers. P102/P105 discusses a generic reporting process applicable across contexts, then limits the detailed definitions here to the bank-to-customer process. Regulatory reporting is separate (P103/P106).

| Family | Purpose and sender/receiver | Evidence |
| --- | --- | --- |
| camt.052 | Servicer to owner or authorised party; reported entries and/or balances at a point in time. Scenario1 includes booked and pending intraday movements. | P78/P132; Word7/19 |
| camt.053 | Servicer to owner or authorised party; booked entries and balances. Scenario1 end-of-day statement supplies booked and available balances. | P80/P132; Word7/19 |
| camt.054 | Servicer to owner or authorised party; one or multiple debit/credit entries. Scenario2 credit threshold is service-agreed, no numeric threshold supplied. | P82/P135; Word7/19 |
| camt.060 | Owner directly or through forwarding agent to account servicing institution; requests report, statement or notification. | P85/P145-P153; Word8/21 |



T6 defines Account Owner by its account/contractual relationship and Account Servicer by management/registration/booking/balance/information obligations. Recipient requires owner authorisation; Forwarding Agent has forwarding/execution responsibility. One institution can hold different roles in different relationships. T7 business roles and T8 mapping remain scoped, and the diagram generalisation connections are retained separately. System lanes in cash positioning/reconciliation are functional responsibilities; they do not establish distinct legal institutions or identifier schemes.

T9/T10 define reporting/reconciliation with prior agreement about report type based on legal/business requirements and trigger completion of a payment process. Their repeated definition is retained, not silently rewritten. T11 financial-impact reporting triggers on settlement completion after debit/credit registration (pending, future, or booked). T12 status reporting runs throughout the lifecycle on status changes after any agent receives the transaction, including accepted/repaired or rejected information. P110 names First, Forwarding and Final Agents and Initiating Party. No exact status-message ID is specified here.

T14 retains every cash-positioning input, balances and closing condition. T15 makes all three notification arrows optional under the service agreement and permits early information before final booking. T16/T17 reconcile internal accounting with external feeds, with unmatched items possibly triggering investigation; aggregate financial reconciliation uses detailed reports as specifications (P121/P124). Source responsibility/label conflicts remain in [issue-000060](source-consistency.md).

The source reporting scenarios distinguish a Recipient that can relay an internal message, a Forwarding Agent serving as concentrating institution, direct request/selected response, and relayed request/response. The authorised recipient mentioned in P141 is absent from that diagram and remains linked as narrative context. A request does not require all three response definitions.

| Source example | Exact supplied definition |
| --- | --- |
| [Intraday account report](examples/intraday-report.md) | camt.052.001.14 |
| [End-of-day statement](examples/end-of-day-statement.md) | camt.053.001.14 |
| [Credit notification](examples/credit-notification.md) | camt.054.001.14 |
| [Account reporting request](examples/reporting-request.md) | camt.060.001.07 |

