---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "System Status ", "Currency Exchange Rate"]
content_origin: "source-transcription"
---

# Currency Exchange Rate

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / System Status  / Currency Exchange Rate.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P288** Currency Exchange Rate

**P289** The transaction administrator is in charge of providing the members with business information. The term business information covers all information related to the management of the system that is, not related to the transactions or requests created in the system. The type of business information available can vary depending on the system.

**P290** When a system manages a pool of accounts in various currencies for a member, it needs to maintain currency exchange details between the various currencies and the reporting on base currency. The reporting on base currency is used to calculate the actual position of the members in terms of aggregate limits and balances. It also allows the system to contain risk within defined and agreed boundaries.

**P291** The currency exchange details can be fixed for the entire operational day or regularly updated according to near real-time market feeds.

**P292** The member can request information about a currency exchange operation through a series of criteria, corresponding to the known information stored within the transaction administrator. Based on the criteria received within the request, the transaction administrator will select items that will match with the request and report them to the requestor.

**P293** The transaction administrator may also send a Return Currency Exchange Rate message with pre-defined information at times previously agreed with the member or to warn the member about a particular problem that may have arisen and which needs the member(s) attention.

