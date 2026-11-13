---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
flow_id: "flow-src-000014-p294-get-return-currency-exchange-rate"
title: "Get/Return Currency Exchange Rate"
domain: "payments"
source_ids: ["src-000014", "src-000015"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
participant_ids: ["participant-src-000014-system-direct-member", "participant-src-000014-system-transaction-administrator", "participant-src-000014-account-owner", "participant-src-000014-account-servicing-institution"]
message_ids: ["camt.016.001.04", "camt.017.001.05"]
message_families: ["camt.016", "camt.017"]
source_locations: [{"source_id": "src-000014", "heading_path": ["BusinessTransactions", "System Status ", "Currency Exchange Rate", "Get/Return Currency Exchange Rate"], "paragraphs": ["P294", "P298"], "rendered_file_page": 30}]
issue_ids: []
limitations: ["The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.", "Solid source exchange lines and ordering are retained. No timeout, condition, response code or mandatory Receipt is inferred solely from the picture."]
---

# Get/Return Currency Exchange Rate

[src-000014](../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md); P294–298; Word figure page30. Exact versions are independently named by Part2 src-000015; the Part1 diagrams use names/families.

## Purpose, trigger, preconditions, alternatives and outcomes

**P288** Currency Exchange Rate

**P289** The transaction administrator is in charge of providing the members with business information. The term business information covers all information related to the management of the system that is, not related to the transactions or requests created in the system. The type of business information available can vary depending on the system.

**P290** When a system manages a pool of accounts in various currencies for a member, it needs to maintain currency exchange details between the various currencies and the reporting on base currency. The reporting on base currency is used to calculate the actual position of the members in terms of aggregate limits and balances. It also allows the system to contain risk within defined and agreed boundaries.

**P291** The currency exchange details can be fixed for the entire operational day or regularly updated according to near real-time market feeds.

**P292** The member can request information about a currency exchange operation through a series of criteria, corresponding to the known information stored within the transaction administrator. Based on the criteria received within the request, the transaction administrator will select items that will match with the request and report them to the requestor.

**P293** The transaction administrator may also send a Return Currency Exchange Rate message with pre-defined information at times previously agreed with the member or to warn the member about a particular problem that may have arisen and which needs the member(s) attention.

**P295** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with business information related to the management of the system, not related to the transactions created in the system. This business information can refer, for instance, to the details of currency exchanges between various currencies.

**P296** At any time during the operating hours of the system, a member can query the transaction administrator to get information about the data related to a currency exchange operation. For this, the member can initiate the exchange by sending a GetCurrencyExchangeRate message to the transaction administrator.

**P297** The transaction administrator replies with a ReturnCurrencyExchangeRate message that will contain either the response to the criteria expressed in the GetCurrencyExchangeRate message, or an error indication.


## Ordered picture exchanges

| Step | Sender | Receiver | Message | Exact supplied definition |
| --- | --- | --- | --- | --- |
| 1 | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | GetCurrencyExchangeRate | [camt.016.001.04](../../../../messages/camt.016.001.04/index.md) |
| 2 | [Transaction Administrator](../../../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | [System Direct Member](../../../../../../../shared/reference/participants/participant-src-000014-system-direct-member.md) | ReturnCurrencyExchangeRate | [camt.017.001.05](../../../../messages/camt.017.001.05/index.md) |


The picture shows only the System Direct Member and Transaction Administrator. Account owner/servicing institution are narrative relationship roles (P75–78), not extra lifelines.

## Related roles and references

[Account owner](../../../../../../../shared/reference/participants/participant-src-000014-account-owner.md) · [Account servicing institution](../../../../../../../shared/reference/participants/participant-src-000014-account-servicing-institution.md) · [Query, push, error and implementation rules](../usage/get-return-query-rules.md) · [Source reconstruction](../diagrams/operational-cash/fig-0024.md)

Cancellation, deletion and modification are the source-named operations. A settlement reversal is not inferred from these labels. Source-defined conditions are retained above; no unstated postcondition is added.
