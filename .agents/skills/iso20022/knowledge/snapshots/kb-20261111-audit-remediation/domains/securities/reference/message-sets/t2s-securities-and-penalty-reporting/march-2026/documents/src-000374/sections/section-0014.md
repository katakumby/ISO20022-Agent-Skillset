---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["Scope and Functionality", "Scope", "Functionality"]
content_origin: "source-transcription"
---

# Functionality

Source: [src-000374](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Locator: heading path Scope and Functionality / Scope / Functionality.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P87** Functionality

**P89** This section provides for an overview of the functionality of each message in the scope of this submission, See Message Definition Report Part 2 for the message definitions and formats.

**P91** The Settlement Queries Responses and Report message definitions are specifically designed to support the following technical functions:

**P93** Securities Account Position Query (semt.025)

**P94** The Securities Account Position Query provides CSDs and T2S participants with the functionality to query for the latest or historical data on balances in the Securities Accounts with multiple criteria and, in some cases, satisfying multiple values or range of values.  

**P95** The Securities Account Position Query message is composed of the following message building blocks.

**P96** Statement

**P97** This building block is mandatory and defines the criteria used to report on the securities account position allowing to choose for the latest or historical data. 

**P98** SearchCriteria

**P99** This building block is mandatory and provides the criteria to extract the securities account position result set.

**P100** In response to the Securities Account Position Query T2S sends a Securities Account Position Response message (semt.040) with the corresponding Securities Account position details matching the criteria as defined within the query.

**P102** Securities Settlement Transaction Query (semt.026)

**P103** The Securities Settlement Transaction Query message is sent by a Central Securities Depository or a Directly Connected T2S Participant (e.g. payment bank/settlement bank) to T2S to query for information on securities settlement instructions with multiple criteria and, in some cases, satisfying multiple values or range of values.

**P104** This message is composed of the following message building block:

**P105** Query Definition

**P106** This building block is mandatory and non-repetitive. It contains the definition of the securities settlement instruction query criteria by using the following two block elements:

**P107** Query Type

**P108** This block element is mandatory and non-repetitive. It defines the type of query and whether the expected query response is related to an Instruction, Status or Status Period query.

**P110** Search Criteria

**P111** This block element is mandatory and non-repetitive. It defines the criteria to extract the securities settlement instruction information.

**P113** The Securities Settlement Transaction Query message covers the following T2S message usages:

**P114** Settlement Instruction Query (corresponding query type – ‘Instruction [INST]’)

**P115** This query type enables the sender to query for information on the details of specific securities settlement instructions by specifying the pertinent criteria allowed from the list of business attributes within [Search Criteria] block element. 

**P116** To query for securities settlement instruction information, the element [Query Type] must be filled with the code “INST” [Instruction].

**P117** Search Criteria Status may be present (optional) when using this query type.

**P118** Settlement Instruction Current Status Query (corresponding query type – ‘Status [STTS]’)

**P119** This query type enables the sender to query for information on the details of specific securities settlement instructions satisfying the defined combination of current business processing statuses by specifying:

**P120** Status Type (e.g. matching status, settlement status).

**P121** Status value (e.g. matched or unmatched for matching status and pending or failing for settlement status).

**P122** All securities settlement instructions satisfying the provided criteria and with a current status matching the status criteria provided are returned.

**P123** To query a securities settlement instruction current status query the element [Query Type] must be filled with the code “STTS” [Status].

**P124** Search Criteria Status/Type must be present (mandatory) when using this query type.

**P125** Settlement Instruction Status Audit Trail Query (corresponding query type – ‘Status Period [STPD]’)

**P126** This query type enables the sender to query for information on the details of specific settlement instructions satisfying specific statuses for a given period. 

**P127** To query a settlement instruction status audit trail query the element [Query Type] must be filled with the code “STPD” [Status Period].

**P128** Search Criteria Status/Type and Status/DatePeriod must be present (mandatory) when using this query type.

**P129** All instructions satisfying the provided criteria and with the status matching the status criteria during the specified period provided are returned.

**P130** In response to the Securities Settlement Transaction Query message, T2S sends a Securities Settlement Transaction Query Response message (semt.027) with the corresponding requested securities settlement instructions based on the criteria as defined within the query message.

**P132** Securities Settlement Transaction Query Response (semt.027)

**P133** The Securities Settlement Transaction Query Response message is sent by T2S to a Central Securities Depository or a directly connected T2S participant (e.g. payment bank/settlement bank). 

**P134** This message is used to provide information on securities settlement instructions, as selected in the search criteria defined in the query message (semt.026).

**P135** The Securities Settlement Transaction Query Response is composed of the following message building blocks:

**P136** Pagination

**P137** This block element is mandatory and non-repetitive. It contains information about pagination of the report.

**P138** ReportGeneralDetails

**P139** This block element is mandatory and non-repetitive. It contains general characteristics related to the report information.

**P140** Transactions

**P141** This block element is optional and repetitive. It contains the specific transactions corresponding to the criteria of the query.

**P143** The Securities Settlement Transaction Query Response message covers the following T2S message usages:

**P144** Settlement Instruction Query Response (corresponding query type – ‘Instruction [INST]’)

**P145** This message usage provides details regarding the securities settlement instructions satisfying the query criteria of the corresponding settlement instruction query message.

**P146** To indicate a settlement instruction query response the element [Query Type] within the block element [Report General Details] is filled with the code “INST” [Instruction]. 

**P147** The element [Status And Reason] within the block element [Transactions] must not be present when using this query type.

**P148** Settlement Instruction Current Status Query Response (corresponding query type – ‘Status [STTS]’)

**P149** This message usage provides details regarding the securities settlement instructions satisfying the query criteria of the corresponding settlement instruction current status query message.

**P150** To indicate a settlement instruction current status query response the element [Query Type] within the block element [Report General Details] is filled with the code “STTS” [Status].

**P151** The element [Status And Reason] within the block element [Transactions] is present when using this query type.

**P152** Settlement Instruction Status Audit Trail Query Response (corresponding query type – ‘Status Period [STPD]’)

**P153** This message usage provides details regarding the securities settlement instructions satisfying the query criteria of the corresponding settlement instruction status audit trail query message.

**P154** To indicate a settlement instruction status audit trail query response the element [Query Type] within the block element [Report General Details] is filled with the code “STPD” [Status Period].

**P155** The element [Status And Reason] within the block element [Transactions] is present when using this query type.

**P157** Securities Account Position Response (semt.040)

**P158** The Securities Account Position Response message is sent by T2S to a CSD or any party authorised by them as response for the Securities Account Position Query message. 

**P159** The Securities Account Position Response provides information about the different securities positions of a T2S Actor’s securities account(s) in T2S. 

**P160** Depending on the search criteria of the Query, the response provides:

**P161** The current position.

**P162** The position at a specific time of the current day.

**P163** The closing position for a specific day in the past.

**P164** The closing positions for a period of days in the past.

**P165**  

**P166** The Securities Account Position Response message is composed of the following message building blocks:

**P167** Pagination

**P168** This building block is mandatory and non-repetitive. It defines the pagination of the message.

**P169** ReportGeneralDetails

**P170** This building blocks is mandatory and non-repetitive. It specifies general information related to response such as the query reference, the activity or whether the data is either historical or current.

**P171** AccountOwner

**P172** This block is optional and non-repetitive. It identifies the party who owns the account.

**P173** AccountServicer

**P174** This block is optional and identifies the party that manages the account on behalf of the account owner, i.e. manages the registration and booking of entries on the account, calculates balances on the account and provides information about the account.

**P175** Balance

**P176** This building block is optional and repetitive. This block provides the net position of a segregated holding, in a single security, within the overall position held in a set of securities accounts.

**P178** Securities Transaction Penalties Report (semt.044)

**P179** The Securities Transaction Penalties Report message definition is specifically designed to support the technical functions depending on the following message usages:

**P181** Daily cash penalty list Report. This report is sent to actors to inform about the cash penalties computed for a given business day. In case of a CSD, the information shall include the cash penalties that are either imposed or credited to all of its participants. In case the actor is a CSD participant, the information shall include the cash penalties that are either imposed or credited to the CSD participant itself.

**P183** List of modified penalties. This report is sent to actors to inform about the modifications made in existing cash penalties that have occurred since the previous recalculation process. The possible modifications that may occur in a penalty, and hence reported in the List of Modified Penalties, are: whether a cash penalty has been removed, re-included, re-allocated or switched by a CSD or whether a cash penalty has been automatically updated after the recalculation of the penalty triggered by a change in the relevant reference data like the valuation of a certain ISIN or the penalty rate to be applied.

**P185** Monthly report of aggregated amounts of cash penalties. This report is sent to actors to inform about the aggregated amounts of the cash penalties computed for the business days of the previous month. Monthly report of aggregated amounts of cash penalties considers the last available value of the amount of each of the cash penalties to be aggregated, considering all the modifications performed on the cash penalties.

**P187** The Securities Transaction Penalties Report message is composed of the following message building blocks:

**P189** Pagination

**P190** This building block is mandatory (the pagination of the report is only allowed when agreed between the parties) and non-repetitive. It contains information about pagination of the report: Page number and Last Page Indicator.

**P191** ReportGeneralDetails

**P192** This building block is mandatory and non-repetitive. It contains general characteristics related to the report information. 

**P193** AccountServicer

**P194** This block is mandatory and non-repetitive. It identifies the party that manages the account on behalf of the account owner, i.e. manages the registration and booking of entries on the account, calculates balances on the account and provides information about the account.

**P195** Penalty

**P196** This block is optional (provided Activity Indicator is TRUE) and repetitive. It contains detailed information related to the computed penalties.

