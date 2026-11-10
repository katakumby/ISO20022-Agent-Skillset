---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.016.001.04"
message_family: "camt.016"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "15 camt.016.001.04 GetCurrencyExchangeRateV04", "file_pages": [505, 510]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.016.001.04 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 15 camt.016.001.04 GetCurrencyExchangeRateV04

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp505–510; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 15 camt.016.001.04 GetCurrencyExchangeRateV04, Functionality, file p505.**

Scope
The GetCurrencyExchangeRate message is sent by a member to the transaction administrator.
It is used to request information on static data maintained by the transaction administrator and related
to currency exchange details as maintained for the system operations by the transaction administrator.
Usage
The transaction administrator is in charge of providing the members with business information. The
term business information covers all information related to the management of the system, i.e., not
related to the transactions created into the system. The type of business information available can vary
depending on the system.
When a system manages a pool of accounts in various currencies for a member, there is a need to
maintain currency exchange details in between the various currencies and the reporting or base
currency. The reporting or base currency is used to calculate the actual position of the members in
terms of aggregate limits and balances and allow the system to contain risk within the defined and
agreed boundaries. The currency exchange details can be fixed for the entire operational day, or
regularly updated according to near real time market feeds.
At any point in time during operating hours of the system, the member can query the transaction
administrator to get information about the static data related to a currency exchange details.
The member can request information based on the following elements:
- the currency to be converted (source currency)
- the currency into which the amount is converted (target currency)
This message will be replied to by a ReturnCurrencyExchangeRate message.
Outline
The GetCurrencyExchangeRateV04 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. CurrencyQueryDefinition
Definition of the currency exchange query.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.016.001.04 GetCurrencyExchangeRateV04
Cash Management - Maintenance 2024 - 2025 505 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [15 camt.016.001.04 GetCurrencyExchangeRateV04](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00361.md) | 505–505 |
| [15 camt.016.001.04 GetCurrencyExchangeRateV04 / 15.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00362.md) | 506–506 |
| [15 camt.016.001.04 GetCurrencyExchangeRateV04 / 15.4 Message Building Blocks / 15.4.2 CurrencyQueryDefinition &lt;CcyQryDef&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00363.md) | 507–507 |
| [15 camt.016.001.04 GetCurrencyExchangeRateV04 / 15.4 Message Building Blocks / 15.4.2 CurrencyQueryDefinition &lt;CcyQryDef&gt; / 15.4.2.2 CurrencyCriteria &lt;CcyCrit&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00364.md) | 508–508 |
| [15 camt.016.001.04 GetCurrencyExchangeRateV04 / 15.4 Message Building Blocks / 15.4.2 CurrencyQueryDefinition &lt;CcyQryDef&gt; / 15.4.2.2 CurrencyCriteria &lt;CcyCrit&gt; / 15.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 15.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 15.4.2.2.2.2.1 SourceCurrency &lt;SrcCcy&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00365.md) | 509–510 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [ACH](../../../../../shared/reference/participants/participant-src-000014-ach.md) | participant | src-000014 |
| [Automated Clearing House (ACH)](../../../../../shared/reference/participants/participant-src-000014-automated-clearing-house-ach.md) | participant | src-000014 |
| [Cash Provider](../../../../../shared/reference/participants/participant-src-000014-cash-provider.md) | participant | src-000014 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000014-central-securities-depositories-csd.md) | participant | src-000014 |
| [Corporate](../../../../../shared/reference/participants/participant-src-000014-corporate.md) | participant | src-000014 |
| [CSD](../../../../../shared/reference/participants/participant-src-000014-csd.md) | participant | src-000014 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000014-market-infrastructure.md) | participant | src-000014 |
| [Real Time Gross Settlement System (RTGS)](../../../../../shared/reference/participants/participant-src-000014-real-time-gross-settlement-system-rtgs.md) | participant | src-000014 |
| [RTGS](../../../../../shared/reference/participants/participant-src-000014-rtgs.md) | participant | src-000014 |
| [Settlement Agent](../../../../../shared/reference/participants/participant-src-000014-settlement-agent.md) | participant | src-000014 |
| [System Member](../../../../../shared/reference/participants/participant-src-000014-system-member.md) | participant | src-000014 |
| [System / Transaction Administrator](../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | participant | src-000014 |
| [Transaction Administrator/System](../../../../../shared/reference/participants/participant-src-000014-transaction-administrator-system.md) | participant | src-000014 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)

<!-- CASH-FLOWS -->
## Operational Cash Management flows

- [Get/Return Currency Exchange Rate](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p294-get-return-currency-exchange-rate.md)
- [Get/Return Currency Exchange Rate Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p299-get-return-currency-exchange-rate-receipt.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
