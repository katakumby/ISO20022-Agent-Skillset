---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "System Status ", "Currency Exchange Rate", "Get/Return Currency Exchange Rate Receipt"]
content_origin: "source-transcription"
---

# Get/Return Currency Exchange Rate Receipt

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / System Status  / Currency Exchange Rate / Get/Return Currency Exchange Rate Receipt.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P299** Get/Return Currency Exchange Rate Receipt

**P300** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with business information related to the management of the system, not related to the transactions created in the system. This business information can refer, for instance, to the details of currency exchanges between various currencies.

**P301** At any time during the operating hours of the system, a member can query the transaction administrator to get information about the data related to a currency exchange operation. For this, the member can initiate the exchange by sending a GetCurrencyExchangeRate message to the transaction administrator.

**P302** If the transaction administrator cannot process the query received immediately, it will reply to the member with a Receipt message where it can indicate the status of the request.

**P303** Later on, the transaction administrator will reply with a ReturnCurrencyExchangeRate message that will contain either the response to the criteria expressed in the GetCurrencyExchangeRate message, or an error indication. To close the cycle, the member can submit a Receipt message to the transaction administrator.

[fig-0025 - original figure evidence](../diagrams/fig-0025.md)

