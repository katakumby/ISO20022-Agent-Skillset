---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "System Status ", "Currency Exchange Rate", "Get/Return Currency Exchange Rate"]
content_origin: "source-transcription"
---

# Get/Return Currency Exchange Rate

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / System Status  / Currency Exchange Rate / Get/Return Currency Exchange Rate.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P294** Get/Return Currency Exchange Rate

**P295** The transaction administrator (which can be a financial institution, a matching engine or a settlement engine) is in charge of providing the members with business information related to the management of the system, not related to the transactions created in the system. This business information can refer, for instance, to the details of currency exchanges between various currencies.

**P296** At any time during the operating hours of the system, a member can query the transaction administrator to get information about the data related to a currency exchange operation. For this, the member can initiate the exchange by sending a GetCurrencyExchangeRate message to the transaction administrator.

**P297** The transaction administrator replies with a ReturnCurrencyExchangeRate message that will contain either the response to the criteria expressed in the GetCurrencyExchangeRate message, or an error indication.

[fig-0024 - original figure evidence](../diagrams/fig-0024.md)

