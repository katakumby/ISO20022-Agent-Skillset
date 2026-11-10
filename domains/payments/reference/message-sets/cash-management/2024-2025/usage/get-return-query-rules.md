---
template: false
document_kind: "usage-guidance"
review_status: "needs-review"
manual_curated: true
title: "Operational Cash Management query, push and error rules"
domain: "payments"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_sets: ["cash-management"]
source_locations: [{"source_id": "src-000014", "paragraphs": ["P111", "P169"], "rendered_file_pages": [13, 14, 15, 16]}]
---

# Query, push and error rules

[src-000014](../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx); P111–169, Word file pages13–16.

Different search criteria combine with AND; repeated values for the same criterion combine with OR. QueryType changes-only requests require the same prior criteria/name. These are business usage rules, distinct from XSD facets. The FIN-inspired codes in T15 are explicitly illustrative and non-exhaustive (P165–168), not the current external code-set enumeration.

**P111** Selecting the appropriate Get/Return Messages

**P112** The Cash Management messages provide a high degree of flexibility. It is up to each particular system (be it a centralised system, a market infrastructure, or an account owner-account servicer relationship) to define its own solution by identifying:

**P113** which messages are allowed

**P114** the level of complexity allowed per message

**P115** This flexible approach results in a broad framework that can be considered as a toolbox. The framework needs to be constrained, taking into account factors such as the existing business needs and the current processes and capabilities of the systems. All these features will determine the particular combination of elements that define a particular implementation. At the same time, they also define the areas of potential evolution in the future.

**P116** Pull Mode versus Push Mode

**P117** The Get/Return messages have been designed in pairs: a Get message is replied to by a Return message. This concept implies that the interaction between the transaction administrator and the member is normally in pull mode where the member initiates the information flow by sending a request in the form of a Get message.

**P118** Return messages can however also be sent without a previous Get message. This is called push mode. The push of information can take place either at pre-agreed times or as a warning or alarm when a problem has occurred.

**P119** Building a Get Message

**P120** A Get message needs to identify the search criteria, that is, the criteria that the transaction administrator will use to retrieve requested information, and the return criteria, that is, the type of information that the member expects in the reply. 

**P121** The full list of possible criteria is described in the individual message definitions but that these criteria can be further restricted in any particular implementation. 

**P122** The build-up of a Get message consists of the following three steps:

**P123** Step 1 - Selection of the Search Criteria

**P124** Each Get message definition describes a potential set of search criteria. These search criteria can be combined. The more search criteria used, the more refined the Get message will be. When different search criteria are combined, these have to be interpreted as an 'AND' operator, for example, if balance information is requested based on the currency of the account AND on the value date, only the balances meeting both criteria at the same time will be returned.

**P125** Step 2 - Search Criteria Value Selection

**P126** For each used search criterion, the value(s) that will be used to retrieve information must be defined.

**P127** Each value may be expressed as:

**P128** a discrete value, for example, a date, an amount, an account identifier, an indicator (true versus false, credit versus debit)

**P129** corresponding to the logical operator 'EQUAL TO',

**P130** a set of values corresponding to more complex logical operators, for example, values from x to y both inclusive, less than or equal to x, greater than or equal to x, etc.

**P131** When the same search criterion is used more than once, (that is, when different values for the same search criterion are requested), these must be interpreted as an 'OR' operator. For example, a matching transaction may be selected on search criterion status with value 1 OR value 2. In this case, all transactions with the specific status value 1 OR value 2 will be returned.

**P132** Step 3 - Return Criteria

**P133** The generic design of the Get messages lets the account owner select the type of information that should be returned by the account servicer (return criteria).

**P134** In systems where this selection is not allowed, a default content of the return message will be pre-defined. In systems where this selection is allowed, some return data is by default mandatory (like the identification of the object).

**P135** It is not necessary to specifically request this data in the return criteria section of the Get message.

**P136** Example of a Get message:

**P137** Step 1 : Two attributes of a transaction that could be used as search criteria are the status of the entry and the value date of the transaction.

**P138** Step 2 : We may be interested only in those transactions that are still pending or have been settled (status) and whose value dates are between July 1, 2017 and July 4, 2017.

**P139** Step 3 : We may want to know the amounts and who originated those transactions with the features mentioned in steps 1 and 2.

**P140** So our final query would be: 'For all payment transactions where the status is pending or settled and the value date is between July 1, 2017 and July 4, 2017, get the identification of the originator and the transaction amount.'

**P141** Building a Return Message

**P142** The Return message contains the result of the Get message processing. Depending on the success or failure of the processing, the Return message may or may not contain an error notification.

**P143** As explained earlier, Return messages could also be sent spontaneously by the transaction administrator.

**P144** The agreement between the parties may stipulate, where relevant, the size and the maximum number of items to be returned within the Return message. The maximum size of the Return message, or the maximum number of occurrences allowed, have to take into account technical constraints, such as the maximum payload size on the communication network. These characteristics are considered external to the standards design and are therefore not explained in this document.

**P145** Features of Get and Return Messages

**P146** Reconciling Get and Return Messages

**P147** The reconciliation of the Get and Return messages takes place via the QueryReference element of the Return message.

**P148** This element contains the message identification of the Get message to which it is replying and, optionally the name of the query.

**P149** Reusing a Query

**P150** In all the Get messages, an element NewQueryName makes it possible to assign a name to the particular combination of search and return criteria that are included in the message. This name may then be used in the element QueryName of subsequent Get messages to simply refer to this combination. Thanks to this option, the account owner may define a query either by selecting the appropriate search and return criteria, or by referring to a previous query by its name.

**P151** This allows the execution of routine queries, ie, the regular submission of Get messages that have the same desired output.

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


[Complete illustrative error-code table](../documents/src-000014/tables/tbl-0015.md)
