---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "How to use the Cash Management Messages", "Controlling the Quantity of Returned Information"]
content_origin: "source-transcription"
---

# Controlling the Quantity of Returned Information

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / How to use the Cash Management Messages / Controlling the Quantity of Returned Information.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P152** Controlling the Quantity of Returned Information

**P153** In all Get messages, an element QueryType makes it possible to limit the returned information to changes compared to the information returned in a preceding Return message. 

**P154** This option should only be used in relation to a query sent previously with the same search criteria/same query name.

**P155** Using Error Codes

**P156** Errors may be expressed at two different levels of the Return message:

**P157** If the Get message could not be processed at all, the error code will be the only relevant information in the Return message, and no retrieved information will be returned.

**P158** Example 1 

**P159** The Get message was correct but the search criteria were not consistent with the agreed service defined between the parties.

**P160** Example 2

**P161** A general error occurred at the account servicer's side (the service was temporarily not available, for instance).

**P162** If the Get message could be processed but some specific problems were encountered, the error code will be added to the information that has been retrieved based on (a part of) the search criteria set.

**P163** Example 1

**P164** One of the search criteria was not processed, such as a valid account number not belonging to the requestor.

**P165** The error codes are not part of the standard, since they will be defined in the agreement between the account owner and the account servicer.

**P166** List of potential error codes (FIN-inspired)

**P167** The following list contains error codes used in the FIN Reject/Return mechanism, which may be considered when defining the error code list for a given service.

**P168** The list is provided for illustration purposes only. It is not exhaustive and should only be regarded as a suggestion for the format and content of error codes to be used.

**P169** Code Reason

[T15 - complete table](../tables/tbl-0015.md)

