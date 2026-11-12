---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.017.001.05"
message_family: "camt.017"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "16 camt.017.001.05 ReturnCurrencyExchangeRateV05", "file_pages": [511, 521]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.017.001.05 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 16 camt.017.001.05 ReturnCurrencyExchangeRateV05

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp511–521; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 16 camt.017.001.05 ReturnCurrencyExchangeRateV05, Functionality, file p511.**

Scope
The ReturnCurrencyExchangeRate message is sent by the transaction administrator to a member of
the system.
It is used to provide information on static data and related to currency exchange details as maintained
for system operations by the transaction administrator.
The ReturnCurrencyExchangeRate message can be sent as a response to a related
GetCurrencyExchangeRate message (pull mode) or initiated by the account servicer (push mode). The
push of information can take place either at prearranged times or as a warning or alarm when a
problem has occurred.
Usage
The transaction administrator is in charge of providing the members with business information. The
term business information covers all information related to the management of the system, that is, not
related to the transactions or requests created in the system. The type of business information available
can vary depending on the system.
When a system manages a pool of accounts in various currencies for a member, it needs to maintain
currency exchange details between the various currencies and the reporting on base currency. The
reporting on base currency is used to calculate the actual position of the members in terms of
aggregate limits and balances. It also allows the system to contain risk within defined and agreed
boundaries.
The currency exchange details can be fixed for the entire operational day or regularly updated
according to near real-time market feeds.
The member can request information about a currency exchange operation through a series of criteria,
corresponding to the known information stored within the transaction administrator. Based on the
criteria received within the request, the transaction administrator will select items that will match with the
request and report them to the requestor.
The transaction administrator may also send a Return Currency Exchange Rate message with pre-
defined information at times previously agreed with the member or to warn the member about a
particular problem that may have arisen and which needs the member(s) attention.
The message from the transaction administrator will contain information based on the following
elements:
- the currency to be converted (source currency)
- the currency into which the amount is converted (target currency)
- the exchange rate
- the quotation date and currency
Approved by the Payments SEG on 04 February 2025 camt.017.001.05 ReturnCurrencyExchangeRateV05
Cash Management - Maintenance 2024 - 2025 511 February 2025

**src-000015, 16 camt.017.001.05 ReturnCurrencyExchangeRateV05, Functionality, file p512.**

Additional information on the generic design of the Get/Return messages can be found in the MDR Part
1 section How to Use the Cash Management Messages.
Outline
The ReturnCurrencyExchangeRateV05 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Reports on currency exchange information.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.017.001.05 ReturnCurrencyExchangeRateV05
Cash Management - Maintenance 2024 - 2025 512 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [16 camt.017.001.05 ReturnCurrencyExchangeRateV05](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00366.md) | 511–512 |
| [16 camt.017.001.05 ReturnCurrencyExchangeRateV05 / 16.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00367.md) | 513–513 |
| [16 camt.017.001.05 ReturnCurrencyExchangeRateV05 / 16.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00368.md) | 514–514 |
| [16 camt.017.001.05 ReturnCurrencyExchangeRateV05 / 16.4 Message Building Blocks / 16.4.2 ReportOrError &lt;RptOrErr&gt; / 16.4.2.1 CurrencyExchangeReport &lt;CcyXchgRpt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00369.md) | 515–515 |
| [16 camt.017.001.05 ReturnCurrencyExchangeRateV05 / 16.4 Message Building Blocks / 16.4.2 ReportOrError &lt;RptOrErr&gt; / 16.4.2.1 CurrencyExchangeReport &lt;CcyXchgRpt&gt; / 16.4.2.1.1 CurrencyReference &lt;CcyRef&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00370.md) | 516–516 |
| [16 camt.017.001.05 ReturnCurrencyExchangeRateV05 / 16.4 Message Building Blocks / 16.4.2 ReportOrError &lt;RptOrErr&gt; / 16.4.2.1 CurrencyExchangeReport &lt;CcyXchgRpt&gt; / 16.4.2.1.1 CurrencyReference &lt;CcyRef&gt; / 16.4.2.1.1.2 TargetCurrency &lt;TrgtCcy&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00371.md) | 517–517 |
| [16 camt.017.001.05 ReturnCurrencyExchangeRateV05 / 16.4 Message Building Blocks / 16.4.2 ReportOrError &lt;RptOrErr&gt; / 16.4.2.1 CurrencyExchangeReport &lt;CcyXchgRpt&gt; / 16.4.2.1.2 CurrencyExchangeOrError &lt;CcyXchgOrErr&gt; / 16.4.2.1.2.1 BusinessError &lt;BizErr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00372.md) | 518–518 |
| [16 camt.017.001.05 ReturnCurrencyExchangeRateV05 / 16.4 Message Building Blocks / 16.4.2 ReportOrError &lt;RptOrErr&gt; / 16.4.2.1 CurrencyExchangeReport &lt;CcyXchgRpt&gt; / 16.4.2.1.2 CurrencyExchangeOrError &lt;CcyXchgOrErr&gt; / 16.4.2.1.2.2 CurrencyExchange &lt;CcyXchg&gt; / 16.4.2.1.2.2.3 QuotationDate &lt;QtnDt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00373.md) | 519–519 |
| [16 camt.017.001.05 ReturnCurrencyExchangeRateV05 / 16.4 Message Building Blocks / 16.4.2 ReportOrError &lt;RptOrErr&gt; / 16.4.2.1 CurrencyExchangeReport &lt;CcyXchgRpt&gt; / 16.4.2.1.2 CurrencyExchangeOrError &lt;CcyXchgOrErr&gt; / 16.4.2.1.2.2 CurrencyExchange &lt;CcyXchg&gt; / 16.4.2.1.2.2.5 HighLimit &lt;HghLmt&gt; / 16.4.2.1.2.2.5.1 Rate &lt;Rate&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00374.md) | 520–521 |

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
- [Unsolicited operational cash reports and warnings](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p118-unsolicited-push-reporting.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
