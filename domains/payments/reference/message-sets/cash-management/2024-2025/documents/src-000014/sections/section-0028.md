---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Get Message"]
content_origin: "source-transcription"
---

# Building a Get Message

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / How to use the Cash Management Messages / Building a Get Message.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

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

