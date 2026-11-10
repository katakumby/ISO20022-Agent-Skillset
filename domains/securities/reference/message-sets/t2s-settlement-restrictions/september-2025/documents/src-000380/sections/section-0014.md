---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["Scope and Functionality", "Functionality"]
content_origin: "source-transcription"
---

# Functionality

Source: [src-000380](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Locator: heading path Scope and Functionality / Functionality.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P122** Functionality

**P123** This section provides for an overview of the functionality of each message in the scope of this submission, See Message Definition Report Part 2 for the message definitions and formats.

**P124** The Settlement Restriction message definitions are specifically designed to support the following technical functions:

**P126** Intra Position Movement Query (semt.028)

**P127** A CSD or other directly connected T2S party sends the Intra Position Movement Query message to T2S. This message allows CSDs or T2S Participants to query for all Intra Position Movement instructions satisfying a set of criteria, including business processing statuses and a corresponding date range period.

**P128** The query type defines whether the query response outputs full details or only its current status values:

**P129** If the query specifies the Full [FULL] parameter as query type then the response to the query will include full details on the movements reported.

**P130** If the query specifies the Status [STTS] parameter as query type then the response will include limited details including the status on the movements reported.

**P131** The Intra Position Movement Query message is composed of the following message building block

**P132** Query Definition

**P133** This building block is mandatory and non-repetitive. It defines whether the query requests full details on the movements to be reported or only limited details including the status of the movements to be reported. It defines as well the criteria for extracting intra position movement information.

**P134** In response to the Intra Position Movement Query T2S sends an Intra Position Movement Query Response message (semt.029) with the corresponding intra position movement details matching the criteria as defined within the query.

**P136** Intra Position Movement Query Response (semt.029)

**P137** The Intra Position Movement Query Response message is sent in response to a semt.028 (Intra Position Movement Query). This message is sent by T2S to a CSD or other directly connected T2S participant. It is used to provide information on Intra-Position Movement instructions.

**P138** This message is composed of the following message building blocks:

**P139** Pagination

**P140** This building block is mandatory and non-repetitive. It contains information about pagination of the report.

**P141** Report General Details

**P142** This building block is mandatory and non-repetitive. It contains general characteristics related to the report information. 

**P143** Among this information, we have:

**P144** <Query Type>: it defines whether the query response relates to an Instruction, Status or Status Period query.

**P145** <Activity Indicator>: it indicates whether there is activity or information update reported in the statement.

**P147** Movements

**P148** This building block is optional and repetitive. It contains information relating to the movements corresponding to the criteria as defined within the query. Several rules apply which are:

**P149** If <Query Type> is equal to Full [FULL], then <Movement Details> linked to <Movements> must be present.

**P150** If <Query Type> is equal to Status [STTS], then <Movement Details> linked to <Movements> must be absent.

**P151** If <Activity Indicator> is equal to false, then <Movements> must be absent.

**P152** If <Activity Indicator> is equal to true, then <Movements> must be present.

**P153** <Account Owner> must be present or <Account Owner> linked to <Movement> must be present, but not both.

**P154** <Safekeeping Account> must be present or <Safekeeping Account> linked to <Movement> must be present, but not both.

**P155** <Status And Reason> must be present or <Status And Reason> linked to <Movement> must be present, but not both.

**P157** Securities Settlement Conditions Modification Request Query (semt.030)

**P158** A CSD or other directly connected party sends the Securities Settlement Conditions Modification Request Query message to T2S. This message allows the requestor to query the full details or current status of Settlement Condition Modification Requests over Settlement Instruction(s) and Intra-position Movement Instruction(s) based on a set of search criteria or business attributes including business processing statuses and a corresponding date range period.

**P159** The query type defines whether the query response outputs full details or only its current status values:

**P160** If the query specifies the Full [FULL] parameter as query type, then the response to the query will include full details on the Securities Settlement Conditions Modification Instructions reported.

**P161** If the query specifies the Status [STTS] parameter as query type, then the response will include limited details including the status on the Securities Settlement Conditions Modification Instructions reported.

**P162** The Securities Settlement Conditions Modification Request Query message is composed of the following message building block:

**P163** Query Definition

**P164** This building block is mandatory and non-repetitive. It defines the criteria to extract the Settlement Condition Modification Request information for Settlement Instructions or Intra-position Movement Instructions. It defines as well whether the query response outputs full details or only its current status values.

**P165** In response to the Securities Settlement Conditions Modification Request Query message, T2S sends a Securities Settlement Modification Query Response (semt.031) with the corresponding Securities Settlement Conditions Modification Instructions details matching the criteria as defined within the query.

**P167** Securities Settlement Conditions Modification Request Report (semt.031)

**P168** The Securities Settlement Conditions Modification Request Report message is sent by T2S to a CSD or any other T2S participant. This message is used to provide information on Securities Settlement Conditions Modification Instructions for Settlement Instructions or Intra-position Movement Instructions. This message is composed of the following message building blocks:

**P169** Pagination

**P170** This building block is mandatory and non-repetitive. It contains information about pagination of the message.

**P171** Report General Details

**P172** This building block is mandatory and non-repetitive. It contains general characteristics related to the report information. 

**P173** Among this information, we have:

**P174** <Query Type>: it defines whether the query response (or report) outputs full details or only the current status values.

**P175** <Activity Indicator>: it indicates whether there is activity or information update reported in the statement.

**P177** Modifications

**P178** This building block is optional and repetitive. It contains details on the modification requests corresponding to the criteria of the query. Several rules apply which are:

**P179** If <Activity Indicator> is equal to false, then <Modifications> must be absent.

**P180** If <Activity Indicator> is equal to true, then <Modifications> must be present.

**P181** <Account Owner> must be present or <Account Owner> linked to <Modification> must be present, but not both.

**P182** <Safekeeping Account> must be present or <Safekeeping Account> linked to <Modification> must be present, but not both.

**P183** <Processing Status> must be present or <Processing Status> linked to <Modification> must be present, but not both.

**P185** Securities Transaction Cancellation Request Query (semt.032)

**P186** A CSD or other directly connected T2S party sends the Securities Transaction Cancellation Request Query message to T2S.

**P187** This message allows users to query for all Cancellation Instructions of Settlement and Intra Position movement instructions based on a set of search criteria or business attributes. 

**P188** The query type defines whether the query response outputs full details or only its current status values:

**P189** If the query specifies the Full [FULL] parameter as query type, then the response to the query will include full details on the cancellations reported.

**P190** If the query specifies the Status [STTS] parameter as query type, then the response will include limited details including the status on the cancellation reported.

**P191** This message is composed of the following message building block:

**P192** Query Definition

**P193** This building block is mandatory and non-repetitive. It defines the criteria to extract the Cancellation Instruction information for Settlement Instructions or Settlement Restrictions on Securities Position. It defines as well whether the query response outputs full details or only its current status values.

**P195** Securities Transaction Cancellation Request Report (semt.033)

**P196** The Securities Transaction Cancellation Request Report is sent by T2S to a CSD or any T2S party, it provides information on Cancellation Instructions for Settlement or Intra Position Movement Instructions.

**P197** When used in response to a semt.032 message (pull mode), it provides the information of those Cancellation Instructions that fulfilled the criteria specified previously on the Query Message.

**P198** When used in response to a configured report (push mode), the content will cover all Securities Accounts under the Reporting Party’s scope. The report in push mode is triggered by defined business and time events.

**P199** This message is composed of the following message building block:

**P200** Query Definition

**P201** This building block is mandatory and non-repetitive. It defines the pagination of the message.

**P202** Report General Details

**P203** This building block is mandatory and non-repetitive. It provides general characteristics related to the report. Among this information we have:

**P204** <Query Type>: it defines whether the query response needs to retrieve full details of the Cancellation instruction or only its current status values.

**P205** <Update Type>: Indicates whether the report is complete (full mode) or contains changes only (delta mode).

**P206** <Activity Indicator>: it indicates whether there is activity or information update reported in the statement.

**P207** Cancellations

**P208** This building block is optional and repetitive. It contains details on the cancellation requests corresponding to the criteria of the query. Several rules apply which are:

**P209** <Account Owner> must be present or <Account Owner> nested under <Cancellation> block must be present, but not both.

**P210** <Processing Status> must be present or <Processing Status> nested under <Cancellation> block must be present, but not both.

**P211** <Safekeeping Account> must be present or <Safekeeping Account> nested under <Cancellation> block must be present, but not both.

**P212** If <Activity Indicator> is equal to false, then <Cancellations> must be absent.

**P213** If <Activity Indicator> is equal to true, then <Cancellations> must be present.

**P215** Intra Position Movement Pending Report (semt.034)

**P216** The Intra Position Movement Pending Report is sent by T2S to a CSD or a directly connected T2S participant who can receive this report in delta mode or full mode. This message is used to provide information on pending intra position movement instructions. 

**P217** In T2S context, this report is triggered by defined business and time events. It returns all new pending intra position movement instructions or pending intra position movement instructions, which were modified or cancelled since the creation of the previous report (delta report).

**P218** This message is composed of the following message building blocks:

**P219** Pagination

**P220** This building block is mandatory and non-repetitive. It contains information about pagination of the report.

**P221** Report General Details

**P222** This building block is mandatory and non-repetitive. It contains general characteristics related to the report information.

**P223** Account Owner

**P224** This building block is optional and non-repetitive. It must contain the identification of the party that owns the account to or from which an entry is made.

**P225** Safekeeping Account

**P226** This building block is mandatory and non-repetitive. It identifies the account to or from which a securities entry is made.

**P227** Movements

**P228** This building block is optional and repetitive. It provides the details of the movements reported. Several rules apply which are:

**P229** If <Activity Indicator> is equal to false, then <Movements> must be absent.

**P230** If <Activity Indicator> is equal to true, then <Movements> must be present.

**P231** <Status And Reason> must be present or <Status And Reason> linked to <Movement> must be present, but not both.

