---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["16 camt.017.001.05 ReturnCurrencyExchangeRateV05"]
file_pages: [511, 512]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.017.001.05"]
---

# 16 camt.017.001.05 ReturnCurrencyExchangeRateV05

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 511 to 512.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 511

```text
16 camt.017.001.05
ReturnCurrencyExchangeRateV05
16.1 MessageDefinition Functionality
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
```

## File page 512

```text
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
```

