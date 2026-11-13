---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["15 camt.016.001.04 GetCurrencyExchangeRateV04"]
file_pages: [505]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.016.001.04"]
---

# 15 camt.016.001.04 GetCurrencyExchangeRateV04

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 505 to 505.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 505

```text
15 camt.016.001.04
GetCurrencyExchangeRateV04
15.1 MessageDefinition Functionality
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
```

